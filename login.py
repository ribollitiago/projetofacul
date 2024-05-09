import customtkinter
from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox

def verificar_credenciais(usuario, senha):
    # Aqui você pode adicionar o código para verificar as credenciais no banco de dados
    # Retorne True se as credenciais estiverem corretas, caso contrário, False
    pass

def esqueci_senha():
    # Aqui você pode adicionar o código para lidar com a situação em que o usuário esqueceu a senha
    pass

def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if verificar_credenciais(usuario, senha):
        print("Login bem-sucedido!")
    else:
        msg = CTkMessagebox(title="Erro", message="Falha no login", icon="cancel", width=200)
        print(usuario)
        print(senha)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
janela_login = customtkinter.CTk()
janela_login.title("Login")
janela_login.iconbitmap("images/dev.png")
janela_login.geometry("600x440")

img1 = ImageTk.PhotoImage(Image.open("images/pattern.png")) 
img2 = customtkinter.CTkImage(dark_image=Image.open("images/logo.png"),  size=(220, 55))


background = customtkinter.CTkLabel(master=janela_login, image=img1)
background.pack()

login_frame = customtkinter.CTkFrame(master=janela_login, width=320, height=360, corner_radius=15)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

entry_usuario = customtkinter.CTkEntry(master=login_frame, placeholder_text="Usuario", width=220, font=("Century Gothic", 16))
entry_usuario.place(x=50, y=135)

entry_senha = customtkinter.CTkEntry(master=login_frame, placeholder_text="Senha", width=220, show="*", font=("Century Gothic", 16))
entry_senha.place(x=50, y=190)

button_fsenha = customtkinter.CTkButton(master=login_frame, width=110, text="Esqueci a senha", fg_color="transparent", font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False)
button_fsenha.place(x=165, y=225)

button_login = customtkinter.CTkButton(master=login_frame, width=220, text="Login", fg_color="#41c269", corner_radius=32, hover_color="#4F5250",font=("Century Gothic", 18), text_color="#FFFFFF", command=login)
button_login.place(x=50, y=270)


logo = customtkinter.CTkLabel(master=login_frame, text="", image=img2)
logo.place(relx=0.5, rely=0.19, anchor="center")

janela_login.mainloop()