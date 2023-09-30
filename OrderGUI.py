import tkinter as tk
from tkinter import messagebox


"""____Button_Funtions___________"""


def Check():
    if _checkout["state"] == "disabled":
       _checkout["state"] = "normal"
    
    
       try:
        global nails, planks, bricks, rope, cable, cement, \
               bolts, cola, pepsi, fanta, dew, water, decimal_checkout
        
        nails = int(_field_nails.get()) * 0.67
        planks = int(_field_planks.get()) * 5.25
        bricks = int(_field_bricks.get()) * 7.34
        rope = int(_field_rope.get()) * 2.20
        cable = int(_field_cable.get()) * 3.46
        cement = int(_field_cement.get()) * 24.59
        bolts = int(_field_bolts.get()) * 0.80
        cola = int(_field_cola.get()) * 3.66
        pepsi = int(_field_pepsi.get()) * 3.54
        fanta = int(_field_fanta.get()) * 3.55
        dew = int(_field_dew.get()) * 4.13
        water = int(_field_water.get()) * 3
      
       except ValueError:
        messagebox.showerror("Error","Missing Order!")
      
       checkout = nails + planks + bricks + rope + cable + cement + bolts + cola + pepsi + fanta + dew + water
       decimal_checkout = "{:.2f}".format(checkout)
       _checkout.delete(0, tk.END)
       _checkout.insert(0, f"{decimal_checkout} RON")

    if _checkout["state"] == "normal":
      _checkout["state"] = "disabled"


#
def Bill():   
    
    if _checkout.get() == '0.00 RON' or _checkout.get() == '':
        messagebox.showerror("Error","Missing Order!")

    
    else:
            
        if _data_display["state"] == "disabled":
            _data_display["state"] = "normal"    

            _data_display.delete("1.0", tk.END)
            _data_display.insert(tk.END,"\n\t**Welcome Customer**\n")
            _data_display.insert(tk.END, "===================================\n")
            _data_display.insert(tk.END, f"Item       Quantity        Price\n")
            _data_display.insert(tk.END, "===================================\n")

            
            if int(_field_nails.get()) > 200 and len(_field_nails.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Nails exceded!")
            else:
               if _field_nails.get()!= "0":
                _decimal_nails = "{:.2f}".format(nails)
                _data_display.insert(tk.END, f"Nails\t\t{_field_nails.get()}\t    {_decimal_nails}\n")


            if int(_field_planks.get()) > 200 and len(_field_planks.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Planks exceded!")
            else:
               if _field_planks.get()!= "0":
                _decimal_planks = "{:.2f}".format(planks)
                _data_display.insert(tk.END, f"Planks\t\t{_field_planks.get()}\t    {_decimal_planks}\n")


            if int(_field_bricks.get()) > 200 and len(_field_bricks.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Bricks exceded!")
            else:
               if _field_bricks.get()!= "0":
                _decimal_bricks = "{:.2f}".format(bricks)
                _data_display.insert(tk.END, f"Bricks\t\t{_field_bricks.get()}\t    {_decimal_bricks}\n")


            if int(_field_rope.get()) > 200 and len(_field_rope.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Rope exceded!")
            else:
               if _field_rope.get()!= "0":
                _decimal_rope = "{:.2f}".format(rope)
                _data_display.insert(tk.END, f"Rope\t\t{_field_rope.get()}\t    {_decimal_rope}\n")


            if int(_field_cable.get()) > 200 and len(_field_cable.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Cable exceded!")
            else:
               if _field_cable.get()!= "0":
                _decimal_cable = "{:.2f}".format(cable)
                _data_display.insert(tk.END, f"Cable\t\t{_field_cable.get()}\t    {_decimal_cable}\n")


            if int(_field_cement.get()) > 200 and len(_field_cement.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Cement exceded!")
            else:
               if _field_cement.get()!= "0":
                _decimal_cement = "{:.2f}".format(cement)
                _data_display.insert(tk.END, f"Cement\t\t{_field_cement.get()}\t    {_decimal_cement}\n")


            if int(_field_bolts.get()) > 200 and len(_field_bolts.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Bolts exceded!")
            else:
               if _field_bolts.get()!= "0":
                _decimal_bolts = "{:.2f}".format(bolts)
                _data_display.insert(tk.END, f"Bolts\t\t{_field_bolts.get()}\t    {_decimal_bolts}\n")


            if int(_field_cola.get()) > 200 and len(_field_cola.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Coca-Cola exceded!")
            else:
               if _field_cola.get()!= "0":
                _decimal_cola = "{:.2f}".format(cola)
                _data_display.insert(tk.END, f"Coca-Cola\t\t{_field_cola.get()}\t    {_decimal_cola}\n")


            if int(_field_pepsi.get()) > 200 and len(_field_pepsi.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Pepsi exceded!")
            else:
               if _field_pepsi.get()!= "0":
                _decimal_pepsi = "{:.2f}".format(pepsi)
                _data_display.insert(tk.END, f"Pepsi\t\t{_field_pepsi.get()}\t    {_decimal_pepsi}\n")


            if int(_field_fanta.get()) > 200 and len(_field_fanta.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Fanta exceded!")
            else:
               if _field_fanta.get()!= "0":
                _decimal_fanta = "{:.2f}".format(fanta)
                _data_display.insert(tk.END, f"Fanta\t\t{_field_fanta.get()}\t    {_decimal_fanta}\n")


            if int(_field_dew.get()) > 200 and len(_field_dew.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Mountain DEW exceded!")
            else:
               if _field_dew.get()!= "0":
                _decimal_dew = "{:.2f}".format(dew)
                _data_display.insert(tk.END, f"DEW\t\t{_field_dew.get()}\t    {_decimal_dew}\n")


            if int(_field_water.get()) > 200 and len(_field_water.get()) == 3:
               messagebox.showerror("Field Error","Maxmium of 200 Water exceded!")
            else:
               if _field_water.get()!= "0":
                _decimal_water = "{:.2f}".format(water)
                _data_display.insert(tk.END, f"Water\t\t{_field_water.get()}\t    {_decimal_water}\n")


        _data_display.insert(tk.END, f"\n\t\t Total {decimal_checkout} RON")
        _data_display.insert(tk.END, "\n===================================")
        _data_display.insert(tk.END, "Aditional Details:\n")
        
        
        if transport_value.get() == 1 and express_value.get() == 0:
            _data_display.insert(tk.END, "*Transport\n")
       
        if transport_value.get() == 0 and express_value.get() == 1:
          _data_display.insert(tk.END, "*Express Transport\n")
       
        if transport_value.get() == 1 and express_value.get() == 1:
            _data_display.insert(tk.END, "*Express Transport\n")
       
        if tracker_value.get() == 1:
          _data_display.insert(tk.END, "*Tracker\n")
       
        if insurance_value.get() == 1:
          _data_display.insert(tk.END, "*Insurance\n") 
       
        if _data_display["state"] == "normal":
          _data_display["state"] = "disabled"
       




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
_material_label = tk.Label(_data_frame, text="Material List", fg="Orange", bg="Grey", font=("Calibri", 13))
_material_label.grid(row=0 ,column=1)
"""____________"""


"""Materials"""
#Nails
_field_nails = tk.Entry(_data_frame,width="14")
_field_nails.grid(row=1, column=1, padx=10, pady=10)
_nails_label = tk.Label(_data_frame, text="Nails", background="Grey", fg="Yellow")
_nails_label.grid(row=1, column=0)
_field_nails.insert(0, 0)

#Planks
_field_planks = tk.Entry(_data_frame, width="14")
_field_planks.grid(row=2, column=1, padx=10, pady=10)
_planks_label = tk.Label(_data_frame, text="Planks", background="Grey", fg="Yellow")
_planks_label.grid(row=2, column=0)
_field_planks.insert(0, 0)

#Bricks
_field_bricks = tk.Entry(_data_frame, width="14")
_field_bricks.grid(row=3, column=1, padx=10, pady=10)
_bricks_label = tk.Label(_data_frame, text="Bricks", background="Grey", fg="Yellow")
_bricks_label.grid(row=3, column=0)
_field_bricks.insert(0, 0)

#Rope
_field_rope = tk.Entry(_data_frame, width="14")
_field_rope.grid(row=4, column=1, padx=10, pady=10)
_rope_label = tk.Label(_data_frame, text="Rope", background="Grey", fg="Yellow")
_rope_label.grid(row=4, column=0)
_field_rope.insert(0, 0)

#Cable
_field_cable = tk.Entry(_data_frame, width="14")
_field_cable.grid(row=5, column=1, padx=10, pady=10)
_cable_label = tk.Label(_data_frame, text="Cable", background="Grey", fg="Yellow")
_cable_label.grid(row=5, column=0)
_field_cable.insert(0, 0)

#Cement
_field_cement = tk.Entry(_data_frame, width="14")
_field_cement.grid(row=6, column=1, padx=10, pady=10)
_cement_label = tk.Label(_data_frame, text="Cement", background="Grey", fg="Yellow")
_cement_label.grid(row=6, column=0)
_field_cement.insert(0, 0)

#Bolts
_field_bolts = tk.Entry(_data_frame, width="14")
_field_bolts.grid(row=7, column=1, padx=10, pady=10)
_bolts_label = tk.Label(_data_frame, text="Bolts", background="Grey", fg="Yellow")
_bolts_label.grid(row=7, column=0)
_field_bolts.insert(0, 0)

"""_______"""




"""Drinks"""

_drinks_label = tk.Label(_data_frame, text="Drinks", fg="Orange", bg="Grey", font=("Calibri", 13))
_drinks_label.grid(row=0 ,column=3)

#Coca-Cola
_field_cola = tk.Entry(_data_frame, width="14")
_field_cola.grid(row=1, column=3, padx=10, pady=10)
_cola_label = tk.Label(_data_frame, text="Coca-Cola", background="Grey", fg="Yellow")
_cola_label.grid(row=1, column=2)
_field_cola.insert(0, 0)

#Pepsi
_field_pepsi = tk.Entry(_data_frame, width="14")
_field_pepsi.grid(row=2, column=3, padx=10, pady=10)
_pepsi_label = tk.Label(_data_frame, text="Pepsi", background="Grey", fg="Yellow")
_pepsi_label.grid(row=2, column=2)
_field_pepsi.insert(0, 0)

#Fanta
_field_fanta = tk.Entry(_data_frame, width="14")
_field_fanta.grid(row=3, column=3, padx=10, pady=10)
_fanta_label = tk.Label(_data_frame, text="Fanta", background="Grey", fg="Yellow")
_fanta_label.grid(row=3, column=2)
_field_fanta.insert(0, 0)

#MountainDEW
_field_dew = tk.Entry(_data_frame, width="14")
_field_dew.grid(row=4, column=3, padx=10, pady=10)
_dew_label = tk.Label(_data_frame, text="MountainDEW", background="Grey", fg="Yellow")
_dew_label.grid(row=4, column=2)
_field_dew.insert(0, 0)

#Water
_field_water = tk.Entry(_data_frame, width="14")
_field_water.grid(row=5, column=3, padx=10, pady=10)
_water_label = tk.Label(_data_frame, text="Water", background="Grey", fg="Yellow")
_water_label.grid(row=5, column=2)
_field_water.insert(0, 0)

"""_______"""






_data_frame.place(x=10 , y=53)

"""_____End_of_Data_Required_for_Order_Completion_____"""  





"""______additional_details________"""

_additional_details = tk.Frame(window,background="Grey",highlightbackground="Black", highlightthickness=3, pady=5)
_additional_details.columnconfigure(0, weight="1")
_additional_details.columnconfigure(1, weight="1")
_additional_details.columnconfigure(2, weight="1")
_additional_details.columnconfigure(3, weight="1")
_additional_details.columnconfigure(4, weight="1")

"""Frame_Message"""

_additional_details_Label = tk.Label(_additional_details, text="Additional Details", fg="Yellow", bg="Grey", padx=5)
_additional_details_Label.grid(row=0 ,column=0)
"""_____________"""

transport_value = tk.BooleanVar()
_additional_transport_box = tk.Checkbutton(_additional_details, variable=transport_value, text="Transport", onvalue=1, offvalue=0)
_additional_transport_box.grid(row=0, column=1)

express_value = tk.BooleanVar()
_additional_express_box = tk.Checkbutton(_additional_details,variable=express_value,  text="Express Transport", onvalue=1, offvalue=0)
_additional_express_box.grid(row=0, column=2)

insurance_value = tk.BooleanVar()
_additional_insurance_box = tk.Checkbutton(_additional_details, variable=insurance_value, text="Insurance", onvalue=1, offvalue=0)
_additional_insurance_box.grid(row=0, column=3)

tracker_value = tk.BooleanVar()
_additional_tracker_box = tk.Checkbutton(_additional_details, variable=tracker_value, text="Tracker", onvalue=1, offvalue=0)
_additional_tracker_box.grid(row=0, column=4)

_additional_details.place(anchor="w", x=10, y=378)

"""_____End_of_additional_details________"""

"""______End_of_Data_Required_for_Order_Completion___________"""






"""Buttons"""
_buttons_check = tk.Button(_data_frame, text="Check", command=Check ,padx=14)
_buttons_check.grid(row=2, column=4, padx=40)

_buttons_bill = tk.Button(_data_frame, text="Bill", command= Bill, padx=22)
_buttons_bill.grid(row=3, column=4)

_buttons_exit = tk.Button(_data_frame, text="Exit", padx=20, command=lambda: window.quit())
_buttons_exit.grid(row=4, column=4)
"""_______"""





"""_____Order_Display_Data_______________"""

_display_frame = tk.Frame(window,bg="Grey", background="Grey",borderwidth=2)
_display_frame.columnconfigure(0, weight="1")
_data_display = tk.Text(_display_frame, bd=4, state= "disabled", foreground="Black", height=21, width=35)
_data_display.grid(row=0 ,column=0)
_display_frame.place(x=463 ,y=53)


"""______________________________________"""





"""_____Total_Checkout______________"""

_checkout = tk.Entry(window, state="disabled", width=14)
_checkout.place(x=260 ,y=325)
_checkout_label = tk.Label(window, text="Total Amount", fg="Orange",bg="Grey", font=("Calibri", 13))
_checkout_label.place(x=160 ,y=318)

"""_________________________________"""


window.mainloop()
