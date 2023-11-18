import time
import random
import pyautogui

print("have fun")

while True:
  time.sleep(5)
  mTime = time.time()
  if mTime % 300 == 0:
    hour = mTime // 3600
    min = mTime % 3600 // 60
    sec = mTime % 60
    print("you have been touching fish for %d h %d min % s" % hour % min % sec)
  try:
    pyautogui.moveTo(x=random.randint(100, 900), y=random.randint(100, 900))
    pyautogui.press("ctrl")
  except:
    print("something error!")