import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = 	[7,8,6,11,7]
eating =   	[2,3,4,3,2]
working =  	[7,8,7,2,2]
playing =  	[8,5,7,8,13]

plt.plot([], [], color = 'c', label = "sleeping", linewidth = 5)
plt.plot([], [], color = 'black', label = "eating", linewidth = 5)
plt.plot([], [], color = 'b', label = "working", linewidth = 5)
plt.plot([], [], color = 'r', label = "playing", linewidth = 5)

plt.stackplot(days, sleeping, eating, working, playing, colors = ['c', 'black', 'b', 'r'])

plt.xlabel("days")
plt.ylabel("time")
plt.legend()
plt.title("Stackplot")
plt.show()