
#Script per l'ordine del fine settimana, chiunque può eseguirlo solo basandosi sui prodotti rimasti davanti ai suoi occhi
#La necessità nasce dalle settimane di ferie, in cui il personale ridotto, risente la mancanza di chi si occupa  di quest mansioni.
#Si piuò evitare di disturbare un collega in ferie ;).
#REGOLE DI UTILIZZO :il programma chiede all'utente una riga alla volta di inserire l quantità di prodotto rimasta in magazzino.
#In questo modo il programma calcola la quantità di prodotto da ordinare.

print("REGOLE DI UTILIZZO : Scrivi il quantitativo rimasto del prodotto richiesto" )
print("ORDINE CASEIFICIO MOIANO")
from ordine_sabato_moiano import ordine_estivo_moiano


print( "ORDINE CASEIFICIO PORTO SANT'ELPIDIO")
from ordine_sabato_p_s_elpidio import ordine_estivo_p_s_elpidio_kg
from ordine_sabato_p_s_elpidio import ordine_estivo_p_s_elpidio_pezzi


print("ORDINE CASEIFICIO ASCOLI")
from ordine_sabato_ascolano import ordine_ascolano


print("ORDINE CASEIFICIO BELFORTE")
from ordine_sabato_belforte import ordine_belforte




	



