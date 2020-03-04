# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:28:02 2020

@author: wany105
"""

class Hurricane(object):
    def __init__(self, name, network, Latitude, Longitude):
        self.name = name
        self.network = network
        self.lat = Latitude
        self.lon = Longitude
    
    def fileimport(self, data):
        '''import information about the hurricane:
        Location, Longitude, Latitude, Wind Pressure, Wind Speed
        '''
        import pandas as pd
        
        CSV = pd.read_csv(data)
        
        self.Infoextract(CSV)
    
    def Infoextract(self, CSV):
        '''Extract hurricane information
        '''
        self.Nlon = np.array(CSV['Longitude'])
        self.Nlat = np.array(CSV['Latitude'])
        self.wp = np.array(CSV['Wind Pressure'])
        self.ws = np.array(CSV['Wind Speed'])
    
    def Basemap(self, Type):
        """Geographical Map within certain locations.
        The location is given by some longitude and latitude interval
        """
        import os
        os.environ['PROJ_LIB'] = r"C:\Users\wany105\AppData\Local\Continuum\anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share"
        
        from mpl_toolkits.basemap import Basemap #Basemap package is used for creating geography map
        from matplotlib import pyplot as plt
        import numpy as np
        
        latinter = self.lat[1] - self.lat[0]
        loninter = self.lon[1] - self.lon[0]
        
        if(Type == 'local'):
            self.Base = Basemap(projection = 'merc', resolution = 'l', area_thresh = 1000.0, lat_0=0, lon_0=0, llcrnrlon = self.lon[0], llcrnrlat = self.lat[0], urcrnrlon = self.lon[1], urcrnrlat = self.lat[1])
        elif(Type == 'whole'):
            self.Base = Basemap(resolution = 'l', area_thresh = 1000.0, lat_0=0, lon_0=0, llcrnrlon = self.lon[0], llcrnrlat = self.lat[1], urcrnrlon = self.lon[1], urcrnrlat = self.lat[1])
        
        plt.figure(figsize = (20, 10))    
        self.Base.drawcoastlines()
        self.Base.drawcountries()
        self.Base.drawmapboundary()
        self.Base.drawparallels(np.arange(self.lat[0] - latinter/5, self.lat[1] + latinter/5, latinter/5), labels=[1,0,0,1], fontsize = 10)
        self.Base.drawmeridians(np.arange(self.lon[0] - loninter/5, self.lon[1] + loninter/5, loninter/5), labels=[1,1,0,1], fontsize = 10)
        
    def verticexy(self, filename, Type, townlat, townlon):
        '''load node coordinates information from CSV
        '''
        import numpy as np
        
        self.fileimport(filename)
        self.Basemap(Type)
        
        townx, towny = self.Base(townlon, townlat)
        self.Base.scatter(townx, towny, marker = 'D', color = 'red', s = 200)

        self.Nx, self.Ny = self.Base(self.Nlon, self.Nlat)
        self.Base.plot(self.Nx, self.Ny, marker = 'D', color = 'm')
        

        