import pyautogui
import time
import keyboard
while True:
    img = pyautogui.screenshot()
    scr_color = img.getpixel((56,202))
    x1 = img.getpixel((816,280))
    x2 = img.getpixel((720,280))
    x3 = img.getpixel((816,280))
    x4 = img.getpixel((710,280))
    y1 = img.getpixel((740,255))
    y2 = img.getpixel((760,255))
    y3 = img.getpixel((723,255))
    y4 = img.getpixel((705,255))

    if scr_color[0]==255:
        if x1[0] != 255 or x2[0] != 255 or x3[0] != 255 or x4[0] != 255 or y1[0] != 255 or y2[0] != 255 or y3[0] != 255 or y4[0] != 255:
            # if true it means that there is an obj hence bkg not white
            pyautogui.press('up')
            time.sleep(0.00001)
    else:
        if x1[0] != 0 or x2[0] != 0 or x3[0] != 0 or x4[0] != 0 or y1[0] != 0 or y2[0] != 0 or y3[0] != 0 or y4[0] != 0:
            #if true it means that there is no obj hence bkg is white
            pyautogui.press('up')

    if keyboard.is_pressed('b'):
        break
