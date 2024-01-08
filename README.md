# Robuk
[A three-layer neural network Ising model](https://goektu.github.io/), with multiple first-order and second-order phase transitions. [Code available on Github](https://github.com/goektu/Robuk)

First-order and second-order phase transitions happen at points with exact trigonometric closed-form expressions. 
Transformation of these trigonometric expressions into Boltzmann factor returns a $tan^2(x) + tan(x)$ equation that is plotted straight from the cellular automaton, showing a critical point inside the driven model with the highest number of cells with state 1, and 2D square lattice percolation threshold with the lowest overall energy.  

The equation $arctan^2(x) + 2arctan(x)$, is derived from the model and then used as an activation function. It has a test accuracy of 89.12%, better than Leaky ReLU's previous best 88.92%, while regular $arctan(x)$ activation function only has a test accuracy of 87.62%. These results can be replicated on: https://colab.research.google.com/github/phlippe/uvadlc_notebooks/blob/master/docs/tutorial_notebooks/tutorial3/Activation_Functions.ipynb

# Dependencies
Since the code was written in Python 2.7, it is important to use a legacy software such as Anaconda 2's Spyder
https://repo.anaconda.com/archive/

The code runs with PyCX Simulator and has to be in the same directory with the simulator file. Package can be downloaded from:
https://github.com/hsayama/PyCX or https://pycx.sourceforge.net/

Running on Spyder requires some settings beforehand or it will throw Tkinter errors.

From Tools-Preferences:
1. Run: Execute in a dedicated module
1. IPython console
- Graphics - Graphics Backend: Qt5 
