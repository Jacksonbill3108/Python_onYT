import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
duracion = 1

tiempo = np.linspace(0,duracion,Fs)
F_brazo = 5

senal_perfecta = np.sin(2*tiempo*np.pi*F_brazo)
fig, ax = plt.subplots(2,2)

ax[0,0].plot(tiempo, senal_perfecta, label = "Senal ideal")
ax[0,0].set_title("Senal esperada")

ruido = 0.5 * np.random.normal(size = Fs)
ax[0,1].plot(tiempo, ruido, label = 'Noise')
ax[0,1].set_title("Ruido")

senal_medida = senal_perfecta+ruido
ax[1,0].plot(tiempo,senal_medida, label = 'Senal censada')
ax[1,0].set_title("Sensor")

# Analisis 
v_max = senal_medida.max()
v_min = senal_medida.min()
v_mean = senal_medida.mean()
print(f"Se detecto un pico maximo de: {v_max}\nSe detecto un voltaje minimo de: {v_min}\nEl valor promedio obtenido es: {v_mean}")

umbral = 1.2 
alerta_booleana = senal_medida>umbral 
n_alertas = np.sum(alerta_booleana)
print(f"El sensor detecto picos altos unas: {n_alertas} veces")
voltajes_altos = senal_medida[alerta_booleana]
print(f"Los voltajes altos fueron: {voltajes_altos[:5]}")

N = 10
senal_filtrada = np.convolve(senal_medida, np.ones(N)/N, mode='valid')
tiempo_filtrado = tiempo[:len(senal_filtrada)]
ax[1,1].plot(tiempo_filtrado, senal_filtrada, label = 'Senal limpia')
ax[1,1].set_title("Senal procesada")


plt.tight_layout()
plt.show()