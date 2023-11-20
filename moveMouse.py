import time
import random
import pynput

# flag for pause
m_pause = False
# app run time without pause time
printTime = 0
# pause with no operator time
bTime = 0
# ctrl mouse instance
c_mouse = pynput.mouse.Controller()
# ctrl keyboard instance
c_keyboard = pynput.keyboard.Controller()


# press func
def on_b_press():
  global m_pause, bTime
  m_pause = True
  bTime = time.time()
  print("get ctrl+alt+b, MoveMouse will pause. press ctrl+alt+r to resume.")


# resume func
def on_r_press():
  global m_pause
  m_pause = False
  print("get ctrl+alt+r, MoveMouse has been resumed.")


def on_key_press(key):
  global bTime
  bTime = time.time()


def on_mousse_move(x, y):
  global bTime
  bTime = time.time()


def init():
  print("Tips:")
  print("press ctrl+alt+b to pause MoveMouse.")
  print("press ctrl+alt+r to resume MoveMouse.")
  print("if MoveMouse is paused and no input for more than 3 min, MoveMouse will be resumed")
  # add hotkey callback func
  hotkey = pynput.keyboard.GlobalHotKeys({
      '<ctrl>+<alt>+b': on_b_press,
      '<ctrl>+<alt>+r': on_r_press,
  })
  # add keyboard listener
  key_press = pynput.keyboard.Listener(on_press=on_key_press)
  # add mouse listener
  mouse_move = pynput.mouse.Listener(on_move=on_mousse_move)

  # start Listense
  mouse_move.start()
  key_press.start()
  hotkey.start()


# -------------main start
init()
print("have fun")
while True:
  time.sleep(5)

  # check pause time
  bbb = time.time() - bTime
  if time.time() - bTime > 3 * 60 and m_pause:
    m_pause = False
    print("No operation for more than 3 min, MoveMouse auto resumed.")

  # no pause, move mouse and press ctrl key
  if not m_pause:
    # print app run time
    printTime += 5
    hour = printTime // 3600
    min = printTime % 3600 // 60
    if (min % 5 == 0) and (min > 0 or hour > 0) and (printTime != min):
      print("you have been touching fish for", hour, "h", min, "min.")
      printTime = min

    # move mouse and press ctrl
    try:
      c_mouse.position = (random.randint(200, 800), random.randint(200, 800))
      c_keyboard.press(pynput.keyboard.Key.ctrl)
      c_keyboard.release(pynput.keyboard.Key.ctrl)
    except:
      print("something error!")
# -------------main end