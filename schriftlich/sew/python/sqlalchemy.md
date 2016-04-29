# Datenbankmanagement

Im folgendem Kapitel wird auf dem Umgang mit Datenbankmanagementsystemen und SQLAlchemy eingegangen. [Diese](http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html#sqlalchemy.orm.query.Query.delete) Seite der Dokumentation für SQLAlchemy sollte simultan angesehen werden.

> The Python Database API (DB-API) defines a standard interface for Python database access modules. It’s documented in PEP 249. Nearly all Python database modules such as sqlite3, psycopg and mysql-python conform to this interface.
>
> -- <cite>The Hitchhicker's Guide to Python</cite>

## Verbindungsaufbau

Die folgenden Parameter werden in Form eines connection_strings, also den Einstellungen zum Verbindungsaufbau, an die Databasemanagement Klasse

```python
DATABASE = "wien_wahl"
USERNAME = "wadmin"
PASSWORD = "password"
HOST = "localhost"
WAHLTERMIN = "2015-10-11"
MANDATE = 100

connection_string = 
	'mysql+mysqldb://{username}:{password}@{host}/{database}'
	.format(username=USERNAME,
		 	 password=PASSWORD,
		 	 host=HOST,
	     	 database=DATABASE)
```
Grundsätzlicher Aufbau einer Verbindung:

```python
# Aufbau mittels Einstellungen im connection_string
self.engine = create_engine(connectionstring)
# Erstellen einer Verbindung
self.conn = self.engine.connect()

# Im allgemeinen ist eine Session ein Objekt welches mit
# welchen wir mit der Datenbank über Queries kommunizieren. 
# Hierfür werden die Tabellen mit allen Eigenschaften 
# als Python Objekte abgespeichert.
self.session = Session(self.engine)

# Tabellen Objekte mittels der von SQLAlchemy gebotenen Funktion.
self.Base = automap_base()
self.Base.prepare(self.engine, reflect=True)

# Datenbanktabellen als Python Objekte
self.Election = self.Base.classes.election
self.Constituency = self.Base.classes.constituency
self.District = self.Base.classes.district
self.JudicalDistrict = self.Base.classes.judicaldistrict
self.Party = self.Base.classes.party
self.Candidacy = self.Base.classes.candidacy
self.Votes = self.Base.classes.votes
self.TotalVotes = self.Base.classes.totalvotes
self.Projection = self.Base.classes.projection
self.ProjectionResult = self.Base.classes.projectionresult

```
## CRUD Befehle

Im allgemeinen kann also gesagt werden, dass mittels den Tabellen Objekten eine Query erzeugt wird und diese an die Session geschickt wird. Die Session bietet einige Funktionen welche es ermlöglichen Daten in die Datenbank zu speichern. Die Query kann alles mögliche sein, also SELECT, DELETE, INSERT und UPDATE.

```python
# Hier wird mittels self.session überprüft ob das übergebene Election Date in der Datenbank
# aufzufinden ist - also ob richtige Parameter übergeben wurden. Man beachte, dass hier bereits
# mittels den Tabellen Objekten gearbeitet wird.
self.enr = first(self.session.query(self.Election.nr).filter(self.Election.dt == self.electiondate).all())

if self.enr is None:
    raise Exception("Invalid election date")
else:
    self.enr = self.enr[0]

```


```python
"""
Die folgenden Befehle sind gleich einem DELETE Command in SQL.
Es wird mittels den Tabellen Objekten Eine Query erzeugt und diese
wird an mittels der Session umgesetzt.
"""

self.session.query(self.ProjectionResult).filter(self.ProjectionResult.enr == self.enr).delete(synchronize_session=False)
self.session.query(self.Projection).filter(self.Projection.enr == self.enr).delete(synchronize_session=False)
self.session.query(self.TotalVotes).filter(self.TotalVotes.enr == self.enr).delete(synchronize_session=False)
self.session.query(self.Votes).filter(self.Votes.enr == self.enr).delete(synchronize_session=False)
self.session.query(self.JudicalDistrict).filter(self.JudicalDistrict.enr == self.enr).delete(synchronize_session=False)
```

Für das speichern von neuen Daten in die Datenbank wird abermals mittels den Tabellen Objekten
		  eine Query erzeugt und diese mittels der Session an die Datenbank geschickt.
		  Man beachte, dass hierfür zwei Listen von den zum schreiben benötigten Tabellen Objekten erstellt
		  werden. Diese Listen beinhalten also viel Information und werden mittels der Session alle auf
		  einmal in die Datenbank gespeichert.
		  
```python
districts = []     # Liste von Tabellen Objekten 1 
votes = []          # Liste von Tabellen Objekten 2
        


# Iterieren des Parameters, erzeugen der Tabellen Objekte mit den Parametern,
# und hinzufügen zu den Listen. Der Parameter data ist ebenfalls eine Liste. 
for line in data:
    districts.append(
        self.JudicalDistrict(
                enr=self.enr,
                dnr=int(line["BZ"]),
                nr=int(line["SPR"]),
                electivecnt=int(line["WBER"]),
                invalidcnt=int(line["UNG"]),
                votecnt=int(line["ABG"])
        )
    )

    for party, pnr in parties.items():
            votes.append(self.Votes(
                enr=self.enr,
                dnr=int(line["BZ"]),
                jdnr=int(line["SPR"]),
                pnr=pnr,
                cnt=int(line[party])
            ))

# Abspeichern der beiden Listen mit den Tabellen Objekten
self.session.bulk_save_objects(districts)
self.session.bulk_save_objects(votes)
self.session.commit()
```

Im allgemeinem können Daten aus der Datenbank geholt werden indem wir die Tabellen Objekte an die Session schicken und ein _.all()_ machen. Selbstverständlich können auch die bereits gezeigten _.filter()_ Methoden verwendet werden.

```python
parties = {}
for party in self.session.query(self.Party).all():
	parties[party.nr] = party.abbr
```

Man kann logischerweise auch selber Queries in Form von Strings schreiben und diese dann mittels der Query ausführen.

```python
query = "SELECT * FROM tab1;"
result = self.session.execute(query)
```
## Umgang mit Stored Routines

Gehen wir davon aus, dass in der Datenbank folgende sotred Routine vorhanden ist:

```sql
DELIMITER //
CREATE PROCEDURE create_projection(IN enr INT, IN ts TIME)
BEGIN
	-- Irgendwelche Operationen
END; //
DELIMITER ;
```
Um nun diese Routine zu verwenden muss folgender Code vorhanden sein:

```python
connection = self.engine.raw_connection()
cursor = connection.cursor()
cursor.callproc("create_projection", [self.enr, self.ts])
cursor.close()
connection.commit()
self.session.commit()
```