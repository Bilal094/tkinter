import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
def switch():
    def switch2():
        window.config(bg='black')
        button.config(text= 'Switch light on', command=switch)
        print('light is off')
    window.config(bg='yellow')
    button.config(text= 'Switch light off', command=switch2)
    print('light is on')

print('light is off')
window.config(bg='black')
button.config(text= 'Switch light on', command=switch)
# schijf hier tussen je code

window.mainloop()