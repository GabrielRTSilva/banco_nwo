class moeda():
    def __init__(self, nome:str, nome_visual:str, preco:float, quantidade=0):
        self.nome = nome
        self.nome_visual = nome_visual
        self.valor = preco
        self.quantidade = quantidade
