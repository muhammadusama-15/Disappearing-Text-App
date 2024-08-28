#Importing relevant libraries
import tkinter as tk
import keyboard

#Creating a global variable
user_input = ""

#Creating a window
window = tk.Tk()
window.title("Disappearing Text App")
window.minsize(width=550, height=550)

#Defining function for typing
def start_typing():
    info_label = tk.Label(master=frame, text="If you do not type anything for 5 seconds, all of your work will be lost permanantly!")
    info_label.grid(row=1, column=0, columnspan=2)

    text = tk.Text(master=frame, height=25, width=50, font=("Times New Roman",14,"normal"))
    text.grid(row=2, column=0, columnspan=2, pady=5)
    text.focus()
    
    #This function deletes everything inn the text box if nothing is typed in for 5 seconds
    def count_down(count):
        global user_input
        print(count)
        if user_input == text.get("0.0", "end"): #If user does not type something, timer starts
            if count > 0:
                window.after(1000,count_down,count-1)
            else:
                text.delete("0.0", "end") #After 5 seconds, text is deleted.

        else: #If user types something, timer resets
            count = 5
            user_input = text.get("0.0", "end")
            window.after(1000,count_down,count)

    #Calling the function
    count_down(5)

#Creating a frame
frame = tk.Frame(master=window, height=500, width=500)
frame.pack(padx=10, pady=10)

#Creating starting widgets
label = tk.Label(master=frame, text="Challenge your writing skills...", font=("Calibri",20,"bold"), fg="green")
label.grid(row=0, column=0, columnspan=2,pady=5)

button = tk.Button(master=frame, text="Start Typing", command=start_typing)
button.grid(row=2, column=0, columnspan=2)

#Creating a mainloop to run the app
window.mainloop()