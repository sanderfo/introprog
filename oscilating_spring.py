import numpy as np
import matplotlib.pyplot as plt

A = -0.3 # Setter A = -0.3 da den trekkes ned, så får i positiv retning opp
k = 4 # resten her er gitt i oppgaven
gamma = 0.15
m = 9

t_array = np.zeros(101) # Fyller arrays med nuller
y_array = np.zeros(101)


# a)
for i in range(len(t_array)): # for-loops for å fylle arrays
    t_array[i] = 25*i/100 # Triks for å få jevnt fordelte t-verdier fra 0 til 25
    y_array[i] = A*np.exp(-gamma*t_array[i])*np.cos(np.sqrt(k/m)*t_array[i]) #y-verdier fra formelen




# b) Den pythoniske løsningen:
t_array2 = np.linspace(0, 25, 101) #linspace for samme formål
y_array2 = A*np.exp(-gamma*t_array)*np.cos(np.sqrt(k/m)*t_array) #bruker arrays direkte

plt.plot(t_array, y_array) #Plotter første arrayene
plt.plot(t_array2, y_array2) # Andre
plt.xlabel("Tid i sekunder")
plt.ylabel("Posisjon i meter fra ekvilibrium")
plt.show()


"""
Terminal > run oscilating_springs
*plott her*

"""
