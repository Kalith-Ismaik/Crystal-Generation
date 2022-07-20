#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import pandas as pd
import numpy as np
    
a_lat    = 4.0
r_lat    = a_lat/2

xl = 4             # In Angstrom
yl = 4             # In Angstrom
zl = 4             # In Angstrom

x_coords = []
y_coords = []
z_coords = []

x   = 0.0
y   = 0.0
z   = 0.0
    
#lx = len(x_coords)
lx = math.floor(xl/a_lat) + 1
ly = math.floor(yl/a_lat) + 1
lz = math.floor(zl/a_lat) + 1

while x <= xl:
    
    pos = [x,y,z]
    x_coords.append(pos[0])
    y_coords.append(pos[1])
    z_coords.append(pos[2])

    x += a_lat
    
s = 0
for cc in range(ly-1):

    for i in range(0,lx):
        x = x_coords[i+s]
        y = y_coords[i+s] + (a_lat)
        z = z_coords[i+s]
    
        pos = [x,y,z]
        x_coords.append(pos[0])
        y_coords.append(pos[1])
        z_coords.append(pos[2])
    
    s += (lx)   
    
s = 0   
for cx in range(lz-1):
        
        for i in range(0,lx*ly):
            x = x_coords[i+s] 
            y = y_coords[i+s] 
            z = z_coords[i+s] + (a_lat)
    
            pos = [x,y,z]
            x_coords.append(pos[0])
            y_coords.append(pos[1])
            z_coords.append(pos[2])
        
        s += (lx*ly)
        
s = 0    
for cc in range(0,ly-1):
        
    for i in range(0,lx-1):
        x = x_coords[i+s] + (r_lat)
        y = y_coords[i+s] + (r_lat)
        z = z_coords[i+s] + (r_lat)
    
        pos = [x,y,z]
        x_coords.append(pos[0])
        y_coords.append(pos[1])
        z_coords.append(pos[2]) 
     
    s += lx

s = lx*ly*lz   
for cx in range(lz-2):
        
        for i in range(0,(lx-1)*(ly-1)):
            x = x_coords[i+s] 
            y = y_coords[i+s] 
            z = z_coords[i+s] + (a_lat)
    
            pos = [x,y,z]
            x_coords.append(pos[0])
            y_coords.append(pos[1])
            z_coords.append(pos[2])
        
        s += (lx-1)*(ly-1)    
        
df = pd.DataFrame(list(zip(x_coords,y_coords,z_coords)),
                  columns =['x_coords','y_coords','z_coords'])
coords = df.to_numpy()
np.savetxt('Initial_conf.out', coords)

