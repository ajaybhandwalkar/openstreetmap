from flask import Flask, render_template, request
from plot_sites_on_map import PlotSitesOnMap


app = Flask(__name__)

plot_points_obj = PlotSitesOnMap()


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route("/map", methods=['POST'])
def mapdata():
    org = request.form.get('org')
    print(org)
    if org:
        return render_template("map.html", org=org)




