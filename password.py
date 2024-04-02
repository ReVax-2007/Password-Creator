import tkinter as tk

# VARIABLES
CharacterCount = " "
Characters = " "
On_switch = False
On_switch2 = False

# LOGIC code
def show_values():
    global Characters
    Characters = str(w.get())
    print("Characters:", Characters)

def toggle_switch(*args):
    global On_switch
    if toggle_var.get() == 1:
        print("Toggle switched on")
        On_switch = True
    else:
        print("Toggle switched off")
        On_switch = False
    Check_toggle()

def toggle_switch2(*args):
    global On_switch2
    if toggle_var2.get() == 1:
        print("Toggle2 switched on")
        On_switch2 = True
    else:
        print("Toggle2 switched off")
        On_switch2 = False
    Check_toggle()

def Check_toggle():
    if On_switch:
        print("Switch 1 is on")
    else:
        print("Switch 1 is off")
    
    if On_switch2:
        print("Switch 2 is on")
    else:
        print("Switch 2 is off")

# UI code
root = tk.Tk()
root.geometry("1000x600")
root.title("Password Generator")
# root.resizable(height=None, width=None)
root.config(bg="gray")

CharacterCount = tk.Label(root, bg="gray", text="Number Of Characters", font=('Arial', 20,'bold'), fg="black")
CharacterCount.pack()

w = tk.Scale(root, from_=12, to=32, orient=tk.HORIZONTAL, length=600, width=30)
w.pack()

Button1 = tk.Button(root, text='Show', command=show_values)
Button1.pack()
toggle_var = tk.IntVar()
toggle_var.trace('w', toggle_switch)  # Tracing changes to toggle_var
toggle_button = tk.Checkbutton(root,width=15, height=2, text="Include Numbers", variable=toggle_var)
toggle_button.pack(padx=10, pady=5, side="left",anchor="nw")

toggle_var2 = tk.IntVar()
toggle_var2.trace('w', toggle_switch2)  # Tracing changes to toggle_var2
toggle_button2 = tk.Checkbutton(root,width=15, height=2, text="Include Symbols", variable=toggle_var2)
toggle_button2.pack(padx=10, pady=5, side="right",anchor="ne")

Check_toggle()  # Initial check of toggle switches

Generate_Button = tk.Button(root, text="------ GENERATE  ------", font=('Arial', 20, 'bold'))
Generate_Button.pack(pady=10)

Output_Label = tk.Text(root, height=5, width=50, background="Waiting For Password to be Generated", font=('Arial', 20, 'bold'))
Output_Label.pack(pady=10)

root.mainloop()