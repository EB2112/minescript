import minescript as ms
import time
import keyboard as k
from pynput.mouse import Controller, Button
import pyautogui
import sys
import threading

mouse = Controller()
potential_blocks =["minecraft:stone", "minecraft:coal_ore", "minecraft:iron_ore"]
inv_slots =[(920, 1020),(1006, 1020),(1095, 1020),(1185, 1020),(1274, 1020),(1368, 1020),(1460, 1020),(1560, 1020),(1640, 1020),
            (920, 750),(1006, 750),(1095, 750),(1185, 750),(1274, 750),(1368, 750),(1460, 750),(1560, 750),(1640, 750),
            (920, 840),(1006, 840),(1095, 840),(1185, 840),(1274, 840),(1368, 840),(1460, 840),(1560, 840),(1640, 840),
            (920, 930),(1006, 930),(1095, 930),(1185, 930),(1274, 930),(1368, 930),(1460, 930),(1560, 930),(1640, 930)]
def check_hand():
        hand = ms.player_hand_items()
        
        try:
            return(hand.main_hand.get("item").strip() == "minecraft:iron_pickaxe")
        except:
            return False

def equip_pick():
    k.press_and_release('e')
    time.sleep(0.5)
    for st in ms.player_inventory():
        if st.item == "minecraft:iron_pickaxe":
            mouse.position = inv_slots[st.slot]
            time.sleep(0.5)
            k.press_and_release("1")
            time.sleep(0.5)
            k.press_and_release("e")
            break
    k.press_and_release("shift")
    time.sleep(0.5)
def sell_items():
     time.sleep(1)
     ms.execute("/sell")
     time.sleep(0.1)
     mouse.click(Button.left)
     time.sleep(0.1)
     mouse.position = (1194,506)
     time.sleep(0.05)
     mouse.click(Button.left)
def has_pick():
    items = []
    for st in ms.player_inventory():
        items.append(st.item)
    if "minecraft:iron_pickaxe" in items:
        return True
    else:
        False
last = None
pick_durability = 250
def set_durability():
    global pick_durability 
    pick_durability = 250
def durability():
    global pick_durability 
    pick_durability -= 1
while True:
    
     if k.is_pressed("k"):
        
         sys.exit()

     current = check_hand()

     if current != last:
         last = current

     if not current:
        if not has_pick():
         sell_items()
         sys.exit()
        else:
         equip_pick()
         time.sleep(1)
   
     if ms.player_get_targeted_block().type in potential_blocks:
         ms.player_press_attack(True)
     elif ms.player_get_targeted_block().type not in potential_blocks:
        durability()
        
        print(pick_durability)
        if pick_durability == 0:
            set_durability()
            k.press_and_release("q")
        ms.player_press_attack(False)
        time.sleep(1.7)
    
        
        
1194,506