#VAMOS IMPLEMENTAR O JOGO DA TORRE DE HANOI
#EXECUTAR ESTE PROGRAMA NO TERMINAL LINUX COM O COMANDO: python3 hanoi_tower.py 


#*****************************************************************************************************************************
#
#
#
#
#0:IMPORTANDO OS MÓDULOS NECESSÁRIOS


#*****************************************************************************************************************************
#
#
#
#
#1:MENSAGEM DE BOAS VINDAS
print('\n\n')
print('\033[94m'+'\033[01m'+'HH   HH   AAA   NN   NN  OOOOO  IIIII    TTTTTTT  OOOOO  WW      WW EEEEEEE RRRRRR'+'\033[0;0m')     
print('\033[94m'+'\033[01m'+'HH   HH  AAAAA  NNN  NN OO   OO  III       TTT   OO   OO WW      WW EE      RR   RR    '+'\033[0;0m')
print('\033[94m'+'\033[01m'+'HHHHHHH AA   AA NN N NN OO   OO  III       TTT   OO   OO WW   W  WW EEEEE   RRRRRR     '+'\033[0;0m')
print('\033[94m'+'\033[01m'+'HH   HH AAAAAAA NN  NNN OO   OO  III       TTT   OO   OO  WW WWW WW EE      RR  RR     '+'\033[0;0m')
print('\033[94m'+'\033[01m'+'HH   HH AA   AA NN   NN  OOOO0  IIIII      TTT    OOOO0    WW   WW  EEEEEEE RR   RR'+'\033[0;0m')

stop=input()

print('\033[01m'+"\nEsta é uma implementação em Python do jogo conhecido como Torre de Hanoi.\nO Objetivo deste jogo é relativamente simples:\nexistem três torres de blocos e você deve transferir o conteúdo da primeira torre para a \nterceira torre na mesma ordem que eles estão dispostos.\nDurante este processo você pode transferir apenas um bloco por vez e não pode empilhar um bloco de peso maior que o bloco no topo de cada torre.\nO peso dos blocos é indicado por um número.\nCada torre é identificada por um número.\nPara executar um movimento você deve inserir dois valores:\no da torre da qual você está retirando um bloco e o da torre na qual você irá colocar o bloco retirado.\nErros na inserção de dados podem acarretar erros de lógica no programa."+'\033[0;0m')

stop=input()

#*****************************************************************************************************************************
#
#
#
#
#2:CRIANDO UMA CLASSE DA ESTRTURA DE DADOS STACK

class hanoi_stack(object):
 '''Esta classe implementa a estrutura de dados stack que emula um apilha de oelementos do mesmo tipo. Métodos são definidos para inserção e remoção de elementos no topo do stack e uma função que retorna o elemento no topo do stack. Esta classe em particular permitirá apenas a  inserção de elementos satisfazendo a condição básica do jogo de inserir apenas elementos menores que os elemento no topo do stack.'''

 #INSTANCIANDO OS ATRIBUTOS DA CLASSE NO CONSTRUTOR DA CLASSE
 def __init__(self):
  stack:list=[]#STACK SERÁ IMPLEMENTADO USANDO LISTAS 
 
 #MÉTODOS DA CLASSE
 def set_empty_stack(self):
  '''Inicializando um stack vazio'''
  self.stack=[]

 def set_full_stack(self, n:int):
  '''Inicializando um stack não vazio'''
  if(n==1):
   self.stack=[30, 20, 10]
  if(n==2):
   self.stack=[50, 40, 30, 20, 10]
  if(n==3):
   self.stack=[80, 70, 60, 50, 40, 30, 20, 10]
  
 def push(self, n:int):
  '''Função que adiciona um elemento ao stack'''
  if(len(self.stack)<1):
   self.stack.append(n)
  if(n<self.top()):
   self.stack.append(n)
  if(n>self.top()):
   print('\033[06m'+'\033[31m'+'ERRO CRÍTICO: você realizou uma operação inválida.'+'\033[0;0m')
   quit()
  self.stack=self.stack #ATUALIZANDO O STACK

 def pop(self):
  '''Função que remove um elemento do stack''' 
  self.stack.pop()
  self.stack=self.stack #ATUALIZANDO O STACK

 def top(self)->int:
  '''Função que retorna o valor alocado no topo do stack'''
  n=self.stack[len(self.stack)-1]
  return n


'''TESTE CLASSE STACK USE UM # APÓS O TESTE'''
#my_stack=hanoi_stack()
#my_stack.set_full_stack(2)
#print(my_stack.stack)
#my_stack.push(10)
#my_stack.push(60)
#print(my_stack.stack)
#my_stack.pop()
#my_stack.pop()
#print(my_stack.stack)
#print(my_stack.top())


#*****************************************************************************************************************************
#
#
#
#
#3: CRIANDO FUNÇÕES PARA PRINTAR A PILHA DE ELEMENTOS NO STACK


#FUNÇÃO QUE CONVERTE NÚMEROS EM STRINGS
def int_to_str(n:int)->str:
 '''Função que converte um número inteiro em um string com cor'''
 if(n==10):
  string='\033[31m'+str(n)+'\033[0;0m'
 if(n==20):
  string='\033[34m'+str(n)+'\033[0;0m'
 if(n==30):
  string='\033[93m'+str(n)+'\033[0;0m'
 if(n==40):
  string='\033[95m'+str(n)+'\033[0;0m'
 if(n==50):
  string='\033[33m'+str(n)+'\033[0;0m'
 if(n==60):
  string='\033[94m'+str(n)+'\033[0;0m'
 if(n==70):
  string='\033[90m'+str(n)+'\033[0;0m'
 if(n==80):
  string='\033[35m'+str(n)+'\033[0;0m'
 return string

#FUNÇÃO QUE PRINTA UMA LISTA DE NÚMEROS COMO UMA TORRE DE HANOI 
def print_hanoi_tower(tower:list, n:int):
 '''Função que printa elementos de uma lista como uma torre de hanoi'''
 #PRINTADO UMA LISTA VAZIA
 if(len(tower)<1):
  print('+----+')
  print('|    |')
  print('+----+')
  print('TORRE {}'.format(n))
  print('\n')
 else:
  #PRITANDO OS ELEMENTOS DA LISTA
  for i in range(len(tower)-1, -1, -1):
   print('+----+')
   print('| {} |'.format(int_to_str(tower[i])))
  #PRITANDO A BASE DA TORRE
  print('+----+')
  print('TORRE {}'.format(n))
  print('\n')

'''TESTE DA FUNÇÃO QUE PRINTA UMA LISTA COMO UMA TORRE DE HAHOI USE UM # APÓS O TESTE'''
#empty_list=[]
#print_hanoi_tower(empty_list, 0)
#print_hanoi_tower(my_stack.stack, 1)

#*****************************************************************************************************************************
#
#
#
#
#4: SELECIONANDO A DIFICULDADE DO JOGO E INICIALIZANDO AS TRÊS STACKS DO PARTIDA

#SELECIONANDO O NÍVEL DE DIFICULDADE
level:int=int(input('Jogador digite:\n"1" para selecionar o modo de jogo com diculdade fácil;\n"2" para selecionar o modo de jogo com diculdade média;\n"3" para selecionar o modo de jogo com diculdade díficil.\n---> '))

#INICIANDO OS OBJETOS DA CLASSE DE STACKS
tower1=hanoi_stack() #TORRE1, USAR n=1 NA FUNÇÃO print_hanoi_tower
tower1.set_full_stack(level)
tower2=hanoi_stack() #TORRE2, USAR n=2 NA FUNÇÃO print_hanoi_tower
tower2.set_empty_stack()
tower3=hanoi_stack() #TORRE3, USAR n=3 NA FUNÇÃO print_hanoi_tower
tower3.set_empty_stack()

#PRINTANDO O TABULEIRO DO JOGO NA TELA
print('Eis o tabuleiro do jogo em sua configuração inicial:\n')
print_hanoi_tower(tower1.stack, 1)
print_hanoi_tower(tower2.stack, 2)
print_hanoi_tower(tower3.stack, 3)


#*****************************************************************************************************************************
#
#
#
#
#5:INICIALIZANDO VARIÁVEIS QUE SERÃO USADAS DURANTE O JOGO

#EXECUÇÃO DE JOGADAS
first:int=0
second:int=0

#FUNÇÃO QUE PROPORCIONA UMA DICA AO JOGADOR PARA PA CASO MAIS SIMPLES
def help():
 '''Função que proporciona a solução do jogo para o caso mais simples'''
 print('Eis a solução do jogo para o caso de deficuldade fácil:\n')
 print('+----+   +----+   +----+')
 print('| 10 |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('| 20 |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('| 30 |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('TORRE 1  TORRE 2  TORRE 3')
 stop=input()
 print('+----+   +----+   +----+')
 print('|    |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('| 20 |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('| 30 |   |    |   | 10 |')
 print('+----+   +----+   +----+')
 print('TORRE 1  TORRE 2  TORRE 3')
 stop=input()
 print('+----+   +----+   +----+')
 print('|    |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('|    |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('| 30 |   | 20 |   | 10 |')
 print('+----+   +----+   +----+')
 print('TORRE 1  TORRE 2  TORRE 3')
 stop=input()
 print('TORRE 1  TORRE 2  TORRE 3')
 print('+----+   +----+   +----+')
 print('|    |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('|    |   | 10 |   |    |')
 print('+----+   +----+   +----+')
 print('| 30 |   | 20 |   |    |')
 print('+----+   +----+   +----+')
 print('TORRE 1  TORRE 2  TORRE 3')
 stop=input()
 print('+----+   +----+   +----+')
 print('|    |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('|    |   | 10 |   |    |')
 print('+----+   +----+   +----+')
 print('|    |   | 20 |   | 30 |')
 print('+----+   +----+   +----+')
 print('TORRE 1  TORRE 2  TORRE 3')
 stop=input()
 print('+----+   +----+   +----+')
 print('|    |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('|    |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('| 10 |   | 20 |   | 30 |')
 print('+----+   +----+   +----+')
 print('TORRE 1  TORRE 2  TORRE 3')
 stop=input()
 print('+----+   +----+   +----+')
 print('|    |   |    |   |    |')
 print('+----+   +----+   +----+')
 print('|    |   |    |   | 20 |')
 print('+----+   +----+   +----+')
 print('| 10 |   |    |   | 30 |')
 print('+----+   +----+   +----+')
 print('TORRE 1  TORRE 2  TORRE 3')
 stop=input()
 print('+----+   +----+   +----+')
 print('|    |   |    |   | 10 |')
 print('+----+   +----+   +----+')
 print('|    |   |    |   | 20 |')
 print('+----+   +----+   +----+')
 print('|    |   |    |   | 30 |')
 print('+----+   +----+   +----+')
 print('TORRE 1  TORRE 2  TORRE 3\n')
 print('A ideia principal é repetir esta mesma manobra um número suficiente de vezes para ir transportanto os elementos da torre 1 para a torre 3.')
 stop=input()


'''TESTE DA FUNÇÃO DE AJUDA USE UM # APÓS O TESTE'''
#help()

#*****************************************************************************************************************************
#
#
#
#
#6: LOOP PRINCIPAL DO JOGO

#INSTRUÇÃO PARA OBTER AJUDA
print('\033[01m'+'DICA ÚTIL: Caso queira usar uma dica durante o jogo para digitar "4" quando lhe for solicitado que você digite o número da torre em que você deseja remover/inserir um bloco.\n'+'\033[0;0m')

#LOOP PRINCIPAL
while(True):
 #CONDIÇÃO QUE DETERMINA O FIM DO JOGO
 if(len(tower1.stack)<1 and len(tower2.stack)<1):
  break

 #RECEBENDO O INPUT DO USUÁRIO
 user_input:int=int(input("Digite o número da torre na qual será retirado um bloco: "))
 first=user_input
 user_input2:int=int(input("Digite o número da torre na qual será adicionado um bloco: "))
 second=user_input2

 #EXECUTANDO O MOVIMENTO DE BLOCOS NAS TORRES
 #TORRE 1 PARA TORRE 2
 if(first==1 and second==2):
  tower2.push(tower1.top()) 
  tower1.pop()
 #TORRE 1 PARA TORRE 3
 if(first==1 and second==3):
  tower3.push(tower1.top()) 
  tower1.pop()

 #TORRE 2 PARA TORRE 1
 if(first==2 and second==1):
  tower1.push(tower2.top()) 
  tower2.pop()

 #TORRE 2 PARA TORRE 3
 if(first==2 and second==3):
  tower3.push(tower2.top()) 
  tower2.pop()

 #TORRE 3 PARA TORRE 2
 if(first==3 and second==2):
  tower2.push(tower3.top()) 
  tower3.pop()

 #TORRE 3 PARA TORRE 1
 if(first==3 and second==1):
  tower1.push(tower3.top()) 
  tower3.pop()

 #SOLICITANDO A AJUDA DO JOGO
 if(first==4 or second==4):
  help()
  continue

 #PRINTANDO O TABULEIRO NA TELA
 print('\n')
 print_hanoi_tower(tower1.stack, 1)
 print_hanoi_tower(tower2.stack, 2)
 print_hanoi_tower(tower3.stack, 3)

#*****************************************************************************************************************************
#
#
#
#
#7:CREDITOS

print("\033[95m"+ "Escrito por Elias Rodrigues Emídio.\n"+"\033[0;0m")

#*****************************************************************************************************************************
#
#
#
#
#8: ENCERRAMENTO

print('\033[34m'+'\033[06m'+'\033[01m'+' OOOOO  BBBBB   RRRRRR  IIIII   GGGG    AAA   DDDDD    OOOOO     PPPPPP   OOOOO  RRRRRR'+'\033[0;0m')  
print('\033[34m'+'\033[06m'+'\033[01m'+'OO   OO BB   B  RR   RR  III   GG  GG  AAAAA  DD  DD  OO   OO    PP   PP OO   OO RR   RR '+'\033[0;0m')
print('\033[34m'+'\033[06m'+'\033[01m'+'OO   OO BBBBBB  RRRRRR   III  GG      AA   AA DD   DD OO   OO    PPPPPP  OO   OO RRRRRR  '+'\033[0;0m')
print('\033[34m'+'\033[06m'+'\033[01m'+'OO   OO BB   BB RR  RR   III  GG   GG AAAAAAA DD   DD OO   OO    PP      OO   OO RR  RR  '+'\033[0;0m')
print('\033[34m'+'\033[06m'+'\033[01m'+' OOOO0  BBBBBB  RR   RR IIIII  GGGGGG AA   AA DDDDDD   OOOO0     PP       OOOO0  RR   RR '+'\n\033[0;0m')
                                                                                         
                                                                                       
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
print('\033[34m'+'\033[06m'+'\033[01m'+'                   JJJ  OOOOO    GGGG    AAA   RRRRRR     !!!    !!!    !!!      '+'\033[0;0m')        
print('\033[34m'+'\033[06m'+'\033[01m'+'                   JJJ OO   OO  GG  GG  AAAAA  RR   RR    !!!    !!!    !!!   '+'\033[0;0m')           
print('\033[34m'+'\033[06m'+'\033[01m'+'                   JJJ OO   OO GG      AA   AA RRRRRR     !!!    !!!    !!!  '+'\033[0;0m')            
print('\033[34m'+'\033[06m'+'\033[01m'+'               JJ  JJJ OO   OO GG   GG AAAAAAA RR  RR                             '+'\033[0;0m')       
print('\033[34m'+'\033[06m'+'\033[01m'+'                JJJJJ   OOOO0   GGGGGG AA   AA RR   RR    !!!    !!!    !!!  '+'\n\n\033[0;0m')
