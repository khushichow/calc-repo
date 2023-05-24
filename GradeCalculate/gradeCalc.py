from tkinter import *


root= Tk()
root.geometry("1000x700")

g1=IntVar()
w1=IntVar()
g2=IntVar()
w2=IntVar()
g3=IntVar()
w3=IntVar()
g4=IntVar()
w4=IntVar()
g5=IntVar()
w5=IntVar()
g6=IntVar()
w6=IntVar()
g7=IntVar()
w7=IntVar()
g8=IntVar()
w8=IntVar()
g9=IntVar()
w9=IntVar()
g10=IntVar()
w10=IntVar()

l1 = Label(root, text = 'Grade', fg ='purple', font = ("Roboto",14))
l1.grid(row=1, column=0,padx=5,pady=10)

l2 = Label(root, text = 'Weigth', fg ='purple', font = ("Roboto",14))
l2.grid(row=1, column=1,padx=5,pady=10)

l1 = Label(root, text = 'Grade Goal', fg ='purple', font = ("Roboto",14))
l1.grid(row=1, column=3,padx=5,pady=10)


a = Entry(root, textvariable = g1, fg = 'blue', font=('Roboto', 15))
a.grid(row=2, column=0)

b = Entry(root, textvariable = w1, fg = 'blue', font=('Roboto', 15))
b.grid(row=2, column=1)

c = Entry(root, textvariable = g2, fg = 'blue', font=('Roboto', 15))
c.grid(row=3, column=0)

d = Entry(root, textvariable = w2, fg = 'blue', font=('Roboto', 15))
d.grid(row=3, column=1)

e = Entry(root, textvariable = g3, fg = 'blue', font=('Roboto', 15))
e.grid(row=4, column=0)

f = Entry(root, textvariable = w3, fg = 'blue', font=('Roboto', 15))
f.grid(row=4, column=1)

g = Entry(root, textvariable = g4, fg = 'blue', font=('Roboto', 15))
g.grid(row=5, column=0)

h = Entry(root, textvariable = w4, fg = 'blue', font=('Roboto', 15))
h.grid(row=5, column=1)

i = Entry(root, textvariable = g5, fg = 'blue', font=('Roboto', 15))
i.grid(row=6, column=0)

j = Entry(root, textvariable = w5, fg = 'blue', font=('Roboto', 15))
j.grid(row=6, column=1)

k = Entry(root, textvariable = g6, fg = 'blue', font=('Roboto', 15))
k.grid(row=7, column=0)

l = Entry(root, textvariable = w6, fg = 'blue', font=('Roboto', 15))
l.grid(row=7, column=1)

m = Entry(root, textvariable = g7, fg = 'blue', font=('Roboto', 15))
m.grid(row=8, column=0)

n = Entry(root, textvariable = w7, fg = 'blue', font=('Roboto', 15))
n.grid(row=8, column=1)

o = Entry(root, textvariable = g8, fg = 'blue', font=('Roboto', 15))
o.grid(row=9, column=0)

p = Entry(root, textvariable = w8, fg = 'blue', font=('Roboto', 15))
p.grid(row=9, column=1)


q = Entry(root, textvariable = g9, fg = 'blue', font=('Roboto', 15))
q.grid(row=10, column=0)

r = Entry(root, textvariable = w9, fg = 'blue', font=('Roboto', 15))
r.grid(row=10, column=1)


s = Entry(root, textvariable = g10, fg = 'blue', font=('Roboto', 15))
s.grid(row=11, column=0)

t = Entry(root, textvariable = w10, fg = 'blue', font=('Roboto', 15))
t.grid(row=11, column=1)

grade = IntVar()
goal = Entry(root, textvariable = grade, fg = 'blue', font=('Roboto', 15))
goal.grid(row=2, column=3)

def calculate():
    lst = [b.get(),d.get(),f.get(),h.get(),j.get(),l.get(),n.get(),p.get(),r.get(),t.get()]
    glst = [a.get(),c.get(),e.get(),g.get(),i.get(),k.get(),m.get(),o.get(),q.get(),s.get()]
    lt = list(map(int, lst))
    glst = [(int(a.get())/100)*int(b.get()),(int(c.get())/100)*int(d.get()),(int(e.get())/100)*int(f.get()),(int(g.get())/100)*int(h.get()),(int(i.get())/100)*int(j.get()),(int(k.get())/100)*int(l.get()),(int(m.get())/100)*int(n.get()),(int(o.get())/100)*int(p.get()),(int(q.get())/100)*int(r.get()),(int(s.get())/100)*int(t.get())]
    new = 100 - sum(lt)
    sm = int(grade.get()) - sum(glst)
    newsum = (sm/new)*100
    newstr = "{:.2f}".format(newsum)
    emptylabel.config(text = "you will need a grade of "+ newstr + "% \nfor your desired final grade")

button = Button(root,command=calculate, text = 'Calculate', fg='green', font=("Arial", 20))
button.grid(row=3, column=3)

emptylabel = Label(root,fg = 'black',font=('Arial',20))
emptylabel.grid(row=4,column=3, padx=5,pady=5)

root.mainloop()

