import yaml
import random
with open('0.yaml') as parameters:
  my_dict = yaml.safe_load(parameters)

levels = list(my_dict["levels"].keys())

waypoint_dict = {}
all_waypoints = []

for i in levels:
    vertices = list(my_dict["levels"][i]["vertices"])
    level_list = []
    for x in vertices:
        if (x[2]['name']) == '':
            continue
        else:
            level_list.append(x[2]['name'])
            all_waypoints.append(x[2]['name'])
    waypoint_dict[i]= level_list

sample_list = random.choices(all_waypoints, k=2)
print(sample_list)


