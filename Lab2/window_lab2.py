
import matplotlib.pyplot as plt

x = []
y = []

fig, ax = plt.subplots(figsize=(3, 3))
ax.set_aspect('equal')

ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)

ax.set_xticks([])  
ax.set_yticks([])


with open('output.txt', 'r') as file:
    for line in file:
        elements = line.split()
        x.append(int(elements[0])) 
        y.append(int(elements[1]))
        
    ax.scatter(x, y, color='black', marker='o', s=1)


plt.grid(True)
plt.show()




