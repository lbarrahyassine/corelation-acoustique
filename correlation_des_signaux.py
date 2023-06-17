import numpy as np
import matplotlib.pyplot as plt

def FIC(signal1, signal2):
    n = len(signal1)
    correlation = []
    for i in range(-n + 1, n):
        if i < 0:
            signal1_decale = signal1[-i:] if -i < n else np.array([])
            signal2_decale = signal2[:n + i] if n + i > 0 else np.array([])
        else:
            signal1_decale = signal1[:-i] if i < n else np.array([])
            signal2_decale = signal2[i:] if -i < n else np.array([])

        if len(signal1_decale) > 0 and len(signal2_decale) > 0:
            correlation.append(np.sum(signal1_decale * signal2_decale))
        else:
            correlation.append(0)
    return np.array(correlation)

t = np.linspace(0, 1, 100)
frequence = 10
amplitude = 1
signal1 = amplitude * np.sin(2 * np.pi * frequence * t)

retard = 25
signal2 = np.concatenate((np.zeros(retard), signal1[:-retard]))

correlation_resultat = FIC(signal1, signal2)

plt.subplots_adjust(hspace=0.9)
plt.subplot(3, 1, 1)
plt.plot(t, signal1)
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.title('Signal 1')

plt.subplot(3, 1, 2)
plt.plot(t, signal2)
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.title('Signal 2')

plt.subplot(3, 1, 3)
plt.plot(range(-len(signal1) + 1, len(signal1)), correlation_resultat)
plt.xlabel('retard')
plt.ylabel('Corrélation')
plt.title('corrélation du signal')

plt.figure(figsize=(10,6))
plt.plot(range(-len(signal1) + 1, len(signal1)), correlation_resultat)
plt.grid()
plt.show()
