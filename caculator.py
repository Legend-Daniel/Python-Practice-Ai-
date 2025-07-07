from customtkinter import *





# the main application. you set it by specifying Initializing CTk and specifiying the app's geometry then adding the mainloop method to let the application run.

calculator = CTk()
calculator.geometry("400x600")
calculator.title("Legon's calcuator")
calculator.resizable(False,False)
 
field = CTkTextbox(master=calculator,height=260,width=375,font=('Segoe UI',25),fg_color="#87CEFA", text_color='#000080')
field.place(relx=0.035,rely=0.01)
# The field text ( this is where the user sees the text input)
field_text = ""
def add_to_field(sth):
    global field_text
    field_text = field_text+str(sth)
    field.delete('1.0',"end")
    field.insert('1.0',field_text)

def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete('1.0',"end")
    field.insert('1.0',result)

def clear():
    global field_text
    field_text = ''
    field.delete('1.0','end')

def deleted():
    global field_text
    field_text=field_text[:-1]
    field.delete('1.0','end')
    field.insert('1.0',field_text)
    
def open_mode_window():
    mode_window = CTkToplevel(calculator)
    mode_window.geometry("300x200")
    mode_window.title("Mode Window")
    label = CTkLabel(master=mode_window, text="This is a new mode window!", font=("Segoe UI", 18))
    label.pack(pady=40)

set_appearance_mode("dark")

# Now the app's code comes here
#---- this portion includes the numbers 1, 4 , 7 and mode

one1 = CTkButton(master=calculator, text="1",corner_radius=20,height=50,width=100, command=lambda:add_to_field(1))
one1.place(relx=0.15,rely=0.5, anchor="center")

four4 = CTkButton(master=calculator, text="4",corner_radius=20,height=50,width=100, command=lambda:add_to_field(4))
four4.place(relx=0.15,rely=0.6, anchor="center")

seven7 = CTkButton(master=calculator, text="7",corner_radius=20,height=50,width=100, command=lambda:add_to_field(7))
seven7.place(relx=0.15,rely=0.7, anchor="center")

mode = CTkButton(master=calculator, text="mode",corner_radius=20,height=50,width=100, fg_color="#FFA500",command=lambda:clear())
mode.place(relx=0.15,rely=0.8, anchor="center")



#---- this portion includes the numbers 2,5 , 8 and 0

two2 = CTkButton(master=calculator, text="2",corner_radius=20,height=50,width=100,command=lambda:add_to_field(2))
two2.place(relx=0.42,rely=0.5, anchor="center")

five5 = CTkButton(master=calculator, text="5",corner_radius=20,height=50,width=100,command=lambda:add_to_field(5))
five5.place(relx=0.42,rely=0.6, anchor="center")

eight8 = CTkButton(master=calculator, text="8",corner_radius=20,height=50,width=100 , command= lambda:add_to_field(8))
eight8.place(relx=0.42,rely=0.7, anchor="center")

zero0 = CTkButton(master=calculator, text="0",corner_radius=20,height=50,width=100 , command=lambda:add_to_field(0))
zero0.place(relx=0.42,rely=0.8, anchor="center")


#---- this portion includes the numbers 3, 6 and 9

three3 = CTkButton(master=calculator, text="3",corner_radius=20,height=50,width=100, command=lambda:add_to_field(3))
three3.place(relx=0.69,rely=0.5, anchor="center")

six6 = CTkButton(master=calculator, text="6",corner_radius=20,height=50,width=100, command= lambda:add_to_field(6))
six6.place(relx=0.69,rely=0.6, anchor="center")

nine9 = CTkButton(master=calculator, text="9",corner_radius=20,height=50,width=100,command=lambda:add_to_field(9))
nine9.place(relx=0.69,rely=0.7, anchor="center")

equal_to = CTkButton(master=calculator, text="=",corner_radius=20,height=50,width=80, command=lambda:calculate())
equal_to.place(relx=0.69,rely=0.8, anchor="center")

#---- this portion includes the features delete , clear and settings

delete = CTkButton(master=calculator, text="del",corner_radius=20,height=50,width=15, fg_color="#FFA500",command=lambda:deleted())
delete.place(relx=0.9,rely=0.5, anchor="center")

plus= CTkButton(master=calculator, text="+",corner_radius=20,height=50,width=15, fg_color="#FFA500",command=lambda:add_to_field('+'))
plus.place(relx=0.9,rely=0.6, anchor="center")

subtract = CTkButton(master=calculator, text="-",corner_radius=20,height=50,width=15, fg_color="#FFA500",command=lambda:add_to_field('-'))
subtract.place(relx=0.9,rely=0.7, anchor="center")

Clear = CTkButton(master=calculator, text="clear",corner_radius=20,height=50,width=15, fg_color="#FFA500",command=lambda:clear())
Clear.place(relx=0.9,rely=0.8, anchor="center")

# The last line (%,*,/,(,))

product = CTkButton(master=calculator, text="X",corner_radius=20,height=50,width=100, command=lambda:add_to_field('*'))
product.place(relx=0.15,rely=0.9, anchor="center")

div = CTkButton(master=calculator, text="/",corner_radius=20,height=50,width=100,command=lambda:add_to_field('/'))
div.place(relx=0.42,rely=0.9, anchor="center")

left_brac = CTkButton(master=calculator, text="(",corner_radius=20,height=50,width=80,command=lambda:add_to_field('('))
left_brac.place(relx=0.69,rely=0.9, anchor="center")

Right_brac = CTkButton(master=calculator, text=")",corner_radius=20,height=50,width=15, fg_color="#FFA500",command=lambda:add_to_field(')'))
Right_brac.place(relx=0.9,rely=0.9, anchor="center")



calculator.mainloop()

