# EJ_MA_Prototype

Problem: 
M&A Analysten benötigen zu viel Zeit um wichtige Kenndaten aus Notizen von Meetings zu sammeln wie bspw. in der Fallstudie Q&A.

Nutzen:
Spart Zeit, Analysten müssen nicht mehr das gesamte pdf durchgehen sondern nur an spezifischen Stellen nachschlagen.

Setup in 5 Schritten: 
1. Run python script
2. Klicke die pdf Datei an die bearbeitet werden soll
3. Wiedergabe wichtigster Kennzahlen aus dem Text mit kurzem Kontext (Seitenzahl)
4. Beende Program und öffne die pdf. Datei auf dem Laptop um die Seitenzahlen nachzuschlagen
5. Sammle wichtige Kennzahlen die benötigt werden

Designentscheide:
Beim ersten Skript musste man die pdf Datei in den Ordner kopieren wo das Script war und es hat nur mit einer einzigen spezifischen pdf funktioniert. Ausserdem wurde der Text abgehackt angezeigt. Dementsprechend wurde das Programm angepasst damit es mit mehreren Pdfs funktioniert und im terminal graphisch besser angezeigt wird. Das Terminal benötigt wenig Leistung und gibt die Daten sehr schnell wieder. 

Grenzen:
Jeder der das Script verwendet muss selbst in VS Code oder PyCharm eine Datei erstellen und den Code Copy pasten und das programm runnen damit dann lokal gespeicherte pdfs gelesen werden können. Hier würde es sich eventuell anbieten eine Webaplikation daraus zu machen damit man nicht immer Pycharm offen haben muss und es einfacher zugänglich ist.

Zeitaufwand: 3h

KI-Notiz: 
Ich habe den Code mit Google Gemini generiert und sozusagen prompt-engineering betrieben und mich mit der KI ausgetauscht bis alle Probleme behoben waren.
Geprüft wurde einfach in dem man das Program selber ausführt auf dem Laptop.

Anmerkung:
Github hat nur max 25MB Videodateien zugelassen, daher nur ein 30s Video
