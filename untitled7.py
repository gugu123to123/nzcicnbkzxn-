from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()
root.geometry("900x500")
burger=ImageTk.PhotoImage(Image.open("burger1.png"))
burger_Image=Label(root)
burger_Image[Image]=burger
burger_Image.place(relx=0.7,rely=0.5,anchor=CENTER)

label_heading=Label(root,text="restaurante el michi de los michis rateros",font=("times",40,"bold"),fg="orange")
label_heading.place(relx=0.12,rely=0.1,anchor=CENTER)

label_select_dish=Label(root,text="seleccionar comida",font=("times",15))
label_select_dish.place(relx=0.10,rely=0.2,anchor=CENTER)

dish_list=["hamburguesa","americano_frío"]
dish_dropdown = ttk.Combobox(root ,state = "readonly",values = dish_list)
dish_dropdown.place(relx=0.34, rely=0.2, anchor= CENTER)

label_select_addons=Label(root,text="Seleccionar complementos",font=("times",15))
label_select_addons.place(relx=0.13, rely=0.5,anchor=CENTER)

toppings=[]
toppings_dropdown = ttk.Combobox(root,state = "readonly",values = toppings) 
toppings_dropdown.place(relx=0.34, rely=0.5, anchor= CENTER)

dish_amount=Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2,rely=0.75,anchor=CENTER)

class parent():
    def __init__(self):
     print("Esta es una clase padre")
     
    def menu(dish):
        if dish=="hamburguesa":
            print("Puedes añadir los siguientes ingredientes")
            toppings=["queso","jalapeño"]
            toppings_dropdown["values"]=toppings
            print("Más queso | Añadir jalapeño")
        elif dish=="americano_frío":
            toppings=["chocolate","caramelo"]
            toppings_dropdown["values"]=toppings
            print("Añadir sabor chocolate | Añadir sabor caramelo")
        else:   
            print("Por favor, ingresa una comida válida")
            
    def final_amount(dish, add_ons):
        if dish=="hamburguesa" and add_ons=="queso":
            dish_amount["text"]="Cantidad a pagar $250"
            print("Cantidad a pagar $25000")
        elif dish=="hamburguesa" and add_ons=="jalapeño":
            dish_amount["text"]="Cantidad a pagar $350"
            print("Cantidad a pagar $35000")
        elif dish=="americano_frío" and add_ons=="chocolate":
            dish_amount["text"]="Cantidad a pagar $25000"
            print("Cantidad a pagar $25000")
        elif dish=="americano_frío" and add_ons=="caramelo":
            dish_amount["text"]="Cantidad a pagar $45000"
            print("Cantidad a pagar $45000")
class child1(parent):
    def __init__(self,dish):
        self.new_dish = dish
        
    def  get_menu(self):
        new_dish=dish_dropdown.get()
        parent.menu(new_dish)
        
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        new_dish=dish_dropdown.get()
        addons=toppings_dropdown.get()
        parent.final_amount(new_dish,addons)

child1_object =child1(dish_dropdown.get())
child1_object.get_menu()
child2_object = child2(toppings_dropdown.get(),dish_dropdown.get())
child2_object.get_final_amount()

btn_addons = Button(root,text="Revisar complementos",command=child1_object.get_menu,bg="Blue", fg="white",relief = FLAT)
btn_addons.place(relx=0.08,rely=0.3,anchor=CENTER)

btn_amount = Button(root,text="revisar cantidad",command=child2_object.get_menu,bg="Blue", fg="white",relief = FLAT)
btn_amount.place(relx=0.04,rely=0.6,anchor=CENTER)

root.mainloop()

