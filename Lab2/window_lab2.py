import sys
sys.path.append(r'Lab1')

import matplotlib.pyplot as plt
from Lab1.lab1 import GaussAI
from collections import defaultdict


guass_ai = GaussAI()
x_coordinates = defaultdict(list)
y_coordinates = defaultdict(list)

fig_width = 6 
fig_height = 6  

with open('Lab1/output.txt', 'r') as file:
    for line in file:
        elements = line.split()
        
        color = elements[2]
        x_coordinates[color].append(int(elements[0]))
        y_coordinates[color].append(int(elements[1]))


fig, ax = plt.subplots(figsize=(3, 3))
ax.set_aspect('equal')

#draw rectangles
for zone in guass_ai.zones:
    
    point1_x = zone['mx'] - zone['ox']
    point1_y = zone['my'] - zone['oy']
    
    point2_x = zone['mx'] - zone['ox']
    point2_y = zone['my'] + zone['oy']
    
    point3_x = zone['mx'] + zone['ox']
    point3_y = zone['my'] - zone['oy']
    
    point4_x = zone['mx'] + zone['ox']
    point4_y = zone['my'] + zone['oy']
    
    xpoints = [point1_x, point2_x, point4_x, point3_x, point1_x]
    ypoints = [point1_y, point2_y, point4_y, point3_y, point1_y]
    
    plt.plot(xpoints, ypoints, color='black', linestyle='-')

#draw points
for (xcolor, x), (ycolor, y) in zip(x_coordinates.items(), y_coordinates.items()):
    ax.scatter(x, y, color=xcolor, marker='o', s=1)
    
    
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)

ax.set_xticks([])  
ax.set_yticks([])  

# Show the plot
plt.grid(True)
plt.show()




