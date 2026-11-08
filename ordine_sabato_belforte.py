caseificio_belforte=["pecorino scodellato", "pecorino caciottone","pecorino canestrato", "pecorino semistagionato", "pecorino formette piccole 800g","caciotta vacca", "sofficella", "mumu", "latte"]

amount_belforte=[ 6, 3, 3, 1, 5, 2, 2, 1 , 2]


	
def ordine_belforte():
    voci={}
    for x, y in zip(caseificio_belforte, amount_belforte):
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

ordine=ordine_belforte()
print("Buongiorno, agente_belforte ecco l'ordine per la settimana prossima,buon fine settimana:")
for x in caseificio_belforte:
    format_belforte =(f"{x} : {ordine[x]}")
    print(format_belforte)    

if __name__=="__main__":
    ordine = ordine_belforte()

