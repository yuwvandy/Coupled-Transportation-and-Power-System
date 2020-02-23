# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:43:07 2020

@author: wany105
"""
class system(object):
    """System object: network of networks
    """
    def __init__(self, name, networks, inters = None):
        self.name = name
        self.networks = networks
        self.inters = inters
        
    def Zlevel(self):
        """Assign each network a Z coordinate so that we can plot them in different level
        """
        
        self.Zlevel = {}
        for i in range(len(self.networks)):
            self.Zlevel[self.networks[i].name] = i*50 
            
        
    def Systemplot3d(self):
        """Plot the whole system in 3D dimension
        XY coordinates are exactly the same while Z coordinate of each network is shifted a little bit
        Interdependence is linked among different networks in different planes
        """
        from mpl_toolkits import mplot3d
        import matplotlib.pyplot as plt
        import numpy as np
        
        fig = plt.figure(figsize = (15, 10))
        ax = fig.add_subplot(111, projection = '3d')
        
        self.Zlevel()
        
        #Within networks
        for i in range(len(self.networks)):
            network = self.networks[i]
            ##Plane Coordinates
            x = np.arange(250, 3200, 1)
            y = np.arange(250, 3200, 1)
            x, y = np.meshgrid(x, y)
            z = np.array([[self.Zlevel[network.name]]*len(x)]*len(y), dtype = float)
            
            X = network.Nx
            Y = network.Ny
        
            #Network node plot
            ax.scatter3D(X, Y, self.Zlevel[network.name], depthshade = False, zdir = 'z', marker = 's', color = network.c, label = network.name, s = 40)
            ax.plot_surface(x, y, z, linewidth=0, antialiased=False, alpha=0.05, color = network.c)
        
            #Network edge plot
            for j in range(len(network.linkf)):
                fnode = network.linkf[j] - 1
                tnode = network.linkt[j] - 1
                
                ax.plot([X[fnode], X[tnode]], [Y[fnode], Y[tnode]], [self.Zlevel[network.name], self.Zlevel[network.name]], network.c, lw = 1)   
        
        
        #Among networks
        for i in range(len(self.inters)):
            
            interdependency = self.inters[i]
            network1 = interdependency.network1
            network2 = interdependency.network2
            
            for j in range(network1.Nnum):
                for k in range(network2.Nnum):
                    if(interdependency.adj[j, k] == 1):
                        fnodex, fnodey, fnodez = network1.Nx[j], network1.Ny[j], self.Zlevel[network1.name]
                        tnodex, tnodey, tnodez = network2.Nx[k], network2.Ny[k], self.Zlevel[network2.name]
                        ax.plot([fnodex, tnodex], [fnodey, tnodey], [fnodez, tnodez], interdependency.c, lw = 1)   
        
        #Link Plots
        Normflow = sf.Normalize(network.flow, Type = 'max'):
        for i in range(network.Nnum):
            for j in range(network.Nnum):
                if(network.A[i, j] == 1):
                    
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend(frameon = 0)
    

        
        
        
        
                    
    