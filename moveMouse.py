import time
import random
import pyautogui

print("have fun")
sTime = time.time()
while True:
  time.sleep(5)
  mTime = (int)(time.time() - sTime)  +47843
  hour = mTime // 3600
  min = mTime % 3600 // 60
  sec = mTime % 60
  if (min % 5 == 0) and (min > 0):
    print("you have been touching fish for", hour, "h", min, "min", sec, "s")
  try:
    pyautogui.moveTo(x=random.randint(100, 900), y=random.randint(100, 900))
    pyautogui.press("ctrl")
  except:
    print("something error!")