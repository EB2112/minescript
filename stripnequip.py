import minescript as ms
import time
import keyboard as k
from pynput.mouse import Controller, Button
import pyautogui
import sys




#just sloppily hard coded the coordinates so i can just index the list, offsets were always a little off 
slot_positions = [(920,420),(1010,420),(1100,420),(1190,420),(1280,420),(1370,420),(1460,420),(1550,420),(1640,420)
                  ,(920,510),(1010,510),(1100,510),(1190,510),(1280,510),(1370,510),(1460,510),(1550,510),(1640,510),
                  (920,600),(1010,600),(1100,600),(1190,600),(1280,600),(1370,600),(1460,600),(1550,600),(1640,600)]

inv_slots =[(920, 1020),(1006, 1020),(1095, 1020),(1185, 1020),(1274, 1020),(1368, 1020),(1460, 1020),(1560, 1020),(1640, 1020),
            (920, 750),(1006, 750),(1095, 750),(1185, 750),(1274, 750),(1368, 750),(1460, 750),(1560, 750),(1640, 750),
            (920, 840),(1006, 840),(1095, 840),(1185, 840),(1274, 840),(1368, 840),(1460, 840),(1560, 840),(1640, 840),
            (920, 930),(1006, 930),(1095, 930),(1185, 930),(1274, 930),(1368, 930),(1460, 930),(1560, 930),(1640, 930),
            
            
            ]


sword_weights = {
    "minecraft:wooden_sword":   1,
    "minecraft:golden_sword":     2, 
    "minecraft:stone_sword":    3,
    "minecraft:iron_sword":     4,
    "minecraft:diamond_sword":  5,
    "minecraft:netherite_sword":6
}

armor_weights= {
    "minecraft:leather_cap":   1,
    "minecraft:leather_tunic": 1,
    "minecraft:leather_pants": 1,
    "minecraft:leather_boots": 1,

    "minecraft:golden_helmet":2,
    "minecraft:golden_chestplate":2,
    "minecraft:golden_leggings":2,
    "minecraft:golden_boots":2,

    "minecraft:chainmail_helmet":3,
    "minecraft:chainmailchestplate":3,
    "minecraft:chainmail_leggings":3,
    "minecraft:chainmail_boots":3,

    "minecraft:iron_hemlet":4,
    "minecraft:iron_chestplate":4,
    "minecraft:iron_leggings":4,
    "minecraft:iron_boots":4,

    "minecraft:diamond_helmet":5,
    "minecraft:diamond_chestplate":5,
    "minecraft:diamond_leggings":5,
    "minecraft:diamond_boots":5,

    "minecraft:netherite_helmet":6,
    "minecraft:netherite_chestplate":6,
    "minecraft:netherite_leggings":6,
    "minecraft:netherite_boots":6

}
armor_types = {
    "helm": "current_helm",
    "cap": "current_helm",
    "chestplate": "current_chest",
    "tunic": "current_chest",
    "leggings": "current_legs",
    "pants": "current_legs",
    "boots": "current_boots"
}

def click_slot(pos):
    mouse.position = pos
    time.sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)

mouse = Controller()
#testing grabbing only certain items
desired_items = ["minecraft:iron_sword",
                 "minecraft:diamond_sword",
                 "minecraft:wooden_sword",
                 "minecraft:golden_sword", 
                 "minecraft:stone_sword",
                    "minecraft:iron_sword",
                    "minecraft:diamond_sword",
                    "minecraft:netherite_sword"
                    "minecraft:leather_cap",
                "minecraft:leather_tunic",
                "minecraft:leather_pants",
                "minecraft:leather_boots",
                "minecraft:golden_helmet",
                "minecraft:golden_chestplate",
                "minecraft:golden_leggings",
                "minecraft:golden_boots",
                "minecraft:chainmail_helmet",
                "minecraft:chainmail_chestplate",
                "minecraft:chainmail_leggings",
                "minecraft:chainmail_boots",
                "minecraft:iron_hemlet",
                "minecraft:iron_chestplate",
                "minecraft:iron_leggings",
                "minecraft:iron_boots",
                "minecraft:diamond_helmet",
                "minecraft:diamond_chestplate",
                "minecraft:diamond_leggings",
                "minecraft:diamond_boots",
]

while True:
    #failsafe quit
    if k.is_pressed("k"):
        sys.exit()
    #epyautogui.mouseInfo()
    if k.is_pressed("c"):
        #press shift for instant shift-click item transfer
        k.press("shift")
        #grab all items from chest. Also grabs stuff from inventory so make sure it doesnt index past the list
        for st in ms.container_get_items():
            if st.item in desired_items:
                if int(st.slot) < 27:
                    click_slot((slot_positions[st.slot]))
                    
            time.sleep(0.03)
            
                
            
        mouse.press(Button.left)
        k.release("shift")
        
    if k.is_pressed("e"):  
        time.sleep(0.1)
        #print(ms.player_inventory())
        inv = ms.player_inventory()
        #set current weapon and armor slots to none 
        current_weapon = None
        weapon_slot = None
        current_helm = None
        current_chest = None
        current_legs = None
        current_boots = None
        armor_slot= None
        #see if there is any armor equipped, armor slots appear at the end of the 'ItemStack' list
        try:
            inv.reverse()
            for x in range(4):
                if inv[x].slot == 39:
                    current_helm = inv[x].item
                elif inv[x].slot == 38:
                    current_chest = inv[x].item
                elif   inv[x].slot == 37:
                    current_legs = inv[x].item
                elif    inv[x].slot == 36:
                    current_boots = inv[x].item
        except:
            
            pass
        inv.reverse()
        
        k.press("shift")
        #iterates over items in inventory
        for st in ms.player_inventory():
            
            #enters if "sword" appears in item name
            if "sword" in st.item:
                #print(sword_weights.get(st.item))
                #checks if there is a current weapon or the current weapon is worse than the new weapon
                if (current_weapon is None or sword_weights.get(st.item) > sword_weights.get(current_weapon)) and st.item in sword_weights:
                   #if true change current weapon
                    current_weapon=st.item
                    weapon_slot = st.slot
                    #print(f"current weapon: {current_weapon} slot: {weapon_slot}")
                    #mouse.position=(inv_slots[weapon_slot])
                else:
                    pass
                #if the item appears in the armor dictionary
            if st.item in armor_weights:
                for keyword, current_var in armor_types.items():
                    #checks type of armor piece
                    if keyword in st.item:
                        #gets variable of current_* if its none, equip and update current_*
                        current_item = globals().get(current_var)  
                        if current_item is None:
                            if st.slot < len(inv_slots):
                                click_slot( inv_slots[st.slot])
                                globals()[current_var] = st.item
                        #if armor is equipped and is less than the selected piece unequip the armor
                        elif armor_weights[st.item] > armor_weights.get(current_item, 0):
                            
                            if "helm" in current_item:
                                
                                click_slot( (920,372))
                            if "chest" in current_item or "tunic" in current_item:
                                
                                click_slot((922,464))
                                
                            if "leggings" in current_item or "pants" in current_item:
                                
                                click_slot((919,548))
                                
                            if "boots" in current_item:
                                
                                click_slot((918,641))
                                
                            # Update tracking
                            globals()[current_var] = st.item
                            # Move + click
                            if st.slot < len(inv_slots):
                                mouse.position = inv_slots[st.slot]
                                time.sleep(0.2)
                                mouse.press(Button.left)
                                mouse.release(Button.left)
            
                    
       
        k.release("shift")
        mouse.position=(inv_slots[weapon_slot])
        time.sleep(0.02)
        k.press_and_release("1")

    if k.is_pressed("i"):
        print(ms.player_inventory())
        for slot in inv_slots:
            mouse.position= (slot)
            time.sleep(0.2)

# k.add_hotkey('ctrl + shift + z', print, args =('Hotkey', 'Detected')) 

# k.wait('esc')
# ms.player_press_use(True)

    
# time.sleep(0.1)
# ms.echo("echo")

920,372
922,464
919,548
918,641

