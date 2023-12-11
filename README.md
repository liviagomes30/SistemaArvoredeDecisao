# Sistema - Árvore de Decisão
## APLICAÇÃO COM ÁRVORE DE DECISÃO - SISTEMA ESPECIALISTA 

### Base de dados utilizada: “Estimation of obesity levels based on eating habits and physical condition” - https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition 

#### Informações sobre a base de dados:
A base de dados contém perguntas relacionadas aos hábitos alimentares e físicos do entrevistado, além de sua condição física atual (idade, peso e altura). 
Possui 17 atributos, 2111 registros e 1 classe de variáveis. 

#### ATRIBUTOS

1.	Gênero 
  a.	Masculino
  b.	Feminino
2.	Idade
3.	Altura (em metros)
4.	Peso (em kg)
5.	Algum membro da família sofre ou já sofreu de sobrepeso?
  a.	Sim
  b.	Não
6.	Você come comida calórica com frequência? (FAVC)
  a.	Sim
  b.	Não
7.	Você costuma comer vegetais nas refeições? (FCVC)
  a.	Nunca (1)
  b.	Às vezes (2)
  c.	Sempre (3)
8.	Quantas refeições principais você faz por dia? (NCP)
  a.	Entre 1 ou 2 (1)
  b.	3 (2)
  c.	Mais que 3 (3)
9.	Você come no intervalo das refeições principais? (CAEC)
  a.	Não 
  b.	Às vezes
  c.	Frequentemente
  d.	Sempre
10.	 Você fuma?
  a.	Sim
  b.	Não
11.	Quanto você bebe de água por dia? (CH2O; está como número decimal)
  a.	Menos de 1 litro (1)
  b.	Entre 1 e 2 litros (2)
  c.	Mais que 2 litros (3)
12.	Você monitora diariamente as calorias ingeridas? (SCC)
  a.	Sim
  b.	Não
13.	Com que frequência por semana você pratica atividades físicas? (FAF; está como número decimal)
  a.	Nunca (0)
  b.	1 a 2 dias (1)
  c.	2 a 4 dias (2)
  d.	4 a 5 dias (3)
14.	Quantas horas por dia você utiliza equipamentos eletrônicos (celular, videogame, televisão, computador, entre outros)? (TUE; está como número decimal)
  a.	Entre 0 a 2 horas (0)
  b.	3 a 5 horas (1)
  c.	Mais que 5 horas (2)
15.	Com que frequência você bebe álcool? (CALC)
  a.	Nunca
  b.	Às vezes
  c.	Frequentemente
  d.	Sempre
16.	Qual meio de transporte você mais utiliza? (MTRANS)
  a.	Carro
  b.	Moto
  c.	Bicicleta
  d.	Transporte público
  e.	A pé
17.	Nível de obesidade (classe de variáveis)
  a.	Abaixo do peso
  b.	Normal 
  c.	Sobrepeso Nível I
  d.	Sobrepeso Nível II
  e.	Obesidade Tipo I 
  f.	Obesidade Tipo II
  g.	Obesidade Tipo III 

### ÁRVORE DE DECISÃO E MATRIZ DE CONFUSÃO
Utilizamos 70% do conjunto de dados para treino e 30% para teste, por meio da ferramenta Orange.
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/3e78e59f-38fd-47ad-8018-a0f6f3e3e669)
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/cfb2a581-46ca-4549-8141-04c634d4338e)
Analisando a Matriz de Confusão, podemos observar que, de 633 registros testados, nosso modelo adivinhou corretamente 603 (soma dos valores na diagonal principal) e errou 30 (soma dos valores que não estão na diagonal principal).

### PROGRAMA DESENVOLVIDO COM BASE NA BASE DE DADOS
Criamos um programa em Python utilizando o framework Streamlit. O programa roda no navegador através de um servidor local.
O objetivo do programa é determinar o nível de obesidade de uma pessoa com base numa série de perguntas. 
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/b4895d46-c447-42a7-b62f-8128a99fd8a9)
A partir das respostas do usuário, o sistema mostra a classificação do nível de obesidade. Exemplo de algumas classificações do programa:
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/3eabfe29-610d-4bb3-b74d-c8de43080db5)
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/9142878f-e794-4dcf-bda0-28d0d77014db)
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/713dcecf-6e0f-46b4-8344-3bb15bd96e48)
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/d70512ab-f759-4697-a53d-cf229bae4532)








