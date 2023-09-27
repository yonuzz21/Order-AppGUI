import tkinter as tk
from tkinter import messagebox


"""____Button_Funtions___________"""

def Check():
   try:
    global nails, planks, bricks, rope, cable, cement, \
           bolts, cola, pepsi, fanta, dew, water
    
    nails = int(_data_Nails.get()) * 0.67
    planks = int(_data_Planks.get()) * 5.25
    bricks = int(_data_Bricks.get()) * 7.34
    rope = int(_data_Rope.get()) * 2.20
    cable = int(_data_Cable.get()) * 3.46
    cement = int(_data_Cement.get()) * 24.59
    bolts = int(_data_Bolts.get()) * 0.80
    cola = int(_data_Cola.get()) * 3.66
    pepsi = int(_data_Pepsi.get()) * 3.54
    fanta = int(_data_Fanta.get()) * 3.55
    dew = int(_data_DEW.get()) * 4.13
    water = int(_data_Water.get()) * 3   
    
   except ValueError:
    messagebox.showerror("Error","Missing Order!")
    
   checkout = nails + planks + bricks + rope + cable + cement + bolts + cola + pepsi + fanta + dew + water
   decimal_checkout = "{:.2f}".format(checkout)
   _Checkout.delete(0, tk.END)
   _Checkout.insert(0, f"{decimal_checkout} RON")

    


#
def Bill():   
    
    if _Checkout.get() == '0.00 RON' or _Checkout.get() == '':
        messagebox.showerror("Error","Missing Order!")

    else:
       _Data_Display.delete("1.0", tk.END)
       _Data_Display.insert(tk.END,"\n\t**Welcome Customer**\n")
       _Data_Display.insert(tk.END, "===================================\n")
       _Data_Display.insert(tk.END, f"Item       Quantity        Price\n")
       _Data_Display.insert(tk.END, "===================================\n")
       
       if _data_Nails.get()!= "0":
        _decimal_nails = "{:.2f}".format(nails)
        _Data_Display.insert(tk.END, f"Nails\t\t{_data_Nails.get()}\t    {_decimal_nails}\n")

       if _data_Planks.get()!= "0":
        _decimal_planks = "{:.2f}".format(planks)
        _Data_Display.insert(tk.END, f"Planks\t\t{_data_Planks.get()}\t    {_decimal_planks}\n")

       if _data_Bricks.get()!= "0":
        _decimal_bricks = "{:.2f}".format(bricks)
        _Data_Display.insert(tk.END, f"Bricks\t\t{_data_Bricks.get()}\t    {_decimal_bricks}\n")

       if _data_Rope.get()!= "0":
        _decimal_rope = "{:.2f}".format(rope)
        _Data_Display.insert(tk.END, f"Rope\t\t{_data_Rope.get()}\t    {_decimal_rope}\n")

       if _data_Cable.get()!= "0":
        _decimal_cable = "{:.2f}".format(cable)
        _Data_Display.insert(tk.END, f"Cable\t\t{_data_Cable.get()}\t    {_decimal_cable}\n")

       if _data_Cement.get()!= "0":
        _decimal_cement = "{:.2f}".format(cement)
        _Data_Display.insert(tk.END, f"Cement\t\t{_data_Cement.get()}\t    {_decimal_cement}\n")

       if _data_Bolts.get()!= "0":
        _decimal_bolts = "{:.2f}".format(bolts)
        _Data_Display.insert(tk.END, f"Bolts\t\t{_data_Bolts.get()}\t    {_decimal_bolts}\n")

       if _data_Cola.get()!= "0":
        _decimal_cola = "{:.2f}".format(cola)
        _Data_Display.insert(tk.END, f"Coca-Cola\t\t{_data_Cola.get()}\t    {_decimal_cola}\n")

       if _data_Pepsi.get()!= "0":
        _decimal_pepsi = "{:.2f}".format(pepsi)
        _Data_Display.insert(tk.END, f"Pepsi\t\t{_data_Pepsi.get()}\t    {_decimal_pepsi}\n") 

       if _data_Fanta.get()!= "0":
        _decimal_fanta = "{:.2f}".format(fanta)
        _Data_Display.insert(tk.END, f"Fanta\t\t{_data_Fanta.get()}\t    {_decimal_fanta}\n") 

       if _data_DEW.get()!= "0":
        _decimal_dew = "{:.2f}".format(dew)
        _Data_Display.insert(tk.END, f"Mountain DEW\t\t{_data_DEW.get()}\t    {_decimal_dew}\n")   

       if _data_Water.get()!= "0":
        _decimal_water = "{:.2f}".format(water)
        _Data_Display.insert(tk.END, f"Water\t\t{_data_Water.get()}\t    {_decimal_water}\n") 

      


"""____End_of_Button_Funtions____"""







"""_______Window_Settings_____________""" 

window = tk.Tk()
window.geometry("800x430")
window.configure(background="Grey")
window.resizable(False, False)
window.title("Order Register")
_message = tk.Label(window, text="Fill the bellow fields to complete the order: ", bg="Grey")
_message.place(y=15 ,x=20)

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
_data_Nails = tk.Entry(_data_frame, width="14")
_data_Nails.grid(row=1, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Nails", background="Grey", fg="Yellow")
_data_label.grid(row=1, column=0)
_data_Nails.insert(0, 0)

#Planks
_data_Planks = tk.Entry(_data_frame, width="14")
_data_Planks.grid(row=2, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Planks", background="Grey", fg="Yellow")
_data_label.grid(row=2, column=0)
_data_Planks.insert(0, 0)
#Bricks
_data_Bricks = tk.Entry(_data_frame, width="14")
_data_Bricks.grid(row=3, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Bricks", background="Grey", fg="Yellow")
_data_label.grid(row=3, column=0)
_data_Bricks.insert(0, 0)

#Rope
_data_Rope = tk.Entry(_data_frame, width="14")
_data_Rope.grid(row=4, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Rope", background="Grey", fg="Yellow")
_data_label.grid(row=4, column=0)
_data_Rope.insert(0, 0)

#Cable
_data_Cable = tk.Entry(_data_frame, width="14")
_data_Cable.grid(row=5, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Cable", background="Grey", fg="Yellow")
_data_label.grid(row=5, column=0)
_data_Cable.insert(0, 0)

#Cement
_data_Cement = tk.Entry(_data_frame, width="14")
_data_Cement.grid(row=6, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Cement", background="Grey", fg="Yellow")
_data_label.grid(row=6, column=0)
_data_Cement.insert(0, 0)

#Bolts
_data_Bolts = tk.Entry(_data_frame, width="14")
_data_Bolts.grid(row=7, column=1, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Bolts", background="Grey", fg="Yellow")
_data_label.grid(row=7, column=0)
_data_Bolts.insert(0, 0)

"""_______"""




"""Drinks"""

_Drinks_Label = tk.Label(_data_frame, text="Drinks", fg="Orange", bg="Grey", font=("Calibri", 13))
_Drinks_Label.grid(row=0 ,column=3)

#Coca-Cola
_data_Cola = tk.Entry(_data_frame, width="14")
_data_Cola.grid(row=1, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Coca-Cola", background="Grey", fg="Yellow")
_data_label.grid(row=1, column=2)
_data_Cola.insert(0, 0)

#Pepsi
_data_Pepsi = tk.Entry(_data_frame, width="14")
_data_Pepsi.grid(row=2, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Pepsi", background="Grey", fg="Yellow")
_data_label.grid(row=2, column=2)
_data_Pepsi.insert(0, 0)

#Fanta
_data_Fanta = tk.Entry(_data_frame, width="14")
_data_Fanta.grid(row=3, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Fanta", background="Grey", fg="Yellow")
_data_label.grid(row=3, column=2)
_data_Fanta.insert(0, 0)

#MountainDEW
_data_DEW = tk.Entry(_data_frame, width="14")
_data_DEW.grid(row=4, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="MountainDEW", background="Grey", fg="Yellow")
_data_label.grid(row=4, column=2)
_data_DEW.insert(0, 0)

#Water
_data_Water = tk.Entry(_data_frame, width="14")
_data_Water.grid(row=5, column=3, padx=10, pady=10)
_data_label = tk.Label(_data_frame, text="Water", background="Grey", fg="Yellow")
_data_label.grid(row=5, column=2)
_data_Water.insert(0, 0)

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

_Additional_Transport_Box = tk.Checkbutton(_Additional_Details, text="Transport")
_Additional_Transport_Box.grid(row=0, column=1)

_Additional_Express_Box = tk.Checkbutton(_Additional_Details, text="Express Transport")
_Additional_Express_Box.grid(row=0, column=2)

_Additional_Insurance_Box = tk.Checkbutton(_Additional_Details, text="Insurance")
_Additional_Insurance_Box.grid(row=0, column=3)

_Additional_Tracker_Box = tk.Checkbutton(_Additional_Details, text="Tracker")
_Additional_Tracker_Box.grid(row=0, column=4)

_Additional_Details.place(anchor="w", x=10, y=378)

"""_____End_of_Additional_Details________"""

"""______End_of_Data_Required_for_Order_Completion___________"""






"""Buttons"""
_Buttons_Check = tk.Button(_data_frame, text="Check", command=Check ,padx=14)
_Buttons_Check.grid(row=2, column=4, padx=40)

_Buttons_Bill = tk.Button(_data_frame, text="Bill", command= Bill, padx=22)
_Buttons_Bill.grid(row=3, column=4)

_Buttons_Exit = tk.Button(_data_frame, text="Exit", padx=20, command=lambda: window.quit())
_Buttons_Exit.grid(row=4, column=4)
"""_______"""





"""_____Order_Display_Data_______________"""

_Display_Frame = tk.Frame(window,bg="Grey", background="Grey",borderwidth=2)
_Display_Frame.columnconfigure(0, weight="1")
_Data_Display = tk.Text(_Display_Frame, bd=4, foreground="Black", height=21, width=35)
_Data_Display.grid(row=0 ,column=0)
_Display_Frame.place(x=463 ,y=53)


"""______________________________________"""





"""_____Total_Checkout______________"""

_Checkout = tk.Entry(window, width=14)

_Checkout.place(x=260 ,y=325)
_Checkout_Label = tk.Label(window, text="Total Amount", fg="Orange",bg="Grey", font=("Calibri", 13))
_Checkout_Label.place(x=160 ,y=318)

"""_________________________________"""


window.mainloop()
