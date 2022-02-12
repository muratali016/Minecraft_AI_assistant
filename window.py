import time
import tkinter as tk
import keyboard
import pyautogui

class Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x400")
        self.label = tk.Label(text="")
        self.label.pack()
        self.default1 = tk.Label(self.root, text="")
        self.default1.pack()
        self.root.title("Minecraft AI assistant")
        self.label1 = tk.Label(text="Minecraft AI assistant by muratali016")
        self.label1.pack()

               



    def show_5(self):

        now = "The jungle tree"
        infos="Biomes= Bamboo Jungle (mega, bush); Jungle \n Fruit = Cocoa Beans (normal)\nGrows on =	Dirt Grass Block, Coarse Dirt,\n Podzol, Mycelium‌[JE only]"
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))


        self.root.after(3000, lambda: self.root.destroy())
        self.root.mainloop()







    def show_4(self):
        now = "The acacia tree"
        infos="Biomes: Savanna ; Jungle \n Fruit: None (normal)\nGrows on =	Dirt Grass Block, Coarse Dirt,\n Podzol, Mycelium‌[JE only]"
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))

        self.root.after(3000, lambda: self.root.destroy())
        self.root.mainloop()


    def show_3(self):
        now = "The birch tree"

        infos = "Biomes: Birch ForestDark ,ForestForest Old, Growth Birch Forest Meadow \n Fruit: None(normal)\n \nGrows on =	Dirt Grass Block, Coarse Dirt,\n Podzol, Mycelium‌[JE only]"
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))
        self.root.after(3000, lambda: self.root.destroy())
        self.root.mainloop()

    def show_2(self):

        now = "The dark tree"
        infos="Biomes: Birch ForestDark ,ForestForest Old, Growth Birch Forest Meadow \n Fruit: None(normal)\n \nGrows on =	Dirt Grass Block, Coarse Dirt,\n Podzol, Mycelium‌[JE only]"
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))
        self.root.after(3000, lambda: self.root.destroy())
        self.root.mainloop()

    def show_1(self):

        now = "The Villager"
        infos="Villagers are passive mobs that inhabit villages,\n work at their professions, \nbreed, and interact with each other. \nTheir outfit varies according to their occupation and biome.\n A player can trade with villagers \nusing emeralds as currency."
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))
        self.root.after(3000, lambda: self.root.destroy())
        self.root.mainloop()

    def show_(self):

        now = "The Creeper"
        infos="A creeper is a common hostile mob that silently approaches\n players and explodes. Due to their distinctive appearance \nand high potential for killing unwary players \nas well as damaging the environment and players'\n constructions, creepers have become one of the\n icons of Minecraft, both among players and non-players."
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))
        self.root.after(3000, lambda: self.root.destroy())
        self.root.mainloop()

    def show_6(self):

        now = "The Lava"
        infos="Lava is a light-emitting fluid that causes fire damage,\nmostly found in the lower reaches of the Overworld and the Nether."
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))
        self.root.after(3000, lambda: self.root.destroy())
        self.root.mainloop()

    def show_7(self):

        now = "The Water"
        infos="Water is a fluid that\naturally generates abundantly in the Overworld."
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))
        self.root.after(3000, lambda: self.root.destroy())
        self.root.mainloop()

    def show_8(self):

        now = "The village house"
        infos="Village buildings and farms never generate completely floating.\n However, if the structure generates partly on an overhang,\n water, etc., a platform of blocks generates beneath the building\n in a square‌[JE only] or circular‌[BE only] shape. \nThe platform is made out of natural \n blocks such as grass, sand, sandstone,\n dirt, stone, and gravel."
        self.root.geometry("600x500")
        self.label.configure(text=now,fg='red',
                            font=("Helvetica", 16))
        self.default1.configure(text=infos,fg='black',
                            font=("Helvetica", 12))


        self.root.after(5000, lambda: self.root.destroy())
        self.root.mainloop()
