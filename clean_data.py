import os
import json
import pandas as pd

# This automatically points to your active folder: C:\Users\samya\Monash\2179\DV2-FIT2179
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(f"Working inside directory: {BASE_DIR}")

# 1. CLEAN THE CYCLONE CSV
try:
    csv_path = os.path.join(BASE_DIR, "ibtracs.SP.list.v04r01.csv")
    print(f"Looking for CSV at: {csv_path}")
    
    df = pd.read_csv(csv_path, header=0, skiprows=[1], low_memory=False)
    df["LAT"] = pd.to_numeric(df["LAT"], errors="coerce")
    df["LON"] = pd.to_numeric(df["LON"], errors="coerce")
    
    # Filter for the Great Barrier Reef region
    gbr_df = df[(df["LAT"] >= -25) & (df["LAT"] <= -10) & (df["LON"] >= 142) & (df["LON"] <= 153)]
    
    output_csv = os.path.join(BASE_DIR, "gbr_cyclones.csv")
    gbr_df.to_csv(output_csv, index=False)
    print("✓ Successfully created: gbr_cyclones.csv")
except Exception as e:
    print(f"Error cleaning CSV: {e}")

# 2. CLEAN THE GEOJSON TRACKS
try:
    # Using lowercase 'all' to match your exact file name
    geojson_path = os.path.join(BASE_DIR, "ibtracs_all_list_v04r01_lines.geojson")
    print(f"Looking for GeoJSON at: {geojson_path}")
    
    with open(geojson_path, "r") as f:
        geojson_data = json.load(f)
        
    filtered_features = []
    for feature in geojson_data["features"]:
        props = feature.get("properties", {})
        lat = props.get("LAT")
        lon = props.get("LON")
        basin = str(props.get("BASIN", ""))
        
        # Keep features if they belong to the South Pacific or cross our GBR coordinates
        if basin == "South Pacific" or (lat and -25 <= lat <= -10 and lon and 142 <= lon <= 153):
            filtered_features.append(feature)
            
    geojson_data["features"] = filtered_features
    
    output_geojson = os.path.join(BASE_DIR, "gbr_cyclone_lines.geojson")
    with open(output_geojson, "w") as f:
        json.dump(geojson_data, f)
    print("✓ Successfully created: gbr_cyclone_lines.geojson")
except Exception as e:
    print(f"Error cleaning GeoJSON: {e}")