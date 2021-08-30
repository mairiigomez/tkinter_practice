"""
Practicing with Tkinter module
User enter the amount of gallons use for each tankful and the miles they drove
make the calculation of miles/gallon for each tankful and also the average of all 
have the 3 buttons: 
- Make individual calculations
- Make average calculation of all the data introduce
- Reset the screen and also the data storage to 0

"""

import tkinter as tk
from tkinter.constants import END 

# Global variable to storage the miles and gallons
total_miles = 0
total_gallons = 0 

def validate_entries(gallons, miles):
    """Verify if the user entries are valids return False if is not a number or empty return True if is valid"""

    # if the variables after taking what was written are alpha print 'enter just numbers'
    if str.isalpha(gallons) or str.isalpha(miles):
        # Create a smaller window on top with same color 
        result_window = tk.Toplevel()
        result_window.geometry('300x200+500+300')
        result_window.configure(background='spring green')

        # Show the result in a label in the second window
        print_result_mp = tk.Label(result_window, text='Enter only numbers')
        print_result_mp.place(x=100,y=100)
        return False

    # If the variable are empty print a different message
    elif gallons == '' or miles == '':
        result_window = tk.Toplevel()
        result_window.geometry('300x200+500+300')
        result_window.configure(background='spring green')

        # Show the result in a label in the second window
        print_result_mp = tk.Label(result_window, text='It cannot be empty')
        print_result_mp.place(x=100,y=100)
        return False
    
    return True

def miles_gallon():
    """Make the calculation of the individual miles/gallons after validate they are numbers"""

    # global keyword so they can be modify 
    global total_miles
    global total_gallons

    # get what was written on the entries
    gallons = gallons_entry.get()
    miles = miles_entry.get()
    
    if validate_entries(gallons, miles):
        # convert to float to make the division 
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())

        # Add it to the storage data for miles and gallons
        total_miles += miles
        total_gallons += gallons

        # Calculate and round it 2 digits after the point 
        miles_per_gallon = round(miles/gallons,2)

        # Show the result in a window on top of root window
        result_window = tk.Toplevel()
        result_window.geometry('200x200+500+300')
        result_window.configure(background='spring green')

        # Show the result in a label in the second window
        print_result_mp = tk.Label(result_window, text=miles_per_gallon)
        print_result_mp.place(x=100,y=100)

        # After making the calculation clean the entries from index 0 to end
        miles_entry.delete(0, END)
        gallons_entry.delete(0, END)

def total_miles_gallons():
    """Make the calculation of the total average of miles/gallons"""

    # Show the result on top of the main screen 200x200 and move it 500x and 300y
    result_window = tk.Toplevel()
    result_window.geometry('200x200+500+300')
    result_window.configure(background='spring green')

    # Try to make the calculation if it result zero division its because there is no data
    try:
        total = round(total_miles/total_gallons,2)
        print_result = tk.Label(result_window, text=total)
        print_result.place(x=100,y=100)
    except ZeroDivisionError:
        print_result = tk.Label(result_window, text='No data store yet')
        print_result.place(x=100,y=100)


def reset():
    """Function for the reset button, reset data storage for miles and gallon
    and clean the entries"""
    
    # Use the global keyword so it can modify the global variable
    global total_miles
    global total_gallons

    # Set the global variables to 0 (reset them)
    total_miles = 0
    total_gallons = 0

    # delete what is written in the entries from index 0 to the end 
    miles_entry.delete(0, END)
    gallons_entry.delete(0, END)


############################################## Main window ############################################
# size, title and color
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
# Individual calculation        
calculate = tk.Button(root,text='Calculate miles/gallon', command=miles_gallon)
calculate.place(x=130,y=140)
# Total Calculation average
totalcalculation = tk.Button(root,text='Calculate total miles/gallons', command=total_miles_gallons)
totalcalculation.place(x=115,y=180)
# Reset the board and the screen
reset_ = tk.Button(root,text='Reset calculation', command=reset)
reset_.place(x=132,y=220)

# Run always the window root 
root.mainloop()




