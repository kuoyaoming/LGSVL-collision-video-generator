import os
import lgsvl
import math
import time
import sys
import numpy as np

from configparser import ConfigParser
config = ConfigParser()

config.read('config.ini')

speed = config.getint('main', 'speed')
rain_level = config.getint('main', 'rain_level')
fog_level = config.getint('main', 'fog_level')
wetness_level = config.getint('main', 'wetness_level')
set_time = config.getint('main', 'set_time')
wetness = config.getint('main', 'save_video')
save_json = config.getint('main', 'save_json')
pedstrain = config.getint('main', 'pedstrain')
vehicle = config.getint('main', 'vehicle')

# speed = 60
# speed = speed/3.6   # km/h => m/s
# rain_level = 0
# fog_level = 0
# wetness_level = 0
# set_time = 12
# save_vidoe = 0
# save_json = 0
# pedstrain = 0
# vehicle = 0

pp = 75-((speed-40)/8)

sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "SanFrancisco":
    sim.reset()
else:
    sim.load("SanFrancisco")

spawns = sim.get_spawn()
forward = lgsvl.utils.transform_to_forward(spawns[0])
up = lgsvl.utils.transform_to_up(spawns[0])
right = lgsvl.utils.transform_to_right(spawns[0])
sim.set_time_of_day(set_time)
sim.weather = lgsvl.simulator.WeatherState(
    rain=rain_level, fog=fog_level, wetness=wetness_level)
# my_car
state1 = lgsvl.AgentState()
state1.transform.position = spawns[0].position + 252.5 * forward + -115*right
state1.transform.rotation.y = spawns[0].rotation.y*-90
state1.velocity = speed*-right
a = sim.add_agent("Lexus2016RXHybrid (Autoware)", lgsvl.AgentType.EGO, state1)

# npc
state = lgsvl.AgentState()
state.transform.position = spawns[0].position + 172*forward - 193 * right
state.transform.rotation.y = spawns[0].rotation.y + 0
b = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)

waypoints = []
x_max = 2
z_delta = 1

layer_mask = 0
layer_mask |= 1 << 0  # 0 is the layer for the road (default)

px_last = 0
pz_last = 0

for i in range(110):
    px = 0
    py = 4
    pz = (i + 1) * z_delta
    angle = spawns[0].rotation
    hit = sim.raycast(state.transform.position +
                      pz * forward + py * up, lgsvl.Vector(0, -1, 0), layer_mask)
    if i == 0:
        wp = lgsvl.DriveWaypoint(hit.point, speed, angle, 0, False, 50)
    wp = lgsvl.DriveWaypoint(hit.point, speed, angle, 0)
    waypoints.append(wp)
    px_last = px
    pz_last = pz


print('pp:', pp)


def on_waypoint(agent, index):
    # print("waypoint {} reached".format(index))
    if index >= pp:
        control = lgsvl.VehicleControl()
        control.steering = 1
        control.throttle = 1
        a.apply_control(control, True)


# The above function needs to be added to the list of callbacks for the NPC
b.on_waypoint_reached(on_waypoint)

b.follow(waypoints)


def on_collision(agent1, agent2, contact):
    print('collision')
    sim.stop()
    sim.reset()


b.on_collision(on_collision)

a_position_x = []
a_position_y = []
a_position_z = []

b_position_x = []
b_position_y = []
b_position_z = []

a_speed = []
b_speed = []
s_time = []
i = 0
if vehicle != 0:
    for _ in range(vehicle):
        sim.add_random_agents(lgsvl.AgentType.NPC)
if pedstrain != 0:
    for _ in range(pedstrain):
        sim.add_random_agents(lgsvl.AgentType.PEDESTRIAN)

sim.run(10)

# # while True:
#    try:
#         sim.run(10)
#         # i=i+0.1
#         # a_position_x.append(a.state.position.x)
#         # a_position_y.append(a.state.rotation.y)
#         # a_position_z.append(a.state.position.z)
#         # b_position_x.append(b.state.position.x)
#         # b_position_y.append(b.state.rotation.y)
#         # b_position_z.append(b.state.position.z)
#         # a_speed.append(a.state.speed)
#         # b_speed.append(11)
#         # s_time.append(i)
#     except:
#         break

# a = np.asarray([s_time,
#                 a_position_x, a_position_y, a_position_z, a_speed,
#                 b_position_x, b_position_y,  b_position_z,  b_speed])

# np.savetxt('RTIP.csv', a.T, delimiter=',', fmt='%.2f')
