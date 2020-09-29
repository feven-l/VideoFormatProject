import os
import subprocess
import win32.win32gui
import time
import pyautogui


videoList = ["Big_Buck_Bunny_1080p_h264.mov", "GoPro HERO4 The Adventure of Life in 4K 2160p (4k).mp4", "XVid.SouthPark.sample.avi", "Vanilla Sky clip.mkv", "Big_Buck_Bunny_1080p_h264.mov", "GoPro HERO4 The Adventure of Life in 4K 2160p (4k).mp4", "XVid.SouthPark.sample.avi", "Vanilla Sky clip.mkv"]
counter = 1
# Open each video in video list 
for video in videoList:
    
    # if count 1-4 open with default else open with windows media player
    if counter > 4:
        # Send each video variable to batch file
        os.putenv("Video", video)
        os.startfile("setDefault.bat")
    else:
        os.startfile(video)
    
    # Start video in full screen
    time.sleep(2)
    pyautogui.click(300,300)
    pyautogui.keyDown('alt')
    pyautogui.press('enter')
    pyautogui.keyUp('alt')
    
    # Capture and save CPU usage
    time.sleep(4)
    # os.system("wmic cpu get loadpercentage >> VideoFormatResult.txt")
    time.sleep(2)
    # Toggle window size
    if counter > 4:
        toResize = win32.win32gui.FindWindow(None, 'Windows Media Player')
    else:
        toResize = win32.win32gui.FindWindow(None, 'Movies & TV')
    x0, y0, x1, y1 = win32.win32gui.GetWindowRect(toResize)
    w = x1 - x0
    h = y1 - y0
    win32.win32gui.MoveWindow(toResize, x0, y0, w-100, h-100, True)
    
    
    # Kill default player and WMplayer at the end of each round
    time.sleep(4)
    if counter == 4:
        subprocess.call(["taskkill","/F","/IM","Video.UI.exe"])
    if counter == 8:
        subprocess.call(["taskkill","/F","/IM","wmplayer.exe"])
    
    os.system("wmic cpu get loadpercentage >> VideoFormatResult.txt")     
    counter += 1



