"""
TO DO:
*after clickin on the command clean the entries 

"""
import tkinter as tk 

total_miles = 0
total_gallons = 0 

def miles_gallon():
    global total_miles
    global total_gallons

    gallons = gallons_entry.get()
    miles = miles_entry.get()

    if str.isalpha(gallons) or str.isalpha(miles):
        result_window = tk.Toplevel()
        result_window.geometry('400x200+500+300')
        # Show the result in a label in the second window
        print_result_mp = tk.Label(result_window, text='Enter only numbers')
        print_result_mp.place(x=100,y=100)
    else: 
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        total_miles += miles
        total_gallons += gallons
        miles_per_gallon = miles/gallons

        # Show the result in a window on top of root window
        result_window = tk.Toplevel()
        result_window.geometry('200x200+500+300')
        # Show the result in a label in the second window
        print_result_mp = tk.Label(result_window, text=miles_per_gallon)
        print_result_mp.place(x=100,y=100)

def total_miles_gallons():
    result_window = tk.Toplevel()
    result_window.geometry('200x200+500+300')
    try:
        total = round(total_miles/total_gallons,2)
        print_result = tk.Label(result_window, text=total)
        print_result.place(x=100,y=100)
    except ZeroDivisionError:
        print_result = tk.Label(result_window, text='No data store yet')
        print_result.place(x=100,y=100)


def reset():
    global total_miles
    global total_gallons

    total_miles = 0
    total_gallons = 0

# Main window, size, title and color
root = tk.Tk()
root.geometry('350x350')
root.title('Miles per Gallon')
root.configure(background='spring green')

# labels in the main window and location
label1 = tk.Label(root,text='Enter miles: ',bg='spring green')
label1.place(x=10,y=30)
label2 = tk.Label(root,text='Enter gallons: ',bg='spring green')
label2.place(x=10,y=80)

# Entries the user can write in the main window, and the location 
miles_entry = tk.Entry(root)
miles_entry.place(x=100,y=30)
gallons_entry = tk.Entry(root)
gallons_entry.place(x=100,y=80)

# Buttons to calculate each mile/gallon and total miles/gallons
# And the command to which they respond
calculate = tk.Button(root,text='Calculate miles/gallon', command=miles_gallon)
calculate.place(x=130,y=140)
totalcalculation = tk.Button(root,text='Calculate total miles/gallons', command=total_miles_gallons)
totalcalculation.place(x=115,y=180)
reset_ = tk.Button(root,text='Reset calculation', command=reset)
reset_.place(x=132,y=220)

# Run always the window root 
root.mainloop()




