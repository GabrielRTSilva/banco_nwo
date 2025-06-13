
🏦 NWO Bank – Simulador de Investimentos em Criptomoedas com Streamlit

New World Order Bank é um aplicativo interativo desenvolvido com Streamlit que simula operações bancárias com criptomoedas. Seu objetivo é educar, informar e provocar reflexão sobre o crescimento exponencial dos ativos digitais com foco especial na valorização entre 2022 e 2025.

------------------------------------------------------------

🚀 Objetivo

O app foi criado como um experimento educacional para demonstrar:

- O conceito de Finanças Descentralizadas (DeFi)
- A importância da diversificação de patrimônio com criptoativos
- O impacto que uma valorização percentual pode ter sobre investimentos passados

Através de uma interface amigável e lúdica, o usuário pode realizar depósitos, saques, acompanhar sua carteira, baixar o extrato em PDF e ver quanto teria lucrado ao investir no fundo do último bear market de 2022.

------------------------------------------------------------

🔧 Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- Pandas
- Matplotlib
- FPDF

------------------------------------------------------------

💼 Funcionalidades

- 📥 Depósito: simula a aplicação de valores em diferentes criptoativos
- 💸 Saque: permite retirada de valores da carteira
- 📊 Carteira: mostra a composição atual dos ativos (em tabela e gráfico)
- 📄 Extrato: exibe o histórico de movimentações, com opção de download em PDF
- 🎉 Aba 2025: mostra quanto cada cripto teria rendido se investido em 2022

------------------------------------------------------------

🧮 Lógica dos Cálculos

A aba "2025" compara o valor aplicado com uma valorização fictícia (baseada em dados reais do último ciclo de mercado), utilizando a fórmula:

Valor Atual = Valor Investido × (1 + Aumento Percentual)

Essa abordagem permite simular o "e se..." de forma clara e visual, reforçando o conceito de FOMO (Fear of Missing Out).

------------------------------------------------------------

📥 Instalação e Execução

1. Clone o repositório:
git clone https://github.com/GabrielRTSilva/banco_nwo.git
cd sistema_bancario

2. Instale as dependências:
pip install -r requirements.txt

3. Execute a aplicação:
streamlit run app.py

------------------------------------------------------------

📎 Estrutura do Projeto

sistema_bancario/
│
├── app.py                  # Aplicação principal em Streamlit
├── objetos.py              # Definição da classe moeda
├── requirements.txt        # Dependências
└── README.md               # Este arquivo

------------------------------------------------------------

📚 Conceitos Abordados

- Blockchain & DeFi
- Tokens e Volatilidade
- Investimento em ciclos de mercado
- Inclusão financeira
- Educação financeira com visualização de dados

------------------------------------------------------------

🧠 Ideia por trás do projeto

Esse projeto foi criado como parte de um estudo pessoal sobre Python, finanças descentralizadas e experiência do usuário com interfaces interativas. Seu objetivo maior é demonstrar, de forma simples e impactante, como decisões financeiras passadas influenciam o futuro: tudo em um ambiente simulado.

------------------------------------------------------------

📩 Contribua

Sugestões de melhoria, forks e PRs são bem-vindos!

------------------------------------------------------------

📜 Licença

Este projeto está licenciado sob a MIT License.

------------------------------------------------------------

“O futuro é digital. E a sua riqueza, descentralizada.”
