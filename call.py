#GUI calculator

#Importing tkinter which is used to create a python app

import tkinter as tk

cal=""

#Below function is used to add value to text area

def add(sy):
    global cal
    cal+=str(sy)
    res.delete(1.0,"end")
    res.insert(1.0,cal)
    
#Below function is used to evaluate the given value
    
def eva():
    global cal
    try:
        cal=str(eval(cal))
        res.delete(1.0,"end")
        res.insert(1.0,cal)
    except:
        clear()
        res.insert(1.0,"Error")

#Below function is used to All clear the text area 

def clear():
    global cal
    cal=""
    res.delete(1.0,"end")
    
root =tk.Tk()
root.title("Calculator")

#Creating a Application for calculator

root.geometry("293x275")
root.config(background='black')                                       

#Fixing the size of the app

res=tk.Text(root,height=2,width=16,font=("Arial",24),background='gray')    

#Using grid plane to insert Button

res.grid(columnspan=5) 

#Below function is used to create button 

def button(x,r,c):
    b1=tk.Button(root,text=x,command=lambda:add(x),width=6,font=("Arial"),background='red')
    b1.grid(row=r,column=c)
    
#Creating a button for '=' and using eva function

b1=tk.Button(root,text="=",command=eva,width=13,font=("Arial"),background='yellow')
b1.grid(row=6,column=3,columnspan=2)

#Creating a button for 'All clear' using clear function

b1=tk.Button(root,text="AC",command=clear,width=6,font=("Arial"),background='green')
b1.grid(row=6,column=2)

#Creating button for calculator

button(1,2,1)
button(2,2,2)
button(3,2,3)
button(4,3,1)
button(5,3,2)
button(6,3,3)
button(7,4,1)
button(8,4,2)
button(9,4,3)
button(0,5,2)
button('(',5,1)
button(')',5,3)
button('+',2,4)
button('-',3,4)
button('*',4,4)
button('/',5,4)
button(".",6,1)

root.mainloop()