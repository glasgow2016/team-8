import json

exclude_condition={
    'rain' : {
        'excludes' : [1,2,15,16]
    },
    'humid_low' : {
        'excludes' : [3,4]
    },
    'humid_high' : {
        'excludes' : [5,6]
    },
    'temp_low' : {
        'excludes' : [7,8,17,18]
    },
    'temp_high' : {
        'excludes' : [9,10]
    },
    'light_low' : {
        'excludes' : [11,12]
    },
    'light_high' : {
        'excludes' : [13, 14]
    }
}

with open('excludes.json','w') as f:
    json.dump(exclude_condition, f)
