# ordine - sabato

Scriptin Python per calcolare  l'ordine del fine settimana.
Chiunque può eseguirlo solo basandosi sui prodotti rimasti in magazzino, nient'altro.
La necessità nasce dalle settimane di ferie, in cui il personale ridotto, risente la mancanza di chi si occupa  di queste mansioni. Si piuò evitare di disturbare un collega in ferie ;).

# REGOLE PER L'UTILIZZO

Il programma chiede all'utente una riga alla volta di inserire la quantità di prodotto rimasta in magazzino.
In questo modo il programma calcola la quantità di prodotto da ordinare.
#  python3 'ordine_sabato_main.py' è il comando che server per avviarlo (Linux o visual studio code)

# Costruzione 
In una prima bozza il programma saltava la riga dove veniva sollevato un ValueError attraverso try/except,
passando direttamente alla successiva.
Per risolvere ho creato dei cicli con While True e break attorno ai singoli input. Se un valore non è accettabile, lo script segnala un Errore scrivendo delle istruzioni per procedere correttamente, richiedendo poi la stessa riga in cui il programma ha riscontrato un errore.
Poi  mi sono accorto di un ulteriore problema, se il numero digitato era troppo grande il valore degli ordini diventava negativo.
Così ho inserito delle condizioni "if ", in modo che il programma potesse continuare solo con dei valori accettabili.
Se i valori non sono accettabili, vengono digitate lettere o l'utente distrattamente salta una riga senza scrivere nulla il programma segnala Errore e una soluzione,ripartendo dalla riga attuale senza perdere progressi.

