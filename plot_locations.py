import folium
import math


class PlotPointsOnMap:

    def __init__(self):
        # Takes this co-ordinates as the center of the map and zoom accordingly
        self.pune = folium.Map(location=[18.520804, 73.855337], zoom_start=13)

        self.bus_stops = [
            {"Katraj": {"lat": 18.446981,  "long": 73.858604}},
            {"Swarget": {"lat": 18.499869,  "long": 73.858242}},
            {"Deccan": {"lat": 18.516287,  "long": 73.842758}},
            {"Shivaji Nagar": {"lat": 18.531597,  "long": 73.849592}},
            {"Kothrud": {"lat": 18.507247,  "long": 73.807519}},
            {"Fatima Nagar": {"lat": 18.505240,  "long": 73.900989}},
            {"Magarpatta": {"lat": 18.514112,  "long": 73.932414}},
            {"Koregao Park": {"lat": 18.535516,  "long": 73.911891}},
            {"Viman Nagar": {"lat": 18.565107,  "long": 73.911274}},
            {"Khadki": {"lat": 18.561463, "long": 73.852817}}
        ]
        self.live_sites = ["Katraj", "Swarget", "Kothrud", "Khadki", "Magarpatta", "Koregao Park"]
        self.current_position = None

    def plot_bus_stop_locations(self):
        for bus_stop in self.bus_stops:
            for name, location in bus_stop.items():
                if name in self.live_sites:
                    folium.Marker(location=[location["lat"], location["long"]], popup=name, icon=folium.Icon(color='green')).add_to(self.pune)
                else:
                    folium.Marker(location=[location["lat"], location["long"]], popup=name, icon=folium.Icon(color='red')).add_to(self.pune)

    def plot_current_location(self):
        # self.current_position = {"lat": 18.545822, "long": 73.912112}
        self.current_position = {"lat": 18.512024, "long": 73.831562}
        folium.Marker(location=[self.current_position["lat"], self.current_position["long"]], popup="current location",
                      icon=folium.Icon(color='blue', prefix='fa', icon='car')).add_to(self.pune)

    def degrees_to_radians(self, degrees):
        return degrees * math.pi / 180

    def distance_in_km_between_two_coordinates(self, lat1, lon1, lat2, lon2):
        earthRadiusKm = 6378.14

        dLat = self. degrees_to_radians(lat2 - lat1)
        dLon = self. degrees_to_radians(lon2 - lon1)

        lat1 = self. degrees_to_radians(lat1)
        lat2 = self. degrees_to_radians(lat2)

        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return round(earthRadiusKm * c, 2)

    def calculate_distance_from_current_location_to_bus_stop(self):
        distance_list = []
        for bus_stop in self.bus_stops:
            for name, location in bus_stop.items():
                if name not in self.live_sites:
                    distance = self.distance_in_km_between_two_coordinates(self.current_position["lat"], self.current_position["long"], location["lat"], location["long"])
                    distance_list.append({"bus_stop": name, "distance": distance})
        return distance_list

    def print_distance(self, distance_list):
        for info in distance_list:
            print("Distance from your current location to", info["bus_stop"], "is", info["distance"])

    def near_location(self, distance_list):
        distance_list.sort(key=lambda x: x["distance"])
        for data in distance_list:
            print(f"You are near {data['bus_stop']}. Distance is {data['distance']} KM")
            return
        
    def stops_near_to_you_within_3kms(self, distance_list):
        distance_list.sort(key=lambda x: x["distance"])
        for data in distance_list:
            if data["distance"] <= 3:
                print(f"You are near {data['bus_stop']}. Distance is {data['distance']} KM")
                return

    def main(self):
        self.plot_bus_stop_locations()
        self.plot_current_location()
        distance_list = self.calculate_distance_from_current_location_to_bus_stop()
        self.print_distance(distance_list)
        print()
        self.near_location(distance_list)
        print()
        self.stops_near_to_you_within_3kms(distance_list)

    def save_in_html(self):
        self.pune.save("./Pune_Bus_Stops.html")


if __name__ == '__main__':
    obj = PlotPointsOnMap()
    obj.main()
    obj.save_in_html()
    print("done")
