import passe_bas
import passe_haut
import passe_bande

def main():
    
    print("1")
    fichier_entree = r'C:\Users\maxim\Documents\lycée\TIPE\Codes\EGALISEUR\audio.wav'
    
    print("\nChoisissez un type de filtre :")
    print("1 - Passe-Bas")
    print("2 - Passe-Haut")
    print("3 - Passe-Bandes")
    choix = input("Votre choix (1/2/3) : ")

    if choix == "1":
        
        cutoff = float(input("Entrez la fréquence de coupure (Hz) : "))
        passe_bas.filtrer_audio(fichier_entree, cutoff)

    elif choix == "2":
        
        cutoff = float(input("Entrez la fréquence de coupure (Hz) : "))
        passe_haut.filtrer_audio(fichier_entree, cutoff)

    elif choix == "3":
        
        cutoff_bas = float(input("Entrez la fréquence de coupure basse (Hz) : "))
        cutoff_haut = float(input("Entrez la fréquence de coupure haute (Hz) : "))
        
        if cutoff_bas >= cutoff_haut:
            print("Erreur : La fréquence basse doit être inférieure à la fréquence haute.")
        else:
            passe_bande.filtrer_audio(fichier_entree, cutoff_bas, cutoff_haut)

    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()
