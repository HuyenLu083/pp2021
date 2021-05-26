from tkinter import *
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math


class Window:
    def __init__(self, stds, crs):
        self.students = stds
        self.courses = crs
        self.root = Tk()
        self.root.title("Welcome admin!")
        self.root.geometry("1300x720")

        # Background for home frame
        # self.home_bg = ImageTk.PhotoImage(Image.open("images//home_frame.png").resize((882, 475), Image.ANTIALIAS))

        # =======================Set background image=====================
        image = ImageTk.PhotoImage(Image.open("images//bg.png").resize((1300, 720), Image.ANTIALIAS))
        canvas = Canvas(self.root)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=image, anchor="nw")

        # =================================================================
        # =======================Create features frame=====================
        # =================================================================
        feature = LabelFrame(self.root, height=300, width=184.689, bg="#3f489d", relief="flat")
        feature.place(x=100, y=200)

        # Home button
        # home_btn = Button(feature, text="HOME", font=("arial", 10, "bold"), width=22,
        #                   bg="#3f489d", fg="white", relief=GROOVE,
        #                   command=self.click_home)
        # home_btn.place(x=-1, y=0)
        # View Detail button
        mana_btn = Button(feature, text="VIEW DETAIL", font=("arial", 10, "bold"), width=22,
                          bg="#3f489d", fg="white", relief=GROOVE,
                          command=self.click_manage)
        mana_btn.place(x=-1, y=27)
        # Exit button
        exit_btn = Button(feature, text="EXIT", font=("arial", 10, "bold"), width=22,
                          bg="#3f489d", fg="white", relief=GROOVE,
                          command=self.click_exit)
        exit_btn.place(x=-1, y=54)

        # =================================================================
        # =============================Log out panel=======================
        # =================================================================
        panel = LabelFrame(self.root, width=800, height=40, bg="white", relief=FLAT)
        panel.place(x=356, y=65)

        welcome = Label(panel, text="Hello, admin", font=("arial", 12), bg='white', fg="#005580")
        welcome.place(x=650, y=6)

        # self.click_home()
        self.root.mainloop()

    def click_manage(self):
        self.view_frame = LabelFrame(self.root, width=882, height=475, bg="white", relief=FLAT)
        self.view_frame.place(x=300, y=126)

        frame_features = LabelFrame(self.view_frame, bg="white", relief=FLAT)
        frame_features.pack(fill="both", expand=True)

        btn_add_std = Button(frame_features, text='Add Student', width=12, height=1, bg="white",
                             command=self.add_student)
        btn_add_std.grid(row=0, column=0, padx=5, pady=5)

        btn_add_crs = Button(frame_features, text='Add Course', width=12, height=1, bg="white", )

        btn_add_crs.grid(row=0, column=1, padx=5, pady=5)

        btn_add_mrk = Button(frame_features, text='Add Mark', width=12, height=1, bg="white", )

        btn_add_mrk.grid(row=0, column=2, padx=5, pady=5)

        btn_list_std = Button(frame_features, text='Students List', width=12, height=1, bg="white", )

        btn_list_std.grid(row=0, column=3, padx=5, pady=5)

        btn_list_crs = Button(frame_features, text='Courses List', width=12, height=1, bg="white", )

        btn_list_crs.grid(row=0, column=4, padx=5, pady=5)

        btn_list_mrk = Button(frame_features, text='Mark List', width=12, height=1, bg="white", )

        btn_list_mrk.grid(row=0, column=5, padx=5, pady=5)

        btn_list_sort = Button(frame_features, text='Sorted List', width=12, height=1, bg="white", )

        btn_list_sort.grid(row=0, column=6, padx=5, pady=5)

    def click_exit(self):
        """ Allows user to terminates the program when chosen yes"""
        self.root.deiconify()
        ask = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Exit?")
        if ask is True:
            self.root.quit()

    # def click_home(self):
    #     home_frame = Label(self.root, image=self.home_bg, bg="white", relief=FLAT)
    #     home_frame.place(x=300, y=126)
    #
    #     # ======================Information frame=============================
    #
    #     id = Label(home_frame, text=str(self.id), fg="#004d99", bg="#e7f5fd", font=("arial", 13))
    #     id.place(x=115, y=88)
    #
    #     name = Label(home_frame, text=self.username, fg="#004d99", bg="#e7f5fd", font=("arial", 13))
    #     name.place(x=172, y=110)
    #
    #     area = Label(home_frame, text=self.area, fg="#004d99", bg="#e7f5fd", font=("arial", 13))
    #     area.place(x=130, y=136)
    #
    #     address = Label(home_frame, text=self.address, fg="#004d99", bg="#e7f5fd", font=("arial", 13))
    #     address.place(x=160, y=160)
    #     # ==========================Water spent frame============================
    #     water_frame = LabelFrame(home_frame, width=330, height=160, bg="#e7f5fd", relief=FLAT)
    #     water_frame.place(x=480, y=60)
    #
    #     fig2 = plt.figure(figsize=(4, 2), dpi=80, tight_layout={'pad': 1})
    #     fig2.patch.set_facecolor('#e7f5fd')
    #     canvas2 = FigureCanvasTkAgg(fig2, master=water_frame)
    #     self.water_consumed("2021")
    #     canvas2.draw()
    #     canvas2.get_tk_widget().place(x=0, y=0)
    #
    #     # ==========================Calendar============================================
    #     cal_frame = LabelFrame(home_frame, width=240, height=180, bg="#e7f5fd", relief=FLAT)
    #     cal_frame.place(x=70, y=250)
    #     cal = Calendar(cal_frame, selectmode="day", year=2021, month=5, day=15, showweeknumbers=False,
    #                    background="#e7f5fd", foreground='black', bordercolor="white",
    #                    headersbackground="white", headersforeground='#1a53ff',
    #                    selectbackground="#ccf3ff", selectforeground="black")
    #     cal.place(x=2, y=2)
    #
    #     # ========================Money spent frame===============================
    #     money_frame = LabelFrame(home_frame, width=330, height=160, bg="#e7f5fd", relief=FLAT)
    #     money_frame.place(x=480, y=280)
    #
    #     fig2 = plt.figure(figsize=(4, 2), dpi=80, tight_layout={'pad': 1})
    #     fig2.patch.set_facecolor('#e7f5fd')
    #     canvas2 = FigureCanvasTkAgg(fig2, master=money_frame)
    #     self.money_consumed("2021")
    #     canvas2.draw()
    #     canvas2.get_tk_widget().place(x=0, y=0)

    def add_student(self):
        frame = Frame(self.view_frame, relief=FLAT, bg="white")
        frame.pack(pady=10)

        lb = Label(frame, text="You chose add Student", bg="white", font=("arial", 10))
        lb.grid(row=0, column=0, pady=10)

        id_lb = Label(frame, text="Student ID:", bg="white", font=("arial", 10))
        id_lb.grid(row=1, column=0, pady=10)
        id_entry = Entry(frame, font=("arial", 12))
        id_entry.grid(row=1, column=4, pady=10)

        name_lb = Label(frame, text="Student name:", bg="white", font=("arial", 10))
        name_lb.grid(row=2, column=0, pady=10)
        name_entry = Entry(frame, font=("arial", 12))
        name_entry.grid(row=2, column=4, pady=10)

        dob_lb = Label(frame, text="Student DoB:", bg="white", font=("arial", 10))
        dob_lb.grid(row=3, column=0, pady=10)
        dob_entry = Entry(frame, font=("arial", 12))
        dob_entry.grid(row=3, column=4, pady=10)

        sub_btn = Button(frame, text="Submit", font=("arial", 10), bg="white")
        sub_btn.grid(row=5, column=3)


if __name__ == '__main__':
    students = []
    courses = []
    Window(students, courses)
