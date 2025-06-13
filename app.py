#Imports
import streamlit as st
from datetime import datetime
from objetos import moeda
import pandas as pd
from fpdf import FPDF
from io import BytesIO
import matplotlib.pyplot as plt

#Data e Hora locais
agora = datetime.now()
data_formatada_br = agora.strftime('%d/%m/%Y %H:%M:%S')


#Inicializando a session state da Carteira

if 'carteira' not in st.session_state:
    st.session_state.carteira = {
        'Bitcoin': moeda('Bitcoin','🪙 BTC', 82_379),
        'Ethereum': moeda('Ethereum','💠 ETH', 6_525),
        'USDC': moeda('USDC','💲 USDC', 5.35),
        'Solana': moeda('Solana','🔷 SOL', 26.05),
        'Cardano': moeda('Cardano','🧱 ADA', 1.67),
        'Dogecoin': moeda('Dogecoin','🐶 DOGE', 0.40),
        'Avalanche': moeda('Avalanche','🏔️ AVAX', 66.09),
        'Ripple': moeda('Ripple','💧 XRP', 1.95),
        'Tether': moeda('Tether','🪙 USDT', 5.354),
        'Real': moeda('Real','🇧🇷 BRL', 1.00),
    }


#Inicializando a session state do Extrato
if 'extrato' not in st.session_state:
    st.session_state.extrato = {
        'OPERAÇÃO': [],
        'DATA': [],
        'MOEDA': [],
        'VALOR MOVIMENTADO': [],
        'CAIXA': []
    }

#Funções globais 
def gerar_pdf_extrato(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Cabeçalhos da tabela
    colunas = df.columns.tolist()
    for coluna in colunas:
        pdf.cell(40, 10, str(coluna), 1)
    pdf.ln()

    # Linhas do extrato
    for _, linha in df.iterrows():
        for valor in linha:
            pdf.cell(40, 10, str(valor), 1)
        pdf.ln()

    # Criar buffer em memória com conteúdo do PDF
    buffer = BytesIO()
    buffer.write(pdf.output(dest='S').encode('latin-1'))
    buffer.seek(0)
    return buffer

#Var globais
moedas = st.session_state.carteira
extrato = st.session_state.extrato

valor_da_moeda_topo_historico = [111970.00, 2651.53, 1.00, 179.70, 0.6628, 0.1823, 20.32, 2.19, 1.00, 4.90]
porcentagem_de_aumento = [5.92, 1.175, 0, 14.2, 2.01, 1.815, 1.03, 4.04, 0,  0]


#App Contet
st.title('🌐 New World Order Bank')
st.subheader('Onde o futuro é digital e sua riqueza é descentralizada!')

with st.expander('Bem vindo ao NWO Bank!'):
    st.write("""
        O NWO Bank é um projeto com o objetivo de despertar o "Feeling of Missing Out" em todos aqueles que o visitarem e ainda não estiverem com parte do seu patrimônio alocado em cripto. O FOMO, nada mais é que a sensação de estar perdendo algo e, nesse caso, o que você está deixando passar é possibilidade de investir no ativo mais revolucionário de nosso século. Através desse app, você poderá simular compras e saques de criptomoedas e então, através da aba "2025" verificar o quanto teria tido de retorno hoje caso tivesse essas moedas em sua carteira. 
             """)
    st.text('Obs.: Os dados dos ativos listados são referente a mínima histórica do BTC que ocorreu em 22/11/2022.')
    st.divider()
    st.subheader('Conheça um pouco sobre o universo das Decentralized Finances.')
    st.write("""
        Vivemos a transição de uma era em que o controle financeiro estava concentrado em poucas instituições para um novo paradigma: a descentralização. 
            """)
    st.write("""
        Tudo isso é possível graças à tecnologia blockchain, um tipo de livro-razão digital que registra cada transação de forma imutável e pública. Isso garante segurança, rastreabilidade e autonomia sobre o seu dinheiro, sem a necessidade de confiar em bancos tradicionais.
            """)
    st.write("""
        Dentro desse ecossistema, emergem as Finanças Descentralizadas, ou DeFi, um conjunto de aplicações que replicam serviços bancários como empréstimos, investimentos e seguros, mas de forma automatizada, segura e acessível a qualquer pessoa com conexão à internet.   
        """)
    st.write("""
        E no centro dessa revolução está o Bitcoin, a primeira criptomoeda da história, criada em 2009 como uma resposta à crise financeira global. Mais do que dinheiro digital, o BTC representa soberania financeira, sendo cada vez mais aceito como reserva de valor em tempos de inflação e instabilidade.     
        """)
    st.write("""
        No cenário macroeconômico atual, esse movimento ganha ainda mais importância.

Desde a pandemia de COVID-19, grandes economias responderam com impressões massivas de dinheiro. Esse excesso de liquidez pressionou moedas fiduciárias e impactou o poder de compra das pessoas. O Bitcoin, com seu suprimento limitado a 21 milhões de unidades, oferece uma proteção natural contra essa erosão monetária.

Ao mesmo tempo, diversos países enfrentam crises de dívida soberana. Para manter suas contas equilibradas, governos recorrem à emissão de mais moeda, o que tende a alimentar ciclos inflacionários. Ao descentralizar o controle financeiro, o Banco NWO entrega ferramentas reais de preservação de valor diretamente ao indivíduo, sem intermediários.

Também vivemos uma fase de alta volatilidade e incertezas geopolíticas. Conflitos, sanções e instabilidades institucionais têm reflexo direto nos mercados e nas moedas nacionais. Ter acesso à tecnologia blockchain e às soluções DeFi permite diversificação, portabilidade e liberdade financeira em escala global.

Além disso, milhões de pessoas ao redor do mundo ainda não têm acesso a serviços bancários. As soluções descentralizadas funcionam via internet, sem burocracias, sem intermediários e sem discriminação. Isso representa um passo decisivo rumo à inclusão financeira em escala planetária.    
        """)
    st.write("""
        Dessa forma, convido a você a explorar um pouco dos lucros grotescos que foram concedidos a todos aqueles que estão acompanhando essa vanguarda. Bem vindo a NWO! 
        """)

aba1, aba2, aba3, aba4, aba5= st.tabs(["🛅 Deposito", "🪙 Saque",  "💼 Carteira",  "📄 Extrato", "🎉 2025 🎉"])


with aba1:
    st.subheader('Realize o seu depósito com a NWO Bank!')

    moeda_deposito_selecionada = st.selectbox('Escolha a moeda que deseja depositar:', list(moedas.keys()))    
    valor_depositado = st.number_input("Digite o valor a ser depositado. Mínimo de R$10",  min_value=10)

    if st.button('Confirmar Depósito'):
        moedas[moeda_deposito_selecionada].quantidade += valor_depositado

        #Adicionar registro no extrato após a operação
        extrato['OPERAÇÃO'].append('Depósito')
        extrato['DATA'].append(data_formatada_br)
        extrato['MOEDA'].append(moeda_deposito_selecionada)
        extrato['VALOR MOVIMENTADO'].append(str(f'R$ {valor_depositado}'))
        extrato['CAIXA'].append(str(f'R${moedas[moeda_deposito_selecionada].quantidade}'))

        #Mensagem que confirma a operação
        st.success('Depósito realizado com sucesso. Verifique sua carteira.')

with aba2:
    st.subheader('Realize o seu saque com a NWO Bank!')

    moeda_saque_selecionada = st.selectbox('Escolha a moeda que deseja sacar:', list(moedas.keys()))    
    valor_sacado = st.number_input("Digite o valor a ser sacado. Mínimo de R$5,",  min_value=5)

    if st.button('Confirmar Saque'):
        if valor_sacado > moedas[moeda_saque_selecionada].quantidade:
            st.error(f'Você não possui o valor de R${valor_sacado} em {moeda_saque_selecionada}. Realize um depósito ou selecione outra moeda.')
        else:
            moedas[moeda_saque_selecionada].quantidade -= valor_sacado

            #Adicionar registro no extrato após a operação
            extrato['OPERAÇÃO'].append('Saque')
            extrato['DATA'].append(data_formatada_br)
            extrato['TOKEN'].append(moeda_saque_selecionada)
            extrato['VALOR MOVIMENTADO'].append(str(f'R$ {valor_sacado}'))
            extrato['CAIXA'].append(str(f'R${moedas[moeda_saque_selecionada].quantidade}'))

            #Mensagem que confirma a operação
            st.success('Saque realizado com sucesso. Verifique seu extrato.')

with aba3:
    st.subheader("Confira abaixo a sua carteira de investimentos!")

    aba6, aba7 = st.tabs(['Tabela', 'Gráfico'])


    with aba6:
        table_carteira = {
        'TOKEN': [i.nome_visual for i in moedas.values()],
        'NOME': [i.nome for i in moedas.values()],
        'VALOR DO TOKEN': [str(f'R${i.valor}') for i in moedas.values()],
        'QTD. TOKENS': [ str(f'{round(i.quantidade/i.valor, 3)}') for i in moedas.values()],
        'VALOR APLICADO': [ str(f'R${i.quantidade}') for i in moedas.values()]
        }

        st.table(table_carteira)
    with aba7:
        # Dados
        tokens = []
        valores = []

        for i in moedas.values():
            if i.quantidade > 0:
                tokens.append(i.nome)
                valores.append(i.quantidade)

        opcao_grafico = st.selectbox("Escolha o tipo a visualização:", ["Distribuição da Carteira", "Valor Aplicado por Token",])

        if sum(valores) == 0:
            st.info("Você ainda não possui valores aplicados na carteira. Realize um depósito para visualizar os gráficos.")
        else:
            if opcao_grafico == "Distribuição da Carteira":
                fig1, ax1 = plt.subplots()
                ax1.pie(valores, labels=tokens, autopct='%1.1f%%', startangle=90)
                ax1.axis('equal')  # Deixa a pizza redonda
                st.pyplot(fig1)

            elif opcao_grafico == "Valor Aplicado por Token":
                fig2, ax2 = plt.subplots()
                ax2.bar(tokens, valores)
                ax2.set_ylabel('Valor investido (R$)')
                ax2.set_title('Valor Aplicado por Criptomoeda')
                plt.xticks(rotation=45)
                st.pyplot(fig2)



with aba4:
    st.write("Confira o seu extrato abaixo")
    st.table(extrato)

    # Converte o dicionário para DataFrame
    df_extrato = pd.DataFrame(extrato)

    # Gerar PDF
    extrato_pdf = gerar_pdf_extrato(df_extrato)

    st.download_button(label="📄 Baixar PDF do Extrato",data= extrato_pdf,file_name="extrato_bancario.pdf",mime="application/pdf")

with aba5: 
    st.header('Quanto você teria hoje se tivesse investido o valor que possui em sua carteira do Banco NWO em criptomoedas na vida real?')
    st.text('O último bearmarket do Bitcoin formou novos milionários ao redor do mundo. O próprio BTC atingiu o seu topo histórico em 22/05/2025 com uma alta de 592% em relação ao seu menor valor no ciclo. As altcoins mais comercializadas hoje, de acordo com a Coin Market Cap, também alavancaram o patrimônio daqueles investidores mais ousados. Veja a seguir uma tabela comparando o valor direto de cada cripto ativo em relação ao seu crescimento em porcentagem.')
    st.text('Obs.: Nesse cálculo não foi considerado a variação do dolar.')
    st.divider()

    investimento_2025 = {
    'TOKEN': table_carteira['TOKEN'],
    'VALOR DO TOKEN EM 2022': table_carteira['VALOR DO TOKEN'],
    'QTD TOKENS': table_carteira['QTD. TOKENS'],
    'VALOR APLICADO EM 2022': table_carteira['VALOR APLICADO'],
    'AUMENTO EM PORCENTAGEM ': [str(f'{round(i * 100,2)} %') for i in porcentagem_de_aumento],
    'VALOR DO TOKEN EM 2025': [str(f'R$ {round(m.valor * (1 + pct), 2)}') for m, pct in zip(moedas.values(), porcentagem_de_aumento)],
    'RENDIMENTO' : [str(f'R$ {round(m.quantidade *(1 + pct), 2)}') for m, pct in zip(moedas.values(), porcentagem_de_aumento)]
}


    st.table(investimento_2025)