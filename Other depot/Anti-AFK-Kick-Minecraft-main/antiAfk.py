#Code by HermanErKu
import win32con, win32api
import time

def click(x,y):  #the clicking function
  win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y)  #right click down
  time.sleep(0.1)  #waits 0,1 seconds
  win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y)  #right click up
  
for i in range(10):  #how many minutes you want it to run
  for i in range(2):
    time.sleep(5)  #waits 5 seconds before start
    click(0,0)  #clicks on the screen where the minecraft door is
    time.sleep(255)  #waits 255 seconds for next cycle
