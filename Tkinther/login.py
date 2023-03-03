class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        if self.email == "" or self.password == "":
            return "Por favor ingrese su correo y contraseña"
        elif self.email == "upq@edu.com" and self.password == "cardenal":
            return f"Bienvenido {self.email}"
        else:
            return "El correo o la contraseña son incorrectos"





