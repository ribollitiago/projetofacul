import customtkinter, tkinter
from customtkinter import *
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

customtkinter.set_window_scaling(1)
customtkinter.set_widget_scaling(1)

janela_home = customtkinter.CTk()
janela_home.title('Home')
janela_home.geometry("{0}x{1}+0+0".format(janela_home.winfo_screenwidth(), janela_home.winfo_screenheight()))

altura = janela_home.winfo_screenheight()

img2 = Image.open("images/logo.png")    

img1 = ImageTk.PhotoImage(Image.open("images/pattern.png")) 
userImage = Image.open("images/user.png")
notaImage = Image.open("images/notas.png")
materiaImage = Image.open("images/calendar.png")

background = customtkinter.CTkLabel(master=janela_home, image=img1)
background.pack()

menu = customtkinter.CTkFrame(master=janela_home, width=300, height=altura)
menu.place(relx=0.00, rely=-0.03)


logo = customtkinter.CTkLabel(master=menu, text="", image=CTkImage(dark_image=img2, size=(220, 55)))
logo.place(relx=0.5, rely=0.07, anchor="n")

user_button = customtkinter.CTkButton(master=menu, width=260, height=40, text="Aluno", fg_color="transparent", corner_radius=6, hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",image=CTkImage(dark_image=userImage), anchor='w')
user_button.place(relx=0.5, rely=0.18, anchor="n")
user_button2 = customtkinter.CTkButton(master=menu, width=260, height=40, text="Notas", fg_color="transparent", corner_radius=6, hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",image=CTkImage(dark_image=notaImage), anchor='w')
user_button2.place(relx=0.5, rely=0.25, anchor="n")
user_button3 = customtkinter.CTkButton(master=menu, width=260, height=40, text="Matérias", fg_color="transparent", corner_radius=6, hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",image=CTkImage(dark_image=materiaImage), anchor='w')
user_button3.place(relx=0.5, rely=0.32, anchor="n")



# logo = customtkinter.CTkLabel(master=login_frame, text="", image=CTkImage(dark_image=img2, size=(220, 55)))
# logo.place(relx=0.5, rely=0.19, anchor="center")

janela_home.mainloop()
