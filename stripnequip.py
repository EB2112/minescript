import minescript as ms
import time
import keyboard as k
from pynput.mouse import Controller, Button
import pyautogui
import sys




#just sloppily hard coded the coordinates so i can just index the list 
slot_positions = [(920,420),(1010,420),(1100,420),(1190,420),(1280,420),(1370,420),(1460,420),(1550,420),(1640,420)
                  ,(920,510),(1010,510),(1100,510),(1190,510),(1280,510),(1370,510),(1460,510),(1550,510),(1640,510),
                  (920,600),(1010,600),(1100,600),(1190,600),(1280,600),(1370,600),(1460,600),(1550,600),(1640,600)]

inv_slots =[(920, 1020),(1000, 1020),(1080, 1020),(1160, 1020),(1240, 1020),(1320, 1020),(1400, 1020),(1480, 1020),(1560, 1020),
            (920, 930),(1000, 930),(1080, 930),(1160, 930),(1240, 930),(1320, 930),(1400, 930),(1480, 930),(1560, 930),
            (920, 840),(1000, 840),(1080, 840),(1160, 840),(1240, 840),(1320, 840),(1400, 840),(1480, 840),(1560, 840),
            (920, 750),(1000, 750),(1080, 750),(1160, 750),(1240, 750),(1320, 750),(1400, 750),(1480, 750),(1560, 750),
            ]
mouse = Controller()
#testing grabbing only certain items
desired_items = ["minecraft:diamond_block",
                 "minecraft:diamond_sword"]

while True:
    #failsafe quit
    if k.is_pressed("k"):
        sys.exit()
    #pyautogui.mouseInfo()
    if k.is_pressed("c"):
        #press shift for instant shift-click item transfer
        k.press("shift")
        #grab all items from chest. Also grabs stuff from inventory so make sure it doesnt index past the list
        for st in ms.container_get_items():
            if st.item in desired_items:
                if int(st.slot) < 27:
                    mouse.position = (slot_positions[st.slot])
                    mouse.press(Button.left)
                
            
            
            
           #q time.sleep(0.03)
            
                
            
        mouse.press(Button.left)
        k.release("shift")
        
    if k.is_pressed("e"):
        time.sleep(0.2)
        print(ms.player_inventory())
        for st in ms.player_inventory():
            if "sword" in st.item:
                print(st.slot)
                mouse.position=(inv_slots[st.slot])
                time.sleep(0.1)
                k.press_and_release("1")

# k.add_hotkey('ctrl + shift + z', print, args =('Hotkey', 'Detected')) 

# k.wait('esc')
# ms.player_press_use(True)

    
# time.sleep(0.1)
# ms.echo("echo")


