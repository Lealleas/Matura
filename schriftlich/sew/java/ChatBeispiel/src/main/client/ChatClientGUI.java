package main.client;

import javax.swing.*;
import java.awt.*;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * ChatClientGUI
 * A simple GUI for the User
 * <p>
 * Author: Daniel Melichar
 * Date: 05/05/16
 * Version: 1.0
 */



public class ChatClientGUI extends JApplet implements Clients {

    private Socket socket = null;
    private DataOutputStream streamOut = null;
    private ChatClientThread client = null;
    private JTextArea display = new JTextArea();
    private JTextField input = new JTextField();
    private String serverName = "localhost";
    private int serverPort = 5555;

    private Button send = new Button("Send"),
            connect = new Button("Connect"),
            quit = new Button("Bye");

    public void init() {
        JPanel keys = new JPanel();
        keys.setLayout(new GridLayout(1, 2));
        keys.add(quit);
        keys.add(connect);

        JPanel messages = new JPanel();
        messages.setLayout(new BorderLayout());
        messages.add("East", send);
        messages.add("Center", input);

        setLayout(new BorderLayout());
        add("Center", display);
        add("North", keys);
        add("South", messages);

        quit.disable();
        send.disable();
        getParameters();
    }

    public boolean action(Event e, Object o) {
        if (e.target == quit) {
            input.setText(".bye");
            send();
            quit.disable();
            send.disable();
            connect.enable();
        } else if (e.target == connect) {
            connect(serverName, serverPort);
        } else if (e.target == send) {
            send();
            input.requestFocus();
        }
        return true;
    }

    public void connect(String serverName, int serverPort) {
        println("Establishing connection. Please wait ...");
        try {
            socket = new Socket(serverName, serverPort);
            println("Connected: " + socket);
            open();
            send.enable();
            connect.disable();
            quit.enable();
        } catch (UnknownHostException uhe) {
            println("Host unknown: " + uhe.getMessage());
        } catch (IOException ioe) {
            println("Unexpected exception: " + ioe.getMessage());
        }
    }

    private void send() {
        try {
            streamOut.writeUTF(input.getText());
            streamOut.flush();
            input.setText("");
        } catch (IOException ioe) {
            println("Sending error: " + ioe.getMessage());
            stop();
        }
    }

    public void handle(String msg) {
        if (msg.equals(".bye")) {
            println("Goodbye!");
            stop();
        } else println(msg);
    }

    public void open() {
        try {
            streamOut = new DataOutputStream(socket.getOutputStream());
            client = new ChatClientThread(this, socket);
        } catch (IOException ioe) {
            println("Error opening output stream: " + ioe);
        }
    }

    public void stop() {
        try {
            if (streamOut != null) streamOut.close();
            if (socket != null) socket.close();
        } catch (IOException ioe) {
            println("Error closing ...");
        }
        client.close();
        client.stop();
    }

    private void println(String msg) {
        display.append(msg + "\n");
    }

    public void getParameters() {
        //this.serverName = this.getParameter("host");
        //this.serverPort = Integer.parseInt(this.getParameter("port"));
    }
}