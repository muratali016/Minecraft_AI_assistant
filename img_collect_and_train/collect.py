import keyboard
import uuid
import time
from PIL import Image
from mss import mss

mon = {
    "top": 214,
    "left": 775,
    "width": 517,
    "height": 566
}
sct = mss()

i = 0


def record_screen(record_id, key):
    global i
    i += 1
    print("{} {}".format(key, i))
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img_test/{}_{}_{}.png".format(key, record_id, i))


is_exit = False


def exit():
    global is_exit
    is_exit = True


keyboard.add_hotkey("esc", exit)
record_id = uuid.uuid4()

while True:
    if is_exit: break
    try:

        if keyboard.is_pressed("1"):
            record_screen(record_id, "1")
            time.sleep(0.1)
        elif keyboard.is_pressed("2"):
            record_screen(record_id, "2")
            time.sleep(0.1)

        elif keyboard.is_pressed("3"):
            record_screen(record_id, "3")
            time.sleep(0.1)
        elif keyboard.is_pressed("4"):
            record_screen(record_id, "4")
            time.sleep(0.1)

        elif keyboard.is_pressed("5"):
            record_screen(record_id, "5")
            time.sleep(0.1)

        elif keyboard.is_pressed("6"):
            record_screen(record_id, "6")
            time.sleep(0.1)

        elif keyboard.is_pressed("7"):
            record_screen(record_id, "7")
            time.sleep(0.1)

        elif keyboard.is_pressed("8"):
            record_screen(record_id, "8")
            time.sleep(0.1)
        elif keyboard.is_pressed("9"):
            record_screen(record_id, "9")
            time.sleep(0.1)
    except RuntimeError:
        continue
