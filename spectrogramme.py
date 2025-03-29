import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def afficher_spectrogramme(fichier_audio):
    
    # Charger le fichier audio
    taux_echantillonnage, donnees = wavfile.read(fichier_audio)

    # Si le fichier est stéréo, le convertir en mono
    if len(donnees.shape) == 2:
        donnees = donnees.mean(axis=1)

    # Normaliser les données pour éviter le dépassement de plage
    donnees = donnees / np.max(np.abs(donnees))

    # Générer le spectrogramme avec la colormap "viridis" qui est plus douce
    plt.figure(figsize=(12, 6))
    Pxx, freqs, bins, im = plt.specgram(donnees, Fs=taux_echantillonnage, NFFT=1024, noverlap=512, cmap='viridis')

    # Limiter l'affichage des fréquences entre 0 et 2500 Hz
    plt.ylim(20, 5000)

    # Ajuster les limites de la barre de couleur pour rendre l'intensité moins lumineuse
    
    plt.clim(-40, 0)  # Limite d'intensité (en dB), ajustez selon vos besoins

    # Ajouter une barre de couleur pour montrer l'intensité en décibels
    plt.colorbar(im, label='Intensité (dB)')

    # Ajouter les titres et labels
    plt.title("Spectrogramme")
    plt.xlabel("Temps (s)")
    plt.ylabel("Fréquence (Hz)")

    # Afficher le graphique
    plt.show()

# Spécifiez le chemin vers votre fichier audio
fichier_audio = r'C:\Users\maxim\Documents\lycée\TIPE\Codes\EGALISEUR\audio.wav'
afficher_spectrogramme(fichier_audio)
