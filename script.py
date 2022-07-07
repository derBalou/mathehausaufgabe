def f(x):
    return x**2 - 2

'''Program to find the zero of x²-2 in the interval [a,b] while using variable n and the bisection method.'''
def bisection(a,b,n):
    '''Function to find the zero of x²-2 in the interval [a,b] while using variable n and the bisection method.'''
    # Test if the interval is valid
    if a > b:
        return 'Invalid interval'
    # Test if the interval is too small
    if not (f(a) < 0 and f(b) >= 0):
        return 'Invalid interval'
    x = (a + b)/2
    # Check if we have reached the desired accuracy
    if abs(f(x)) < 10**(-n):
        return x
    # Check wheter f(x) is bigger or smaller than 0
    if f(x) < 0:
        return bisection(x,b,n-1)
    elif f(x) > 0:
        return bisection(a,x,n-1)
    else:
        return x
    

'''gui to get three user inputs: a, b, and n.'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('Bisection Method')
root.geometry('300x200')

a = tk.StringVar()
b = tk.StringVar()
n = tk.StringVar()

label_a = ttk.Label(root, text='a:')
label_a.grid(row=0, column=0, sticky=tk.W)
entry_a = ttk.Entry(root, textvariable=a)
entry_a.grid(row=0, column=1)

label_b = ttk.Label(root, text='b:')
label_b.grid(row=1, column=0, sticky=tk.W)
entry_b = ttk.Entry(root, textvariable=b)
entry_b.grid(row=1, column=1)

label_n = ttk.Label(root, text='n:')
label_n.grid(row=2, column=0, sticky=tk.W)
entry_n = ttk.Entry(root, textvariable=n)
entry_n.grid(row=2, column=1)

button = ttk.Button(root, text='Find Zero', command=lambda: 

    messagebox.showinfo('Result', bisection(float(a.get()), float(b.get()), float(n.get())))

)
button.grid(row=3, column=0, columnspan=2)

root.mainloop()