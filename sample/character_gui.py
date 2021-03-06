import tkinter as tk
import json
import io
import os
class main_ui(tk.Frame):
    #self.v = tk.IntVar()
    def __init__(self):
        self.count = 1

        super().__init__()
        self.initUI()

    def initUI(self):
        self.pack()

        self.name_frame = tk.Frame(self)
        self.name_frame.pack()
        self.name_label = tk.Label(self.name_frame, text="Character Name:")
        self.name_label.pack(side=tk.LEFT)
        self.name_text = tk.Entry(self.name_frame)
        self.name_text.pack()

        self.species_frame = tk.Frame(self)
        self.species_frame.pack()
        self.species_label = tk.Label(self.species_frame, text="Species:")
        self.species_label.pack(side=tk.LEFT)
    def addSpecies(self, name:str=""):
        tk.Radiobutton(self.species_frame, text=name, value=self.count).pack()
        #self.count += 1

def main():
    root = tk.Tk()
    #root.geometry("300x300")
    ui = main_ui()
    species_list = os.listdir("../json/Species")
    print(species_list)
    for species in species_list:
        species_file = open("../json/Species/" + species)
        species_data = json.load(species_file)
        ui.addSpecies(species_data["name"])

    root.mainloop()


if __name__ == '__main__':
    main()
