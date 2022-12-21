# from PIL import ImageGrab


import pyscreenshot 
from datetime import datetime
import keyboard
import pyautogui
import time   

# while True:
#     im = ImageGrab.grab()
#     dt = datetime.now()
#     fname = "pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.minute // 1)
#     im.save(fname, 'png') 
#     break

######################################################################################################################

    
while True:
    if keyboard.is_pressed('ctrl + f10'):
        datetimeNow = datetime.now()
        datetimeString = datetimeNow.strftime("%d-%m-%Y %H-%M-%S")
        fileName = (f"screenshot-{datetimeString}.png")
        image = pyscreenshot.grab()
        image.save(fileName)
        
   
        
        

        
        
########################################################################################################################

   