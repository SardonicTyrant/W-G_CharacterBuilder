import tkinter as tk

class main_ui(tk.Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pack()

        name_frame = tk.Frame(self)
        name_frame.pack()
        name_label = tk.Label(name_frame, text="Hello")
        name_label.pack(side=tk.LEFT)
        name_text = tk.Entry(name_frame)
        name_text.pack()




def main():
    root = tk.Tk()
    #root.geometry("300x300")
    ui = main_ui()
    root.mainloop()

if __name__ == '__main__':
    main()
