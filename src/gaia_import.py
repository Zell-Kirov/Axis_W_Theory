from astroquery.gaia import Gaia
import pandas as pd
from entity import Entity

def fetch_gaia_sample(limit=100):
    """
    Retrieves an enriched sample from Gaia, including stellar mass.
    """
    query = f"""
    SELECT TOP {limit}
        gs.source_id, gs.ra, gs.dec, gs.parallax, gs.pmra, gs.pmdec,
        ap.mass_flame
    FROM gaiadr3.gaia_source AS gs
    JOIN gaiadr3.astrophysical_parameters AS ap
    ON gs.source_id = ap.source_id
    WHERE gs.parallax IS NOT NULL AND ap.mass_flame IS NOT NULL
    """

    job = Gaia.launch_job(query)
    results = job.get_results()
    df = results.to_pandas()

    # Derived calculations
    df['distance_pc'] = 1000 / df['parallax']
    df['velocity'] = (df['pmra']**2 + df['pmdec']**2)**0.5

    return df

def gaia_to_entities(df):
    """
    Converts a Gaia DataFrame into a list of Entity objects.
    """
    entities = []

    for _, row in df.iterrows():
        name = f"Star_{row['source_id']}"
        position = (row['ra'], row['dec'], row['distance_pc'])
        velocity = row['velocity'] / 10
        mass = row['mass_flame']
        gravity = max(0.1, min(mass, 10.0))  # Clamp between 0.1 and 10

        entity = Entity(name, position_xyz=position, velocity=velocity, gravity_factor=gravity)
        entities.append(entity)

    return entities
