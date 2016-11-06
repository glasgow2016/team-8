#!flask/bin/python
from flask import Flask, jsonify, request
from itertools import combinations
# import helix_map
import json
import config
import random
import data_accessor
# import map_data

app = Flask(__name__)

SPOTS_WALKING = data_accessor.SPOTS_WALKING
SPOTS_BICYCLE = data_accessor.SPOTS_BICYCLE
COMBO_WALKING = data_accessor.COMBO_WALKING
COMBO_BICYCLE = data_accessor.COMBO_BICYCLE
SITE = data_accessor.SITE


@app.route('/')
def index():
    return "Hey! Human"

@app.route('/map', methods=['GET'])
def get_map():
    return jsonify(SPOTS)

@app.route('/map/walking/<string:ori>/<string:dest>', methods=['GET'])
def get_map_walking(ori, dest):
    res = SPOTS_WALKING.get(ori+'_'+dest)
    distance = res.get("distance").split(' ')[0]
    duration = res.get("duration").split(' ')
    if len(duration) <= 2:
        duration = duration[0]
    if len(duration) > 2:
        duration = str(int(duration[0])*60+int(duration[2]))

    walking_info = {}
    walking_info['distance'] = distance
    walking_info['duration'] = duration
    walking_info['details'] = res
    return jsonify(walking_info)
    # origins = [str(ori_pos.get('latitude'))+','+str(ori_pos.get('longitude'))]
    # destinations = [str(desti_pos.get('latitude'))+','+str(desti_pos.get('longitude'))]
    # res = helix_map.get_distance_walking(ori, dest)
    # return jsonify(SPOTS.get(ori+'_'+dest))

@app.route('/map/bicycling/<string:ori>/<string:dest>', methods=['GET'])
def get_map_bicycling(ori, dest):
    res = SPOTS_BICYCLE.get(ori+'_'+dest)
    distance = res.get("distance").split(' ')[0]
    duration = res.get("duration").split(' ')
    if len(duration) <= 2:
        duration = duration[0]
    if len(duration) > 2:
        duration = str(int(duration[0])*60+int(duration[2]))

    walking_info = {}
    walking_info['distance'] = distance
    walking_info['duration'] = duration
    walking_info['details'] = res
    return jsonify(walking_info)

@app.route('/map/recommend', methods=['GET'])
def get_recommend():
    mode = request.get('mode')
    time_limit = request.get('time_limit')
    distance_limit = request.get('dist_limit')
    times_exclude = requestwa.get('excludes')

@app.route('/map/recommend_time/walking', methods=['GET'])
def find_map_within_time_limit_walking():
    result = []
    dur_limit = float(request.args.get('duration'))
    for k,v in COMBO_WALKING.iteritems():
        if v.get('duration') <= dur_limit:
            result.append({k:v})
    return jsonify(result)


@app.route('/map/recommend_time/bicycling', methods=['GET'])
def find_map_within_time_limit_bicycling():
    result = []
    dur_limit = float(request.args.get('duration'))
    for k,v in COMBO_BICYCLE.iteritems():
        if v.get('duration') <= dur_limit:
            result.append({k:v})
    return jsonify(result)


@app.route('/map/recommend_distance/walking', methods=['GET'])
def find_map_within_distance_limit_walking():
    result = []
    dur_limit = float(request.args.get('distance'))
    for k,v in COMBO_WALKING.iteritems():
        if v.get('distance') <= dur_limit:
            result.append({k:v})
    return jsonify(result)


@app.route('/map/recommend_distance/bicycling', methods=['GET'])
def find_map_within_distance_limit_bicycling():
    result = []
    dur_limit = float(request.args.get('distance'))
    for k,v in COMBO_BICYCLE.iteritems():
        if v.get('distance') <= dur_limit:
            result.append({k:v})
    return jsonify(result)
    # mode = requests.get('mode')
    # time_limit = requests.get('time_limit')

@app.route('/recommend/walking/time', methods=['GET'])
def recommend_walking_time():
    biu = request.args.get('duration')
    excludes = request.args.get('excludes',[])
    return recommend('duration', biu, COMBO_WALKING, excludes=excludes)


@app.route('/recommend/walking/distance', methods=['GET'])
def recommend_walking_distance():
    biu = request.args.get('distance')
    excludes = request.args.get('excludes',[])
    return recommend('distance', biu, COMBO_WALKING)


@app.route('/recommend/bicycling/time', methods=['GET'])
def recommend_bicycling_time():
    biu = request.args.get('duration')
    excludes = request.args.get('excludes',[])
    return recommend('duration', biu, COMBO_BICYCLE)


@app.route('/recommend/bicycling/distance', methods=['GET'])
def recommend_bicycling_distance():
    biu = request.args.get('distance')
    excludes = request.args.get('excludes',[])
    return recommend('distance', biu, COMBO_BICYCLE)


def recommend(this_key,biu, di, excludes=[]):
    result = []
    filtered_result = []
    dur_limit = float(biu)
    for k,v in di.iteritems():
        if v.get(this_key) <= dur_limit:
            count = 0
            for exclude in excludes:
                if exclude in k:
                    count += 1
            result.append({'path':{k:v},'ex_hits':count})

    if len(result) > 3:
        filtered_result = sorted(result, key=lambda k:k['ex_hits'])[:len(result)/2]
    else:
        filtered_result = sorted(result, key=lambda k:k['ex_hits'])
    # filtered_result = [x for x in result if int(x.values()[0].get(this_key)) > int(biu)/2]
    # if filtered_result == []:
        # filtered_result = result

    filtered_result = random_selection(filtered_result, SITE)
    return jsonify(filtered_result)



def random_selection(paths, di=SITE):
    result = {}
    index = random.randint(0,len(paths))
    path = paths[index]['path']
    nodes = path.keys()[0].split('_')
    result['distance'] = path.values()[0]['distance']
    result['duration'] = path.values()[0]['duration']
    result['nodes'] = []
    print nodes[0] in di.keys()
    for node in nodes:
        result['nodes'].append(di[node])
    return result



@app.route('/ranking')
def get_rank():
    return 'rank here'

@app.route('/sensor')
def sensor():
    return 'sensor'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
