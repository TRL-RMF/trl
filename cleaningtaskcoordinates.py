import yaml
import collections

#the building I'm making this for is called TRL with L2,3,4,5,6 and cleaning zones A,B,C on each floor.
#assumptions: only using 1 cleanerBot for now...

cleanerbot = "cleanerBotA"
building_name = "TRL"
levels = ["L2", "L3", "L4", "L5", "L6"]
clean_zone_names = ["zoneA","zoneB","zoneC"]
clean_zone_index = {}
output_file_name = "/home/ubuntu/trl_demos_ws/src/trl/trl_demos/include/docker/trl_docker_config.yaml"
building_file_path = "/home/ubuntu/trl_demos_ws/src/trl/trl_demos_maps/maps/trl/trl.building.yaml"
zone_index = 0


# scaling, x,y,z offsets manually input for now
floors = {
    "TRL_L2" : "0.1092, 0.0, 0.0, 0.0",
    "TRL_L3" : "0.0914, 10.1, 2.6, 15.0",
    "TRL_L4" : "0.0806, 55.1, 1210.1, 30.0",
    "TRL_L5" : "0.1097, 20.1, 802.8, 45.0",
    "TRL_L6" : "0.0924, 25.4, 1073.5, 60.0"
}

def zone_indexing():
    count = 0
    for a in levels:
        for b in clean_zone_names:
            clean_zone_index[a+"_"+b]=count
            count+=1
    print(clean_zone_index)
    return(clean_zone_index)


def define_level_and_clean_zone():
    global clean_zone, level_name
    clean_zone = "L2_zoneB"
    level_name = str("TRL_" + clean_zone[:2])  #obtain floor from clean zone

def calculating(x_pixel, y_pixel, level):
    scale = list(map(float, floors[level].split(',')))
    x_meter = round((x_pixel-scale[1])*scale[0],3) 
    y_meter = round((scale[2]-y_pixel)*scale[0],3)
    clean_coordinate = [x_meter, y_meter, 0.0]
    return(clean_coordinate)


def get_number(clean_zone_thing):
    x = clean_zone_thing[-1].split("_")
    return(int(x[-1])) #obtain clean zone coordinate number

def get_cleaning_points(clean_zone_place, level_name):
    cleaning_points_list = []
    with open(building_file_path, 'r') as stream:
        content = yaml.load(stream, Loader=yaml.FullLoader)
        get = content.get("levels").get(level_name).get("vertices")
        for i in get:
            for a in i:
                try:
                    if a.startswith(clean_zone_place + "_clean"):
                         cleaning_points_list.append(i)
                except AttributeError:
                    pass
        cleaning_points_list.sort(key=get_number) #sort list by clean zone number
        for i in get:
            for a in i:
                try:
                    if a == (clean_zone_place + "_start"):
                        cleaning_points_list.insert(0,i)
                    elif a == clean_zone_place:
                        cleaning_points_list.insert(len(cleaning_points_list),i)
                except AttributeError:
                    pass
    return(cleaning_points_list)


def get_new_cleaning_points(clean_zone_place, level_name):
    new_cleaning_points_list = []
    new_cleaning_points = get_cleaning_points(clean_zone_place, level_name)
    for i in new_cleaning_points:
        new_x_pixel = i[0]
        new_y_pixel = i[1]
        c = calculating (new_x_pixel, new_y_pixel, level_name)
        new_cleaning_points_list.append(c)
    print("New cleaning points list:", new_cleaning_points_list)
    return(new_cleaning_points_list)


def convert_points_to_append(clean_zone_place, level_name):
    converted_points =[]
    points = get_new_cleaning_points(clean_zone_place, level_name)
    for i in points:
        converted_points.append(i)
    # print (converted_points)
    return(converted_points)

def clear_file():
    open(output_file_name, 'w').close()

def zone_write_to_file(cleanerbot_type,clean_zone_place,level_name,index_number):
    # check if cleanerBotA is already there
    try:
        with open(output_file_name, 'r') as stream:
            content = yaml.load(stream, Loader=yaml.FullLoader)
            res = str(list(content.keys())[0])
        if cleanerbot_type == res:
            cleanerbot_type = ' '
    except AttributeError:
        pass
    unique_pointer = "pointer"+str(index_number)
    input_points = str(convert_points_to_append(clean_zone_place, level_name))
    d = {cleanerbot_type:{clean_zone_place:{'level_name' : level_name, 'path': unique_pointer}}}
    with open(output_file_name, 'a') as yaml_file:
        yaml.dump(d, yaml_file, default_flow_style=False)
    ## gotta do this coz yaml can't accept lists in yaml.dump zzz so sian
    with open(output_file_name, 'r') as yaml_file:
        filedata = yaml_file.read()
        filedata = filedata.replace(unique_pointer, input_points)
    with open(output_file_name, 'w') as yaml_file:
        yaml_file.write(filedata)

def cleanup(): ##really quick and dirty way sadness
    a_file = open(output_file_name, "r")
    lines = a_file.readlines()
    a_file.close()
    new_file = open(output_file_name, "w")
    for line in lines:
        if line.strip("\n") != "' ':":
            new_file.write(line)
    new_file.close()
def main():
    clear_file()
    zone_indexing()
    for k in clean_zone_index:
        index = clean_zone_index[k]
        clean_zone = k
        level_name = str("TRL_" + clean_zone[:2])  #obtain floor from clean zone
        zone_write_to_file(cleanerbot,clean_zone,level_name,index)
    cleanup()

# zone_indexing()
# # define_level_and_clean_zone()
# zone_write_to_file(cleanerbot,'L2_zoneA')
main()


### UNUSED CODE USED EARLY ON

# coordinates = []

# def file_writing(f,coordinates):
#     #yaml parser doesn't allow for tabs, only spaces...
#     count = 0
#     f.write(cleanerbot+":"+ "\n")
#     f.write("  "+clean_zone+":"+ "\n")
#     f.write("    "+"level_name: "+ '"'+level_name+'"'+"\n")
#     f.write("    "+"path: [ ")
#     for element in coordinates:
#         if count == 0 :
#             f.write("[" + element + "]," + "\n")
#             count+=1
#         elif "l" in element:
#             element = element.replace("l","")
#             f.write("            "+"[" + element + "] ]" + "\n")
#             count+=1
#         else:
#             f.write("            "+"[" + element + "]," + "\n")
#             count+=1
#     f.close()
#     count = 0

# #used this for testing my function initially
# def user_input():    
#     while (True):
#         user_input = input('Enter the x,y coordinates:') 

#         if user_input == "s": #save and overwrite
#             f = open(output_file_name+".yaml", "w")
#             # f = open("coordinates.txt", "w")
#             file_writing(f,coordinates)
#         elif user_input == "d":
#             coordinates.pop()

#         else:
#             user_input = user_input.replace(",",", ") + ", 0.0"
#             coordinates.append(user_input)


#         # elif user_input == "a": #append
#         #     f = open("coordinates.txt", "a")
#         #     file_writing(f,coordinates)
#         print(coordinates)
