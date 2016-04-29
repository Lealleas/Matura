# Python Interpreter (2 vs 3)

Bei der Entwicklung einer Python Applikation sollte sich als erstes die Frage gestellt werden, ob man Python 2.* oder Python 3.* verwendet. Die Antwort auf diese Frage ist nicht immer die selbe ist immer Projektabhängig.

1. Python 2.7 ist ein Standard den es schon laaange gibt.
2. Python 2.7 wird nur noch bis 2020 untrstüzt [[1]](https://www.python.org/dev/peps/pep-0373/#id2)
2. Python 3 hat große Änderungen zur Sprache gebracht die viele Nerds unglücklich gemacht haben
3. Python 3 wird für eine längere Zeit unterstüzt

Im Allgemeinen kann gesagt werden, dass man in den meisten Fällen Python 3 verwenden sollte, da es bei jeder neuen Version neue und verbesserte Module, Sicherheit und Bug Fixes mit sich bringt. Es ist möglich Applikationen zu schreiben die mit Python 2 und für Python 3 funktionieren - die Schwirigkeit davon ist abermals Projektabhängig.

Es gibt genügend Webseiten die bei der Wahl des Interpreters unterstüzten, wie z.B. [caniusepython3.com](caniusepython3.com).

In den folgenden Sektionen werden die großten, für uns relevanten Unterschiede von Python 2 und Python 3 durch Code veranschaulicht.

## Die print Funktion
Eine kleine Änderung die wahrscheinlich am bekanntesten ist. Python 2 verwendet ein so gennantes _print statement_, hingegen verwendet Python 3 die _print()_ Funktion, was bedeutet, dass das auszugebende Objekt in Klammern gesetz werden muss.

Es ist zu beachten, dass Python 2 kein Problem mit zusätzlichen Klammern hat. Python 3 würde aber einen _SyntaxError_ ausgeben bei Aufruf ohne Klammern.

__Python 2__

```python
print 'Python', python_version()
print 'Hello, World!'
print('Hello, World!')
print "text", ; print 'print more text on the same line'
```

```
Python 2.7.6
Hello, World!
Hello, World!
text print more text on the same line
```

__Python 3__

```python
print('Python', python_version())
print('Hello, World!')

print("some text,", end="")
print(' print more text on the same line')
```

```
Python 3.4.1
Hello, World!
some text, print more text on the same line
```

## Integer Division
Diese Änderung ist zu beachten wenn man Code porten will, oder wenn man Python 3 Code mittels Python 2 ausführen will. Das große Problem hierbei ist, dass es keinen Error geben wird (wie z.B. einen _SyntaxError_).

__Python 2__

```python
print 'Python', python_version()
print '3 / 2 =', 3 / 2
print '3 // 2 =', 3 // 2
print '3 / 2.0 =', 3 / 2.0
print '3 // 2.0 =', 3 // 2.0
```

```
Python 2.7.6
3 / 2 = 1
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

__Python 3__

```python
print('Python', python_version())
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)
```

```
Python 3.4.1
3 / 2 = 1.5
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

## Exception Handling
Python 2 unterstüzt beide Notationen, die _alte_ und die _neue_ Syntax. Bei Python 3 muss die Error Message einer Exception in Klammern stehen. 

__Python 2__

```python
print 'Python', python_version()
raise IOError, "file error"
# ODER
raise IOError("file error")
```

```
IOError                                   Traceback (most recent call last)

<ipython-input-9-6f1c43f525b2> in <module>()
----> 1 raise IOError("file error")


IOError: file error
```

__Python 3__

```python
print('Python', python_version())
raise IOError("file error")
```

```
OSError                                   Traceback (most recent call last)

<ipython-input-11-c350544d15da> in <module>()
      1 print('Python', python_version())
----> 2 raise IOError("file error")


OSError: file error
```

Zusätzlich dazu muss bei Python 3 das _as_ Keyword verwendet werden.

__Python 2__

```python
print 'Python', python_version()
try:
    let_us_cause_a_NameError
except NameError, err:
    print err, '--> our error message'
```

```
Python 2.7.6
name 'let_us_cause_a_NameError' is not defined --> our error message
```

__Python 3__

```python
print('Python', python_version())
try:
    let_us_cause_a_NameError
except NameError as err:
    print(err, '--> our error message')
```

```
Python 3.4.1
name 'let_us_cause_a_NameError' is not defined --> our error message
```
