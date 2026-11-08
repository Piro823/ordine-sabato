caseificio_p_s_elpidio_kg = ["mozzarella fiordilatte (kg)", "mozzarella treccia (kg)" ]
caseificio_p_s_elpidio_pezzi=["bufala campana", "burrata" , "stracchino"]
 

amount_p_s_elpidio_kg=[ 6, 2,]
amount_p_s_elpidio_pezzi=[8, 5, 8]



#per questo ordine ho diviso in due categorie i prodotti
#alcuni prodotti vengono calcolati in base al peso, altri in base al numero dei pezzi.

def ordine_estivo_p_s_elpidio_kg():
      while True:
            try:
                  fiordilatte_rimaste=int(input("mozzarella fiordilatte (kg) : "))
                  trecce_rimaste= int(input("mozzarella treccia (kg) : "))
                  trecce_necessarie=(2-trecce_rimaste)
                  
                  if 0<=fiordilatte_rimaste <=2 and 0<= trecce_rimaste <=2 :
                        fiordilatte_necessaria = 6 
                        print(f"mozzarella fiordilatte (kg) : {fiordilatte_necessaria}")
                        print(f"mozzarella treccia :  {trecce_necessarie}")
                        break
                  elif 3<=fiordilatte_rimaste <= 6 and 0<= trecce_rimaste<=2:
                        fiordilatte_necessaria= 3
                        print (f"mozzarella fiordilatte (kg): {fiordilatte_necessaria}")
                        print(f"mozzarella treccia :  {trecce_necessarie}")
                        break
                  else: 
                        print(f"Errore! Un numero compreso tra {0} e {6} fiordilatte,un numero compreso tra {0} e {2} trecce")            
            except ValueError:
                  print("Errore! Scrivi il numero dei pezzi rimasti.")
      return trecce_necessarie, fiordilatte_necessaria
trecce_necessarie, fiordilatte_necessaria= ordine_estivo_p_s_elpidio_kg()





def ordine_estivo_p_s_elpidio_pezzi():
    
    while True:
        try:
            errore_1=f"Errore! Inserisci valore dei pezzi rimasti,un numero compreso tra {0} e {8}"
            errore_2=f"Errore! Scrivi il numero dei pezzi rimasti."
            bufala_rimasta=int(input("bufala campana : "))
            if 0<= bufala_rimasta <= 8:
                bufala_necessaria = 8 - bufala_rimasta
                print(f"bufala campana : {bufala_necessaria}")
                break
            else:
                print(errore_1)
        except ValueError:
            print(errore_2)

    while True:
        try:   
            burrata_rimasta=int(input("burrata  : "))
            if 0<= burrata_rimasta <= 2:
                burrata_necessaria= f"burrata :  {3}"
                print(burrata_necessaria)
                break
            elif 3<=burrata_rimasta<=5:
                burrata_necessaria= 0
                print(burrata_necessaria)
                break 
            else:
                print(f"Errore! Inserisci valore dei pezzi rimasti,un numero compreso tra {0} e {5}")
        except ValueError:
            print(errore_2)


    while True:
        try:
            stracchino_rimasto=int(input(f"stracchino : "))	
            if 0<= stracchino_rimasto <=3:
                stracchino_necessario=(8)
                print(f"stracchino {stracchino_necessario} pezzi ")
                break
            elif 4<= stracchino_rimasto <= 8:
                stracchino_necessario= 4
                print(f"stracchino {stracchino_necessario} pezzi  ")
                break
            else:
                print(errore_1)
        except ValueError:
            print(errore_2)
    return stracchino_necessario, burrata_necessaria, bufala_necessaria

stracchino_necessario, burrata_necessaria, bufala_necessaria= ordine_estivo_p_s_elpidio_pezzi()
                 

               




format_p_s_elpidio ={"mozzarella treccia (Kg)  " : trecce_necessarie,
                     "fiordilatte (Kg) " : fiordilatte_necessaria,
                     "stracchino  " : stracchino_necessario, 
                     "burrata  " : burrata_necessaria,
                     "bufala campana  " : bufala_necessaria}
#in un ciclo for il dizionario stampaa solo le chiavi, in questo caso i nomi senza numeri.
#si può usare items() in questo caso.

print("Buongiorno, agente_p_s_elpidio ecco l'ordine per la settimana prossima,buon fine settimana: ")
for nome , valore in format_p_s_elpidio.items():
    print(f"{nome} : {valore}")
    


if __name__=="__main__" :
    ordine_estivo_p_s_elpidio_kg()
    ordine_estivo_p_s_elpidio_pezzi











