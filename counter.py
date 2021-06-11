import tkinter as tk
import tkinter.font as font
root=tk.Tk()
count =0
my_font = font.Font(size=24)
root.title('Counter')


canvas1 = tk.Canvas(root,width=300, height=300)
canvas1.pack()

def count_update(incr):
    global count
    count += incr
    label1 = tk.Label(root,text=str(count), fg='black', font=('helvetica', 16, 'bold'))
    canvas1.create_window(150,150,window=label1)

button1 = tk.Button(text=' - ', command=lambda:count_update(-1), bg='blue', fg='white')
button1['font']= my_font
canvas1.create_window(80,150,window=button1)

button2 = tk.Button(text=' + ', command=lambda:count_update(1), bg='red', fg='white')
button2['font']= my_font
canvas1.create_window(220,150,window=button2)

root.mainloop()
