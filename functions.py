class ClassificadorObesidade:
  def calcular_imc(self, peso, altura):
    return peso / (altura ** 2)
  
  def arvore(self, dados):
    """
    Método para verificar o nível de obesidade usando árvore de decisão (J48).

    Espera-se receber um array:
    arvore_J48(array dados)

    Retorno: string
    """

    i = dados

    # respostasUsu = [
    #   0:genero, 1:idade, 2:altura, 3:float(peso), 4:historico, 5:calorico,
    #   6:consumo_vegetais, 7:refeicoes, 8:comida_entre_refeicoes,
    #   9:fumante, 10:agua, 11:calorias, 12:atividades_fisicas,
    #   13:tempo_em_dipositivos, 14:alcool, 15:meio_de_transporte
    # ]
    obesidade = ''

    if i[3] <= 98.44:
      if i[3] > 60.00:
        if i[3] > 76:
          if i[2] > 1.69:
            if i[3] > 91.05:
              if i[2] <= 1.78:
                obesidade = "Overweight_Level_I"
              else:
                obesidade = "Obesity_Type_I"
            else:
              if i[2] <= 1.72:
                obesidade = "Overweight_Level_I"
              else:
                if i[2] <= 1.80:
                  if i[3] <= 82.22:
                    if i[2] <= 1.76:
                      obesidade = "Overweight_Level_I"
                    else:
                      if i[3] <= 80:
                        obesidade = "Normal_Weight"
                      else:
                        obesidade = "Overweight_Level_I"
                  else:
                    if i[7] == '3 refeições':
                      if i[7] == 'Mais que 3':
                        obesidade = "Overweight_Level_II"
                      else:
                        if i[1] <= 26:
                          obesidade = "Overweight_Level_I"
                        else:
                          obesidade = "Overweight_Level_II"
                else:
                  if i[3] <= 84:
                    obesidade = "Normal_Weight"
                  else:
                    if i[8] == 'Às vezes' or i[8] == 'Não':
                      obesidade = "Overweight_Level_I"
                    else:
                      obesidade = "Normal_Weight"
          else:
            if i[3] <= 80.99:
              if i[2] <= 1.62:
                obesidade = "Obesity_Type_I"
              else:
                obesidade = "Overweight_Level_II"
            else:
              obesidade = "Obesity_Type_I"
        else:
          if i[2] > 1.6:
            if i[2] > 1.73:
              if i[2] <= 1.85:
                if i[3] <= 75.00:
                  obesidade = "Normal_Weight"
                else:
                  obesidade = "Overweight_Level_I"
              else:
                if i[3] > 64.1:
                  obesidade =  "Normal_Weight"
                else:
                  obesidade = "Insufficient_Weight"
            else:
              if i[3] <= 67:
                if i[2] <= 1.61:
                  if i[3] <= 64:
                    obesidade =  "Normal_Weight"
                  else:
                    obesidade = "Overweight_Level_I"
                else:
                  obesidade =  "Normal_Weight"
              else:
                if i[2] <= 1.65:
                  if i[6] == 'Nunca' or i[6] == 'Às vezes':
                    obesidade = "Overweight_Level_I"
                  else:
                    if i[1] <= 20:
                      if i[5] == 'Não':
                        obesidade = "Overweight_Level_II"
                      else:
                        obesidade = "Overweight_Level_I"
                    else:
                      obesidade = "Overweight_Level_I"
                else:
                  if i[3] <= 72:
                    if i[1] <= 26:
                      obesidade = "Normal_Weight"
                    else:
                      obesidade = "Overweight_Level_I"
                  else:
                    obesidade = "Overweight_Level_I"
          else:
            if i[5] == 'Não':
              obesidade = "Overweight_Level_II"
            else:
              if i[3] <= 65.42:
                obesidade = "Overweight_Level_I"
              else:
                obesidade = "Obesity_Type_I"
      else:
        if i[2] > 1.66:
          if i[3] <= 59.99:
            if i[3] <= 54.98:
              obesidade = "Insufficient_Weight"
            else:
              if i[2] <= 1.75:
                if i[4] == 'Sim':
                  obesidade = "Normal_Weight"
                else:
                  obesidade = "Insufficient_Weight"
              else:
                obesidade = "Insufficient_Weight"
          else:
            if i[2] <= 1.8:
              obesidade = "Normal_Weight"
            else:
              obesidade = "Insufficient_Weight"
        else:
          if i[3] <= 46.65:
            if i[2] <= 1.51:
              obesidade = "Normal_Weight"
            else:
              obesidade = "Insufficient_Weight"
          else:
            if i[2] <= 1.51:
              if i[3] <= 55:
                obesidade = "Normal_Weight"
              else:
                if i[1] <= 19:
                  obesidade = "Overweight_Level_I"
                else:
                  obesidade = "Overweight_Level_II"
            else:
              if i[3] <= 50.42:
                if i[2] <= 1.6:
                  obesidade = "Normal_Weight"
                else:
                  obesidade = "Insufficient_Weight"
              else:
                obesidade = "Normal_Weight"
    else:
      if i[0] == "Feminino":
        obesidade = "Obesity_Type_III"
      else:
        if i[3] <= 109.59:
          if i[10] == 'Menos de 1L':
            if i[2] <= 1.74:
              obesidade = "Obesity_Type_II"
            else:
              if i[2] <= 1.79:
                obesidade = "Obesity_Type_I"
              else:
                obesidade = "Overweight_Level_II"
          else:
            if i[2] <= 1.84:
              obesidade = "Obesity_Type_I"
            else:
              obesidade = "Overweight_Level_II"
        else:
          if i[3] > 109.59:
            if i[1] <= 22:
              if i[6] == 'Nunca':
                obesidade = "Obesity_Type_I"
              else:
                if i[8] == 'Não' or i[8] == 'Às vezes':
                  obesidade = "Obesity_Type_II"
                else:
                  obesidade = "Obesity_Type_I"
            else:
              obesidade = "Obesity_Type_II"

    return obesidade

  def renomear_respostas(self, dados):
    """
    Método para percorrer o vetor de respostas e renomear.

    Espera-se receber um array:
    renomear_respostas(array dados)

    Retorno: array
    """

    mapeamento = {
        'Entre 1 e 2': 1,
        '3 refeições': 2,
        'Mais que 3': 3,
        'Menos de 1L': 1,
        'Entre 1L e 2L': 2,
        'Mais de 2L': 3,
        'Não bebo': 'Não',
        'Não faço': 0,
        '1 ou 2 dias': 1,
        '3 ou 4 dias': 2,
        '5 dias ou mais': 3,
        'De 0 a 2 horas': 0,
        'De 3 a 5 horas': 1,
        'Mais de 5 horas': 2,
        'Sempre': 3,
        'Às vezes': 2,
        'Nunca': 1
    }

    for i in range(len(dados)):
        x = dados[i]
        dados[i] = mapeamento.get(x, x)

    return dados

    
  def classificar_obesidade(self, dados):
    """
    Método para receber os dados de entrada do usuário e retornar uma resposta
    relacionado ao seu nível de obesidade.

    Espera-se receber um array:
    classificar_obesidade(array dados)

    Retorno: string
    """
    criticidade = 0

    dados_novo = self.renomear_respostas(dados)
    obesidade = self.arvore(dados_novo)

    if obesidade == 'Insufficient_Weight':
        obesidade = 'Peso Insuficiente'
        criticidade = 1
    elif obesidade == 'Normal_Weight':
        obesidade = 'Peso Normal'
    elif obesidade == 'Overweight_Level_I':
        obesidade = 'Sobrepeso Nível I'
        criticidade = 1
    elif obesidade == 'Overweight_Level_II':
        obesidade = 'Sobrepeso Nível II'
        criticidade = 2
    elif obesidade == 'Obesity_Type_I':
        obesidade = 'Obesidade Tipo I'
        criticidade = 3
    elif obesidade == 'Obesity_Type_II':
        obesidade = 'Obesidade Tipo II'
        criticidade = 4
    elif obesidade == 'Obesity_Type_III':
        obesidade = 'Obesidade Tipo III'
        criticidade = 5
    # ...

    elif obesidade =='':
        # Se a árvore de decisão não classificar, calcular o IMC
        peso = dados[3]  # Índice correspondente ao peso nos dados
        altura = dados[2]  # Índice correspondente à altura nos dados

        imc = self.calcular_imc(peso, altura)

        # Classificação de acordo com o IMC
        if imc < 18.5:
            obesidade = 'Abaixo do Peso'
        elif 18.5 <= imc < 24.9:
            obesidade = 'Peso Normal'
        elif 25 <= imc < 29.9:
            obesidade = 'Sobrepeso'
            criticidade = 1
        elif 30 <= imc < 34.9:
            obesidade = 'Obesidade Grau I'
            criticidade = 2
        elif 35 <= imc < 39.9:
            obesidade = 'Obesidade Grau II'
            criticidade = 3
        else:
            obesidade = 'Obesidade Grau III'
            criticidade = 4



    
    return obesidade, criticidade
