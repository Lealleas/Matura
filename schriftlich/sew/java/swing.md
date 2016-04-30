# Swing

[toc]

##Fenster und Dialoge

|Klasse| Kurzbeschreibung |
|--------|--------|
|    JFrame    |   Dieses Hauptfenster bildet die Grundlage der meisten GUIs. Es zeichnet sich durch eine Men&uuml;leiste aus.     |
|JDialog|Ein Dialogfenster, das in der Regel nur einfache und nur wenige Bedienelemente besitzt und &uuml;ber keine Men&uuml;leiste verf&uuml;gt. Es ist immer abh&auml;ngig von einem anderen Fenster. Der meistverwendete Anwendungsfall ist als Modal, sprich als zusatz Informationsfenster. Bei einem Modal können keine anderen Fenster ausgewählt werden! |
|JColorChooser|Ein Dialog, &uuml;ber das aus einer Farbpalette eine Farbe ausgew&auml;hlt werden kann, wie man es aus Grafikprogrammen kennt. Dieser kann in einen JDialog oder JFrame integriert werden.|
|JFileChooser|Mit dem JFileChooser k&ouml;nnen Dateien ausgew&auml;hlt werden. Dieser wird daher meistens eingesetzt, um Dateien zu &ouml;ffnen oder zu speichern.|
|JOptionPane|Das JOptionPane ist wahrscheinlich einer der bekanntesten Dialoge. Es wird oft f&uuml;r Fehlermeldungen oder Benutzerbest&auml;tigungen verwendet ( z.B. &quot;Wollen Sie wirklich l&ouml;schen?&quot;)|

Code Beispiel JFrame
```Java
// import undso
 
public class NicesFrame {
     public static void main(String[] args){             
        JFrame myFrame = new JFrame("Nices Frame");          
        myFrame.setSize(200,200);
        myFrame.add(new JLabel("Boah! Ist das ein Label?"));
        myFrame.setVisible(true);
    }
}
```

Code Beispiel JDialog
```Java
// import undso
 
public class NicerDialog {
    public static void main(String[] args) {
        JDialog myDialog = new JDialog();
        myDialog.setTitle("Nicht so nicer Error");
        myDialog.setSize(200,200);
        myDialog.setModal(true);
        myDialog.add(new JLabel("Da is was kaputt bruder");
        myDialog.setVisible(true);
    }
}
```

Code Beispiel JColorChooser

```Java
//import undso
 
public class FarbRadSoGrossWieRiesenRad{
    public static void main(String[] args){
        Color eineFarbe = JColorChooser.showDialog(null, 
            "Nimm dir was du brauchst bruder!", null);
        System.out.println(eineFarbe);
    }
}

//wobei.

public static Color showDialog(Component component, String title, Color initialColor) throws HeadlessException
```
Code Beispiel JFileChooser

```Java
//import undso
 
public class OpenSeFile{
    public static void main(String[] args){
        JFileChooser chooser = new JFileChooser();
        int back = chooser.showOpenDialog(null);
        
        if(back == JFileChooser.APPROVE_OPTION){
            System.out.println("Die zu öffnende Datei ist: " +
                  chooser.getSelectedFile().getName());
        }
    }
}
```
Beispiel JOptionPane
```Java
//import undso

public class PutandShow{
    public static void main(String[] args){
    	String ganzwichtig = JOptionPane.showInputDialog("Sag mir was!")
        JOptionPane.showMessageDialog(null,"Aha! "+ganzwichtig+ " also.")
    }
}
```
## Menüs
| Klasse | Kurzbeschreibung |
|--------|--------|
|JMenuItem|    Ein JMenuItem stellt einen Menüpunkt (Eintrag in einem Menü) dar, also z.B. "Datei öffnen" oder "Beenden".    |
|JMenu|Das JMenu ist ein Container für JMenuItems, welchem beliebig viele JMenuItems hinzugefügt werden können. "Datei" in der Menüleiste Ihres Browsers oder Textverarbeitungsprogramm wäre ein Beispiel für ein JMenu.|
|JMenuBar|Die JMenuBar ist die gesamte Menüleiste eines Fensters. Sie kann beliebig viele JMenus enthalten.|
|JCheckBoxMenuItem|Ein JCheckBoxMenuItem ist dem JMenuItem ähnlich, allerdings besitzt es zusätzlich ein Kontrollkästchen (Checkbox). Beim Anklicken wird das Häkchen gesetzt bzw. entfernt. JCheckBoxMenuItems werden z.B. häufig zur Aktivierung bzw. Deaktivierung von Fensterinhalten benutzt.|
|JRadioButtonMenuItem|	Ähnlich dem JCheckBoxMenuItem, allerdings werden hier Optionsfelder (Radiobutton) verwendet. In der Regel sind mindestens zwei JRadioButtonMenuItems vorhanden, die die Optionen repräsentieren, zwischen denen ausgewählt werden soll.|
|JPopupMenu|Bei dem JPopupMenu handelt es sich um das sogenanntes Kontextmenü, welches beim Betätigen der rechten Maustaste erscheint.|
|JSeperator|Trennstrich, um das Menü optisch zu gliedern. Dient dazu, vor allem längere Menüs übersichtlich zu gesalten.|

CodeBeispiel JMenuBar + JMenu + JMenuItem + JSeperator
```Java
//import undso

public class JMenuBeispiel {
    public static void main(String[] args) {
        JDialog myDialog = new JDialog();
        myDialog.setTitle("JMenuBar für unser Java Tutorial Beispiel.");
        myDialog.setSize(450,300);
        
        JMenuBar bar = new JMenuBar();
        
        JMenu menu = new JMenu("File");
        JMenuItem save = new JMenuItem("Save");
        JMenuItem save_as = new JMenuItem("Save As");
        JMenuItem open = new JMenuItem("Open")
        JSeparator sep = new JSeparator();
        
        menu.add(open);
        menu.add(sep);
        menu.add(save);
        menu.add(save_as);
        
        bar.add(menu);
        
        myDialog.setJMenuBar(bar);
        myDialog.setVisible(true);
    }
}
```
Das JPopupMenu ist im prinzip genau das selbe wie ein JMenu. Hier können auch genauso JMenuItem's aller variation eingefügt werden. Wie schon beschrieben ist der einzige unterschied, dass nicht über die JMenuBar darauf zugegriffen wird sondern über einen Rechtsclick. Wichtig ist das dieses Menu auch auf Visible gesetzt werden muss und dieses eine Location braucht.

```Java
JPopupMenu pop = new JPopupMenu();
pop.setLocation(100,100);
pop.setVisible(true);
```

## Container
| Klasse | Kurzbeschreibung |
|--------|--------|
|JPanel|Standard-Container|
|JTabbedPane|Verwaltet mehrere andere Container über Registerkarten.|
|JSplitPane|Ein zweigeteilter Container (horizontal oder vertikal), Größe der Teilung veränderbar|
|JScrollPane|Ermöglicht das Scrollen innerhalb eines Containers. Wird häufig bei Tabellen verwendet.|
|JToolBar|Werkzeugleiste, die man beliebig mit Icons für einen schnellen Zugriff auf bestimmte Funktionen ausstatten kann.|
|JDesktopPane|Ein JDesktopPane kann interne Fenster enthalten (JInternalFrame).|
|JInternalFrame|Wird üblicherweise einem JDesktopPane hinzugefügt.|
|JLayeredPane|Unterscheidet sich vom JPanel darin, dass die Ebene der enthaltenen Komponenten angegeben werden kann, so dass diese z.B. in den Vorder- bzw. Hintergrund geschoben werden können.|

Das sind die möglichkeiten die geboten werden. Um eineser dieser Panels zu erstellen/anzuzeigen muss zuerst ein JFrame erstellt werden. Danach wird eine Instanz des Containers erstellt. Alle anzuzeigenen Objekte werden in den Container mit `.add(...)` hinzugefügt. Am Ende wird noch der Container selbst zum JFrame hinzugefügt.


## Bedienelemente
| Klasse | Kurzbeschreibung |
|--------|--------|
|JLabel|	statischer Text, nicht editierbar|
|JButton|	Schaltfläche (Button)|
|JToggleButton|Schaltfläche, welche zwei Zustände (gedrückt und nicht gedrückt) kennt.|
|JCheckBox|Auswahlkästchen, das, wenn es ausgewählt wurde, mit einem Häkchen oder Kreuz versehen wird.|
|JRadioButton|Schaltfläche zur Auswahl zwischen mehreren Optionen, in der Regel sind sie in einer ButtonGroup angeordnet. Im Gegensatz zur JCheckBox kann nur maximal eine Option selektiert werden.|
|ButtonGroup|Dient der Gruppierung von JRadioButtons. So kann sichergestellt werden, dass tatsächlich nur eine Element aus der Gruppe selektiert wurde.|
|JComboBox|Dropdown-Liste (auch als Auswahlliste oder Listbox bezeichnet), die zur Auswahl eines Elementes aufgeklappt wird. Wenn die JComboBox editierbar ist, kann über ein Textfeld der ausgewählte Wert auch vom Anwender gesetzt werden.|
|JList|Einfache Liste, die mehrere Elemente enthalten kann. Einfach- und Mehrfachauswahl möglich.|
|JTextField|einfache einzeilige Texteingabe|
|JTextArea|einfache mehrzeilige Texteingabe|
|JScrollBar|	Schieberregler zum Scrollen.|
|JSlider|Schieberregler, der mit einer Skala versehen werden kann.|
|JProgressBar|Fortschrittsbalken|
|JFormattedTextField|Textfeld, für welches eine Formatierung (z.B. für  Datumseingaben) festgelegt werden kann.|
|JPasswordField|Textfeld zur Passworteingabe. Für jeden eingegebenen Buchstaben erscheint ein Sternchen oder ein anderer vorgegebener Character.|
|JSpinner|Ähnlich der JComboBox, allerdings klappt die Liste nicht auf, sondern die Navigation durch die Liste erfolgt über Pfeiltasten.|
|JSeperator|einfache Trennlinie|
|JEditorPane|mehrzeiliges Textfeld zur Bearbeitung von formatiertem Text, mit HTML- und RTF-Unterstützung.|
|JTextPane|Spezialisierung von JEditorPane, dient der Bearbeitung und Anzeige grafisch aufbereiteter Texte.|
|JTree|Baumstruktur. Wird häufig verwendet, um Verzeichnisstrukturen abzubilden, wie man es z.B. vom Windows Explorer kennt.|
|JTable|einfache Tabelle, kann auch Texteingaben entgegen nehmen.|

Darauf geh ich nicht ein das ist alles zu viel und zu speziell. Im prinzip einfach das Objekt erzeugen und zu einem Container oder Frame hinzufügen und die Sache hat sich!

## Events und KeyListener

### Events
| Klasse | Kurzbeschreibung |
|--------|--------|
|ActionEvent|Dieses Event wird bei der Aktionsauslösung bestimmter GUI-Komponenten erzeugt (z.B. Betätigen eines Buttons)|
|AdjustmentEvent|Wird bei der Interaktion mit  Komponenten erzeugt, die das Interface Adjustable implementieren (z.B. JScrollBar)|
|FocusEvent|Dieses Event wird erzeugt, wenn eine Komponente den Fokus bekommt oder verliert.|
|ItemEvent|Wird erzeugt, wenn Einträge (Items) von Komponenten, die das Interface ItemSelectable implementieren (z.B. JCheckBox, JComboBox), selektiert oder deselektiert werden.|
|MouseEvent|Wird von einer Komponente erzeugt, wenn die Maustaste gedrückt, losgelassen oder geklickt (drücken und loslassen) wird. Außerdem wird ein MouseEvent generiert wenn der Cursor den nicht verdeckten Teil der Komponente betritt oder verlässt.|
|TextEvent|Ein TextEvent-Objekt wird erstellt, wenn sich der Text einer Komponente wie z.B. eines Textfeldes ändert.|
|WindowEvent|Dieses Event tritt auf, wenn der Zustand eines Fensters sich ändert, also z.B. geöffnet, geschlossen, aktiviert, deaktiviert oder ikonifiziert (auf das Icon reduziert) wird.|


```Java
JButton send = new JButton();
send.addActionListener(new ActionListener(){
	@Override
	public void actionPerformed(ActionEvent e){
		System.out.println("Der Send Button wurde gedrückt!");
	}
});
```

### Listener

```Java
JTextArea temp = new JTextArea();
temp.addKeyListener(new KeyListener() {
	@Override
	public void keyTyped(KeyEvent e) {}

	@Override
	public void keyPressed(KeyEvent e) {
		if(e.getKeyCode() == e.VK_ENTER){
			System.out.println("Enter wurde gedrückt!");
		}else{
        	System.out.println("Eine andere Taste wurde gedrückt!");
        }
	}
	@Override
	public void keyReleased(KeyEvent e) {}
});
```

## Layouts

### FlowLayout
![Beispiel eines FlowLayouts](http://www.java-tutorial.org/upload/image/FlowLayout.PNG)
FlowLayout ist der das Standardlayout für JPanels. Die Komponenten werden in einer Reihe nebeneinander angeordnet. Wenn eine Komponente nicht mehr in die Reihe passt, bildet diese den Anfang einer neuen Reihe.


### BorderLayout
![Beispiel eines BorderLayout](http://www.java-tutorial.org/upload/image/BorderLayout.PNG)
Content Panes von JFrame, JApplet und JDialog verwenden standardmäßig diesen Layout Manager. BorderLayout untergliedert den ContentPane in fünf Bereiche, die sich an den Himmelsrichtungen orientieren (North, East, South, West und Center). Diesen kann jeweils eine GUI-Komponente zugeordnet werden. Wählt man dafür ein JPanel, so kann diesem wieder ein eigener Layoutmanager zugewiesen werden, sodass auch sehr komplexe Hierarchien aufgebaut werden können.
### BoxLayout
![Beispiel eines BoxLayout](http://www.java-tutorial.org/upload/image/BoxLayout.PNG)
Dieser Layout Manager platziert die Komponenten in einer horizontalen oder vertikalen Reihe. Im Unterschied zum FlowLayout wird keine neue Zeile bzw. Spalte angefangen, wenn die Komponente nicht mehr reinpasst. Durch Schachtelung von mehreren BoxLayouts kann man auch komplexere Layouts abbilden.
### CardLayout
![Beispiel eines CardLayout](http://www.java-tutorial.org/upload/image/CardLayout1.PNG)
Bei diesem Layout werden die Komponenten wie Karten auf einem Kartenstapel angeordnet. Wie auch bei Registerkarten wird nur eine Komponente angezeigt. Oft  wird eine JComboBox dazu verwendet, um  zwischen den Komponenten zu wechseln. Auch hier kann das eine Element wieder ein JPanel sein, dem seinerseits ein Layout Manager zugeordnet werden kann.
### GridLayout
![Beispiel eines GridLayout](http://www.java-tutorial.org/upload/image/GridLayout.PNG)
Das GridLayout ordnet die Komponenten in einem Gitternetz aus Zellen an. Alle Zellen sind gleich groß und jede Komponente nimmt genau eine Zelle ein. Lediglich der Zeilen- und Spaltenabstand kann angegeben werden.
### GridBagLayout
![Beispiel eines GridBagLayout](http://www.java-tutorial.org/upload/image/GridBackLayout.PNG)
Dieser Layout Manager ist sehr komplex, aber dafür auch sehr anpassungsfähig, so dass man damit so gut wie jedes Layout abbilden kann. Wie beim GridLayout wird die Oberfläche in ein Raster unterteilt, jedoch können sich Komponenten über mehrere Zellen ausdehnen. Des Weiteren können die Reihen unterschiedliche Breiten und die Zeilen verschiedene Höhen annehmen.