caseificio_moiano= ["mozzarella di bufala intera", "mozzarella di bufala bocconcini", "mozzarella di vacca", "provola affumicata",  ]

amount_moiano=[14, 14, 6, 2]

			
        
def ordine_estivo_moiano():
    voci={}
    for x, y in zip(caseificio_moiano, amount_moiano):
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

ordine=ordine_estivo_moiano()
print("Buongiorno, agente_moiano ecco l'ordine per la settimana prossima,buon fine settimana:")
for x in caseificio_moiano:
    format_moiano =(f"{x} : {ordine[x]}")
    print(format_moiano)  
print("ricottine di vacca", 16)   

if __name__=="__main__":
    ordine= ordine_estivo_moiano()
    

