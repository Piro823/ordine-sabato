caseificio_ascoli=["bufala ligatti", "bufala ligatti bocconcini", "bufala leoni","gorgonzola dolce","caciotta mista" ]

amount_ascoli=[6, 6, 4, 2, 2]
			
        
def ordine_ascolano():
    voci={}
    for x, y in zip(caseificio_ascoli, amount_ascoli):
        while True:
            try:
                rimasta=int(input(f"{x} :"))
                if 0 <= rimasta <=y :
                    break
                else :
                    print(f"Errore! Inserisci valore dei pezzi rimasti,un numero compreso tra {0} e {y}")
            except ValueError:
                print("Errore! Scrivi il numero dei pezzi rimasti.")
        necessaria= y - rimasta
        voci[x]=necessaria 
        print(f"{x} :  {necessaria}")	
    return voci

ordine=ordine_ascolano()
print("Buongiorno, agente_ascoli ecco l'ordine per la settimana prossima,buon fine settimana:")
for x in caseificio_ascoli:
    format_ascoli =(f"{x} : {ordine[x]}")
    print(format_ascoli)     




