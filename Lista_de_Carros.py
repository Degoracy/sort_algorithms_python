class carros:
    def _init_(self, modelo):
        self.modelo = modelo
        self.mensagem1 = "Qual modelo do seu carro: "

    def mostrar(self, mensagem1):
        if mensagem1 == 'cobalt' or mensagem1 == 'voyage' or mensagem1 == 'logan':
            print("Otima marca.")
        elif mensagem1 == 'citroen' or mensagem1 == 'fiat' or mensagem1 == 'ford ka':
            print('Essas marcas não são favoraveis')
        else:
            print('Obrigado por participar. ')


carro1 = carros()
carro1.mostrar('fusca')
