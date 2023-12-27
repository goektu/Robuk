# Robuk
A driven Ising model, with multiple first-order and second-order phase transitions.

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

# How to link first-order and second-order phase transitions:
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

To create a coupling between the cell and its neighborhood states, the update rule is reversed. Instead of a neighborhood updating a cell, a cell's state dictates the neighborhood states.

<p align="center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/1a0815cb-b8a5-4d24-8e36-1ab49632150c" alt="image" width="50%" height="auto" align= "center">
  <img src="https://github.com/goektu/Robuk/assets/154448923/9525906f-b608-489d-b03d-5cc6298bb9c3" alt="image" width="30%" height="auto" align= "center">
</p>

### Moore and von Neumann Neighborhood Competition

To create the coupling between driving cells, competition in cell neighborhoods are established. To define von Neumann and Moore neighborhoods, von Neumann is a cross-type 4-neighbor space, and Moore is a square-type 8-neighbor space.

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

