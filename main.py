#importando as bibliotecas
import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from functions import ClassificadorObesidade


# biblioteca Pandas - conjunto de dados
# biblioteca Streamlit - interface do nosso App
# Sklearn - dividir o nosso conjunto de dados em treino e teste, utilizando para isso um classificador baseado em árvore de decisão, podendo no final verificar a acurácia do nosso modelo criado.

class InterfaceClassificador:
  
  #título
  # O método especial __init__ é o construtor da classe. É chamado automaticamente quando um objeto da classe é instanciado. Aqui, ele configura o título da página Streamlit (st.set_page_config) como "Classificador de Obesidade" e inicializa um objeto da classe ClassificadorObesidade chamado self.funcoes.
  def __init__(self):
    st.set_page_config(page_title="Classificador de Obesidade")
    self.funcoes = ClassificadorObesidade() # self.funcoes é uma instância da classe ClassificadorObesidade. 

  # 0 Gender : Gênero
  # 1 age : idade
  # 2 height : altura
  # 3 weight : peso
  # 4 family-history-with-overweight : historico
  # 5 favc : comida calorica
  # 6 fcvc : comer vegetais
  # 7 ncp : refeições
  # 8 caec : intervalo refeições

  # 9 ch20 : agua
  # 10 scc : calorias
  # 11 faf : ativ fisica

  # 12 calc : alcool



  #dados dos usuários com a função
  # criar uma barra lateral com widgets interativos para coletar as respostas do usuário
  def get_user_date(self):
   
    peso = st.sidebar.number_input("Peso (em kg): ", step=0.01, value=57.80, min_value=0.01)
    
    genero = st.sidebar.selectbox("Seu gênero: ", ["Feminino", "Masculino"])
    
    idade = st.sidebar.number_input("Idade: ", step=1, value=20, min_value=0, max_value=110)
    
    altura = st.sidebar.number_input("Altura (em metros): ", step=0.01, value=1.70, min_value=0.01)
    
    historico = st.sidebar.selectbox("Existe casos de obesidade em sua família?", ["Não", "Sim"])
    
    calorico = st.sidebar.selectbox("Frequentemente consome alimentos de grandes calorias?", ["Não", "Sim"])
    
    consumo_vegetais = st.sidebar.selectbox("Com que frequência consome vegetais?", ["Sempre", "Às vezes", "Nunca"])

    refeicoes = st.sidebar.selectbox("Quantas refeições principais por dia?", ["Entre 1 e 2", "3 refeições", "Mais que 3"])
    
    comida_entre_refeicoes = st.sidebar.selectbox("Você consome qualquer comida entre as refeições principais?", ["Sempre", "Às vezes", "Frequentemente", "Nunca"])
    
    
    agua = st.sidebar.selectbox("Como está seu consumo de água por dia?", ["Menos de 1L", "Entre 1L e 2L", "Mais de 2L"])
    
    calorias = st.sidebar.selectbox("Tem  costume de monitorar o consumo diário de calorias?", ["Sim", "Não"])
    
    atividades_fisicas = st.sidebar.selectbox("Com que frequência faz atividades físicas na semana?", ["Não faço", "1 ou 2 dias", "3 ou 4 dias", "5 dias ou mais"])
    
    
    alcool = st.sidebar.selectbox("Sobre o consumo de bebidas alcoólicas: ", ["Não bebo", "Às vezes", "Frequentemente", "Sempre"])
    

    #Armazena as respostas do usuário em uma lista 
    respostasUsu = [
      genero, idade, altura, float(peso), historico, calorico,
      consumo_vegetais, refeicoes, comida_entre_refeicoes, agua, calorias, atividades_fisicas, alcool
    ]

    resultado, criticidade = self.funcoes.classificar_obesidade(respostasUsu)
    # chamando o método classificar_obesidade dessa instância específica da classe ClassificadorObesidade
    # O método classificar_obesidade retorna dois valores, que são atribuídos a resultado e criticidade 

    # Esses valores (resultado e criticidade) são então passados como argumentos para o método self.dados(resultado, criticidade)
    # No método dados, esses valores são utilizados para exibir informações na interface com o usuário.
    self.dados(resultado, criticidade)



  def dados(self, resultado, criticidade):
    st.title("CLASSIFICADOR DE OBESIDADE 📊")

    if resultado != "Peso Normal":
      # Cria uma métrica na interface mostrando o rótulo "Peso", o valor do resultado e o delta (diferença) que inclui a criticidade.
      st.metric(label="Peso", value=resultado, delta="- nível de criticidade: {}".format(criticidade))
      if resultado == "Obesidade Tipo III":
          # Exibe uma mensagem de erro na interface indicando que as informações do usuário apresentam um quadro crítico para a saúde.
          st.error("Atenção :loudspeaker:  As suas informações apresentam um quadro crítico para a sua saúde.")
      else:
          # exibe uma mensagem de aviso indicando que é necessário dar mais atenção à saúde.
          st.warning("Atenção :mega:  É necessário dar mais atenção à sua saúde.")
      # Adiciona um texto na interface sugerindo ações que o usuário pode realizar para melhorar a situação do seu peso.
      st.write("Agora que você está ciente da sua situação de peso, é recomendável que você incorpore hábitos saudáveis para promover o bem-estar e cuidar da sua saúde de forma consciente.")
      # Fornece mais instruções ao usuário sobre como usar as opções disponíveis na interface para alcançar um peso normal.
      st.write("Explore as opções disponíveis no menu lateral para criar combinações que levem ao peso normal. Isso permitirá que você identifique as mudanças necessárias e saiba como alcançar o peso recomendado.😉")
    else:
        botao = False
        st.metric(label="Peso", value=resultado, delta="{} (nível de criticidade)".format(criticidade))
        st.success("Parabéns :tada:")
        st.write("Você atingiu um nível saudável considerando suas características e hábitos. Lembre-se de que isso é apenas uma dedução com 93,4% de assertividade. Vale a pena sempre estar atento à sua saúde!")
        st.write("Está feliz com seu resultado? Vamos comemorar juntos!")
        
        if botao == False:
            x = st.button("Comemorar")
            if x == True:
                st.balloons()

# Verifica se o script está sendo executado diretamente (não importado como módulo).
if __name__ == "__main__":
    # Cria uma instância da classe InterfaceClassificador chamada obj.
    obj = InterfaceClassificador()
    # Chama o método questionario para iniciar a interação com o usuário.
    obj.get_user_date()
    
# streamlit run c:\\Users\\livia\\Documents\\2-termo\\ciencD\\trabObesidade\\main.py
