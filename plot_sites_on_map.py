import json

import folium
import math
import os


class PlotSitesOnMap:
    def __init__(self):
        self.map_view = []
        self.world = folium.Map(location=[34.051153, -118.244541], zoom_start=10)

    def plot_sites(self, zone):
        counter = 0
        all_data = None
        file = None
        for i in os.listdir("./data"):
            if zone in i:
                file = i

        with open("./data/" + file, "r") as f:
            all_data = json.load(f)

        if "features" in all_data:
            for data in all_data["features"]:

                if "properties" in data and "site" in data["properties"] and "coordinates" in "coordinates" in \
                        data["properties"]["site"] and "latitude" in data["properties"]["site"][
                    "coordinates"] and "longitude" in data["properties"]["site"]["coordinates"] and data["status_check"] == "live":
                    folium.Marker(location=[data["properties"]["site"]["coordinates"]["latitude"],
                                            data["properties"]["site"]["coordinates"]["longitude"]], popup=data["id"],
                                  icon=folium.Icon(color='green')).add_to(self.world)
                if "properties" in data and "site" in data["properties"] and "coordinates" in "coordinates" in \
                        data["properties"]["site"] and "latitude" in data["properties"]["site"][
                    "coordinates"] and "longitude" in data["properties"]["site"]["coordinates"] and \
                        data["status_check"] == "disabled":
                    folium.Marker(location=[data["properties"]["site"]["coordinates"]["latitude"],
                                            data["properties"]["site"]["coordinates"]["longitude"]],
                                  popup=data["id"], icon=folium.Icon(color='red')).add_to(self.world)

                counter += 1
        print(counter)

    def main(self):
        self.plot_sites("lametro")

    def save_in_html(self):
        self.world.save("./templates/site_data.html")


if __name__ == '__main__':
    obj = PlotSitesOnMap()
    obj.main()
    obj.save_in_html()
    print("done")
