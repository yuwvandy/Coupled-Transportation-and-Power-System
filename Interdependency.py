# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:52:42 2020

@author: wany105
"""
import ShareFunction as sf


class Interdependency(object):
    """Establish one type of the Power-Transportation Interdependency:
        Power Provides Electricity to Transportation Signals
    """
    def __init__(self, network1, network2, name, color):
        self.name = name
        ##Network2 depends on Network1, flow moves from network1 to network2
        self.network1 = network1
        self.network2 = network2
        self.c = color

    def distadj(self):
        """Calculate the distance matrix for two networks
        distance matrix D: network1.Nnum \times network2.Nnum
        D[i, j] represents the distance between node i in network1 and node j in network2
        """
        
        self.D = np.zeros([self.network1.Nnum, self.network2.Nnum])
        
        for i in range(self.network1.Nnum):
            for j in range(self.network2.Nnum):
                node1 = np.array([self.network1.Nx[i], self.network1.Ny[i]])
                node2 = np.array([self.network2.Nx[j], self.network2.Ny[j]])
                
                self.D[i, j] = sf.dist(node1, node2)
                
    def dependadj(self, DepenNum):
        """Define the adjacent matrix for the interdependency A of dimension network1.Nnum*network2.Nnum
        A[i, j] = 1: there is an arc from node i in network1 to node j in network2, flow can move from node j in network2 to network1
        A[i ,j] = 0: there is no arc currently
        DepenNum[j]: The number of nodes in network1 that node j relies on
        """
        import math
        self.adj = np.zeros([self.network1.Nnum, self.network2.Nnum])
        for i in range(self.network2.Nnum):
            Index = sf.sortget(list(self.D[:, i]), DepenNum[i])
            self.adj[Index, i] = 1
        
       