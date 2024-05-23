import pandas as pd
from tkinter import *

class Arquivo():
    def limpa_tela(self):
        self.add_product.delete(0, END)

    def limpa_tela2(self):
        self.reduzir_produto.delete(0, END)
        

    def lendo(self):        

        self.cod_inteiro = self.add_product.get()        
        self.seis_primeiros = self.cod_inteiro[1:7]        
        self.seis_ultimos = self.cod_inteiro[7:13]
        self.limpa_tela()

    def somando(self):
        df = pd.read_excel("EstoqueMatriz.xlsx")        
        self.lendo()

        cod_produto = int(self.seis_primeiros)
        dt = df.loc[df["Código"] == cod_produto]
        print(dt)

        if not dt.empty:
            linha = dt.index[0]

            peso_anterior = float(df.at[linha, "estoque atual"])
            preco_venda = float(df.at[linha,"Preço Unitário de Venda"])            
            seis_ult = float(self.seis_ultimos)

            peso_pelo_preco = seis_ult / preco_venda
            peso_etiqueta = float(peso_pelo_preco / 1000)
            peso_etiqueta_arrendodado = round(peso_etiqueta, 3)
            novo_peso = peso_anterior + peso_etiqueta_arrendodado
            
            print("Peso anterior: ",peso_anterior)
            print("Peso da etiqueta: ",peso_etiqueta_arrendodado)
            print(round("Novo peso na planilha: ",novo_peso, 3))

            df.at[linha, "estoque atual"] = novo_peso
            df.to_excel("EstoqueMatriz.xlsx", index = False)
            
            with open("Balanço.csv", "a", newline="", encoding="utf-8") as arquivo:
                linhaa = dt.at[linha,"Descrição"]
                arquivo.write(f"{linhaa}, {peso_etiqueta_arrendodado}Kg \n ")
                arquivo.closed
        else:
            print("Linha não encontrada") 


    def reading (self):        
        self.cod_inteiro = self.reduzir_produto.get()        
        self.seis_primeiros = self.cod_inteiro[1:7]        
        self.seis_ultimos = self.cod_inteiro[7:13]
        self.limpa_tela2()

    def subtraindo (self):
        
        df = pd.read_excel("EstoqueMatriz.xlsx")        
        self.reading()

        cod_produto = int(self.seis_primeiros)
        dt = df.loc[df["Código"] == cod_produto]
        print(dt)

        if not dt.empty:
            linha = dt.index[0]

            peso_anterior = float(df.at[linha, "estoque atual"])
            preco_venda = float(df.at[linha,"Preço Unitário de Venda"])            
            seis_ult = float(self.seis_ultimos)

            peso_pelo_preco = seis_ult / preco_venda
            peso_etiqueta = float(peso_pelo_preco / 1000)
            peso_etiqueta_arrendodado = round(peso_etiqueta, 3)
            novo_peso = peso_anterior - peso_etiqueta_arrendodado
            
            print(peso_etiqueta_arrendodado)
            print(round(novo_peso, 3))
            df.at[linha, "estoque atual"] = novo_peso
            df.to_excel("EstoqueMatriz.xlsx", index = False)
        else:
            print("Linha não encontrada") 

janela = Tk()

class Tela(Arquivo):
    def __init__(self):
        self.tela = janela
        self.tela_()
        self.entrys()
        self.botao()

        janela.mainloop()

    def tela_(self):
        self.tela.title("Inventario de Estoque")
        self.tela.configure(background = "#255255266")
        self.tela.geometry("300x420")
        self.tela.resizable(True, True)
        self.tela.maxsize(width = 1350, height = 720)
        self.tela.minsize(width = 550, height = 250 )

    def entrys(self):
        self.add_product = Label(janela, text = "Código", bg = "#255255250", fg = "white", font = ("verdana", 8, "bold"))
        self.add_product.place(relx = 0.05, rely = 0.08)
        self.add_product = Entry(janela, bg = "#266200266", fg = "white")
        self.add_product.place(relx = 0.05, rely = 0.12, relheight = 0.06)


        self.add_peso = Label(janela, text = "Peso", bg = "#255255250", fg = "white", font = ("verdana", 8, "bold"))
        self.add_peso.place(relx = 0.05, rely = 0.4)
        self.add_peso = Entry(janela, bg = "#266200266", fg = "white")
        self.add_peso.place(relx = 0.05, rely = 0.45, relheight = 0.06)


        self.reduzir_produto = Label(janela, text = "Código", bg = "#255255250", fg = "white", font = ("verdana", 8, "bold"))
        self.reduzir_produto.place(relx = 0.4, rely = 0.08)
        self.reduzir_produto = Entry(janela, bg = "#266200266", fg = "white")
        self.reduzir_produto.place(relx = 0.4, rely = 0.12, relheight = 0.06)

    def botao (self):
        self.somar = Button(janela, text = "Adicionar", command = self.somando)
        self.somar.place(relx = 0.05, rely = 0.20, relheight = 0.06)
        self.add_product.bind("<Return>", lambda event : self.somando())
        

        self.subtrair = Button(janela, text = "Remover", command = self.subtraindo)
        self.subtrair.place(relx = 0.4, rely = 0.20, relheight = 0.06)
        self.reduzir_produto.bind("<Return>", lambda event : self.subtraindo())
Tela()