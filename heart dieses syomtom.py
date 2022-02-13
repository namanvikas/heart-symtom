from tkinter import *
root=Tk()
root.title("symtoms")
root.geometry("600x400")

q1_radio=StringVar(value="0")

Q1=Label(root,text="do you have fever")
Q1.pack()
q1_r1=Radiobutton(root,text="yes",variable=q1_radio,value="yes")
q1_r1.pack()
q1_r2=Radiobutton(root,text="no",variable=q1_radio,value="no")
q1_r2.pack()

q2_radio=StringVar(value="0")

Q2=Label(root,text="do you flling week")
Q2.pack()
q2_r1=Radiobutton(root,text="yes",variable=q2_radio,value="yes")
q2_r1.pack()
q2_r2=Radiobutton(root,text="no",variable=q2_radio,value="no")
q2_r2.pack()

q3_radio=StringVar(value="0")

Q3=Label(root,text="do your heart beating wiedly")
Q3.pack()
q3_r1=Radiobutton(root,text="yes",variable=q3_radio,value="yes")
q3_r1.pack()
q3_r2=Radiobutton(root,text="no",variable=q3_radio,value="no")
q3_r2.pack()

def fever():
    score=0
    if q1_radio.get()=="yes":
        score=score+20
        print(score)
        
    if q2_radio.get()=="yes":
        score=score+20
        print(score)
        
        
    if q3_radio.get()=="yes":
        score=score+20
        print(score)
        
    if score<=20:
        messagebox.showinfo("report","you don't need to visit a doctor")
        
    elif score>20 and score<=40:
         messagebox.showinfo("report","You might have to go to doctor")
    else:
        messagebox.showinfo("report","i strongly advised you to visit a doctor")
        
    
btn=Button(root,text="show report",command=fever)
btn.pack()

root.mainloop()    
    
    
    
    