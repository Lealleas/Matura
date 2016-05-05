# GUI Entwicklung mit Qt

Qt ist ein C++ Applikations Framework welches von allen gängigen Betriebssystemen unterstüzt wird (Windows, OS X und Linux). Es gibt einige Python Libaries, wie z.B. PySide und PyQt, welche auf diese C++ Funktionen zugreift (so gennante _bindings_) und somit die Funktinalität auch mit Python verwendet werden kann. Aufgrund dessen muss immer Qt installiert werden und um dann die Module mittels Python zu verwenden, entweder PySide oder PyQt.

Im allgemeinen ist Qt mehr als nur ein GUI Toolkit. Es gibt unter anderem auch Funktionen für Netzwerk Sockets, Threads, Unicode, regex, SQL und OpenGL.

__ACHTUNG:__ Es gibt so gesehen keine gröberen Unterschiede zwischen den Funktionalitäten von PySide und PyQt. Die Auswahl sollte sich daher hauptsächlich auf folgende Kriterien beschränken: Dokumentation, Community, Last Update, vorhandende Beispiele.

In der folgenden Sektion wird der Umgamg mit __PySide__ erklärt. Nachdem es hier um GUI Programmierung geht sollte klar sein, dass das MVC-Pattern verwendet wird.

## Hello World

```python
# Imports
 
# Create the QApplication object
qt_app = QApplication(sys.argv)
 
class HelloWorldApp(QLabel):
    ''' A Qt application that displays the text, "Hello, world!" '''
    def __init__(self):
        # Initialize the object as a QLabel
        QLabel.__init__(self, "Hello, world!")
 
        # Set the size, alignment, and title
        self.setMinimumSize(QSize(600, 400))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('Hello, world!')
 
    def run(self):
        ''' Show the application window and start the main event loop '''
        self.show()
        qt_app.exec_()
 
# Create an instance of the application and run it
HelloWorldApp().run()
```

## Model-View-Control

Im allgemeinem kann zu MVC gesagt werden, dass das Model die eigentlichen Daten beinhaltet, die View für die Visualisierung zuständig ist, und der Controller die Operationen, welche man mit den Daten durchführen kann, managed.

Die einzigen beiden Klassen/Files die für Probleme sorgen könnten sind das Model und der Controller - unter der Annahme, dass die View mittels dem QtDesigner entwickelt wurde. 

Durch Qt wird die Möglichkeit geboten das MVC Pattern komplett umzusetzen: es gibt einige abstrakte Klassen in Form von QXyzModel (z.B. QAbstractTableModel, QProxyModel, QAbstractListModel) welche das Model für unser Pattern sind.

Wir gehen davon aus, dass wir die View im folgendem Format bekommen:

```python
# -*- coding: utf-8 -*-

# Created: Tue Apr 5 19:36:22 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.move(30, 30)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtGui.QTableView(self.centralWidget)
        ...
```

Die View beinhaltet ein Menu mit einigen Unterpunkten welche alle so gennante _actions_ haben. In den meisten Fällen sollte man Keyboard Shorcuts auf diese Actions setzten (auch hier bietet Qt eine Hilfe, bitte nicht _"Ctrl + N"_ als  Parameter übergeben

```python
self.actionOpen = QtGui.QAction(MainWindow)
self.actionOpen.setObjectName("actionOpen")
self.actionOpen.setShortcut(QtGui.QKeySequence.Open)
```

Wir gehen außerdem davon aus, dass die Applikation folgendermaßen gestartet wird

```python
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	controller = MyController()
	controller.show_window()
	sys.exit(app.exec_())
```

Im allgemeinem wird das __Model__ von einem abstrakten Qt-Model erben und die eigentlichen Daten in Form einer Liste [] oder eines Dictionaries {} speichern.

```Python
class MyModel(QAbstractTableModel:
	 def __init__(self, parent, datalist, header, *args):
	 	# Geht aus der Dokumentation hervor
        QAbstractTableModel.__init__(self, parent, *args)
        self.header = []
        self.list = []
        self.set_list(datalist, header)
        
     def set_list(self, datalist, header=None):
     	 # Wir überprüfen die Einräge und setzen unsere
     	 # Listen mit den Daten
        self.list = datalist
        if header is None:
            self.get_header()
        else:
            self.header = header
            
     def get_list(self):
        return self.list

     def get_header(self):
        return self.header

```

Zusätzlich dazu sind im Model alle Operationen die mit den Daten durchgeführt werden können, in Form von Functions geboten. Das bedeutet: Getter-/Setter-Methoden, Duplizieren von Einträgen, usw.

Der __Controller__ managed die Daten des Modells und führt die vom User, durch die View gestellten Anfragen, durch. In den meisten Fällen - da wir hauptsächlich Qt für GUI Programmierung verwenden - wird der Controller ein _QtGui.QMainWindow_ sein. 

Man kann also allgemein sagen, dass der Controller einzelne Funktionen hat, welche die Methoden des Models verwendet um die Daten zu manipulieren und die Methoden der View verwendet um die Daten anzuzeigen.

```python
class MyController(QtGui.QMainWindow):

	def __init__(self, parent=None):
		super().__init__(parent)
		
		 # Aufsetzten der View
		 self.view = Ui_MainWindow()
         self.view.setupUi(self)
         
	     # Aufsetzen des Models
	     self.model = MyModel(self, datalist=[], header=[])   
```

Die Actions einer View müssen mit einer Python Funktion in unserem Controller zugeordnet werden (also, was soll passieren wenn diese Action ausgeführt wird)

```python
# Actions der View auf unsere Funktionen setzen
self.view.actionOpen.triggered.connect(selflopen)
```

Und die Funktio für open könnte dann so aussehen (mit Filemanager):

```python
def open(self):
	try:
		 # Wir holen uns den Namen des Files (und den Pfad)
		 # Man beachte, dass wir hier festlegen, welcher Datentyp angenommen wird (-> Dokumentation von Qt)
		 fileName = QFileDialog.getOpenFileName(
		 			self, 			
		 			self.tr("Open Text File"), os.getcwd(),
					self.tr("Text Files (*.txt)"))[0]
           
          if fileName is not None and fileName is not "":
	       	  # Und updaten unser Model mit den neuen Daten
	          self.model.update(fileName)
	  except FileNotFoundError:
	  		# Eine Qt Error Message
            QtGui.QMessageBox.critical(self, "Read Error",
                                 "Error reading Txt File:\nFile \"" + self.filename + "\" not found!",
                                 QtGui.QMessageBox.Close)
```

Im obrigen Beispiel updaten wir das Model mit einem neuen File, dies könnte so aussehen:

```python
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
```

## Signals und Slots

Im allgemeinen werden Signals und Slots für die Kommunikation zwischen Objekten verwendet. Ein Beispiel hierfür ist ein ganz normaler Button. Beim Klicken des Buttons wird ein Signal gesendet, welches dann ein spezifisches Slot (also in den meisten Fällen eine Python Methode) ausführt. Die Signals des Buttons sind zahlreich: _clicked_, _released_, _hover_ oder eigensgeschriebene. 

Ein simples Beispiel.

```python
from PySide.QtCore import QObject, Signal, Slot
 
class PunchingBag(QObject):
    ''' Represents a punching bag; when you punch it, it
        emits a signal that indicates that it was punched. '''
    punched = Signal()
 
    def __init__(self):
        # Initialize the PunchingBag as a QObject
        QObject.__init__(self)
 
    def punch(self):
        ''' Punch the bag '''
        self.punched.emit()
```

Hier verbinden wir jetzt unser Signal zu dem entsprechendem Slot, welcher dann was macht

```python
@Slot()
def say_punched():
    ''' Give evidence that a bag was punched. '''
    print('Bag was punched.')
 
bag = PunchingBag()
# Connect the bag's punched signal to the say_punched slot
bag.punched.connect(say_punched)
```

Hier führen wir dann alles aus und bekommen folgenden output.

```python
# Punch the bag 10 times
for i in range(10):
    bag.punch()
```

```python
Bag was punched.
Bag was punched.
Bag was punched.
Bag was punched.
Bag was punched.
Bag was punched.
Bag was punched.
Bag was punched.
Bag was punched.
Bag was punched.
```

## Commands und Undo/Redo

Okay, der Blödsinn ist wirklich nicht so schwer. Im allgemeinen ist ein Undo und Redo eigentlich eine Veränderung von Daten auf eine Version die vorab gespeichert wurde. Das heißt konkret, dass wir eine Liste haben in welcher alle Versionen unserer Daten sind. Wir als Qt Entwickler können festlegen wann wir eine neue Version haben wollen und wann wir revertieren (bzw. wieder vorspult). 

Der __QUndoStack__ ist eigentlich eine Liste in welcher alle Versionen gespeichert werden. Mittels dem __QUndoCommand__ können wir genau sagen was passieren sollen wenn wir ein Undo oder ein Redo machen wollen.

Das folgende Beispiel ist recht simple gestalltet, es sollte aber erklären wie man grundsätzlich vorgeht.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import QUndoCommand, QUndoStack

class MyDocument(object):

    def __init__(self):
        self.document = []

    def __repr__(self):
        return repr(self.document)

    def chop(self):
        self.document = self.document[:-1]

    def append(self, item):
        self.document.append(item)


class MyCommand(QUndoCommand):

    def __init__(self, doc, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        self.document = doc

    def undo(self):
        self.document.chop()
        print("undo: {0}, undo-text: {1}".format(self.document, self.text()))

    def redo(self):
        self.document.append(self.text())
        print("redo: {0}, redo-text: {1}".format(self.document, self.text()))


if __name__ == '__main__':
    stack1 = QUndoStack()
    document1 = MyDocument()

    c = MyCommand(document1)
    c.setText("comamnd1")
    stack1.push(c)
    print(stack1.count())

    c = MyCommand(document1)
    c.setText("comamnd2")
    stack1.push(c)
    print(stack1.count())

    stack1.undo()
    stack1.undo()
    stack1.redo()
    print(stack1.count())

    c = MyCommand(document1)
    c.setText("comamnd3")
    stack1.push(c) # command2 gets deleted
    print(stack1.count())
```
Folgendes wird dann ausgegeben

```python
redo: [u'comamnd1'], redo-text: comamnd1
1
redo: [u'comamnd1', u'comamnd2'], redo-text: comamnd2
2
undo: [u'comamnd1'], undo-text: comamnd2
undo: [], undo-text: comamnd1
redo: [u'comamnd1'], redo-text: comamnd1
2
redo: [u'comamnd1', u'comamnd3'], redo-text: comamnd3
2
```


