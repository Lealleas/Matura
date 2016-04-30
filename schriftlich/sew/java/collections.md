#Collections

[toc]

Collections in Java sind in a nut shell Arrays auf steroiden, wobei sich Collections nicht nur auf Listen beschrenken. Die einfachste erklärung wäre eine Ansammlung von einem definierten Datentyp. Diese können verkettet oder anders speziell strukturiert sein.

Es ist grundlegend zwischen folgenden zu unterscheiden:

- Listen
- Sets
- Maps
- Ques

## Listen

Die meist verwendeten Listen Klassen sind Vector, Stack, **ArrayList** und **LinkedList**

### ArrayList

Dies ist im prinzip das selbe wie ein Array wobei bei einer ArrayList die Anzahl der Elemente nicht fix ist. Die Länge der  Liste kann also dynamisch verändert werden. Die Elemente haben wie bei einem Array einen Index und können so aus der Liste abgerufen werden.

Die Wichtigsten Funktionen sind:

```Java
// Dies muss vorher importiert werden!
import java.util.ArrayList;

// Erstellen der Liste
ArrayList<String> aList = new ArrayList<String>();

//Hinzufügen eines Elements an letzter Stelle. (Element hat neuen größten Index)
aList.add("Ich bin gerade Letzter");

//Hinzufügen mit bestimmten Index.
aList.add(2, "Ich bin neuer Letzter");

//Bearbeiten eines Elements
aList.set(1, "Ich bin nicht mehr Letzter");

//Auslesen eines Elements
aList.get(1);

//Entfernen eines Elements
aList.remove(1)

//Rest ist eh speziell also schau DOKU!
```
### LinkedList

LinkedList ist eine Liste wo prinzipiell nur am Anfang und am Ende hinzugefügt wird. Natürlich können auch ähnliche Befehle wie bei einer ArrayList aufgerufen werden nur deckt diese Art von Liste nicht diese Art von Verwendung ab.

Die Wichtigsten Funktionen sind:

```Java
// Dies muss vorher importiert werden!
import java.util.LinkedList;

// Erstellen der Liste
LinkedList<String> lList = new LinkedList<String>();

/****************************
 * Hinzufügen am Anfang/Ende
 ****************************/
lList.addFirst("Ich bin gerade Erster");
lList.addLast("Ich bin gerade Letzter");
//bzw.
lList.add("Ich bin gerade Letzter");

/*************************************************************
 * Bearbeiten eines Elements (Index aufruf nicht recomended!)
 *************************************************************/
aList.set(1, "Ich bin nicht mehr Letzter");

/**************************************
 * Auslesen des ersten/letzen Elements
 **************************************/
lList.getFirst();
lList.getLast()

/***************************************
 * Entfernen des ersten/letzen Elements
 ***************************************/

// nur Entfernen mit removeFirst
lList.removeFirst();
//bzw. entfernen und Daten auslesen mit poll
lList.poll()

// Entfernen mit removeLast
lList.removeLast()
//bzw. entfernen und Daten auslesen mit pop
lList.pop();

//Rest ist eh speziell also schau DOKU!
```

## Sets

Die meist verwendeten Set Klassen sind **TreeSet**, **HashSet** und EnumSet

### TreeSet

> In a Nutshell: Ein dynamischer Array der automatisch sortiert!

![](http://www.java-tutorial.org/upload/image/tree.JPG)
Die oben abgebildete Baumstruktur besitzt drei Ebenen. Der Knoten in der ersten Ebene ist die Wurzel (root). Die Knoten in der zweiten Ebene werden als Äste (branches) bezeichnet, da sie noch Nachfolger haben. Die Knoten der dritten Ebene werden Blätter (leaves) genannt.

Da in dem obigen Bild jeder Vorgänger maximal zwei Nachfolger besitzt, spricht von von einem Binärbaum.

Alle Klassen, die in ein TreeSet eingefügt werden sollen, müssen das Interface Comparable und dessen Methode compareTo implementieren. Durch compareTo können Elemente miteinander verglichen werden. Damit ein Vergleich überhaupt möglich ist, müssen die Objekte im TreeSet vom selben Datentyp sein.

Am einfachsten ist ein Treeset anhand diverser Integer werte zu erklären. Man nimmt an man hat eine Liste von Zahlen die so aussieht: [5,15,17,18,20,22,25,27,30]. Man kann erkennen das 20 das mittelelement ist und somit auch gleichzeitig die Root des Treesets. Alle werte kleiner als 20 werden nun links angezeigt und alle Werte größer als 20 werden rechts angezeigt. Dies gilt auch für alle folgenden Äste wie man bei 15, 30, 18 und 25 sehen kann.

![](http://www.cs.wcupa.edu/rkline/assets/img/DS/bst2.png?1264796754)

```Java
TreeSet<Integer> ts = new TreeSet<Integer>();
        
ts.add(new Integer(27));
ts.add(new Integer(5));
ts.add(new Integer(22));
ts.add(new Integer(15));
ts.add(new Integer(17));
ts.add(new Integer(30));
ts.add(new Integer(18));
ts.add(new Integer(20));
ts.add(new Integer(25));
        
Iterator i = ts.iterator();
        
while(i.hasNext()){
	System.out.println(""+i.next());
}

//Ausgabe [5,15,17,18,20,22,25,27,30];
```

### HashSet

> In a Nutshell: Eine dynamische yolo ansammlung von Daten in irgendeiner Form.

Eine gängige Mengen-Klasse, die das Interface Set implementiert, ist die Klasse HashSet (java.util.HashSet). Die Elemente werden in einer Hash-Tabelle gespeichert, wodurch ein schneller Zugriff möglich ist. Diese Klasse bietet jedoch nur einfache möglichkeiten um die Menge der Daten zu bearbeiten. Mit `.add(object)` kann etwas hinzugefügt werden, mit `.contains(object)` kann überprüft werden ob das angegebene Element vorhanden ist und mit `.remove(object)` kann ein Element entfernt werden. Das HashSet bietet keine direkete Funktion um auf die Elemente zuzugreifen, dafür muss ein Iterator verwendet werden.

```Java
HashSet<String> set = new HashSet<String>();

//Hinzufügen von Elementen
set.add("nice");
set.add("Hallo");
set.add("Welt!");
set.add("Welt!"); // Wird nicht nochmal hinzugefügt!

System.out.println("Das Set ist mit "+set.size()+" Elementen gefüllt.")

if(set.contains("nice")) set.remove("nice")

//Abfragen aller Elemente
Iterator it = set.iterator();
while (it.hasNext()){
        String setText = (String) it.next();
        System.out.println(setText);
}
```

## Maps

Die meist verwendeten Map Klassen sind **TreeMap**, **HashMap** und EnumMap
Maps sind immer eine Form von Key Value Liste. Es kann also gewählt werden welcher Datentyp Key ist und welcher Datentyp Value ist.

### TreeMap

Das selbe wie ein TreeSet nur das nach den Keys geordnet wird. Der Datentyp der Keys muss also comparable sein!

### HashMap

Das selbe wie ein HashSet nur das auf die Daten mit einer Funktion zugegriffen werden kann. (`.get(key)`)

## Ques

Die meist verwendeten Ques Klassen sind PriorityQue und DelayQue

Haben wir als so nicht durchgemacht und werde ich deshalb auch nicht beschreiben