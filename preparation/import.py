import os
import json
from dotenv import load_dotenv
from tqdm import tqdm
from supabase import create_client, Client
from shapely import wkt, Point
import pyproj
import sys

load_dotenv("../frontend/.env")

url: str = os.environ.get("VITE_SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(url, key)

if len(sys.argv) == 2:
    path_to_geojson = sys.argv[1]
else:
    raise ValueError("""
    No path to the geojson file was provided. Please provide the file path as an argument when starting the script:
    python3 import.py /tmp/my-super-geo-json-file.json
    """)


projection = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')
def unproject(x, y):
    return projection(x, y, inverse=True)


def create_insert_data(feature):
    geo_coordinates = feature["geometry"]["coordinates"]

    point = unproject(geo_coordinates[0], geo_coordinates[1])
    point_data = "POINT(" + str(point[0]) + " " + str(point[1]) + ")"
    if "inf" in point_data:
        print("SKIPPING tree with coordinates", geo_coordinates[0], geo_coordinates[1])
        return None

    return {
        "location": feature["properties"]["Standort_N"],
        "location_addition": feature["properties"]["Zusatz"],
        "current_number": feature["properties"]["laufende_n"],
        "chopped": feature["properties"]["gefaellt"],
        "trunk_diameter": feature["properties"]["Stammdurch"],
        "crown_diameter": feature["properties"]["Kronendurc"],
        "height": feature["properties"]["Baumhoehe_"],
        "trunk_circumference": feature["properties"]["Stammumfan"],
        "tree_group": feature["properties"]["Baumgruppe"],
        "district_reference": feature["properties"]["ref_distri"],
        "district_number": feature["properties"]["Bezirk_Nr"],
        "district_name": feature["properties"]["Bezirk_Bez"],
        "outside_reference": feature["properties"]["ref_outsid"],
        "object_number": feature["properties"]["Objekt_Nr"],
        "object_name": feature["properties"]["Objekt_Bez"],
        "tree_type_reference": feature["properties"]["ref_Baumar"],
        "tree_type_botanic": feature["properties"]["Baumart_bo"],
        "tree_type_german": feature["properties"]["Baumart_de"],
        "tree_type_short": feature["properties"]["Baumart_ku"],
        "outdoor_reference": feature["properties"]["ref_outdoo"],
        "care_number": feature["properties"]["PflE_Art_N"],
        "care_type": feature["properties"]["PflE_Art_B"],
        "trunk_radius": feature["properties"]["Stammradiu"],
        "crown_radius": feature["properties"]["Kronenradi"],
        "geocoordinates": point_data
    }


with open(path_to_geojson) as f:
    data = json.load(f)

    rows = [create_insert_data(feature) for feature in tqdm(data["features"])]
    rows = [row for row in rows if row is not None]
    supabase.table("trees").insert(rows).execute()