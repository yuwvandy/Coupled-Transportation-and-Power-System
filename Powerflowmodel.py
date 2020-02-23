# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:22:17 2020

@author: wany105
"""
from graph import Graph
from PowerNetwork import Power
import ShareFunction as sf
from docplex.mp.model import Model
import numpy as np
from collections import defaultdict

class PowerFlowModel:
    ''' Power FLOW ASSIGN MODEL
        Cplex solver is used to perform linear optimization
    '''
    def __init__(self, network):
        self.__network = network
    
    def load(self, psignal = None, interdependency = None):
        '''Calculate the load of other network on this network
        '''
        self.load = interdependency.loadnetwork1(psignal)
        
    def optimizationprob(self, cost = None):
        '''Set up the linear optimization problem to initial the flow based on the demand value
        '''
        self.mdl = Model('powerflow')
        self.flowsetup()
        self.flowconstraint()
        self.objection(cost)
    
    def flowsetup(self):
        '''Define flow of each link for later optimization to use
        '''
        self.PFflow = np.zeros([self.__network.Nnum, self.__network.Nnum], dtype = object)
        self.flowlist = []
        
        for i in range(self.__network.Enum):
            node1 = self.__network.linkf[i]
            node2 = self.__network.linkt[i]
            exec('f{}_{} = self.mdl.continuous_var(name = "Pf{}_{}")'.format(node1, node2, node1, node2))
            self.PFflow[node1 - 1, node2 - 1] = eval('f{}_{}'.format(node1, node2))
            self.flowlist.append([node1 - 1, node2 - 1, eval('f{}_{}'.format(node1, node2))])
            
    def flowconstraint(self):
        '''Define constraint on flow by flow conservation
        '''
        for i in range(self.__network.Nnum):
            if(i != 0):
                self.mdl.add_constraint(self.mdl.sum(self.PFflow[:, i]) - self.mdl.sum(self.PFflow[i, :]) == self.load[i])
    
    def objection(self, cost):
        '''Define the objective function for the flow optimization
        Calculate the cost to transport single unit flow along the link
        '''
        
        linkcost = self.__network.D/1000*cost #cost/km
        self.obj = self.mdl.sum(self.flowlist[i][2] * linkcost[self.flowlist[i][0], self.flowlist[i][1]]\
                for i in range(len(self.flowlist)))
        
        self.mdl.minimize(self.obj)
    
    def reportopt(self):
        '''Print the optimization information
        Objective function, constraint, variables to be programmed
        '''
        print(self.mdl.export_to_string())
        
    def solve(self):
        '''solve the linear programming and report
        '''
        self.reportopt()
        
        print("\nSolving model....")
        self.msol = self.mdl.solve(log_output = True)
        self.msol.display()
        
        self.solexport()
        
    def solexport(self):
        '''Create the flow matrix tracking down the solution for the intial flow optimization
        '''
        self.__network.flow = np.zeros([self.__network.Nnum, self.__network.Nnum])
        for flow in self.flowlist:
            self.__network.flow[flow[0], flow[1]] = flow[2].solution_value
        
            
                

        
        