def affichage(tab):
    print(tab[0],tab[1],tab[2])
    print(tab[3],tab[4],tab[5])
    print(tab[6],tab[7],tab[8])
        

def jouer(tab,compteTour ): 
    position=int(input("Sur quelle case jouer ? [1-9]"))
    while(tab[position-1]=="X" or tab[position-1]=="O"):            #
        print("Case déjà jouée, veuillez en sélectionner un autre.")
        position=int(input("Sur quelle case jouer ? [1-9]"))
    if(compteTour%2==0):tab[position-1]="X"
    else : tab[position-1]="O"
    affichage(tab)



def victoire(tab):
    if((tab[0]==tab[1] and tab[1]==tab[2]) or (tab[3]==tab[4] and tab[4]==tab[5]) or (tab[6]==tab[7] and tab[7]==tab[8])    #victoire horizontale
        or (tab[0]==tab[3] and tab[3]==tab[6]) or (tab[1]==tab[4] and tab[4]==tab[7]) or (tab[2]==tab[5] and tab[5]==tab[8]) #victoire verticale
        or (tab[0]==tab[4] and tab[4]==tab[8]) or (tab[2]==tab[5] and tab[5]==tab[6]) ):                                     #victoire diagonale
        return True
    return False

def grilleComplete(nbTour):
    if(nbTour==9):return True
    return False


def tictactoe():
    grille=[ 1,2,3,4,5,6,7,8,9]
    compteTour=0
    gagner=False
    fullGrid=False
    while( not gagner and not fullGrid):
        jouer(grille,compteTour)
        compteTour+=1
        gagner=victoire(grille)
        fullGrid=grilleComplete(compteTour)
    if(fullGrid): print("Dommage !")
    elif (compteTour%2==0): print("Victoire du joueur ", 2," !")
    else : print("Victoire du joueur ", 1," !")
    
tictactoe()

#Pour l'adapter au Puissance 4 il faudra changer
#les conditions de victoires pour qu'elles fonctionnent pour 4 valeurs
#et la grille pour qu'elle soit en 4x4