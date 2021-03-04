# from make_photo import right_photo_name

########################################################################################################
# gui
import tkinter as tk
import datetime
import os

from PIL import ImageTk, Image

from face_take_photo import take_photo
from face_detection import detection

from config.settings import CONFIG_DIR, DB_DIR


class GUI:
    def __init__(self, root):
        self.WIGHT = 900
        self.HEIGHT = 700
        self.bg_image = ImageTk.PhotoImage(Image.open(os.path.join(CONFIG_DIR, 'img.jpeg')))

        self.root = root

        self.base_frame = tk.Frame(self.root, width=self.WIGHT, height=self.HEIGHT)
        self.base_frame.pack()

        self.frame1 = tk.Frame(self.root, width=self.WIGHT, height=self.HEIGHT)
        # the same for another buttons

        # self.cv = tk.Canvas(self.base_frame, width=self.WIGHT, height=self.HEIGHT)
        self.cv = self.make_cv(self.base_frame)
        self.show_gui_1()

    def make_cv(self, frame):
        cv = tk.Canvas(frame, width=self.WIGHT, height=self.HEIGHT)
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(0, 0, image=self.bg_image, anchor='nw')
        return cv

    def handler1(self):
        self.base_frame.pack_forget()
        self.frame1.pack()
        cv1 = self.make_cv(self.frame1)
        cv1.create_text(60, 30, text="Введите имя нового работника\n"
                                     "После введения имени будет сделано фото", fill="black",
                        anchor='nw',
                        font=("Segoe Script", 25), justify=tk.CENTER)
        label = tk.Label(cv1, text="Имя пользователя в формате:\n"
                                   "Ivan_Ivanov")
        label.place(relx=0.1, rely=0.2)
        entry = tk.Entry(cv1)
        entry.place(relx=0.4, rely=0.2)
        button1_1 = tk.Button(cv1, text="Ok", font=("Segoe Script", 15),
                              command=lambda: self.handler1_1(entry.get()))
        button1_1.place(relx=0.3, rely=0.3)

    def handler1_1(self, name):
        self.root.quit()
        take_photo(os.path.join(DB_DIR, f"{name}.jpg"))

    def handler2(self):
        self.root.quit()
        # print("ok")
        detection()
        # video_capture()

    def show_gui_1(self):
        self.root.geometry("%dx%d+0+0" % (self.WIGHT, self.HEIGHT))
        self.cv.create_text(60, 30, text="СКУД 2020", fill="red", anchor='nw',
                            font=("Segoe Script", 60, "bold"),
                            justify=tk.RIGHT)

        button1 = tk.Button(self.base_frame, highlightbackground='#3E4149', height=2, bg="black",
                            fg="black",
                            text="Добавить работника\nв базу данных", font=("Segoe Script", 15),
                            command=self.handler1)
        button1.place(relx=0.1, rely=0.4)

        button2 = tk.Button(self.cv, highlightbackground='#3E4149', text="Включить\nраспознавание",
                            font=("Segoe Script", 15), command=self.handler2)
        button2.place(relx=0.45, rely=0.4)

        button3 = tk.Button(self.cv, highlightbackground='#3E4149',
                            text="Удалить работника\nиз базы данных",
                            font=("Segoe Script", 15))
        button3.place(relx=0.7, rely=0.4)


def main():
    # print("d")
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
