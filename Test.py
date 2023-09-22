import tkinter as tk










"""_______Window_Settings_____________""" 

window = tk.Tk()
window.geometry("840x560")
window.configure(background="Grey")
window.title("Order Register")
_message = tk.Label(window, text="Fill the bellow fields for order completion: ", bg="Grey")
_message.place(y=25 ,x=20)

"""___________________________________""" 






"""_______Data_Required_for_Order_Completion___________"""  


_data_frame = tk.Frame(window, bg="Grey")
_data_frame.columnconfigure(0, weight="1") #Material
_data_frame.columnconfigure(1, weight="1")
_data_frame.columnconfigure(2, weight="1") #Drinks
_data_frame.columnconfigure(3, weight="1")
_data_frame.columnconfigure(4, weight="1") #Buttons



"""Frame_Message"""
_Material_Label = tk.Label(_data_frame, text="Material List", fg="Orange", bg="Grey", font=("Calibri", 13))
_Material_Label.grid(row=0 ,column=1)
"""____________"""


"""Materials"""
#Nails
_data_Nails = tk.Text(_data_frame, height="1", width="10", )
_data_Nails.grid(row=1, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Nails", background="Grey", fg="Yellow")
_data_label.grid(row=1, column=0)

#Planks
_data_Planks = tk.Text(_data_frame, height="1", width="10")
_data_Planks.grid(row=2, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Planks", background="Grey", fg="Yellow")
_data_label.grid(row=2, column=0)

#Bricks
_data_Bricks = tk.Text(_data_frame, height="1", width="10")
_data_Bricks.grid(row=3, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Bricks", background="Grey", fg="Yellow")
_data_label.grid(row=3, column=0)

#Rope
_data_Rope = tk.Text(_data_frame, height="1", width="10")
_data_Rope.grid(row=4, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Rope", background="Grey", fg="Yellow")
_data_label.grid(row=4, column=0)

#Cable
_data_Cable = tk.Text(_data_frame, height="1", width="10")
_data_Cable.grid(row=5, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Cable", background="Grey", fg="Yellow")
_data_label.grid(row=5, column=0)

#Cement
_data_Cement = tk.Text(_data_frame, height="1", width="10")
_data_Cement.grid(row=6, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Cement", background="Grey", fg="Yellow")
_data_label.grid(row=6, column=0)

#Bolts
_data_Bolts = tk.Text(_data_frame, height="1", width="10")
_data_Bolts.grid(row=7, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Bolts", background="Grey", fg="Yellow")
_data_label.grid(row=7, column=0)

"""_______"""




"""Drinks"""

_Drinks_Label = tk.Label(_data_frame, text="Drinks", fg="Orange", bg="Grey", font=("Calibri", 13))
_Drinks_Label.grid(row=0 ,column=3)

#Coca-Cola
_data_Cola = tk.Text(_data_frame, height="1", width="10")
_data_Cola.grid(row=1, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Coca-Cola", background="Grey", fg="Yellow")
_data_label.grid(row=1, column=2)

#Pepsi
_data_Pepsi_Cola = tk.Text(_data_frame, height="1", width="10")
_data_Pepsi_Cola.grid(row=2, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Pepsi", background="Grey", fg="Yellow")
_data_label.grid(row=2, column=2)

#Fanta
_data_Fanta = tk.Text(_data_frame, height="1", width="10")
_data_Fanta.grid(row=3, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Fanta", background="Grey", fg="Yellow")
_data_label.grid(row=3, column=2)

#MountainDEW
_data_DEW = tk.Text(_data_frame, height="1", width="10")
_data_DEW.grid(row=4, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="MountainDEW", background="Grey", fg="Yellow")
_data_label.grid(row=4, column=2)

#Water
_data_water = tk.Text(_data_frame, height="1", width="10")
_data_water.grid(row=5, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Water", background="Grey", fg="Yellow")
_data_label.grid(row=5, column=2)
"""_______"""



"""Buttons"""
_Buttons_Check = tk.Button(_data_frame, text="Check", padx=14, command=True)
_Buttons_Check.grid(row=2, column=4, padx=40)

_Buttons_Print = tk.Button(_data_frame, text="Print", padx=17)
_Buttons_Print.grid(row=3, column=4)

_Buttons_Exit = tk.Button(_data_frame, text="Exit", padx=20, command=lambda: window.quit())
_Buttons_Exit.grid(row=4, column=4)
"""_______"""


_data_frame.place(x=10 , y=53)

"""_____End_of_Data_Required_for_Order_Completion_____"""  








"""______Additional_Details________"""

_Additional_Details = tk.Frame(window,background="Grey",highlightbackground="Black", highlightthickness=3, pady=5)
_Additional_Details.columnconfigure(0, weight="1")
_Additional_Details.columnconfigure(1, weight="1")
_Additional_Details.columnconfigure(2, weight="1")
_Additional_Details.columnconfigure(3, weight="1")
_Additional_Details.columnconfigure(4, weight="1")

"""Frame_Message"""

_Additional_Details_Label = tk.Label(_Additional_Details, text="Additional Details", fg="Yellow", bg="Grey", padx=5)
_Additional_Details_Label.grid(row=0 ,column=0)
"""_____________"""


_Additional_Details_Box = tk.Checkbutton(_Additional_Details, text="Transport")
_Additional_Details_Box.grid(row=0, column=1)

_Additional_Details_Box = tk.Checkbutton(_Additional_Details, text="Express Transport")
_Additional_Details_Box.grid(row=0, column=2)

_Additional_Details_Box = tk.Checkbutton(_Additional_Details, text="Insurance")
_Additional_Details_Box.grid(row=0, column=3)

_Additional_Details_Box = tk.Checkbutton(_Additional_Details, text="Tracker")
_Additional_Details_Box.grid(row=0, column=4)

_Additional_Details.place(anchor="w", x=10, y=378)

"""_____End_of_Additional_Details________"""

"""______End_of_Data_Required_for_Order_Completion___________"""





"""____Button_Funtions___________"""




"""____End_of_Button_Funtions____"""







"""_____Order_Display_Data_______________"""

_Display_Frame = tk.Frame(window,bg="Grey", background="Grey", highlightthickness=3, highlightbackground="Black")
_Display_Frame.columnconfigure(0, weight="1")

_Data_Display = tk.Text(_Display_Frame, state="disabled", height=21, width=35)
_Data_Display.grid(row=0 ,column=0)
_Display_Frame.place(x=463 ,y=53)

 
"""______________________________________"""






window.mainloop()
