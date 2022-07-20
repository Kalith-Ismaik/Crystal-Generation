#!/usr/bin/env python
# coding: utf-8

# In[32]:


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
for cc in range(ly-1):
    
    for i in range(0,lx-1):
        x = x_coords[i+s] + (r_lat)
        y = y_coords[i+s] + (r_lat)
        z = z_coords[i+s]
    
        pos = [x,y,z]
        x_coords.append(pos[0])
        y_coords.append(pos[1])
        z_coords.append(pos[2])
    
    s += (lx)
    
lnn = len(x_coords)  

s = 0
for cc in range(lx):
    
    for i in range(0,lx-1):
        x = x_coords[i+s] + (r_lat)
        y = y_coords[i+s] 
        z = z_coords[i+s] + (r_lat)
    
        pos = [x,y,z]
        x_coords.append(pos[0])
        y_coords.append(pos[1])
        z_coords.append(pos[2])
    
    s += (lx)

s = 0
for cc in range(lx-1):
    
    for i in range(0,lx):
        x = x_coords[i+s] 
        y = y_coords[i+s] + (r_lat)
        z = z_coords[i+s] + (r_lat)
    
        pos = [x,y,z]
        x_coords.append(pos[0])
        y_coords.append(pos[1])
        z_coords.append(pos[2])
    
    s += (lx)
    
ln = len(x_coords)
       
s = 0
for cx in range(lz-1):
        
    for i in range(0,lnn):
        x = x_coords[i+s] 
        y = y_coords[i+s] 
        z = z_coords[i+s] + (a_lat)
    
        pos = [x,y,z]
        x_coords.append(pos[0])
        y_coords.append(pos[1])
        z_coords.append(pos[2])
        
    if cx < (lz-2):
        
        for j in range(0,(ln-lnn)):
            x = x_coords[j+s+lnn] 
            y = y_coords[j+s+lnn] 
            z = z_coords[j+s+lnn] + (a_lat)
    
            pos = [x,y,z]
            x_coords.append(pos[0])
            y_coords.append(pos[1])
            z_coords.append(pos[2])
        
    s += ln     

df = pd.DataFrame(list(zip(x_coords,y_coords,z_coords)),
                  columns =['x_coords','y_coords','z_coords'])
coords = df.to_numpy()
np.savetxt('Initial_conf.out', coords)

