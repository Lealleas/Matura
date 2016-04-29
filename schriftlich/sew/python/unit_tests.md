# Code Testung

Eine Testung der Funktionalität des Codes ist sehr wichtig. Es sollte eine Angewohnheit sein den Code für die Testung und die eigentliche Implementierung parallel zu entwickeln.

Einige grundsätzliche Regeln/Vorschläge zum Testen sind:

- Ein Unit Test sollte sich auf einen möglichst kleinen Teil einer Funktion der Applikation fokusieren und deren richtigkeit uberprüfen
- Jeder Test muss von einander unabhängig sein. Die Entsprechenden vorkehrungen hierfür sollten in den Methoden _setUp()_ und _tearDown()_ durchgeführt werden.
- Für die Namensgebung der Methodennamen der Testfunktionen sollten möglichst lange und beschreibende Namen gewählt werden. So sollte z.B. für die Methode _square()_ die entsprechende Testfunktion gleich _test\_square\_of\_number\_2()_

## Unittest
Das __unitttest__ Modul ist die Standard Libary für Testung in Python. Die API ist jener in Java und C++ sehr ähnlich.

Um einen Test-Case zu erstellen muss _unittest.TestCase_ überschrieben werden.

```python
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
```

## Mock
Die _unittest.mock_ libary erlaubt es Objekte von Testungen zu erzeugen. Ab der Python Version 3.3. ist die Libary standardmäßig integriert, ansonsten muss es über pip installiert werden.

Grundsätzlich werden _Mock_ und _MagicMock_ Objekte erstellt welche alle Attribute und Methoden der originalen Objekts haben. Diese neuen Objekte können konfiguriert werden und Dinge wie die Return Values oder die Sichbarkeit von Attributen können gesetzt werden.

```python
>>> from mock import MagicMock
>>> thing = ProductionClass()
>>> thing.method = MagicMock(return_value=3)
>>> thing.method(3, 4, 5, key='value')
3
>>> thing.method.assert_called_with(3, 4, 5, key='value')
```
