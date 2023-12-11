# Sistema - Árvore de Decisão
## APLICAÇÃO COM ÁRVORE DE DECISÃO - SISTEMA ESPECIALISTA 

### Base de dados utilizada: “Estimation of obesity levels based on eating habits and physical condition” - https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition 



#### Informações sobre a base de dados:
A base de dados contém perguntas relacionadas aos hábitos alimentares e físicos do entrevistado, além de sua condição física atual (idade, peso e altura). 
Possui 17 atributos, 2111 registros e 1 classe de variáveis. 

#### ATRIBUTOS

1. Gênero 
   *	Masculino
   *	Feminino
2. Idade
3.	Altura (em metros)
4.	Peso (em kg)
5.	Algum membro da família sofre ou já sofreu de sobrepeso?
   *	Sim
   *	Não
6.	Você come comida calórica com frequência?
   *	Sim
   *	Não
7.	Você costuma comer vegetais nas refeições?
  *	Nunca (1)
  *	Às vezes (2)
  *	Sempre (3)
8.	Quantas refeições principais você faz por dia?
  *	Entre 1 ou 2 (1)
  *	3 (2)
  *	Mais que 3 (3)
9.	Você come no intervalo das refeições principais?
  *	Não 
  *	Às vezes
  *	Frequentemente
  *	Sempre
10.	 Você fuma?
  *	Sim
  *	Não
11.	Quanto você bebe de água por dia?
  *	Menos de 1 litro (1)
  *	Entre 1 e 2 litros (2)
  *	Mais que 2 litros (3)
12.	Você monitora diariamente as calorias ingeridas?
  *	Sim
  *	Não
13.	Com que frequência por semana você pratica atividades físicas?
   	*Nunca (0)
   	*1 a 2 dias (1)
   	*2 a 4 dias (2)
   	*4 a 5 dias (3)
14.	Quantas horas por dia você utiliza equipamentos eletrônicos (celular, videogame, televisão, computador, entre outros)?
  *	Entre 0 a 2 horas (0)
  *	3 a 5 horas (1)
  *	Mais que 5 horas (2)
15.	Com que frequência você bebe álcool?
  *	Nunca
  *	Às vezes
  *	Frequentemente
  *	Sempre
16.	Qual meio de transporte você mais utiliza?
  *	Carro
  *	Moto
  *	Bicicleta
  *	Transporte público
  *	A pé
17.	Nível de obesidade (classe de variáveis)
  *	Abaixo do peso
  *	Normal 
  *	Sobrepeso Nível I
  *	Sobrepeso Nível II
  *	Obesidade Tipo I 
  *	Obesidade Tipo II
  *	Obesidade Tipo III 


### ÁRVORE DE DECISÃO E MATRIZ DE CONFUSÃO
Utilizamos 70% do conjunto de dados para treino e 30% para teste, por meio da ferramenta Orange.
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/3e78e59f-38fd-47ad-8018-a0f6f3e3e669)
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/cfb2a581-46ca-4549-8141-04c634d4338e)
Analisando a Matriz de Confusão, podemos observar que, de 633 registros testados, nosso modelo adivinhou corretamente 603 (soma dos valores na diagonal principal) e errou 30 (soma dos valores que não estão na diagonal principal).

### PROGRAMA DESENVOLVIDO COM BASE NA BASE DE DADOS
Criamos um programa em Python utilizando o **framework Streamlit**. O programa roda no navegador através de um servidor local.
O objetivo do programa é determinar o nível de obesidade de uma pessoa com base numa série de perguntas. 

![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/b4895d46-c447-42a7-b62f-8128a99fd8a9)


A partir das respostas do usuário, o sistema mostra a classificação do nível de obesidade. Exemplo de algumas classificações do programa:
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/3eabfe29-610d-4bb3-b74d-c8de43080db5)
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/9142878f-e794-4dcf-bda0-28d0d77014db)
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/713dcecf-6e0f-46b4-8344-3bb15bd96e48)
![image](https://github.com/liviagomes30/SistemaArvoredeDecisao/assets/97247583/d70512ab-f759-4697-a53d-cf229bae4532)








