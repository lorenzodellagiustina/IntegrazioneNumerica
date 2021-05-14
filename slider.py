# Tutorial grafici: https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# Tutorial slider: http://www.math.buffalo.edu/~badzioch/MTH337/PT/PT-matplotlib_slider/PT-matplotlib_slider.html
import matplotlib.pyplot as plt # Libreria grafici
import numpy as np # Libreria per gestire array e matrici
from matplotlib.widgets import Slider # Libreria per slider
from matplotlib.widgets import TextBox # Libreria per input



# ---------------

# Funzione che andremo a plottare
def f(x, k):
    return k*(x**2)

# ---------------

k_min = 0
k_max = 1
k_init = 0.5
k = k_init

graph_axis = plt.axes([0.1, 0.3, 0.8, 0.65]) # Coordinate left, bottom, width, height
slider_axis = plt.axes([0.1, 0.15, 0.8, 0.05])
input_axis = plt.axes([0.1, 0.05, 0.8, 0.075])

expression = 'x ** 2 + k'

# GRAFICO

x = np.arange(0.0, 10.0, 0.1) # Array di punti (con numpy), da 0 a 10 con passo 0.1
plt.sca(graph_axis) # Selezione assi grafico
plt.title(expression) # Titolo grafico
plt.axis([0, 10, 0, 100]) # Visualizza range da 0 a 10 sulle ascisse e da 0 a 100 sulle ordinate
line, = plt.plot(x, eval(expression), 'red') # Crea grafico di f(x) mappando i punti di x
# La virgola alla linea sopra dopo "line" ha un significato preciso in Python, se ti interessa dimmi che ti spiego

# SLIDER

def update(val_k): # Funzione chiamata ogni volta che lo slider si aggiorna
    k = val_k
    line.set_ydata(eval(expression)) # Ricalcola i punti col nuovo k
    plt.title(expression)
    # TODO: modificare la proporzione degli assi in caso, dovrebbe essere fattibile

k_slider = Slider( # Costruisce oggetto slider
    ax = slider_axis,
    label = 'k',
    valmin = k_min,
    valmax = k_max,
    valinit = k_init
)
k_slider.on_changed(update) # Imposta la funzione da chiamare quando lo slider cambia

# INPUT

text_box = TextBox(input_axis, 'Evaluate')
text_box.set_val(expression)

def submit(expr):
    expression = expr
    ydata = eval(expression)
    line.set_ydata(ydata)
    plt.title(expression)
    #ax.relim()
    #ax.autoscale_view()
    plt.draw()

text_box.on_submit(submit)


plt.show() # Mostra grafico e tutto








"""
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)


def submit(expression):
    ydata = eval(expression)
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()


axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.

plt.show()
"""
