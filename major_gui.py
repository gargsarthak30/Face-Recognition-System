from Tkinter import *
from PIL import Image, ImageTk
from combination import combination


class Head:
    def click_first(self, filename, dict_name):
        c = combination()
        c.execute(filename, dict_name)
        
## Function for showing options page on button click 
    def options(self,event):
        self.bottom_frame.pack_forget()
        self.options_frame.pack()

## Function for showing training page, New user registration
    def train_system(self, event):
        self.middle_frame.pack_forget()
        self.options_frame.pack_forget()
        self.existing_user_frame.pack_forget()
        self.new_user_frame.pack()

    def test_system(self,event):
        self.bottom_frame.pack_forget()
        self.options_frame.pack_forget()
        self.existing_user_frame.pack()

    def __init__(self,master):
        self.master=master
        self.master.title="Face Recognition System"
        
        self.main_frame = Frame(self.master, pady=10)
        self.main_frame.pack()

        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack(side="top")

        self.heading = Label(self.top_frame,text = "Face Recognition System",font=("Helvetica", 20), borderwidth=2, relief="solid")
        self.heading.pack()

        self.middle_frame = Frame(self.main_frame)
        self.middle_frame.pack()

        self.background_image = Image.open("test.png")
        self.background = ImageTk.PhotoImage(self.background_image)
        self.back_label = Label(self.middle_frame, image=self.background)
        self.back_label.pack()

        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack(side = "bottom")
        
        self.application = Button(self.bottom_frame, text = "Go To Application", relief = "groove" ,font = ("Helvetica", 15, "bold"))
        self.application.bind('<Button-1>', self.options)
        self.application.pack()

        self.bottom_bottom_frame = Frame(self.bottom_frame, pady = 20)
        self.bottom_bottom_frame.pack(side = "bottom")
        
        self.project_by = Label(self.bottom_bottom_frame, text = "Project Submitted By: ", font = ("Helvetica", 15, "bold"))
        self.project_by.pack()

        self.member_1 = Label(self.bottom_bottom_frame, text = "SARTHAK GARG - 13/ICS/047", font = ("Helvetica", 12, "bold italic"))
        self.member_2 = Label(self.bottom_bottom_frame, text = "SHOBHIT SHARMA - 13/ICS/051", font = ("Helvetica", 12, "bold italic"))
        self.member_3 = Label(self.bottom_bottom_frame, text = "VIVEK BHARTI - 13/ICS/062", font = ("Helvetica", 12, "bold italic"))
        self.member_1.pack()
        self.member_2.pack()
        self.member_3.pack()
        
## Frame for options, training or testing, STARTS
        self.options_frame = Frame(self.main_frame, pady=10)
        self.train_button = Button(self.options_frame, text = "Register, New User",relief = "groove" ,font = ("Helvetica", 15, "bold"), pady=10, padx=10)
        self.train_button.bind("<Button-1>", self.train_system)
        self.train_button.pack(side = "left")
        self.test_button = Button(self.options_frame, text = "Login, Existing User",relief = "groove" ,font = ("Helvetica", 15, "bold"), pady=10, padx=10)
        self.test_button.pack(side="right")
        self.test_button.bind("<Button-1>", self.test_system)
## Frame for options, training or testing, ENDS
        
## New USER, Registration Code (Frame) starts. Separate frames for user details and all buttons.
        self.new_user_frame = Frame(self.main_frame, pady=10)

        self.entry_details_frame = Frame(self.new_user_frame, pady=10)
        self.entry_details_frame.pack(fill = BOTH)
        self.new_user_name_label = Label(self.entry_details_frame, text = "Enter Person's Name:  ", font = ("Helvetica", 12, "bold italic"))
        self.new_user_name_label.pack(side="left")
        self.new_user_name_field = Entry(self.entry_details_frame, font = ("Helvetica", 15, "bold"),relief = "groove")
        self.new_user_name_field.pack(side="right")

        self.train_1_frame = Frame(self.new_user_frame, pady=10)
        self.train_1_frame.pack(fill = BOTH)
        self.train_1_label = Label(self.train_1_frame, text = "Click First Photo: ", font = ("Helvetica", 12, "bold italic"))
        self.train_1_label.pack(side = "left")
        self.dict_name = 'first'
        self.train_1 = Button(self.train_1_frame, text = "First Photo", font = ("Helvetica", 15, "bold"), pady=5, padx=10,relief = "groove", command=lambda: self.click_first(self.new_user_name_field.get(),self.dict_name))
## Function calling for first training photo
##        self.dict_name = 'first'
##        self.train_1.bind("<Button-1>", self.click_first(self.received_entry,self.dict_name))
        self.train_1.pack(side = "right")

        self.train_2_frame = Frame(self.new_user_frame, pady=10)
        self.train_2_frame.pack(fill = BOTH)
        self.train_2_label = Label(self.train_2_frame, text = "Click Second Photo: ", font = ("Helvetica", 12, "bold italic"))
        self.train_2_label.pack(side = "left")
        self.train_2 = Button(self.train_2_frame, text = "Second Photo", font = ("Helvetica", 15, "bold"), pady=5, padx=10, relief = "groove")
        self.train_2.pack(side = "right")

        self.train_3_frame = Frame(self.new_user_frame, pady=10)
        self.train_3_frame.pack(fill = BOTH)
        self.train_3_label = Label(self.train_3_frame, text = "Click Third Photo: ", font = ("Helvetica", 12, "bold italic"))
        self.train_3_label.pack(side = "left")
        self.train_3 = Button(self.train_3_frame, text = "Third Photo", font = ("Helvetica", 15, "bold"), pady=5, padx=10, relief = "groove")
        self.train_3.pack(side = "right")

        self.train_4_frame = Frame(self.new_user_frame, pady=10)
        self.train_4_frame.pack(fill = BOTH)
        self.train_4_label = Label(self.train_4_frame, text = "Click Fourth Photo: ", font = ("Helvetica", 12, "bold italic"))
        self.train_4_label.pack(side = "left")
        self.train_4 = Button(self.train_4_frame, text = "Fourth Photo", font = ("Helvetica", 15, "bold"), pady=5, padx=10, relief = "groove")
        self.train_4.pack(side = "right")

        self.train_5_frame = Frame(self.new_user_frame, pady=10)
        self.train_5_frame.pack(fill = BOTH)
        self.train_5_label = Label(self.train_5_frame, text = "Click Fifth Photo: ", font = ("Helvetica", 12, "bold italic"))
        self.train_5_label.pack(side = "left")
        self.train_5 = Button(self.train_5_frame, text = "Fifth Photo", font = ("Helvetica", 15, "bold"), pady=5, padx=10, relief = "groove")
        self.train_5.pack(side = "right")

        self.train_save_frame = Frame(self.new_user_frame, pady=10)
        self.train_save_frame.pack(fill = BOTH)
        self.train_save_label = Label(self.train_save_frame, text = "Save User's Record: ", font = ("Helvetica", 12, "bold italic"))
        self.train_save_label.pack(side = "left")
        self.train_save = Button(self.train_save_frame, text = "Save Record", font = ("Helvetica", 15, "bold"), pady=5, padx=10, relief = "groove")
        self.train_save.pack(side = "right")
## New USER Registration Code (Frame) ends

## Existing User, Login Code STARTS
        self.existing_user_frame = Frame(self.main_frame, pady=10)
        self.details_frame = Frame(self.existing_user_frame, pady=10)
        self.details_frame.pack(fill=BOTH)
        self.name_label = Label(self.details_frame, text = "Enter Person's Name:  ", font = ("Helvetica", 12, "bold italic"))
        self.name_label.pack(side="left")
        self.name_field = Entry(self.details_frame, font = ("Helvetica", 15, "bold"),relief = "groove")
        self.name_field.pack(side="right")
        self.verify = Button(self.existing_user_frame, text = "Verify User", font = ("Helvetica", 15, "bold"), pady=5, padx=10, relief = "groove")
        self.verify.pack()
## Existing User, Login Code ENDS
        
        
root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(600,650))
root.title('Face Recognition System')
app = Head(root)
root.mainloop()



