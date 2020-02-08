from tkinter import *

root =Tk()
root.title("Simple Calculator")
# Set fixed window size
root.geometry("294x430")
# Disable window resize 
root.resizable(False, False)

first_number=0
math=""

e=Entry(root, width=35, borderwidth=4)
e.grid(row=0,columnspan=3,padx=10,pady=10)

# write clicked symbols to the input field
def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

# clear function
def button_clear():
    e.delete(0, END)

# add function
def button_add():
    global first_number
    global math
    math="addition"
    first_number= int(e.get())
    e.delete(0,END)

# subtract function
def button_subtract():
    global first_number
    global math
    math="subtraction"
    first_number= int(e.get())
    e.delete(0,END)

# multiply function
def button_multiply():
    global first_number
    global math
    math="multiplication"
    first_number= int(e.get())
    e.delete(0,END)

# divide function
def button_divide():
    global first_number
    global math
    math="division"
    first_number= int(e.get())
    e.delete(0,END)

# equal function
def button_equal():
    second_number=e.get()
    e.delete(0,END) 
    if math == "addition":
        e.insert(0, first_number + int(second_number))
    if math=="subtraction":
        e.insert(0, first_number - int(second_number))
    if math=="multiplication":
        e.insert(0, first_number * int(second_number))
    if math=="division":
        e.insert(0, first_number / float(second_number))



# Define buttons for numbers between 0-9
button_1=Button(root,text="1",padx=40,pady=20,command=lambda :button_click(1) )
button_2=Button(root,text="2",padx=40,pady=20,command=lambda :button_click(2) )
button_3=Button(root,text="3",padx=40,pady=20,command=lambda :button_click(3) )
button_4=Button(root,text="4",padx=40,pady=20,command=lambda :button_click(4) )
button_5=Button(root,text="5",padx=40,pady=20,command=lambda :button_click(5) )
button_6=Button(root,text="6",padx=40,pady=20,command=lambda :button_click(6) )
button_7=Button(root,text="7",padx=40,pady=20,command=lambda :button_click(7) )
button_8=Button(root,text="8",padx=40,pady=20,command=lambda :button_click(8) )
button_9=Button(root,text="9",padx=40,pady=20,command=lambda :button_click(9) )
button_0=Button(root,text="0",padx=40,pady=20,command=lambda :button_click(0) )

# Define buttons for symbols 
button_add=Button(root,text="+",padx=38,pady=20,command=button_add)
button_subtract=Button(root,text="-",padx=40,pady=20,command=button_subtract)
button_multiply=Button(root,text="*",padx=41,pady=20,command=button_multiply)
button_divide=Button(root,text="/",padx=41,pady=20,command=button_divide)

button_equal=Button(root,text="=",padx=91,pady=20,command=button_equal)
button_clear=Button(root,text="Clear",padx=80,pady=20,command=button_clear)

# Add buttons to the layout
button_1.grid(row=3 ,column=0 )
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_subtract.grid(row=6,column=0)    
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

root.mainloop()