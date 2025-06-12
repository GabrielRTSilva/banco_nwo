import streamlit as st

class moeda():
    def __init__(self, nome:str, nome_visual:str, preco:float, quantidade=0):
        self.nome = nome
        self.nome_visual = nome_visual
        self.valor = preco
        self.quantidade = quantidade
    
    def depositar(self, quantidade_deposito):
        self.quantidade += quantidade_deposito
    
    def saque(self, quantidade_saque):
        if quantidade_saque > self.quantidade:
            st.erro('Você não possui saldo suficiente para realizar essa operação.')
        else:
            self.quantidade -= quantidade_saque