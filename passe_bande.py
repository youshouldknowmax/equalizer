import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

def creer_filtre_passe_bande(cutoff_bas, cutoff_haut, fs, ordre=4):
    
    """Crée un filtre passe-bande Butterworth"""
    nyquist = 0.5 * fs
    return butter(ordre, [cutoff_bas / nyquist, cutoff_haut / nyquist], btype='band', analog=False)

def afficher_spectres_et_bode(signal, signal_filtre, b, a, fs):
    
    """Affiche :
    1. Le spectre en fréquence (FFT) avant/après filtrage
    2. Le diagramme de Bode (magnitude et phase)
    """
    
    # Calcul de la FFT
    N = len(signal)
    freqs = np.fft.rfftfreq(N, 1/fs)
    spectre_signal = np.abs(np.fft.rfft(signal))
    spectre_filtre = np.abs(np.fft.rfft(signal_filtre))

    # Réponse en fréquence (Bode)
    w, h = freqz(b, a, worN=8000)
    freq_hz = (w / (2 * np.pi)) * fs

    plt.figure(figsize=(12, 8))

    # Spectre du signal (avant/après filtrage)
    plt.subplot(3, 1, 1)
    plt.plot(freqs, spectre_signal, label='Signal Original', alpha=0.7)
    plt.plot(freqs, spectre_filtre, label='Signal Filtré (Passe-Bande)', color='red', alpha=0.7)
    plt.title('Spectre du Signal (Amplitude vs Fréquence)')
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    # Diagramme de Bode - Magnitude
    plt.subplot(3, 1, 2)
    plt.semilogx(freq_hz, 20 * np.log10(abs(h)), 'b')
    plt.title('Diagramme de Bode - Magnitude')
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Gain (dB)')
    plt.grid()

    # Diagramme de Bode - Phase
    plt.subplot(3, 1, 3)
    plt.semilogx(freq_hz, np.angle(h, deg=True), 'g')
    plt.title('Diagramme de Bode - Phase')
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Phase (degrés)')
    plt.grid()

    plt.tight_layout()
    plt.show()

def filtrer_audio(fichier_entree, cutoff_bas, cutoff_haut):
    
    """Applique un filtre passe-bande et affiche les résultats"""
    fs, signal = wavfile.read(fichier_entree)

    # Convertir en mono si stéréo
    if signal.ndim == 2:
        signal = signal.mean(axis=1)

    # Vérifier si les fréquences sont valides
    if cutoff_bas >= cutoff_haut:
        print("Erreur : La fréquence basse doit être inférieure à la fréquence haute.")
        return

    # Créer et appliquer le filtre passe-bande
    b, a = creer_filtre_passe_bande(cutoff_bas, cutoff_haut, fs)
    signal_filtre = lfilter(b, a, signal)

    # Afficher les résultats
    afficher_spectres_et_bode(signal, signal_filtre, b, a, fs)
    
#==========================================================================
# DEBUG
#==========================================================================

# Demande à l'utilisateur le fichier et les fréquences de coupure
#fichier_entree = input("Entrez le chemin du fichier audio (.wav) : ")
#cutoff_bas = float(input("Entrez la fréquence de coupure basse (Hz) : "))
#cutoff_haut = float(input("Entrez la fréquence de coupure haute (Hz) : "))

# Exécuter le filtrage
#filtrer_audio(fichier_entree, cutoff_bas, cutoff_haut)
