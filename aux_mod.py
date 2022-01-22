from os import path
from random import *

import copy


# Início do jogo e controles internos

def grade_vazia(linhas, colunas):
    grade = []

    for i in range(linhas):
        line = []

        for j in range(colunas):
            line.append(0)

        grade.append(line)
    
    return grade



def preenchimento(grade):

    vazios = []  #lista de posições vazias
    for i in range(len(grade)):
        for j in range(len(grade[i])):
            pos = (i, j)
            if grade[i][j] == 0:
                vazios.append(pos)
  
    if len(vazios) == 0: # Se a lista de vazios está vazia, não há o que preencher
        return grade

    elif len (vazios) >= 1:

        pos = sample(vazios, 1) # sample escolherá aleatoriamente uma posição da lista vazios
        

        if randint(0, 9) == 0: # 10% de chance do valor preenchido ser 4
            valor = 4
        else:
            valor = 2
            
        grade[pos[0][0]][pos[0][1]] = valor

        return grade


# Condições de vitória e derrota

def venceu(grade):
    cond = False # Condição para que a tela de vitória no jogo apareça
    for i in grade:
        for j in i:
            if j == 2048:
                cond = True
    return cond

def venceu_3x3(grade):
    cond = False # Condição para que a tela de vitória no jogo apareça no modo versus 3x3
    for i in grade:
        for j in i:
            if j == 512:
                cond = True
    return cond
    
                    
# 
# Movimento:
def zerar(lin, a, b):
    for i in range(a, b+1): #a toda a lista no range
        lin[i] = 0
    return lin



def combinate(lin):
    l_grade = lin # Receberá as linhas da grade
    num = []
    for i in l_grade:
        if i != 0:# Números em uma lista
            num.append(i)
    length = len(num)
    if length == 5:
        if num[0] == num[1]:
            l_grade[0] = num[0] + num[1]

            if num[2] == num[3]:
                l_grade[1] = num[2] + num[3]
                l_grade[2] = num[4]
                zerar(l_grade, 3, 4)

            elif num[3] == num[4]:
                l_grade[1] = num[2]
                l_grade[2] = num[3] + num[4]
                zerar(l_grade, 3, 4)

            else:
                for i in range(1,4):
                    l_grade[i] = num[i+1]
                l_grade[4] = 0
        
        elif num[1] == num[2]: # O primeiro não combina

            l_grade[0] = num[0]
            l_grade[1] = num[1] + num[2]

            if num[3] == num[4]:
                l_grade[2] = num[3] + num[4]
                zerar(l_grade, 3, 4)
            else:
                l_grade[2] = num[3]
                l_grade[3] = num[4]
                l_grade[4] = 0
        
        elif num[2] == num[3]:
            l_grade[2] = num[2] + num[3]
            l_grade[3] = num[4]
            l_grade[4] = 0
        
        elif num[3] == num[4]:
            l_grade[3] = num[3] + num[4]
            l_grade[4] = 0

        else: # 5 números diferentes
            for i in range(length):
                l_grade[i] = num[i]
    
    elif length == 4:
        if num[0] == num[1]: # 
            l_grade[0] = num[0] + num[1]
            
            if num[2] == num[3]:
                l_grade[1] = num[2] + num[3]
                l_grade[2] = 0
                l_grade[3] = 0
                if len(l_grade) == 5:
                    l_grade[4] = 0
            else:
                l_grade[1] = num[2]
                l_grade[2] = num[3]
                l_grade[3] = 0
                if len(l_grade) == 5:
                    l_grade[4] = 0

        elif num[1] == num[2]: # O primeiro não combina
            l_grade[0] = num[0]
            l_grade[1] = num[1] + num[2]
            l_grade[2] = num[3]
            l_grade[3] = 0
            if len(l_grade) == 5:
                l_grade[4] = 0
           
        elif num[2] == num[3]:# O primeiro e o segundo não combinam
            l_grade[0] = num[0]
            l_grade[1] = num[1]
            l_grade[2] = num[2] + num[3]
            l_grade[3] = 0
            if len(l_grade) == 5:
                l_grade[4] = 0

        else: # 4 números diferentes
            for i in range(length):
                l_grade[i] = num[i]
            if len(l_grade) == 5:
                l_grade[4] = 0
    elif length == 3:# Apenas três números na linha
        if num[0] == num[1]: 
            l_grade[0] = num[0] + num[1]
            l_grade[1] = num[2]
            l_grade[2] = 0
            if len(l_grade) >= 4:
                l_grade[3] = 0
            if len(l_grade) == 5:
                l_grade[4] = 0
            
           
        elif num[1] == num[2]:
            l_grade[0] = num[0]
            l_grade[1] = num[1] + num[2]
            l_grade[2] = 0
            if len(l_grade) >= 4:
                l_grade[3] = 0
            if len(l_grade) == 5:
                l_grade[4] = 0
        else:# 3 números diferentes
            for i in range(length):
                l_grade[i] = num[i]
            if len(l_grade) >= 4:
                l_grade[3] = 0
            if len(l_grade) == 5:
                l_grade[4] = 0

    elif length == 2:# Dois números na linha
        if num[0] == num[1]:# Apenas uma possibilidade de combinação
            l_grade[0] = num[0] + num[1]
            l_grade[1] = 0
            l_grade[2] = 0
            if len(l_grade) >= 4:
                l_grade[3] = 0
            if len(l_grade) == 5:
                l_grade[4] = 0
        else:# Números não combinam
            for i in range(length):
                l_grade[i] = num[i]
            l_grade[2] = 0
            if len(l_grade) >= 4:
                l_grade[3] = 0
            if len(l_grade) == 5:
                l_grade[4] = 0
    elif length == 1:
        l_grade[0] = num[0]
        zerar(l_grade, 1, 2)
        if len(l_grade) >= 4:
                l_grade[3] = 0
        if len(l_grade) == 5:
            l_grade[4] = 0
    else:
        pass # Não faz nenhuma operação
    return l_grade




def score_linha(lin):
    score = 0
    l_grade = lin 
    num = []
    for i in l_grade:
        if i != 0:
            num.append(i)
    length = len(num)
    if length == 5:
        if num[0] == num[1]:
            n = num[0] + num[1]
            score += n

            if num[2] == num[3]:
                n = num[2] + num[3]
                score += n
            

            elif num[3] == num[4]:
        
                n = num[3] + num[4]
                score += n
            

        elif num[1] == num[2]: 

            n = num[1] + num[2]
            score += n

            if num[3] == num[4]:
                n = num[3] + num[4]
                score += n
        
        elif num[2] == num[3]:
            n = num[2] + num[3]
            score += n

        
        elif num[3] == num[4]:
            n = num[3] + num[4]
            score += n

    
    elif length == 4:
        if num[0] == num[1]: 
            n = num[0] + num[1]
            score += n
            
            if num[2] == num[3]:
                n = num[2] + num[3]
                score += n

        elif num[1] == num[2]:
            n = num[1] + num[2]
            score += n
            
           
        elif num[2] == num[3]:
            n = num[2] + num[3]
            score += n

    elif length == 3:
        if num[0] == num[1]: 
            n = num[0] + num[1]
            score += n
           
        elif num[1] == num[2]:
            n = num[1] + num[2]
            score += n

    elif length == 2:
        if num[0] == num[1]:
            n = num[0] + num[1]
            score += n

    return score

def left(grade):# Jogador pressiona a tecla para mover à esquerda
    teste = copy.deepcopy(grade)
    for i in range(len(grade)):
        new_line = combinate(grade[i])
        for j in range(len(grade[i])):
            grade[i][j] = new_line[j]
    if teste != grade:
        grade = preenchimento(grade)
    return grade



def score_left(grade):
    score = 0
    for i in range(len(grade)):
        score += score_linha(grade[i])
    return score


def right(grade): #Jogador pressiona a tecla para mover à direita
    teste = copy.deepcopy(grade)
    for i in range(len(grade)):
        new_line = combinate(grade[i][::-1]) #lê a linha ao contrário
        for j in range(len(grade[i])):
            grade[i][(len(grade[i])-1) - j] = new_line[j] # Adiciona os elementos ao contrário às colunas
    if teste != grade:
        grade = preenchimento(grade)
    return grade

def score_right(grade):
    score = 0
    for i in range(len(grade)):
        score += score_linha(grade[i][::-1]) 
    return score
     
def up(grade):#Jogador pressiona a tecla para mover para cima
    teste = copy.deepcopy(grade)
    for i in range(len(grade[0])):
        col = [] # O código trabalhará com a coluna "deitada" como uma linha
        for j in range(len(grade)):
            col.append(grade[j][i])
        new_line = combinate(col)
        for k in range(len(grade)):
            grade[k][i] = new_line[k]
    if teste != grade:
        grade = preenchimento(grade)
    return grade

def score_up(grade):
    score = 0
    for i in range(len(grade[0])):
        col = [] 
        for j in range(len(grade)):
            col.append(grade[j][i])
        score += score_linha(col)
    return score


def down(grade): #Jogador pressiona a tecla para mover para baixo
    teste = copy.deepcopy(grade)
    for i in range(len(grade[0])):
        col = []
        for j in range(len(grade)):
            col.append(grade[(len(grade)-1) - j][i])
        new_line = combinate(col)
        for k in range(len(grade)):
            grade[(len(grade)-1) - k][i] = new_line[k]
    if teste != grade:
        grade = preenchimento(grade)
    return grade

def score_down(grade):
    score = 0
    for i in range(len(grade[0])):
        col = []
        for j in range(len(grade)):
            col.append(grade[(len(grade)-1) - j][i])
        score += score_linha(col)
    return score
