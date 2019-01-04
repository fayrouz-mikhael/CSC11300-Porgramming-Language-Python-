import math
import random
from tkinter import *
from tkinter import messagebox
from turtle import *


top = Tk()
num=0
def click():
    global num
    try:
        num = int(E1.get())
        if (num >26 or num==0):
            messagebox.showinfo("Sorry", "Please Enter number from 1 to 26")
        else:
             top.destroy()
    except ValueError:
        messagebox.showinfo("Sorry", "Please Enter Integers only")
       


l1 = Label(top,text ="Enter Number",font=('Arial', 20),fg="DarkGreen", background="beige")
l1.pack(side =LEFT)

E1 = Entry(top, bd = 10, font=('Arial 18 bold'), background="gold")
E1.pack(side = LEFT)

b = Button(text='OK', width =8, height=4, font=('Arial', 16),fg="DarkGreen", command=click)
b.pack(side =RIGHT)

top.mainloop()

def floating_decimals(f_val, dec):
    number = "{:."+str(dec)+"f}" #first cast decimal as str
    print(number) #str format output is {:.3f}
    return number.format(f_val)


charcters =0
count = 0
sumprob = 0
remaining =0
total = 0.99999999999
x = 0
y = 0

    
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
colors  = ["red","green","blue","orange","purple","pink","yellow","cyan"]
with open('Words.txt') as infile:
    text=infile.read()
    text = text.lower()
    newlist = [27]
    alphabet = alphabet[:26]
    lettercount = {char: 0 for char in alphabet}   
    for charcters in text:
        if charcters in alphabet:
            key = charcters
            count= count+1
            lettercount[charcters]+=1
            dictionary = dict(lettercount)
            
sort = [(k, dictionary[k]) for k in sorted(dictionary, key=dictionary.get, reverse=True)]

bar = dict(sort)
for key, value in bar.items():
    prob = value/count
    bar[key]=prob
print(bar)    
barz = bar.items()

colors  = ["red","green","blue","orange","purple","pink","yellow"]
RADIUS = 175
LABEL_RADIUS = RADIUS * 1.33
FONTSIZE = 18
FONT = ("Ariel", FONTSIZE, "bold")
        
pie = Turtle()  
pie.penup()
pie.sety(-RADIUS)
pie.pendown()    
for _, fraction in barz:
    if x < num:
        sumprob = sumprob+fraction
        remaining = 1- sumprob
        print(fraction)
        colorchoice = random.choice(colors)
        pie.color("black",colorchoice )
        pie.begin_fill()
        pie.circle(RADIUS, fraction * 360 / total)
        position = pie.position()
        pie.goto(0, 0)
        pie.end_fill()
        pie.setposition(position)
        x = x+1
        
pie.color("black","light grey")
pie.begin_fill()
pie.circle(RADIUS, remaining * 360 / total)
position = pie.position()
pie.goto(0, 0)
pie.end_fill()
pie.setposition(position)   
           
pie.penup()
pie.sety(-LABEL_RADIUS)
for label, fraction in barz:
    if y < num:
        pie.circle(LABEL_RADIUS, fraction * 360 / total / 2)
        pie.write(label, align="right", font=FONT)
        pie.write(",", align="center", font=FONT)
        pie.write(floating_decimals(fraction,4), align="left", font=FONT)
        pie.circle(LABEL_RADIUS, fraction * 360 / total / 2)
        y =y+1
        
pie.circle(LABEL_RADIUS, remaining * 360 / total / 2)
pie.write("Other Letters , ", align="right", font=FONT)
pie.write(floating_decimals(remaining,4), align="left", font=FONT)
pie.circle(LABEL_RADIUS, remaining * 360 / total / 2)        
        
pie.end_fill()
pie.hideturtle()
screen = Screen()
screen.exitonclick()


        
      





    

