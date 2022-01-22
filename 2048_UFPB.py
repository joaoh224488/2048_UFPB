from pygame.event import clear
import saves as s      
import aux_mod as au
import dicts_n_ks as dks
import telas
import pygame
import copy
from pygame.locals import *
from sys import exit

pygame.init()

# Visualização e controladores:
# Cores iniciais:
dia = s.find_dia()
som = s.find_som()

# Atribuições:
lado_quadrado = 70

#Fontes:
fonte = pygame.font.SysFont("arial", 20, True, False)
fonte_frases = pygame.font.SysFont("arial", 15, True, False) # Fonte das frases
fonte_12 = pygame.font.SysFont("arial", 30, True, False) # Fonte de números com 1 ou 2 dígitos
fonte_34 = pygame.font.SysFont("arial", 27, True, False) # Fonte de números com 3 ou 4 dígitos
fonte_5 = pygame.font.SysFont("arial", 23, True, False)
fonte_6 = pygame.font.SysFont("arial", 19, True, False)
fonte_7 = pygame.font.SysFont("arial", 17, True, False)
fonte_8 = pygame.font.SysFont("arial", 15, True, False)
fonte_2048 = pygame.font.SysFont("arial", 80, True, False)

# Status 1 - Menu; status 2 - Jogo individual; status 3 - Modo versus; status 4 - Opções:
tela_status = 1

# Tela mais baixa de um notebook padrão:
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption ("2048")

# Controladores booleanos
jogo = True
vitoria = False
pode_anterior = False
vitoria_j1 = False
vitoria_j2 = False
v1 = True   # Primeira vitória
imprimir = False # Imprimir ou não na tela a mensagem de vitória
cont_versus = True # Primeira vitória do modo
l = s.find_l()
c = s.find_c()
grade = s.find_grade(l, c)
gesq = s.find_gesq(l, c)
gdir = s.find_gdir(l, c)
pont = s.find_pt(grade)
best = s.find_best(grade)

# Loop do Pygame:
while jogo:
    # Cores do loop:
    if dia:
        dictcolor1 = dks.dictbloco_diurno
        dictcolor2 = dks.dicttexto_b_diurno
        fundo = dks.fundo_dia # fundo
        contorno = dks.contorno_dia # contorno
        cor_texto = dks.cor_texto_dia
    else:
        dictcolor1 = dks.dictbloco_noturno
        dictcolor2 = dks.dicttexto_b_noturno
        fundo = dks.fundo_noite
        contorno = dks.contorno_noite
        cor_texto = dks.cor_texto_noite
    # Informações das grades:
    if grade == au.grade_vazia(l, c):
        for i in range(2):
            grade = au.preenchimento(grade)                         
        s.save_grade(grade)
    if gesq == au.grade_vazia(l,c):
        for i in range(2):
                gesq = au.preenchimento(gesq)
    
    if gdir == au.grade_vazia(l, c):
        for i in range(2):
            gdir = au.preenchimento(gdir)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            s.save_gesq(gesq)
            s.save_gdir(gdir)
            s.save_grade(grade)
            s.save_pt(grade, pont)
            s.save_best(grade, best)
            pygame.quit()
            exit()
            
        if tela_status == 1: #Menu
            telas.Menu(dia, fonte_2048, fonte, tela, contorno, cor_texto, fundo)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = evento.pos

                if 250 <= mouse_x <= 550 and 240 <= mouse_y <= 300:
                    tela_status = 2 #Tela de jogo individual.
            
                elif 250 <= mouse_x <= 550 and 330 <= mouse_y <= 390:
                    tela_status = 3 #Tela de modo versus.
            
                elif 250 <= mouse_x <= 550 and 420 <= mouse_y <= 480:
                    tela_status = 4 #Tela de opções.
        
        elif tela_status == 2: #Tela de jogo individual
            telas.show_single(grade,tela, fundo, imprimir, pont, best, cor_texto, fonte, dictcolor1, dictcolor2, lado_quadrado, fonte_12, fonte_34, fonte_5, fonte_6, fonte_7, fonte_8, contorno, dia, fonte_frases)
            dis_xi_nj = 400 - lado_quadrado * c // 2 - 2 # x inicial do botão de novo jogo
            dis_xf_nj = dis_xi_nj + (c - 1) * lado_quadrado - 1 # x final do botão de novo jogo
            dis_xi_voltar = dis_xf_nj + 5 # inicial do voltar
            dis_xf_voltar = dis_xi_voltar + lado_quadrado - 1 
            dis_yi = 300 + lado_quadrado * l // 2 # y inicial dos botões da parte de baixo
            dis_yf = dis_yi + lado_quadrado + 4 # y final

            if evento.type == pygame.KEYDOWN:
                pode_anterior = True
                if evento.key == pygame.K_a or evento.key == pygame.K_LEFT:

                    grade_anterior = copy.deepcopy(grade)
                    pt_anterior = pont
                    pont += au.score_left(grade)
                    grade = au.left(grade)
                   
                
                if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:

                    grade_anterior = copy.deepcopy(grade)
                    pt_anterior = pont
                    pont += au.score_right(grade)
                    grade = au.right(grade)
                   
                
                if evento.key == pygame.K_w or evento.key == pygame.K_UP:

                    grade_anterior = copy.deepcopy(grade)
                    pt_anterior = pont
                    pont += au.score_up(grade)
                    grade = au.up(grade)
                    
                
                if evento.key == pygame.K_s or evento.key == pygame.K_DOWN:

                    grade_anterior = copy.deepcopy(grade)
                    pt_anterior = pont
                    pont += au.score_down(grade)
                    grade = au.down(grade)

            if pont > best:
                best = pont
    
            if len(grade) == 3 and len(grade[0]) == 3:
                vitoria = au.venceu_3x3(grade)
            else:
                vitoria = au.venceu(grade)
            
            if vitoria:
                imprimir = True
                if v1:
                    if som:
                        msc_go = pygame.mixer.music.load('sons/Victory Theme.mp3')
                        pygame.mixer.music.play(1)
                v1 = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = evento.pos

                if 10 <= mouse_x <= 140 and 10 <= mouse_y <= 50:
                    tela_status = 1
                    s.save_grade(grade)
                    s.save_pt(grade, pont)
                    s.save_best(grade, best)
                    pode_anterior = False
                
                elif dis_xi_nj <= mouse_x <= dis_xf_nj and dis_yi <= mouse_y <= dis_yf:
                    grade = au.grade_vazia(len(grade), len(grade[0]))
                    for i in range(2):
                        grade = au.preenchimento(grade)
                    pont = 0
                
                elif dis_xi_voltar <= mouse_x <= dis_xf_voltar and dis_yi <= mouse_y <= dis_yf:
                    if pode_anterior:
                        grade = grade_anterior
                        pont = pt_anterior                     
                        

        
        elif tela_status == 3: #Modo versus
            telas.show_versus(gesq, gdir, vitoria_j1, vitoria_j2, fonte, cor_texto, tela, fundo, dictcolor1, dictcolor2, lado_quadrado, fonte_12, fonte_34, fonte_5, fonte_6, fonte_7, fonte_8, contorno, fonte_frases, dia)

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    gesq = au.right(gesq)
                        
                if evento.key == pygame.K_w:
                    gesq = au.up(gesq)
                
                if evento.key == pygame.K_a:
                    gesq = au.left(gesq)
            
                if evento.key == pygame.K_s:
                    gesq = au.down(gesq)
            
                if evento.key == pygame.K_LEFT:
                    gdir = au.left(gdir)
            
                if evento.key == pygame.K_RIGHT:
                    gdir = au.right(gdir)
            
                if evento.key == pygame.K_UP:
                    gdir = au.up(gdir)
                
                if evento.key == pygame.K_DOWN:
                    gdir = au.down(gdir)
                   

            if len(gesq) == 3 and len(gesq[0]) == 3:
                vitoria_j1 = au.venceu_3x3(gesq)
                vitoria_j2 = au.venceu_3x3(gdir)
            else:
                vitoria_j1 = au.venceu(gesq)
                vitoria_j2 = au.venceu(gdir)
            
            if vitoria_j1:
                if cont_versus:
                    if som:
                        msc_go = pygame.mixer.music.load('Victory Theme.mp3')
                        pygame.mixer.music.play(1)
                cont_versus = False

            if vitoria_j2:
                if cont_versus:
                    if som:
                        msc_go = pygame.mixer.music.load('Victory Theme.mp3')
                        pygame.mixer.music.play(1)
                cont_versus = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = evento.pos

                if 320 <= mouse_x <= 480 and 510 <= mouse_y <= 550:
                    gesq = au.grade_vazia(len(gesq), len(gesq[0]))
                    for i in range(2):
                        gesq = au.preenchimento(gesq)

                    gdir = au.grade_vazia(len(gdir), len(gdir[0]))
                    for i in range(2):
                        gdir = au.preenchimento(gdir)
                elif 10 <= mouse_x <= 140 and 10 <= mouse_y <= 50:
                    tela_status = 1
                    s.save_gesq(gesq)
                    s.save_gdir(gdir)

        elif tela_status == 4: #Opções
            telas.Opcoes(som, dia, l, c, fonte, cor_texto, fonte_7, contorno, tela, fundo)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = evento.pos

                if 260 <= mouse_x <= 385 and 80 <= mouse_y <= 140:
                    som = True
                    s.change_som(som)
                    
                
                elif 415 <= mouse_x <= 540 and 80 <= mouse_y <= 140:
                    som = False
                    s.change_som(som)
                   
                
                if 260 <= mouse_x <= 385 and 230 <= mouse_y <= 290:
                    dia = False
                    s.change_dia(dia)
                    
                
                elif 415 <= mouse_x <= 540 and 230 <= mouse_y <= 290:
                    dia = True
                    s.change_dia(dia)
                    

                if 465 <= mouse_x <= 525 and 380 <= mouse_y <= 440:
                    l = 3
                    s.save_l(l)
                    
                    
                elif 540 <= mouse_x <= 600 and 380 <= mouse_y <= 440:
                    l = 4
                    s.save_l(l)
                    
                    
                elif 615 <= mouse_x <= 675 and 380 <= mouse_y <= 440:
                    l = 5
                    s.save_l(l)
                    

                if 505 <= mouse_x <= 565 and 450 <= mouse_y <= 510:
                    c = 3
                    s.save_c(c)
                    
                    
                elif 580 <= mouse_x <= 640 and 450 <= mouse_y <= 510:
                    c = 4
                    s.save_c(c)
                    
                    
                elif 655 <= mouse_x <= 715 and 450 <= mouse_y <= 510:
                    c = 5
                    s.save_c(c)
                    

                if 450 <= mouse_x <= 750 and 530 <= mouse_y <= 590:
                    grade = s.find_grade(l,c)
                    pont = s.find_pt(grade)
                    best = s.find_best(grade)
                    gesq = s.find_gesq(l,c)
                    gdir = s.find_gdir(l, c)
                    tela_status = 1
                continue

pygame.display.update()

