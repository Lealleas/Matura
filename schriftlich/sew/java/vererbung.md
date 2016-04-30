# Vererbung

[toc]

##Was ist vererbung prinzipiell?

Wenn man von Vererbung spricht gibt es in Java prinzipiell zwei Klassen, die Superklasse und Subklasse. Die Subklasse bekommt sämtliche Attribute und Methoden der Superklasse wobei jederzeit neue hinzugefügt werden können.

Bei der Vererbung gibt es prinzipiell 3 Typen von Superklassen. Eine normale Klasse, ein Interface und eine Abstracte Klasse. Die normale Klasse vererbt ihre Attribute und Methoden ganz normal, sprich sie können in der Subklasse überschrieben werden bzw. in einem Objekt davon aufgerufen werden. Ein Interace ist nur eine vorgabe welche Attribute und Methoden vorkommen müssen. Dies bedeuted, dass im Interface diverse Attribute und Methoden definiert sein können welche dann in der Subklasse überschrieben werden **müssen**. Ein Interface ist also als solches auch nicht instanzierbar, sprich kein Objekt kann davon erstellt werden. Eine abstracte Klasse ist eine Mischung der beiden. Hier können normale Methoden und aber auch sogenannte abstracte Methoden definiert werden. Somit kann hier der Entwickler angeben welche Methoden wahlweise und welche zwanghaft bei der vererbung überschrieben werden müssen bzw. können.

Wichtig ist auch welche Schlüsselwörter bei den Methoden und Attributen stehen. Es wird alles was public, protected oder nicht definiert ist vererbt. Das Schlüsselwort **private** wird bei der vererbung **nicht** mitgenommen.

Zusätzlich ist wichtig das in Java die Vererbung von Interfaces (falls das überhaupt vererbung heißt, hab ja im prinzip ka) unabhängig ist von der Vererbung vom normalen und abstracten Klassen. Es kann eine Subklasse meherer Interfaces implementieren aber nur von einer Klasse erben.

##Beispiel einer normalen Klasse

```Java
public class normaleKlasse {

	private String abc;
    
    public void eineMethode(){
    	System.out.println("Ich bin eine Methode");
    }
}
```
```Java
public class extends normaleKlasse subKlasse {

	private String abc;
    
    @override
    public void eineMethode(){
    	System.out.println("Ich bin überschriebene Methode");
    }
}
```

##Beispiel für eine abstracte Klasse

```Java
public abstract class abstracteKlasse {

	private String abc;
    
    public void eineMethode(){
    	System.out.println("Ich bin eine Methode");
    }
    
    public abstract void andereMethode();
}
```

```Java
public class extends abstracteKlasse subKlasse {

	private String abc;
    
    @override
    public void andereMethode(){
    	System.out.println("Ich bin eine andere überschriebene Methode");
    }
}
```
##Beispiel für ein Interface

```Java
public interface meinInterface {

	final private String abc;
    
    public void eineMethode();
}
```
```Java
public class implements meinInterface subKlasse {

	private String abc;
    
    @override
    public void eineMethode(){
    	System.out.println("Ich bin eine Methode");
    }
}
```
