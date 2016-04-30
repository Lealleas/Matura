# JUnit

JUnit ist ein Framework das einem Entwickler ermo ̈glicht, relativ schnell Unittests zu schreiben und zu jedem Zeitpunkt eine Sammlung von Tests—eine sogenannte Testsuite—automatisch ablaufen zu lassen.

JUnit bietet unter anderem verschiedene Methoden (wie z.B., assertTrue(), assertFalse(), assertEquals()) , um leicht Bedingungen im Code nachzupru ̈fen und viele Annotationen (Anno- tationen erfordern allerdings Java 5) womit man Methoden als Test, Setup, Teardown oder Ignored auszeichnen kann.

Um eine Klasse zu testen, werden in der Regel folgende Methoden erstellt:

• eine Setup-Methode, die alle no ̈tigen Objekte anlegt und auf den fu ̈r den Test no ̈tigen Aus- gangszustand bringt.
• eine Reihe von Tests, die die eigentlichen Tests beinhalten.
• eine Teardown-Methode, um aufzuräumen.

Mittels einer GUI ist es dann möglich die Tests automatisch ablaufen zu lassen, um sich die Ergebnisse und Ursachen im Falle eines Fehlschlags anzeigen zu lassen.

```Java
import org.junit.Test;
import static org.junit.Assert.*;

public class JUnitHelloWorld { 
	@Test
	public void testHelloWorld () {
		String s = "HelloWorld";
		assertEquals("Just a test to see if everything works ...", "HelloWorld", s);
	} 
}
```