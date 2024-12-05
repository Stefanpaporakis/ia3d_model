import numpy as np
import matplotlib.pyplot as plt
import os

def nearest_n(alist,thresh):
    nearest = []
    for a in alist:
        atom_to_a = []
        for b in alist:
            norm = np.sqrt(np.dot(a-b,a-b))
            if norm < thresh:
                atom_to_a.append(b)
        nearest.append(atom_to_a)
    return nearest

def create_channel(v1,v2, nring, radius, num_circle_points,):
    v1,v2 = np.array(v1),np.array(v2)
    channel_points = []


    #create vector along the channel before populating it with rings
    line_vector = v2-v1
    line_length = np.linalg.norm(line_vector)
    if line_length ==0:
        return channel_points
    line_vector /=line_length #normalise

    #make number of rings between atoms based on the ring spacing
    points = np.linspace(0,2,nring)

    #create vectors perpendicular above and below the line vector (will set the rings of channel)
    perp_vector_above = np.array([-line_vector[1],line_vector[0],0])
    if np.allclose(perp_vector_above,0):
        perp_vector_above=np.array([1,0,0]) #needed to make sure line vector isnt parallel to the same axis as the channel
    perp_vector_above /=np.linalg.norm(perp_vector_above)
    perp_vector_below = np.cross(line_vector,perp_vector_above)


    for i in points:
        centre_point = v1+i*line_vector #middle point of each ring
        
        #make cylindrical rings with radius about centre_point 
        angles = np.linspace(0,2*np.pi,num_circle_points,endpoint=False)
        for j in angles:
            point = (centre_point+radius*np.cos(j)*perp_vector_above+radius*np.sin(j)*perp_vector_below)
            channel_points.append(point)
    
    return np.array(channel_points)


fname = "Ia3d_vertices_with_elements.xyz"
alist = np.loadtxt( os.path.join("ia3d",fname), usecols=(1,2,3), skiprows=2 )
elist = np.loadtxt( os.path.join("ia3d",fname), usecols=(0), skiprows=2, dtype=np.str_ )
#print(elist)


# Lattice parameter
d = 12

#Number of rings 
nring = 12


#Theshold distance for nearest neighbour 
thresh = 5

# Radius of the channels (nm)
radius = 0.5

# How many circles are applied to make a ring around atom, the higher the smoother the ring
num_circle_points = 10

a = np.array([1.0,0.0,0.0])*d
b = np.array([0.0,1.0,0.0])*d
c = np.array([0.0,0.0,1.0])*d
alist *= d
#print(alist)

# stretch
xscale = 1.00
alist[:,0] *= xscale

yscale = 1.00
alist[:,1] *= yscale


na, nb, nc = 1, 1, 1   # 5 5 5 will crash VESTA

alist2 = []
for i in np.arange( na ):
    for j in np.arange( nb ):
        for k in np.arange( nc ):
            for ia in np.arange(alist.shape[0]):
                alist2.append( i*a + j*b + k*c + alist[ia,:] )
                if (i==0)and(j==0)and(k==0):
                    elist2 = elist.copy()
                else:
                    print( elist2.shape, elist.shape)
                    elist2 = np.concatenate( (elist2, elist) )

alist = np.array(alist2)
#print( elist2.shape, alist.shape)

#Make nearest neighbours
nearest = nearest_n(alist,thresh)

#Make channels and points between them
channel_points = []
for i, j in enumerate(nearest):
    for k in j:
        points_between = create_channel(alist[i],k,nring, radius, num_circle_points)
        channel_points.extend(points_between)

channel_points = np.array(channel_points).reshape(-1,3) #Had to reshape, only way it worked



#Combine em all together
array = np.zeros( (len(alist)+len(channel_points),4) )
#The original points
array[:len(alist),:3] = alist 
#The channel points
array[len(alist):,:3] = channel_points

elements = np.array(['A']*len(alist)+['C']*len(channel_points))

#
# output an xyz file that vesta can read
#
fname = f"ia3d_{na}_{nb}_{nc}_channels_with_radius.xyz"

f = open(os.path.join("ia3d/results",fname), 'w')
f.write(str(array.shape[0])+"\n")
f.write(fname[:-4]+"\n")
txt = "{x:12.6f}{y:12.6f}{z:12.6f}"
for i in range(array.shape[0]):
    f.write(f" {elements[i]}"+txt.format(x=array[i,0],y=array[i,1],z=array[i,2])+"\n" )
f.close()

