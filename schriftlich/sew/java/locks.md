# Locks

## Dead Lock


Ein Deadlock beschreibt eine Situation wo zwei oder mehr Threads sich für immer blockieren, da sie für immer auf sich gegenseitig warten. Hier ein denkbeispiel:


Lukas und Daniel sind Freunde und vertretten die Meinung immer höflich zu sein. Sie haben gegenseitig eine Regel aufgestellt. Wenn einer der beiden sich verbeugt, dann muss er so lange verbeugt bleiben bis der andere die Chance hat sich auch zu verbeugen. Leider haben die beiden nicht bedacht, dass sie sich auch gleichzeitig verbeugen können und so niemand die Chance hat sich zu verbeugen. Es warten also beide gleichzeitig auf die Chance, dass sich der andere verbeugt und keiner der beiden darf sich aufrichten. In der Software Entwicklung würden wir diesen Zustand Deadlock nennen. Der Lukas wartet auf eine Ressource von Daniel die er aber nie bekommen kann, da Daniel genauso auf eine Ressource von Lukas wartet.

## Starvation

Starvation bedeuted übersetzt verhungern und beschreibt den Zustand eines Threads. Ein Thread1 braucht eine Ressource um fortfahren zu können, jedoch gibt einen gierigeren anderen Thread2 welcher ständig auf diese Ressource zugreift. Der Thread1 verhungert also weil ihm der Thread2 nichts von den Ressourcen abgeben kann. Das Resultat ist das der Thread1 nicht mehr weiterlaufen kann.

## Livelock


Ein Thread1 ist oft von den Handlungen eines anderen Threads2 abhängig. Wenn aber der Thread2 genauso von den Handlung des Thread1 abhängig ist, dann resultiert meistens in einem Livelock. Genau wie bei den Deadlocks wird auch bei Livelocks kein fortschritt gemacht, jedoch passiert dies nicht durch totales anhalten der Threads. Die Threads laufen dabei eher im Kreis und machen immer wieder das selbe weil sie zu beschäftigt sind den anderen zu antworten anstatt weiter zu arbeiten.

Es gibt ein einfaches Denkbeispiel: Zwei Personen versuchen in einem Gang aneinander vorbei zu gehen. Lukas geht zur linken Seite um Daniel vorbei zu lassen, jedoch bewegt sich Daniel zur selben Seite und beide stehen wieder voreinander. Lukas bewegt sich nun auf die rechte Seite und Daniel vorbei zu lassen, jedoch bewegt sich Daniel wieder auf die selbe Seite und beide stehen wieder voreinenander. Dies geht unendlich lange weiter.