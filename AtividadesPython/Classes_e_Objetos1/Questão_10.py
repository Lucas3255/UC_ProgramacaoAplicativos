# 10 Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):Atributos: Nome, Fome, Saúde e Idade b. Métodos:
# Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos
# levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde,
# ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode
# ser calculada a qualquer momento.

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_dados(self):
        return f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}"

    def retornar_humor(self):
        humor = (self.fome + self.saude) / 2
        return f"Humor: {humor}"

tamagushi_exemplo = Tamagushi(nome="Thomas", fome=5, saude=8, idade=2)
print("Dados do Tamagushi:")
print(tamagushi_exemplo.retornar_dados())
print(tamagushi_exemplo.retornar_humor())
