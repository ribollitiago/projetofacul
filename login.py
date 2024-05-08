import customtkinter, tkinter
from customtkinter import *
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela_login = customtkinter.CTk()
janela_login.title("Login")
janela_login.geometry("600x440")

img1 = ImageTk.PhotoImage(Image.open("images/pattern.png")) 
img2 = Image.open("images/logo.png")    


background = customtkinter.CTkLabel(master=janela_login, image=img1)
background.pack()

login_frame = customtkinter.CTkFrame(master=janela_login, width=320, height=360, corner_radius=15)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

entry_usuario = customtkinter.CTkEntry(master=login_frame, placeholder_text="Usuario", width=220, font=("Century Gothic", 16))
entry_usuario.place(x=50, y=110)

entry_senha = customtkinter.CTkEntry(master=login_frame, placeholder_text="Senha", width=220, show="*", font=("Century Gothic", 16))
entry_senha.place(x=50, y=165)

button_fsenha = customtkinter.CTkButton(master=login_frame, width=110, text="Esqueci a senha", fg_color="transparent", font=("Century Gothic", 12))
button_fsenha.place(x=165, y=195)

button_login = customtkinter.CTkButton(master=login_frame, width=220, text="Login", corner_radius=32, fg_color="#8F05AD", hover_color="#6A0481",font=("Century Gothic", 18))
button_login.place(x=50, y=240)


logo = customtkinter.CTkLabel(master=login_frame, text="", image=CTkImage(dark_image=img2, size=(220, 55)))
logo.place(relx=0.5, rely=0.14, anchor="center")

janela_login.mainloop()
