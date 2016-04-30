#Patterns

[toc]

## MVC

Model View Controll ist eine Möglichkeit GUI Applikationen besser zu Strukturieren. Der englischsprachige Begriff model view controller (MVC, englisch für Modell-Präsentation-Steuerung) ist ein Muster zur Strukturierung von Software-Entwicklung in die drei Einheiten Datenmodell (engl. model), Präsentation (engl. view) und Programmsteuerung (engl. controller). Manche Autoren stufen es als Architekturmuster ein, andere als Entwurfsmuster. Ziel des Musters ist ein flexibler Programmentwurf, der eine spätere Änderung oder Erweiterung erleichtert und eine Wiederverwendbarkeit der einzelnen Komponenten ermöglicht. Es ist dann zum Beispiel möglich, eine Anwendung zu schreiben, die dasselbe Modell nutzt und es dann für Windows, Mac, Linux oder für das Internet zugänglich macht. Die Umsetzungen nutzen dasselbe Modell, nur Controller und View müssen dabei jeweils neu implementiert werden.

```Java
public class Model{

	private count = 0;

	public void extendCount(){
		this.count = this.count+1;
	}
    
    public int getCount(){
    	return this.count;
    }

}
```
```Java
public class View extends JFrame{

	private Model model;
    protected JButton button;

	public View(Model model){
    	this.model = model
        this.button = new JButton(""+model.getCount());
        
        this.add(button);
    }
    
    public void updateButton(){
    	this.button.setText(""+this.model.getCount());
    }

}
```
```Java
public class Controller{
	private Model model;
    private View view;
    
    public Controller(){
    	this.model = new Model()
        this.view = new View(model);
        
        this.view.button.addActionListener(new ActionListener(){
        	@Override
			public void actionPerformed(ActionEvent e){
				this.model.extendCount();
                this.view.updateButton();
			}
        });
        
        this.view.setSize(200,200);
        this.view.setVisible(true);
    }
    
    public static void main(String[] args){
    	Controller c = new Controller();
    }
}
```

## Observer

Das Observer Pattern ermöglicht, dass sich Objekte (Observer, beobachtendes Objekt) bei einem anderem Objekt (Subject, beobachtetes Objekt) registrieren und fortan vom diesem informiert werden, sobald es sich ändert.

Für die Observer wird eine einheitliche Schnittstelle (Interface) mit mindestens einer Aktualisierungsmethode definiert. Diese wird vom Subject im Falle von Aktualisierungen aufgerufen und ist in den meisten Fällen mit näheren Daten zur Änderung parametrisiert. Konkrete Observer implementieren das Interface und damit die Aktualisierungsmethode und bestimmen somit, wie der Observer auf die Benachrichtigung reagieren soll.

Das Subject benötigt Administrationsmethoden, damit sich Observer an- und abmelden können. Meldet sich ein Observer an, so nimmt das Subject es in seine Liste der zu benachrichtigen Objekte auf. Treten nun Änderungen am Subjectzustand auf, so werden alle registrierten Observer informiert (notifyObservers()). Dies geschieht, in dem über die Observerliste des Subjects iteriert wird, und auf jedem Observer die Aktualisierungsmethode (update()) aufgerufen wird.

Allgemein kann man sagen, dass das Observer Pattern wie eine Broadcast Nachricht an alle verbundenen Observer ist. Das Subject verwaltet alle Observer und sendet dessen gespeicherte Daten an alle, wenn sich z.B die Daten ändern.

Um auf ein bereits erstelltes System zurückzugreifen werde ich als Beispiel Code einen Observer für ein Chat System zeigen. Das Observer System soll unabhängig davon laufen und nur die Anzahl der verbundenen User an verschiedene Anzeigen übermitteln. Es gibt also ein Subject welches die Anzahl der User speichert und an 2 verschiedene Observer typen senden soll. Einmal werden die Daten als Konsolen Output angezeigt und einmal als JOptionPane. Es sind also 3 Klassen und ein Observer Interface notwendig.

```Java
public class ChatSubject { 

    private List observerList = new ArrayList<ChatObserver>(); 
    
    private int useranzahl = 25;

    public void register(ChatObserver pNewObserver){ 
        observerList.add(pNewObserver); 
    } 

    public void unregister(ChatObserver pNewObserver){ 
        observerList.remove(pNewObserver); 
    } 

    protected void notifyObservers(){ 
        for (ChatObserver observer : observerList) { 
            observer.update(this.useranzahl); 
        } 
    } 
} 
```

```Java
public interface ChatObserver {
	public void update(int useranzahl); 
}

public class KonsolenObserver {
	public void update(int useranzahl){
    	System.out.println("Es sind derzeit "+ useranzahl +" User verbunden");
    }
}

public class JOptionObserver {
	public void update(int useranzahl){
    	JOptionPane.showMessageDialog(null,"Es sind derzeit "+ useranzahl +" User verbunden");
    }
}
```

Um das ganze in der Verwendung zu zeigen habe ich noch eine Client Klasse erstellt.

```Java
public class Client { 

    public static void main(String[] args) { 
        ChatSubject chatSubject = new ChatSubject(); 
        chatSubject.register(new KonsolenObserver()); 
        chatSubject.register(new JOptionObserver()); 

        chatSubject.setState(77);
    } 
    
}
```

## Decorator

Das Decorator Design Pattern ermöglicht das dynamische Hinzufügen von Fähigkeiten zu einer Klasse. Dazu wird die Klasse, dessen Verhalten wir erweitern möchten (Component, Komponente), mit anderen Klassen (Decorator, Dekorierer) dekoriert (vgl. engl. "to wrap": umhüllen). Das heißt der Decorator umschließt (enthält) die Component. Der Decorator ist vom selben Typ wie das zudekorierende Objekt, hat somit die gleiche Schnittstelle und kann an der selben Stelle wie die Component benutzt werden. Er delegiert Methodenaufrufe an seine Component weiter und führt sein eigenes Verhalten davor oder danach aus.

Eine Component kann mit beliebig vielen Decorators dekoriert werden, um so seine Fähigkeiten immer weiter auszubauen.

Realisiert wird das Pattern beginnend mit einer abstrakten Superklasse (oder einem Interface) AComponent. Sowohl die konkreten Components als auch alle Decorators sind von diesem Typ. AComponent definiert weiterhin beliebig viele abstrakte Methoden, die alle konkreten Subklassen implementieren müssen (hier operate()). Die konkreten Components erweitern AComponent direkt und implementieren ihr Basisverhalten. Die abstrakte Klasse ADecorator erweitert AComponent ebenfalls und hält zugleich eine Referenz auf ein (beliebiges) Objekt vom Typ AComponent. Konkrete Decorators erweitern schließlich ADecorator (sind damit auch AComponents) und implementieren ihr Zusatzverhalten (operate()). Darin rufen sie zum einen die Methode(n) (operate()) der AComponent (geerbt von ADecorator) auf und fügen davor oder danach ihr decoratorspezifisches Verhalten hinzu. Da es keine Rolle spielt, ob ihre AComponentreferenz nun eine konkrete Component oder wiederum ein anderer Decorator ist, können Decorators beliebig geschachtelt werden.

Ich werde anhand eines einfachen String Decorates versuchen das Pattern zu erklären

```Java
public abstract class Component { 
    protected String text;
    
    public Component(String text){
    	this.text = text;
    }
    
    public abstract String anzeigen(); 
}
```
```Java
public class StringRueckgabe extends Component {
    
    public StringRueckgabe(String text){
    	super(text);
    }
	
    public String anzeigen() { 
        return this.text; 
    } 
}
```
```Java
public abstract class Decorator extends Component{

	protected Component component;

	public Decorator(Component component,String decoraterText){
    	super(decoratorText);
        this.component = component;
    }
    
}
```
```Java
public class PunktDecorator{

	public PunktDecorator(Component component){
    	super(component,".");
    }
    
    public String anzeigen(){
    	String ausgabe = this.text + this.component.operate + this.text;
        return ausgabe;
    }

}
public class DoppelPunktDecorator{

	public PunktDecorator(Component component){
    	super(component,":");
    }
    
    public String anzeigen(){
    	String ausgabe = this.text + this.component.anzeigen() + this.text;
        return ausgabe;
    }

}
```
```Java
public class Test{
	public static void main(String[] args) { 
    	Component mystring = new StringRueckgabe("BeispielText")
        System.out.println(mystring.anzeigen());
        // Ausgabe: BeispielText
        
        mystring = new PunktDecorator(mystring);
        System.out.println(mystring.anzeigen());
        //Ausgabe: .BeispielText.
        
        mystring = new DoppelPunktDecorator(mystring);
        mystring = new PunktDecorator(mystring);
        System.out.println(mystring.anzeigen());
        //Ausgabe: .:.BeispielText.:.
    }
}

```

## Factory

Das Factory Method Entwurfsmuster dient der Entkopplung des Clients von der konkreten Instanziierung einer Klasse. Das erstellte Objekt kann elegant ausgetauscht werden. Oft wird es zur Trennung von (zentraler) Objektverarbeitung und (individueller) Objektherstellung verwendet.

Der Erstellungscode eines Objektes (Product genannt) wird in einer eigenen Klasse (Creator, Factory) ausgelagert. Dieser Creator ist abstrakt und delegiert die konkrete Objektinstanziierung wiederrum an seiner Unterklasse. Erst die Unterklasse entscheidet welches Product erstellt wird. Da der Client sich komplett auf Abstraktion stützt (sowohl beim Creator als auch bei den Products), ist er vollkommen von den Implementierungen entkoppelt und unabhängig.

Der Creator ist abstrakt, und kennt nur die abstrakte Schnittstelle vom Product und instanziiert nicht ein konkretes Productobjekt, sondern lässt seine Unterklassen entscheiden, welches konkrete Product erzeugt werden soll. Dazu definiert es eine abstrakte Methode (die namensgebende factoryMethod()), die es in seiner createProduct()-Methode aufruft und die seine Unterklassen implementieren müssen. Unterklassen (ConcreateCreators) implementieren diese Methode und geben ein ConcreteProduct zurück.

Nachdem die Unterklasse des Creators das konkrete Product an den Creator zurückgegeben hat, kann der Creator noch allgemeinen Herstellungscode enthalten, die auf jedes Product angewandt werden muss, bevor es an den Client geliefert wird.

Der Creator kann beliebig erweitert werden (ConcreteCreatorB, ConcreateCreatorC) und somit verschiedene Products liefern.

```Java
public abstract class Creator { 

    public Product createProduct() { 
        //holt konkretes Product, weiß nicht welches. 
        Product product = factoryMethod(); 

        //allgemeiner Productherstellungscode 
        product.setState(23); 
        product.prepare(); 
        return product; 
    } 

    protected abstract Product factoryMethod(); 
} 

class ConcreteCreatorA extends Creator { 

    protected Product factoryMethod() { 
        ConcreteProductA concProd = new ConcreteProductA(); 
        //ggf. noch das ConcreateProductA bearbeiten... 
        return concProd; 
    } 
} 

class ConcreteCreatorB extends Creator { 

    protected Product factoryMethod() { 
        ConcreteProductB concProd = new ConcreteProductB(); 
        //ggf. noch das ConcreateProductB bearbeiten... 
        return concProd; 
    } 
} 
```
```Java
public abstract class Product { 

    private int basisState; 

    public void prepare() { 
        System.out.println("preparing general Product"); 
    } 

    public void setState(int pState) { 
        basisState = pState; 
    } 

    public int getState() { 
        return basisState; 
    } 

    public abstract int getPrice(); 
    //further code 
} 

class ConcreteProductA extends Product { 

    @Override 
    public int getPrice() { 
        return 1400; 
    } 
    //further code 
} 

class ConcreteProductB extends Product { 

    @Override 
    public int getPrice() { 
        return 2200; 
    } 
    //further code 
} 

class ConcreteProductC extends Product { 

    @Override 
    public int getPrice() { 
        return 800; 
    } 
    //further code 
} 
```
```Java
public class Client { 
    public static void main(String[] args) { 
        Creator creator = new ConcreteCreatorA(); 
        Product product = creator.createProduct(); 
        System.out.println(product.getPrice()); 
    } 
}
```

## Strategy

Das Verhalten (Funktionalität, Algorithmus) eines Objekts (dem Context) in eine eigene Strategieklasse (Strategie = gekapselter Algorithmus) ausgelagert. Der Context hält eine Referenz auf sein Strategieobjekt und wenn er das ausgelagerte Verhalten ausführen soll, so delegiert er den Aufruf an sein referenziertes Strategieobjekt. Der Context arbeitet dabei nicht mit einer konkreten Implementierung, sondern mit einer Schnittstelle. Er ist damit implementierungsunabhängig und kann somit mit neuen Verhalten ausgestattet werden, ohne dass sein Code dafür geändert werden muss. Einzige Bedingung ist, dass die neue Strategie das Strategyinterface korrekt implementiert.

Weiterhin kann durch die Auslagerung des Verhaltens auch andere (verwandte) Contextklassen die Strategien wiederverwenden und müssen sie nicht selbst implementieren.

Der Client kann folglich das Verhalten eines Contextobjekts sowohl zur Designzeit als auch zur Laufzeit dynamisch ändern.

- Verhalten wird contextunabhängig
- Context wird implementierungsunabhängig.

Ein einfaches und gutes Beispiel hiefür ist die Ausgabe eines Textes. Während der Laufzeit soll geändert werden das der Text nicht auf der Konsole sondern als JOptionPane ausgegeben wird. Das Pattern wird also angewendet auf die Ausgabe selbst.

```Java
interface Ausgabe { 
    public void show(String text); 
} 

class KonsolenAusgabe implements Ausgabe{ 
    public void show(String text) { 
        System.out.println(text); 
    } 
} 

class JOptionAusgabe implements Ausgabe { 
    public void show(String text) { 
        JOptionPane.showMessageDialog(null,text); 
    } 
}
```

```Java
class Textausgabe { 

    String text = "Text";
    Ausgabe ausgabe = new KonsolenAusgabe();


    public void setAusgabe(Ausgabe ausgabe) { 
        this.ausgabe = ausgabe; 
    } 

    public void ausgeben(){
        ausgabe.show(this.text); 
    } 
} 
```

```Java
public class Client { 
    public static void main(String[] args) { 
        Textausgabe ausgabe = new Textausgabe();
        ausgabe.ausgeben();
        //"Text" in der Konsole.
        
        ausgabe.setAusgabe(new JOptionAusgabe());
        ausgabe.ausgeben();
        //"Text" als JOptionPane Message
    } 
} 
```