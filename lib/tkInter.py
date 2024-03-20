import tkinter as tk
from PIL import Image, ImageTk

class InterfaceTemperaturas:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface de Temperaturas")
        self.temp1 = 0
        self.temp2 = 0
        self.presenceSensor = False

        self.switch1Old = None
        self.switch2Old = None
        self.switch3Old = None

        self.commandIsUpdated=False

        self.root.configure(bg="white")

        # Elemento 1: Temperatura 1
        self.label_temp1_nome = tk.Label(root, text="Temperatura 1", bg='white')
        self.label_temp1_nome.grid(row=0, column=0)

        self.temp1_valor = tk.Label(root, text=f"{self.temp1}°C", borderwidth=1, relief="solid", bg='white',padx=10, pady=10)
        self.temp1_valor.grid(row=1, column=0)

        # Elemento 2: Temperatura 2
        self.label_temp2_nome = tk.Label(root, text="Temperatura 2", bg='white')
        self.label_temp2_nome.grid(row=0, column=1)

        self.temp2_valor = tk.Label(root, text=f"{self.temp2}°C", borderwidth=1, relief="solid", bg='white',padx=10, pady=10)
        self.temp2_valor.grid(row=1, column=1)

        # Elemento 3: Sensor de Presença
        self.label_presence_nome = tk.Label(root, text="Sensor de Presença", bg='white')
        self.label_presence_nome.grid(row=0, column=2)

        # Carregar imagens
        self.img_presence_true = Image.open("lib/true.png").resize((80, 80))
        self.img_presence_false = Image.open("lib/false.png").resize((80, 80))

        self.presence_image_label = tk.Label(root, bg='white')
        self.presence_image_label.grid(row=1, column=2)

        # Adicionando a imagem do ar condicionado abaixo do nome do elemento
        self.ar_condicionado_img = Image.open("lib/ac.png")  # Substitua "ar_condicionado.png" pelo nome do arquivo da sua imagem do ar condicionado
        self.ar_condicionado_img = self.ar_condicionado_img.resize((80, 80))  # Ajuste o tamanho conforme necessário
        self.ar_condicionado_img = ImageTk.PhotoImage(self.ar_condicionado_img)

        # Elemento 4: Ar Condicionado
        self.nome_elemento = tk.Label(root, text="Ar-Condicionado 1",bg='white')
        self.nome_elemento.grid(row=2, column=0)

        self.ar_condicionado_label = tk.Label(root, image=self.ar_condicionado_img,bg='white')
        self.ar_condicionado_label.grid(row=3, column=0)

        # Adicionando o switch
        self.switch1_var = tk.BooleanVar()
        self.switch1 = tk.Checkbutton(root, variable=self.switch1_var, bg='white')
        self.switch1.grid(row=4, column=0)

        # Elemento 5: Ar Condicionado
        self.nome_elemento = tk.Label(root, text="Ar-Condicionado 2",bg='white')
        self.nome_elemento.grid(row=2, column=1)

        # Adicionando a imagem do ar condicionado abaixo do nome do elemento
        self.ar_condicionado_label1 = tk.Label(root, image=self.ar_condicionado_img,bg='white')
        self.ar_condicionado_label1.grid(row=3, column=1)

        self.switch2_var = tk.BooleanVar()
        self.switch2 = tk.Checkbutton(root, variable=self.switch2_var, bg='white')
        self.switch2.grid(row=4, column=1)

        # Adicionando a imagem do ar condicionado abaixo do nome do elemento
        self.light_img = Image.open("lib/light.png")  # Substitua "ar_condicionado.png" pelo nome do arquivo da sua imagem do ar condicionado
        self.light_img = self.light_img.resize((80, 80))  # Ajuste o tamanho conforme necessário
        self.light_img = ImageTk.PhotoImage(self.light_img)
        self.light_label = tk.Label(root, image=self.light_img,bg='white')
        self.light_label.grid(row=3, column=2)

        self.switch3_var = tk.BooleanVar()
        self.switch3 = tk.Checkbutton(root, variable=self.switch3_var, bg='white')
        self.switch3.grid(row=4, column=2)
    
    def getSwitchInfo(self):
        return self.switch1_var.get(),self.switch2_var.get(),self.switch3_var.get()
    
    def checkCommandIsUpdated(self):
        switch1_state = self.switch1_var.get()
        switch2_state = self.switch2_var.get()
        switch3_state = self.switch3_var.get()
    
        if (switch1_state == self.switch1Old and switch2_state == self.switch2Old and switch3_state == self.switch3Old):
            self.commandIsUpdated = False
        else:
            self.commandIsUpdated = True
    
        self.switch1Old = switch1_state
        self.switch2Old = switch2_state
        self.switch3Old = switch3_state
    
        return self.commandIsUpdated
    
    def updateSensorsData(self, temp1, temp2, presenceSensor):
        # Atualizar os valores dos labels de temperatura e sensor de presença
        self.temp1_valor.config(text=f"{temp1:.2f}°C")
        self.temp2_valor.config(text=f"{temp2:.2f}°C")
        if presenceSensor:  # Verificar se o sensor de presença está ativado
            presence_image = ImageTk.PhotoImage(self.img_presence_true)
        else:
            presence_image = ImageTk.PhotoImage(self.img_presence_false)

        self.presence_image_label.configure(image=presence_image)
        self.presence_image_label.image = presence_image

        # Agendar a próxima atualização
        self.root.after(1000, self.updateSensorsData, temp1, temp2, presenceSensor)
