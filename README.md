# Robuk
A three-layer neural network Ising model, with multiple first-order and second-order phase transitions. [Code available on Github](https://github.com/goektu/Robuk)

![network-1](https://github.com/goektu/Robuk/assets/154448923/a65897e5-735f-41ab-9704-f2c72ee70efe)


First-order and second-order phase transitions happen at points with exact trigonometric closed-form expressions. 
Transformation of these trigonometric expressions into Boltzmann factor returns a $tan^2(x) + tan(x)$ equation that is plotted straight from the cellular automaton, showing a critical point inside the driven model with the highest number of cells with state 1, and 2D square lattice percolation threshold with the lowest overall energy.  

The equation $arctan^2(x) + 2arctan(x)$, is derived from the model and then used as an activation function. It has a test accuracy of 89.12%, better than Leaky ReLU's previous best 88.92%, while regular $arctan(x)$ activation function only has a test accuracy of 87.62%. These results can be replicated on: https://colab.research.google.com/github/phlippe/uvadlc_notebooks/blob/master/docs/tutorial_notebooks/tutorial3/Activation_Functions.ipynb


[Download Portfolio](https://github.com/goektu/Robuk/files/13787025/Portfolio.pdf)

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

# Index
1. [Definition of the Model](https://github.com/goektu/Robuk/blob/main/README.md#definition-of-the-model)
1. [Definition of Coupling](https://github.com/goektu/Robuk/blob/main/README.md#definition-of-coupling)
1. [Trigonometric Identities](https://github.com/goektu/Robuk/blob/main/README.md#trigonometric-identities)

# Connecting first-order and second-order phase transitions
## Definition of the model

A cellular automaton is a search function around a cell. There is an update rule, which initiates the process of determining the cell's state in the next step of the function.
<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/f3bcc1ca-f6d6-45d2-85b3-4586b009a16b" alt="image" width="30%" height="auto">
</p>

### What is a Driven Model?

General analogy would be driving a car. A tailing car is driving to the frontal car's position, but is forced to leave a trailing distance to avoid crashing. This driving action can be called an **attraction** and the trailing distance is then called **repulsion**. Attraction-repulsion forces plays a major role in the driven model.  
<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/844ca11f-d965-4cd8-b640-cf16ea903d16" alt="image" width="30%" height="auto">
</p>

### Inversing the Update Rule

To initiate a drive command forward between the cell and its neighborhood states, the update rule is reversed. Instead of a neighborhood updating a cell, a cell's state dictates the neighborhood states.

<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/1a0815cb-b8a5-4d24-8e36-1ab49632150c" alt="image" width="50%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/9525906f-b608-489d-b03d-5cc6298bb9c3" alt="image" width="30%" height="auto" align= "center">
</p>

### Moore and von Neumann Neighborhood Competition

Competition between cells in multiple neighborhoods are established to fine tune the model. To define von Neumann and Moore neighborhoods, von Neumann is a cross-type 4-neighbor space, and Moore is a square-type 8-neighbor space.

<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/bdbe2444-4bc2-429b-bc9f-94bbf4f511dc" alt="image" width="30%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/b87ec8b0-caa3-43c3-ace9-acbf3b027df0" alt="image" width="30%" height="auto" align= "center">
</p>

Initially, the cells are placed into driving motion towards right. The cell's state on the right is updated to 1 and on the left is updated to 0 if conditions are met.
On upper and lower neighbors, a shift is introduced between Moore neighborhood into von Neumann neighborhood, which causes cell states to compete with each other, or **frustrate**. 

<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/86f21e31-9dd4-4f91-8da1-3b3e77688392" alt="image" width="40%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/fb7cf47c-8d90-482e-bcec-f24411b94141" alt="image" width="40%" height="auto" align= "center">
</p>

Then, fine tuning of these neighborhoods allows the model to **magnetize**, or return higher density values of cells with value 1, from inverse Ising temperature to the ferromagnetic critical point.

<p align="left">
  <img src="https://github.com/goektu/Robuk/assets/154448923/7b003912-bb32-46fd-bc86-b29242a756bb" alt="image" width="40%" height="auto" align= "left">
  <img src="https://github.com/goektu/Robuk/assets/154448923/3e15562c-bd7b-4363-9bcf-98cf3452ccfd" alt="image" width="40%" height="auto" align= "center">
  <br>
  <img src="https://github.com/goektu/Robuk/assets/154448923/e8c15da6-323b-42a8-baf9-cde7d7091c9f" alt="image" width="40%" height="auto" align= "center">
</p>

Below is the graphical representation of the magnetization. When the *g* values above are kept at 4 or 5, the inverse Ising temperature has the highest cell density. However when *g* values are fixed to 6, the model finds another critical point.

<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/2927720a-e867-4deb-8b3d-99028274dc95" alt="image" width="40%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/f5e6237c-c5dc-44d3-b021-aa6d68cee79c" alt="image" width="40%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/2901abbd-ad0d-40ef-9218-68c1daf6090e" alt="image" width="40%" height="auto" align= "center">
</p>

Now, onto exploration of this behavior. 

## Definition of Coupling

A coupling function is inserted into the cellular automaton. The equation is given as below.

$p(1-p) = \dfrac{1}{8}$, where $\dfrac{1}{8}$ is the Moore neighborhood average *g*. Solving for the equation:

$$ p^2 - p + \dfrac{1}{8} = 0 $$

$$ p = \dfrac{1}{2} \pm \dfrac{1}{2\sqrt{2}} $$ 

<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/736e2620-6468-41ea-a381-7316a1cfe6a2" alt="image" width="50%" height="auto" align= "center">
</p>

When the initial probability *p* is assigned to these roots, with immediate values above (for + root) and below (for - root) first-order phase transition takes place. This is because the values of these roots are coupled. 

<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/1392f43f-180d-4aed-942a-0c8995fb5663" alt="image" width="50%" height="auto" align= "center">
</p>

Example images, from top-left, clockwise:
1. No coupling equation
1. No drive mechanism
1. *+* root
1. Above *+* root
1. Below *-* root
1. *-* root

<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/55887e0c-af3e-46b0-8ba3-0d3c37d8139a" alt="image" width="30%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/c1d54263-a2bb-473d-96d0-1d40afb043f8" alt="image" width="30%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/07c978aa-a52c-4b1c-91d8-526c11c3e35e" alt="image" width="30%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/7f92640f-476c-4b71-bc3a-7244cc4508bb" alt="image" width="30%" height="auto" align= "center">  
  <img src="https://github.com/goektu/Robuk/assets/154448923/a56df567-7c59-456f-a7d5-632240678893" alt="image" width="30%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/c365f329-52ed-4bc6-87ba-3371acd28791" alt="image" width="30%" height="auto" align= "center">   
</p>

As one can tell, the evolution of the coupled system is towards being stretched horizontally in thin line segments. The critical point of the system is then defined as the probability density that can contain the most cells withs state value 1.

## Trigonometric Identities

$cos^2(\pi/8) = \dfrac{1}{2} + \dfrac{1}{2\sqrt{2}} $, and $sin^2(\pi/8) = \dfrac{1}{2} - \dfrac{1}{2\sqrt{2}} $, where $cos^2(\pi/8) - sin^2(\pi/8) = 2sin(\pi/8)cos(\pi/8) = \dfrac{1}{\sqrt{2}} $. 


