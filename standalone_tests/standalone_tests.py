import random
import argparse
import subprocess
import sys
import time

standalone1_list = ['tinyRobot_2W_spawn', 'tinyRobot_2X_spawn', 'tinyRobot_2Y_spawn' , 'tinyRobot_2Z_spawn']
standalone2_list = ['tinyRobot_2V_spawn', 'tinyRobot_2T_spawn', 'tinyRobot_2U_spawn']
standalone3_list = ['L2_liftlobby', 'L3_liftlobby', 'L4_liftlobby', 'L5_liftlobby', 'L6_liftlobby']

parser = argparse.ArgumentParser(description="Check what standalone scenario:")

parser.add_argument('pos_arg1', type=int, help='scenario')
parser.add_argument('seconds', type=int, help='every x seconds')

args = parser.parse_args()
print("Standalone scenario number: "+ str(args.pos_arg1)+ " every " + str(args.seconds) + " seconds")
delay = float(args.seconds)
starttime = time.time()

if (args.pos_arg1 == 1):
    while(True):
        waypoints = random.sample(standalone1_list, k=2)
        print("Dispatch Loop Task from " + str(waypoints[0]) + " to " + str(waypoints[1]) + " and vice versa")
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[0] ,"-f", waypoints[1] ,"-n", "1" ,"--use_sim_time"])
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[1] ,"-f", waypoints[0] ,"-n", "1" ,"--use_sim_time"])
        time.sleep(delay - ((time.time() - starttime) % delay)) #every 20 seconds send new command


elif (args.pos_arg1 == 2):
    while(True):
        waypoints = random.sample(standalone2_list, k=2)
        print("Dispatch Loop Task from " + str(waypoints[0]) + " to " + str(waypoints[1]) + " and vice versa")
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[0] ,"-f", waypoints[1] ,"-n", "1" ,"--use_sim_time"])
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[1] ,"-f", waypoints[0] ,"-n", "1" ,"--use_sim_time"])
        time.sleep(delay - ((time.time() - starttime) % delay)) #every 20 seconds send new command

elif (args.pos_arg1 == 3):
    while(True):
        waypoints = random.sample(standalone3_list, k=2)
        print("Dispatch Loop Task from " + str(waypoints[0]) + " to " + str(waypoints[1]) + " and vice versa")
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[0] ,"-f", waypoints[1] ,"-n", "1" ,"--use_sim_time"])
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[1] ,"-f", waypoints[0] ,"-n", "1" ,"--use_sim_time"])
        time.sleep(delay - ((time.time() - starttime) % delay)) #every 20 seconds send new command

else:
    print("Not a valid integer.")