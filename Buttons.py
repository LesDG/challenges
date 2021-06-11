import tkinter as tk
import tkinter.font as font
root_obj=tk.Tk()
root_obj.title('Button Press')
my_font = font.Font(size=24)

canvas1 = tk.Canvas(root_obj,width=300, height=300)
canvas1.pack()

def hello(x,txt):
    label1 = tk.Label(root_obj,text=txt, fg='red', font=('helvetica', 16, 'bold'))
    canvas1.create_window(x,200,window=label1)

button1 = tk.Button(text=' - ', command=lambda : hello(100,'Goodbye'), bg='blue', fg='white')
button1['font']=my_font
canvas1.create_window(100,150,window=button1)

button2 = tk.Button(text=' + ', command=lambda:hello(200,'Hello'), bg = 'green', fg = 'white')
button2['font']=my_font
canvas1.create_window(200, 150, window=button2)

root_obj.mainloop()
