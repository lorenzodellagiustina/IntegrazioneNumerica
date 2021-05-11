# Tutorial grafici: https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# Tutorial slider: http://www.math.buffalo.edu/~badzioch/MTH337/PT/PT-matplotlib_slider/PT-matplotlib_slider.html
import matplotlib.pyplot as plt # Libreria grafici
import numpy as np # Libreria per gestire array e matrici
from matplotlib.widgets import Slider # Libreria per slider

# ---------------

# Funzione che andremo a plottare
def f(x, k):
    return k*(x**2)

# ---------------

k_min = 0
k_max = 1
k_init = 0.5

graph_axis = plt.axes([0.1, 0.2, 0.8, 0.65]) # Coordinate left, bottom, width, height
slider_axis = plt.axes([0.1, 0.05, 0.8, 0.05])

# GRAFICO

x = np.arange(0.0, 10.0, 0.1) # Array di punti (con numpy), da 0 a 10 con passo 0.1
plt.sca(graph_axis) # Selezione assi grafico
plt.title('y=kx^2') # Titolo grafico
plt.axis([0, 10, 0, 100]) # Visualizza range da 0 a 10 sulle ascisse e da 0 a 100 sulle ordinate
line, = plt.plot(x, f(x, k_init), 'red') # Crea grafico di f(x) mappando i punti di x
# La virgola alla linea sopra dopo "line" ha un significato preciso in Python, se ti interessa dimmi che ti spiego

# SLIDER

def update(val_k): # Funzione chiamata ogni volta che lo slider si aggiorna
    line.set_ydata(f(x, val_k)) # Ricalcola i punti col nuovo k
    # TODO: modificare la proporzione degli assi in caso, dovrebbe essere fattibile

k_slider = Slider( # Costruisce oggetto slider
    ax = slider_axis,
    label = 'k',
    valmin = k_min,
    valmax = k_max,
    valinit = k_init
)
k_slider.on_changed(update) # Imposta la funzione da chiamare quando lo slider cambia

plt.show() # Mostra grafico e tutto