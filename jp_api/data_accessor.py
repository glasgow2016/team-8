#!flask/bin/python
import json
with open('data/all_pairs.json','r') as f:
    SPOTS_WALKING = json.loads(f.read())

with open('data/all_pairs_bicycle.json','r') as f:
    SPOTS_BICYCLE = json.loads(f.read())

with open('data/all_dist_duration_walking.json','r') as f:
    COMBO_WALKING = json.loads(f.read())

with open('data/all_dist_duration_bicycle.json','r') as f:
    COMBO_BICYCLE = json.loads(f.read())

with open('data/helix_site.json','r') as f:
    SITE = json.loads(f.read()).get('sights')
