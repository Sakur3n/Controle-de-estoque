import pandas as pd
import cv2
from pyzbar.pyzbar import decode
from time import sleep

class arq():
    def puvdef(self):
        #ler a tabela
        df = pd.read_excel("Estoque1.xlsx")
    
    #entrada do codigo do produto
        out = int(self.cod)

        #Localizando o produto
        dk = df.loc[df['Código'] == out]
        if not dk.empty:
            linha = dk.index[0]
            self.pp = peso_ant = int(df.at[linha,'Preço Unitário de Venda'])

#--------------------------ADIÇÃO ABAIXO----------------------------------------    
    def adicao(self):
        #ler a tabela
        df = pd.read_excel("Estoque1.xlsx")
    
    #entrada do codigo do produto
        out = int(self.cod)

        #Localizando o produto
        dt = df.loc[df['Código'] == out]
        print (dt)

        #Adiconando o peso na coluna vazia
        peso = float(self.final)

        if not dt.empty:
            linha = dt.index[0]
        
        #somando o peso
            peso_ant = float(df.at[linha,'estoque atual'])
            new_peso = peso_ant + peso

            df.at[linha,'estoque atual'] = float(new_peso)

            df.to_excel('Estoque1.xlsx', index=False)

        else:
            print('Linha não encontrada!!')

        #ptint
        dt = df.loc[df['Código'] == out]
        print (dt)


class ler_cod_barras(arq):
    
    def decodificar_codigo(self):
        # Converter o self.frame para tons de cinza
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        
        # Decodificar o código de barras
        self.codigos = decode(self.gray)
        
        return self.codigos

    def cap_tela(self):
        self.cap = cv2.VideoCapture(0)
        self.sucesso, self.frame = self.cap.read()

        while self.sucesso:

            # Ler o self.frame
            self.sucesso, self.frame = self.cap.read()

            # Decodificar o código de barras
            self.codigos = self.decodificar_codigo()

            for codigo in self.codigos:
                
                self.p = codigo.data.decode('utf-8')[1:7]
                self.g = codigo.data.decode('utf-8')[7:12]
                
                self.cod = int(self.p)
                self.preco = int(self.g)
                
                if self.preco != 0:
                    self.puvdef()
                    ppv = float(self.pp)
                    ante_final = float(self.preco)
                    semi_final= float(ante_final / ppv)
                    self.final = float(semi_final / 100)
                    sleep(1)               
                self.adicao()
                sleep(2)
               

            cv2.imshow('Leitor de Código de Barras', self.frame)
            key = cv2.waitKey(1)
            if key == 27:
                break

    
        self.cap.release()
        cv2.destroyAllWindows()


d = ler_cod_barras()
d.cap_tela()

