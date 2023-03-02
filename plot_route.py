import json

import folium
import math
import os


class PlotRoute:
    def __init__(self):

        self.world = folium.Map(location=[40.224655, -74.429239], zoom_start=10)
        self.truck_route = [
            {"lat": 40.224655, "long": -74.429239},
            {"lat": 40.240382, "long": -74.463571},
            {"lat": 40.238285, "long": -74.474557},
            {"lat": 40.281253, "long": -74.502023},
            {"lat": 40.304297, "long": -74.496530},
            {"lat": 40.324193, "long": -74.482797},
            {"lat": 40.345129, "long": -74.474557},
            {"lat": 40.378614, "long": -74.462198},
            {"lat": 40.404763, "long": -74.449838},
            {"lat": 40.439263, "long": -74.429239},
            {"lat": 40.466433, "long": -74.414132},
            {"lat": 40.500902, "long": -74.379800},
            {"lat": 40.522828, "long": -74.315255},
            {"lat": 40.544746, "long": -74.294656},
            {"lat": 40.547877, "long": -74.291910},
            {"lat": 40.5400499, "long": -74.534982}
        ]

    def plot_bus_stop_locations(self):
        for stop in self.truck_route:
            folium.Marker(location=[stop["lat"], stop["long"]], icon=folium.Icon(color='blue')).add_to(self.world)
            self.world.save("map.html")


if __name__ == '__main__':
    obj = PlotRoute()
    obj.plot_bus_stop_locations()
