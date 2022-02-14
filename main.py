from keras.models import model_from_json
import numpy as np
from PIL import Image
import keyboard
from mss import mss
from img_collect_and_train.data_classes import Window

mon = {
    "top": 214,
    "left": 775,
    "width": 517,
    "height": 566
}
sct=mss()

width=125
height=50

model=model_from_json(open("model.json","r").read())
model.load_weights("model.h5")

if __name__ == "__main__":
    while True:
        a=1
        if keyboard.is_pressed("1"):
            for a in range(a):

                img = sct.grab(mon)
                im = Image.frombytes("RGB", img.size, img.rgb)
                im2 = np.array(im.convert("L").resize((width, height)))
                im2 = im2 / 255

                X = np.array([im2])
                X = X.reshape(X.shape[0], width, height, 1)
                r = model.predict(X)

                result = np.argmax(r)

                element=Window()

                if result ==0:
                    element.show_2()
                elif result == 1:
                    element.show_4()
                elif result ==2:
                    element.show_5()
                elif result ==3:
                    element.show_3()
                elif result ==4:
                    element.show_1()
                elif result ==5:
                    element.show_0()
                elif result ==6:
                    element.show_6()
                elif result ==7:
                    element.show_7()
                elif result ==8:
                    element.show_8()
