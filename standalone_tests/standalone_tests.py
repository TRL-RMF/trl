import random
import argparse
import subprocess
import sys
import time

standalone1_list = ['tinyRobot_2W_spawn', 'tinyRobot_2T_spawn', 'tinyRobot_2Y_spawn' , 'tinyRobot_2Z_spawn']
standalone2_list = ['tinyRobot_2V_spawn', 'tinyRobot_2X_spawn', 'tinyRobot_2U_spawn']
standalone3a_list = ['L2_liftlobby', 'L3_liftlobby', 'L4_liftlobby', 'L5_liftlobby', 'L6_liftlobby']
standalone3b_list = ['tinyRobot_2X_spawn', 'tinyRobot_3X_spawn', 'tinyRobot_4X_spawn', 'tinyRobot_5X_spawn', 'tinyRobot_6X_spawn']

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
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[0] ,"-f", waypoints[1] ,"-n", "1" ,"--use_sim_time"], shell=False ,stdout=subprocess.PIPE)
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[1] ,"-f", waypoints[0] ,"-n", "1" ,"--use_sim_time"], shell=False ,stdout=subprocess.PIPE)
        print("============================================================================================")
        print("Dispatch Loop Task: Scenario 1, testing holding points")
        print("From: " + str(waypoints[0]))
        print("To:   " + str(waypoints[1]) + " and vice versa")
        print("============================================================================================")

        time.sleep(delay - ((time.time() - starttime) % delay)) #every X seconds send new command


elif (args.pos_arg1 == 2):
    while(True):
        waypoints = random.sample(standalone2_list, k=2)
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[0] ,"-f", waypoints[1] ,"-n", "1" ,"--use_sim_time"], shell=False ,stdout=subprocess.PIPE)
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[1] ,"-f", waypoints[0] ,"-n", "1" ,"--use_sim_time"], shell=False ,stdout=subprocess.PIPE)
        print("============================================================================================")
        print("Dispatch Loop Task: Scenario 2, testing doors")
        print("From: " + str(waypoints[0]))
        print("To:   " + str(waypoints[1]) + " and vice versa")
        print("============================================================================================")   
        time.sleep(delay - ((time.time() - starttime) % delay)) #every X seconds send new command

elif (args.pos_arg1 == 3):
    while(True):
        waypoints = random.sample(standalone3a_list, k=2)
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[0] ,"-f", waypoints[1] ,"-n", "1" ,"--use_sim_time"], shell=False ,stdout=subprocess.PIPE)
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[1] ,"-f", waypoints[0] ,"-n", "1" ,"--use_sim_time"], shell=False ,stdout=subprocess.PIPE)
        print("============================================================================================")
        print("Dispatch Loop Task: Scenario 3a, testing lifts")
        print("From: " + str(waypoints[0]))
        print("To:   " + str(waypoints[1]) + " and vice versa")
        print("============================================================================================")
        time.sleep(delay - ((time.time() - starttime) % delay)) #every X seconds send new command

elif (args.pos_arg1 == 4):
    while(True):
        waypoints = random.sample(standalone3b_list, k=2)
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[0] ,"-f", waypoints[1] ,"-n", "1" ,"--use_sim_time"], shell=False ,stdout=subprocess.PIPE)
        subprocess.Popen(["ros2", "run", "rmf_demos_tasks", "dispatch_loop", "-s", waypoints[1] ,"-f", waypoints[0] ,"-n", "1" ,"--use_sim_time"], shell=False ,stdout=subprocess.PIPE)
        print("============================================================================================")
        print("Dispatch Loop Task: Scenario 3b, testing lifts")
        print("From: " + str(waypoints[0]))
        print("To:   " + str(waypoints[1]) + " and vice versa")
        print("============================================================================================")
        time.sleep(delay - ((time.time() - starttime) % delay)) #every X seconds send new command

else:
    print("Not a valid integer.")