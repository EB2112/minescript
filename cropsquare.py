import minescript as ms
import time
import keyboard as k
from pynput.mouse import Controller, Button
import pyautogui
import sys

mouse = Controller()

#get player position
player_pos = tuple(round(num) for num in ms.player_position())
player_x, player_y, player_z = player_pos
#determine range of planting and iterate over blocks in radius
look_range = 4
player_y -=1
for x in range(-look_range, look_range + 1):
    for z in range(-look_range, look_range + 1):
        target_x = player_x +x 
        target_z = player_z +z 
        target_y = player_y - 1
        #add offset to get center of block
        ms.player_look_at(target_x + 0.5, target_y + 1, target_z + 0.5)
        ms.player_press_use(True)
        time.sleep(0.1)
        ms.player_press_use(False)
sys.exit()
while True:
    if k.is_pressed('k'):
        sys.exit()