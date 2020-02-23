# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:52:10 2020

@author: wany105
""" 
from graph import Graph
from PowerNetwork import Power
from TransportationNetwork import Transportation
from Powerflowmodel import PowerFlowModel
from Trafficflowmodel import TrafficFlowModel
import Interdependency as interlink
import Tdata as td
import Pdata as pd
from System import system

#Define the traffic network
TXtraffic = Transportation(graph_dict = td.Tadjl, color = td.color, name = td.name, lat = td.lat, lon = td.lon, nodenum = td.nodenum, edgenum = td.edgenum, \
                           O = td.O, D = td.D, nodefile = td.nodefile, edgefile = td.edgefile, Type = td.Type)
#Define the power network
TXpower = Power(graph_dict = pd.Padjl, color = pd.color, name = pd.name, lat = pd.lat, lon = pd.lon, nodenum = pd.nodenum, edgenum = pd.edgenum, \
                nodefile = pd.nodefile, edgefile = pd.edgefile, Type = pd.Type)


##Define the interdependency
TX_TPInter1 = interlink.PTinter1(TXpower, TXtraffic, name = 'TX_PowerSignal', color = 'orange')
TX_TPInter1.distadj()
DepenNum = [2]*TX_TPInter1.network2.Nnum
TX_TPInter1.dependadj(DepenNum)

##Define the power flow
TXPflow = PowerFlowModel(TXpower)
TXPflow.load([100]*TX_TPInter1.network2.Nnum, TX_TPInter1)
TXPflow.optimizationprob(cost = 1)
TXPflow.solve()

##Transportation flow
TXTflow = TrafficFlowModel(td.Tadjl, td.origins, td.destinations, td.demand, td.free_time, td.capacity, td.function, \
                       td.InterType, td.SigFun, td.Cycle, td.Green, td.t_service, td.hd, TXtraffic)

TXTflow.solve(td.accuracy, td.detail, td.precision)

TX_TP = system(name = 'TX_TP', networks = [Tgraph, Pgraph], inters = [TX_TPInter1])
TX_TP.systemplot3d()





