from customtkinter import *
from tkmacosx import Button


root = CTk()
root.geometry("600x550")
root.resizable(False, False)
root.title("Todo list by la cacahuète 🥜")
set_appearance_mode("system")



class Item:
    def __init__(self, parent, item):
        
        self.item = item
        self.frame = CTkFrame(parent, height=200, width=500 )
        self.frame.grid(pady=(0,10))
        
        
        self.label = CTkLabel(self.frame, text=item, font=("roboto", 18))
        self.label.grid(row=0 , column=0 , padx=(60, 60))

    
        self.destroy_btn = Button(self.frame, text='delete', bg='#C70000' , fg="#FFF",activebackground = "#C70000", borderless=1, command=self.delete)
        self.destroy_btn.grid(row= 0 , column=1)
        
    def delete(self):
        self.frame.destroy()

        
    
new_list = None

def list():
    todo_list = CTkScrollableFrame(root, orientation='vertical',width=500, height=200, corner_radius=2)
    todo_list.pack(pady=20)
    
    
    return todo_list

def popup():
    global new_list , todo_arr
    popup_wd = CTkInputDialog(title="New task", text="Write a task", font=('Roboto', 20))
    if new_list == None:
        new_list = list() 
    else : 
        pass
    Item(new_list ,str(popup_wd.get_input()))


title = CTkLabel(root, font=('Roboto', 40), text="TODO LIST APP")
title.pack(padx=(10, 15), pady=20)

subtitle = CTkLabel(root, font=('Roboto', 12), text="You can use this todo list to organize your day, your homework etc... ")
subtitle.pack()

new_list_btn = CTkButton(root, text="+ Add something" , command=popup)
new_list_btn.pack(padx=50, pady=(100,0))


root.mainloop()
