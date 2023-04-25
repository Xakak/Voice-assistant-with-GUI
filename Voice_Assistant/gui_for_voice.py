import tkinter as tk
import subprocess
from PIL import ImageTk, Image

#main window
root=tk.Tk()
root.title("Virtual Assistant")
root.geometry("600x750")
root.minsize(1200,700)
root.maxsize(1200,700)

#background img:
img=Image.open("C:\\Users\\admin\\Documents\\GIT\\Voice_Assistant\\assis.jpg")
resized_img=img.resize((1200,900))
img=ImageTk.PhotoImage(resized_img)

bg_canvas=tk.Canvas(root,width=img.width(),height=img.height())
bg_canvas.create_image(0,0,anchor="nw",image=img)
bg_canvas.pack()

#text
text_label=tk.Label(root,text="Virtual Assistant",fg="black",bg="#dddddd")
text_label.place(x=400,y=50)
text_label.config(font=("Barlow", 40))

def button_clicked():
    
    process = subprocess.Popen(["python.exe","C:\\Users\\admin\\Documents\\GIT\\Voice_Assistant\\voice_assistant.py"], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output_label.config(text=output.decode(),fg="white")
    output_label.config(font=("Georgia", 20))
    output_label.place(x=70,y=220)

#Img for button
img2=Image.open("C:\\Users\\admin\\Documents\\Python\\recorder.jpg")
resized_2=img2.resize((80,80))
img2=ImageTk.PhotoImage(resized_2)

#rectangular
canvas=tk.Canvas(root,width=1100,height=500,bg="black",highlightcolor="#666362")
canvas.place(x=60,y=180)
canvas.create_rectangle(0,0,1100,500,outline="#666362")

#output
output_label=tk.Label(root,text="Output:",fg="white",bg="black")
output_label.place(x=70,y=190)
output_label.config(font=("Georgia", 30))

#button

button=tk.Button(root,image=img2,command= button_clicked)
button.place(x=1050,y=190)


#Always at the end of the code else throws wm error
root.mainloop()