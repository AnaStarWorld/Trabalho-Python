import PySimpleGUI as tk
from PySimpleGUI import messagebox
import json
import os

# Nome do arquivo onde os dados serão persistidos
DATA_FILE = 'users_data.json'

# Função para carregar os dados do arquivo JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Função para salvar os dados no arquivo JSON
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Função para validar os dados de login
def validate_login(username, password):
    data = load_data()
    if username in data and data[username] == password:
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha inválidos.")

# Função para registrar um novo usuário
def register_user(username, password, confirm_password):
    data = load_data()
    if username in data:
        messagebox.showerror("Registro", "Nome de usuário já existe.")
    elif password != confirm_password:
        messagebox.showerror("Registro", "As senhas não coincidem.")
    else:
        data[username] = password
        save_data(data)
        messagebox.showinfo("Registro", "Registro bem-sucedido!")

# Classe para a tela de Login
class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tela de Login")

        self.label_username = tk.Label(self, text="Nome de usuário:")
        self.label_username.pack(pady=5)

        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self, text="Senha:")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack(pady=5)

        self.button_register = tk.Button(self, text="Registrar", command=self.go_to_register)
        self.button_register.pack(pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username and password:
            validate_login(username, password)
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    def go_to_register(self):
        self.destroy()
        RegisterScreen().mainloop()

# Classe para a tela de Registro
class RegisterScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tela de Registro")

        self.label_username = tk.Label(self, text="Nome de usuário:")
        self.label_username.pack(pady=5)
        self.theme('Dark Blue 3')

        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self, text="Senha:")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        self.label_confirm_password = tk.Label(self, text="Confirme a senha:")
        self.label_confirm_password.pack(pady=5)

        self.entry_confirm_password = tk.Entry(self, show="*")
        self.entry_confirm_password.pack(pady=5)

        self.button_register = tk.Button(self, text="Registrar", command=self.register)
        self.button_register.pack(pady=5)

        self.button_back = tk.Button(self, text="Voltar ao Login", command=self.go_to_login)
        self.button_back.pack(pady=5)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        if username and password and confirm_password:
            register_user(username, password, confirm_password)
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    def go_to_login(self):
        self.destroy()
        LoginScreen().mainloop()

# Inicializar a tela de login
if __name__ == "__main__":
    LoginScreen().mainloop()
