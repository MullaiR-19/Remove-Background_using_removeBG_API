#import required modules
from removebg import RemoveBg
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
#reatea global root window
win = Tk()
win.geometry('320x280')
win.title('removeBg')
win.config(background='white')
bgc='white'

#funtion to remove background
def remove_bg(file_path):
    pass
    try:
        cursor = RemoveBg('Your API Here','error.log') #replace your API here!
        cursor.remove_background_from_img_file(file_path,size='regular',bg_color=None)
        messagebox.showinfo('Success','Image Background removed!\nSaved to source folder')
    except ValueError:
        messagebox.showerror('Error','File or API Error')
#funtion to call and display image in the main screen
def call_file():
    file_path = filedialog.askopenfilename(filetypes=[('Image File',"*.jpg *.png *.jpeg")])
    if file_path:
        image = Image.open(file_path)
        max_width = image_label.winfo_width()
        max_height = image_label.winfo_height()
        resized_img = image.resize((max_width, max_height))
        image = ImageTk.PhotoImage(resized_img)
        image_label.config(image=image)
        image_label.image = image
    remove_bg(file_path) #funtion call to remove bg and save
#Funtion to generate main window with tkinter elements
def main_window():
    global image_label
    title_lable = Label(win,text="Remove Background", font=('Verdana', 20,'bold'),fg='blue',bg=bgc)
    title_lable.place(relx=0.5,rely=0.07,anchor='center')
    sub_title_lable = Label(win, text="Remove Background from jpg jpeg png", font=('Verdana', 10), fg='blue',bg=bgc)
    sub_title_lable.place(relx=0.5, rely=0.18, anchor='center')
    button_1 = Button(win, text="Select Image", bg="green",fg='white',command=call_file,height=2,width=15)
    button_1.place(relx=0.5,rely=0.32,anchor='center')
    update_label = Label(win,text='Select an Image',font=('Verdana',12),fg='Blue',bg=bgc)
    update_label.place(relx=0.5,rely=0.45,anchor='center')
    image_label = Label(win,height=130,width=200,bg=bgc)
    image_label.place(relx=0.50,rely=0.5,anchor='n')

#main funtion
if __name__ == '__main__':
    main_window()
    version_label = Label(win,text='V1.0.1',font=('Arial',8),fg='black',bg=bgc)
    version_label.place(relx=0.93,rely=0.96,anchor='center')
    win.mainloop()
