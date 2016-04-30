# Sockets

[toc]

> *Vorsicht! Alle Beispiele wurden ohne Exception Handling gemacht! Davon wird bei wirklicher Umsetzung stark abgeraten!*

Ein Socket ist ein Endpunkt einer zweiweg kommunikation zwischen zwei programmen welche im Netzwerk laufen. Ein Socket kann entweder ein Client oder Server sein. Hierfür werden zwei Klassen von Java bereitgestellt. Einmal ein Socket welcher den Client repräsentiert und einen ServerSocket welcher wie der name schon sagt den Server repräsentiert. Diese Sockets können in Java mittels Stream miteinander kommunizieren.

Grundlegend wird in einer Client Klasse ein Socket erstellt. Dieser Verbindet sich mit einem ServerSocket. Dieser ServerSocket ist in einer Server Klasse welcher dort auch erstellt wird. Der ServerSocket erkennt die eingehende Verbindung da er im Prinzip nur auf eine Verbindung wartet. Der ServerSocket bekommt nun ein neues Socket Objekt für die eingehende Verbindung. Über dieses Socket Objekt am Server kann der Server selbst mit dem Client kommunizieren.

## Client

Ein Client wird, wie schon erwähnt, durch einen Socket repräsentiert. Dieser hat zwei grundlegende Optionen. Einmal die IP Adresse des Servers und zusätzlich den Port des Servers. Ein Socket hat immer einen Input und Output Stream wobei hier zwischen zwei Situationen unterschieden werden muss. Diese Streams sind unterschiedlich je nach dem ob Sie im Client erstellt wurden oder von ServerSocket angenommen werde.

Wenn ein Socket direkt von Client erstellt wird dann ist der InputStream ein Stream der eingehende Nachrichten vom Server bekommt. Der OutputStream ist der Stream an den Nachrichten an den Server gesendet werden können.

Wenn ein Socket vom ServerSocket angenommen werden dann ist der InputStream ein Stream der die eingehenden Nachrichten von Client bekommt. Der OutputStream ist der Stream an den Nachrichten an den Client gesendet werden können.

Beispiel einer Client Klasse:

```Java
//imports undso

public class Client throws Exception{

	public static void main(String[] args){

        String ip = "127.0.0.1";
        int port = "9999";

        Socket socket = new Socket(ip, port);

        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        while(true){
        	JOptionPane.showInputDialog("enter a message");
			System.out.Println(in.readline());
        }
    }
}
```

##Server

Ein Server wird, wie schon erwähnt, durch einen ServerSocket repräsentiert. Dieser wird in einer Server Klasse erstellt. Beim Erstellen dieses Sockets wird lediglich ein Port gebraucht, da die IP Adresse des Systems verwendet wird. Mit diesem ServerSocket kann weiters mit der Funktion `.accept();` auf eine eingehende Verbindung eines Sockets gewartet werden. Wird diese Verbindung eingegangen so gibt diese Funktion einen Socket, sprich den ClientSocket, zurück und dieser kann gespeichert werden. Ist der Server it einem Client verbunden kann gleich wie in der Client Klasse mit dem In bzw. Output Stream des ClientSockets gearbeitet werden. Was was darstellt kann unter der Überschrift Client nachgelesen werden.

Wichtig! Unter dieser Konfiguration kann immer nur ein Client sich mit Server verbinden. Sobald diese Verbindung abgebrochen wurde muss der Server neu gestartet werden!

```Java
//imports undso

public class Server throws Exception{

	public static void main(String[] args){

        int port = "9999";

        ServerSocket serverSocket = new ServerSocket(port);

        Socket clientSocket = serverSocket.accept();
        
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        
        while(true){
        	String input = in.readLine();
            out.println("Server Response:"+input);
        }
    }
}
```
## Server Threads

Möchte man, dass sich mehrere Clients mit einem Server verbinden können, dann muss man mit Threads arbeiten. Hierfür muss die ServerKlasse verändert werden und eine neue ServerThread Klasse erstellt werden. Der Server hat nun nur noch die Aufgabe auf eingehende Verbindungen zu warten und diese zu akzeptieren mit der Funktion `.accept();`. Wurde nun eine Verbindung akzeptiert wird der ClientSocket einer neuen Instanz des neu erstellten ServerThread Klasse übergeben. In diesem wird in der `run()` methode der in bzw. output stream bearbeitet.
```Java
//imports undso

public class Server throws Exception{

	public static void main(String[] args){

        int port = "9999";

        ServerSocket serverSocket = new ServerSocket(port);
        
        ExecutorService es = Executors.newCachedThreadPool();
        
        while(true){
        	Socket clientSocket = serverSocket.accept();
			ServerThread st = new ServerThread(clientSocket);
			System.out.println(clientSocket.getInetAddress()+ " connected!");
			es.execute(st);
        }
    }
}
```
```Java
//import undso

public class ServerThread implements Runnable throws Exception{

	private Socket socket;
    private PrintWriter out;
    private BufferedReader in;
    
    public ServerThread(Socket socket){
    	this.socket = socket;
        this.out = new PrintWriter(this.socket.getOutputStream(), true);
        this.in = new BufferedReader(new InputStreamReader(this.socket.getInputStream()));
    }
    
    @Override
    public void run(){
    	String input = in.readLine();
        out.println("Server Response:"+input);
    }

}
```

## Serialization

Wenn man zwischen Sockets nicht nur einfache Strings herumschicken möchte kann man auch Objekt Instanzen versenden. Hierfür wird einerseits ein Serializable Objekt gebraucht (implementiert Serializable Interface) aber auch andererseits ein `ObjectInputStream` bzw. `ObjectOutputStream`. Das Prinzip der Connection der Sockets ist genau das selbe nur das senden und lesen an des Streams wird mittels `.readObject()` bzw. `.writeObject(object)` druchgeführt!

Code Beispiel:

```Java
//import undso
 
public class Student implements Serializable {
 
    private static final long serialVersionUID = 5950169519310163575L;
    private int id;
    private String name;
 
    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
 
    public int getId() {
        return id;
    }
 
    public void setId(int id) {
        this.id = id;
    }
 
    public String getName() {
        return name;
    }
 
    public void setName(String name) {
        this.name = name;
    }
 
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
 
        Student student = (Student) o;
 
        if (id != student.id) return false;
        if (name != null ? !name.equals(student.name) : student.name != null) return false;
 
        return true;
    }
 
    public int hashCode() {
        return id;
    }
 
    public String toString() {
        return "Id = " + getId() + " ; Name = " + getName();
    }
}
```
```Java
//import undso

public class Client throws Exception {
    private Socket socket = null;
    private ObjectInputStream inputStream = null;
    private ObjectOutputStream outputStream = null;
    private boolean isConnected = false;
 
    public Client() {
 
    }
 
    public void communicate() {
 
        while (!isConnected) {
            socket = new Socket("127.0.0.1", 4445);
            System.out.println("Connected");
            isConnected = true;
            outputStream = new ObjectOutputStream(socket.getOutputStream());
            Student student = new Student(1, "Bijoy");
            System.out.println("Object to be written = " + student);
            outputStream.writeObject(student);
        }
    }
 
    public static void main(String[] args) {
        Client client = new Client();
        client.communicate();
    }
}
```
```Java
//import undso

public class Server throws Exception{
    private ServerSocket serverSocket = null;
    private Socket socket = null;
    private ObjectInputStream inStream = null;
 
 
    public Server() {
 
    }
 
    public void communicate() {

        serverSocket = new ServerSocket(4445);
        socket = serverSocket.accept();
        System.out.println("Connected");
        inStream = new ObjectInputStream(socket.getInputStream());
 
        Student student = (Student) inStream.readObject();
        System.out.println("Object received = " + student);
        socket.close();
 
    }
 
    public static void main(String[] args) {
        Server server = new Server();
        server.communicate();
    }
}

```

## Protokolle?