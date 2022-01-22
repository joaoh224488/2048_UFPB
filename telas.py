import pygame

# Visualização e telas:

#Menu:
def Menu(dia, fonte_2048, fonte, tela, contorno, cor_texto, fundo):
    if dia:
        txt_2048 = fonte_2048.render("2048", True, contorno)
    else:
        txt_2048 = fonte_2048.render("2048", True, cor_texto)
    txt_jogar = fonte.render("JOGAR", True, cor_texto)
    txt_modvs = fonte.render("MODO VERSUS", True, cor_texto)
    txt_opc = fonte.render("OPÇÕES", True, cor_texto)

    tela.fill(fundo)
    pygame.draw.rect(tela, contorno, (250, 240, 300, 60), 0, 30, 30, 30, 30) #Retângulo 'Jogar' 
    #                                  x    y   largura altura preenchimento, raios das bordas
    pygame.draw.rect(tela, contorno, (250, 330, 300, 60), 0, 30, 30, 30, 30)
    pygame.draw.rect(tela, contorno, (250, 420, 300, 60), 0, 30, 30, 30, 30)

    tela.blit (txt_2048, (310, 120))
    tela.blit (txt_jogar, (360, 260))
    tela.blit (txt_modvs, (320, 350))
    tela.blit (txt_opc, (352, 440))

    pygame.display.update()

#Tela do Modo Individual:

def show_single(grade,tela, fundo, imprimir, pont, best, cor_texto, fonte, dictcolor1, dictcolor2, lado_quadrado, fonte_12, fonte_34, fonte_5, fonte_6, fonte_7, fonte_8, contorno, dia, fonte_frases):
    l = len(grade)
    c = len(grade[0])

    #Caixas de texto:
    txt_pont = fonte.render(f"PONTUAÇÃO: {pont}", True, cor_texto)
    txt_best = fonte.render(f"MELHOR PONT.: {best}", True, cor_texto)
    txt_novoj = fonte.render("NOVO JOGO", True, cor_texto)
    txt_voltar = fonte.render("VOLTAR", True, cor_texto)

    #Criação da tela:
    tela.fill(fundo)
    for i in range (l):
        for j in range (c):
            pygame.draw.rect(tela, dictcolor1[grade[i][j]], (400 - lado_quadrado * c // 2 + lado_quadrado * j, 300 - lado_quadrado * l // 2 + lado_quadrado * i, lado_quadrado, lado_quadrado), 0)
            pygame.draw.rect(tela, fundo, (400 - lado_quadrado * c // 2 + lado_quadrado * j, 300 - lado_quadrado * l // 2 + lado_quadrado * i, lado_quadrado, lado_quadrado), 4)
            if grade[i][j] != 0:
                if grade[i][j] < 100:
                    numero = fonte_12.render('%4s' %(grade[i][j]), 1, dictcolor2[grade[i][j]])
                elif grade[i][j] < 10000:
                    numero = fonte_34.render('%4s' %(grade[i][j]), 1, dictcolor2[grade[i][j]])
                elif grade[i][j] < 100000:
                    numero = fonte_5.render('%4s' %(grade[i][j]), 1, dictcolor2[grade[i][j]])
                elif grade[i][j] < 1000000:
                    numero = fonte_6.render('%4s' %(grade[i][j]), 1, dictcolor2[grade[i][j]])
                elif grade[i][j] < 10000000:
                    numero = fonte_7.render('%4s' %(grade[i][j]), 1, dictcolor2[grade[i][j]])
                elif grade[i][j] < 100000000:
                    numero = fonte_8.render('%4s' %(grade[i][j]), 1, dictcolor2[grade[i][j]])
                str_num = str(numero)
                tela.blit (numero, (415 - lado_quadrado * c // 2 + lado_quadrado * j - (len(str_num) // 2), 315 - lado_quadrado * l // 2 + lado_quadrado * i + 25 - len(str_num)))
        pygame.draw.rect(tela, contorno, (400 - lado_quadrado * c // 2 - 2, 300 - lado_quadrado * l // 2 - 72, c * lado_quadrado + 4, lado_quadrado + 4), 0, 0, 5, 5, 0)     # Topo da pontuação e best
        pygame.draw.line(tela, fundo, (400 - lado_quadrado * c // 2 - 2, 300 - lado_quadrado * l // 2 - 37), (400 - lado_quadrado * c // 2 + lado_quadrado * c + 2, 300 - lado_quadrado * l // 2 - 37), 2) # Linha de divisão entre pontuação e best
        pygame.draw.rect(tela, contorno, (400 - lado_quadrado * c // 2 - 2, 300 + lado_quadrado * l // 2, (c - 1) * lado_quadrado - 1, lado_quadrado + 4), 0, 5, 0, 0, 5) # Novo jogo
        pygame.draw.rect(tela, contorno, (400 - lado_quadrado * c // 2 + (c - 1) * lado_quadrado + 3, 300 + lado_quadrado * l // 2, lado_quadrado - 1, lado_quadrado + 4), 0, 5, 0, 0, 5)   # Setinha     
        pygame.draw.rect(tela, contorno, (10, 10, 130, 40), 0, 20, 0, 20, 0) # Voltar menu

        tela.blit (txt_pont, (400 - lado_quadrado * c // 2 + 5, 300 - lado_quadrado * (l + 1) // 2 - 28))
        tela.blit (txt_best, (400 - lado_quadrado * c // 2 + 5, 300 - lado_quadrado * (l + 1) // 2 + 3))
        tela.blit (txt_novoj, (400 - lado_quadrado * c // 2 + 5, 300 + lado_quadrado * (l + 1) // 2 - 10))
        tela.blit (txt_voltar, (20, 17))

    if imprimir:
        vit1 = "PARABÉNS!"
        vit2 = "Você venceu!"
        vit3 = "Continue jogando."
        if dia:
            txt_vit1 = fonte_frases.render (vit1, True, contorno)
            txt_vit2 = fonte_frases.render (vit2, True, contorno)
            txt_vit3 = fonte_frases.render (vit3, True, contorno)
        else:
            txt_vit1 = fonte_frases.render (vit1, True, cor_texto)
            txt_vit2 = fonte_frases.render (vit2, True, cor_texto)
            txt_vit3 = fonte_frases.render (vit3, True, cor_texto)
        tela.blit (txt_vit1, (600, 280))
        tela.blit (txt_vit2, (600, 300))
        tela.blit (txt_vit3, (600, 320))

    if dia:
        voltar = pygame.image.load('imagens/Voltar Diurno.png')
    else:
        voltar = pygame.image.load('imagens/Voltar Noturno.png')
    tela.blit (voltar, (400 + lado_quadrado * c // 2 - 45, 300 + lado_quadrado * (l + 1) // 2 - 10))

    pygame.display.update()


#Modo Versus:
def show_versus(gesq, gdir, vitoria_j1, vitoria_j2, fonte, cor_texto, tela, fundo, dictcolor1, dictcolor2, lado_quadrado, fonte_12, fonte_34, fonte_5, fonte_6, fonte_7, fonte_8, contorno, fonte_frases, dia):
    l = len(gesq)
    c = len(gesq[0])

    #Caixas de texto:
    txt_novoj = fonte.render(f"NOVO JOGO", True, cor_texto)
    txt_voltar = fonte.render("VOLTAR", True, cor_texto)

    #Criação da tela:
    tela.fill(fundo)
    for i in range (l):
        for j in range (c):
            pygame.draw.rect(tela, dictcolor1[gesq[i][j]], (200 - lado_quadrado * c // 2 + lado_quadrado * j, 300 - lado_quadrado * l // 2 + lado_quadrado * i, lado_quadrado, lado_quadrado), 0)
            pygame.draw.rect(tela, dictcolor1[gdir[i][j]], (600 - lado_quadrado * c // 2 + lado_quadrado * j, 300 - lado_quadrado * l // 2 + lado_quadrado * i, lado_quadrado, lado_quadrado), 0)                
            pygame.draw.rect(tela, fundo, (600 - lado_quadrado * c // 2 + lado_quadrado * j, 300 - lado_quadrado * l // 2 + lado_quadrado * i, lado_quadrado, lado_quadrado), 4)            
            pygame.draw.rect(tela, fundo, (200 - lado_quadrado * c // 2 + lado_quadrado * j, 300 - lado_quadrado * l // 2 + lado_quadrado * i, lado_quadrado, lado_quadrado), 4)

            if gesq[i][j] != 0:
                if gesq[i][j] < 100:
                    numero = fonte_12.render('%4s' %(gesq[i][j]), 1, dictcolor2[gesq[i][j]])
                elif gesq[i][j] < 10000:
                    numero = fonte_34.render('%4s' %(gesq[i][j]), 1, dictcolor2[gesq[i][j]])
                elif gesq[i][j] < 100000:
                    numero = fonte_5.render('%4s' %(gesq[i][j]), 1, dictcolor2[gesq[i][j]])
                elif gesq[i][j] < 1000000:
                    numero = fonte_6.render('%4s' %(gesq[i][j]), 1, dictcolor2[gesq[i][j]])
                elif gesq[i][j] < 10000000:
                    numero = fonte_7.render('%4s' %(gesq[i][j]), 1, dictcolor2[gesq[i][j]])
                elif gesq[i][j] < 100000000:
                    numero = fonte_8.render('%4s' %(gesq[i][j]), 1, dictcolor2[gesq[i][j]])
                str_num = str(numero)
                tela.blit (numero, (215 - lado_quadrado * c // 2 + lado_quadrado * j - (len(str_num) // 2), 315 - lado_quadrado * l // 2 + lado_quadrado * i + 25 - len(str_num)))

            if gdir[i][j] != 0:
                if gdir[i][j] < 100:
                    numero = fonte_12.render('%4s' %(gdir[i][j]), 1, dictcolor2[gdir[i][j]])
                elif gdir[i][j] < 10000:
                    numero = fonte_34.render('%4s' %(gdir[i][j]), 1, dictcolor2[gdir[i][j]])
                elif gdir[i][j] < 100000:
                    numero = fonte_5.render('%4s' %(gdir[i][j]), 1, dictcolor2[gdir[i][j]])
                elif gdir[i][j] < 1000000:
                    numero = fonte_6.render('%4s' %(gdir[i][j]), 1, dictcolor2[gdir[i][j]])
                elif gdir[i][j] < 10000000:
                    numero = fonte_7.render('%4s' %(gdir[i][j]), 1, dictcolor2[gdir[i][j]])
                elif gdir[i][j] < 100000000:
                    numero = fonte_8.render('%4s' %(gdir[i][j]), 1, dictcolor2[gdir[i][j]])
                str_num = str(numero)
                tela.blit (numero, (615 - lado_quadrado * c // 2 + lado_quadrado * j - (len(str_num) // 2), 315 - lado_quadrado * l // 2 + lado_quadrado * i + 25 - len(str_num)))

        pygame.draw.rect(tela, contorno, (320, 510, 160, 40), 0, 5, 5, 5, 5) # Novo Jogo
        pygame.draw.rect(tela, contorno, (10, 10, 130, 40), 0, 20, 0, 20, 0) #  Voltar
        tela.blit (txt_novoj, (337, 518))
        tela.blit (txt_voltar, (20, 17))

        if vitoria_j1:
            vit1 = "PARABÉNS, JOGADOR 1!"
            vit2 = "Você venceu!"
            vit3 = 'Aperte em "Novo Jogo" para recomeçar.'
            if dia:
                txt_vit1 = fonte_frases.render (vit1, True, contorno)
                txt_vit2 = fonte_frases.render (vit2, True, contorno)
                txt_vit3 = fonte_frases.render (vit3, True, contorno)
            else:
                txt_vit1 = fonte_frases.render (vit1, True, cor_texto)
                txt_vit2 = fonte_frases.render (vit2, True, cor_texto)
                txt_vit3 = fonte_frases.render (vit3, True, cor_texto)
            tela.blit (txt_vit1, (50, 518))
            tela.blit (txt_vit2, (50, 538))
            tela.blit (txt_vit3, (50, 558))
        
        if vitoria_j2:
            vit1 = "PARABÉNS, JOGADOR 2!"
            vit2 = "Você venceu!"
            vit3 = 'Aperte em "Novo Jogo" para recomeçar.'
            if dia:
                txt_vit1 = fonte_frases.render (vit1, True, contorno)
                txt_vit2 = fonte_frases.render (vit2, True, contorno)
                txt_vit3 = fonte_frases.render (vit3, True, contorno)
            else:
                txt_vit1 = fonte_frases.render (vit1, True, cor_texto)
                txt_vit2 = fonte_frases.render (vit2, True, cor_texto)
                txt_vit3 = fonte_frases.render (vit3, True, cor_texto)
            tela.blit (txt_vit1, (500, 518))
            tela.blit (txt_vit2, (500, 538))
            tela.blit (txt_vit3, (500, 558))

    pygame.display.update()

# Opções:

def Opcoes(som, dia, l, c, fonte, cor_texto, fonte_7, contorno, tela, fundo):
    txt_sons = fonte.render("SONS", True, cor_texto)
    txt_grade = fonte.render("GRADE", True, cor_texto)
    txt_mdnot = fonte.render("MODO NOTURNO", True, cor_texto)
    txt_voltar = fonte.render("VOLTAR", True, cor_texto)
    txt_sim = fonte.render("SIM", True, cor_texto)
    txt_nao = fonte.render("NÃO", True, cor_texto)
    txt_lin = fonte.render("LINHAS: ", True, cor_texto)
    txt_col = fonte.render("COLUNAS: ", True, cor_texto)
    txt_3 = fonte.render("3", True, cor_texto)
    txt_4 = fonte.render("4", True, cor_texto)
    txt_5 = fonte.render("5", True, cor_texto)

    if dia:
        txt_icon3 = fonte_7.render("3", True, contorno)
        txt_icon4 = fonte_7.render("4", True, contorno)
        txt_icon5 = fonte_7.render("5", True, contorno)
    else:
        txt_icon3 = fonte_7.render("3", True, cor_texto)
        txt_icon4 = fonte_7.render("4", True, cor_texto)
        txt_icon5 = fonte_7.render("5", True, cor_texto)

    tela.fill(fundo)
    pygame.draw.rect(tela, contorno, (250, 10, 300, 60), 0, 30, 30, 30, 30) # SONS
    pygame.draw.rect(tela, contorno, (260, 80, 125, 60), 0, 30, 30, 30, 30) # SIM
    pygame.draw.rect(tela, contorno, (415, 80, 125, 60), 0, 30, 30, 30, 30) # NÃO
    pygame.draw.rect(tela, contorno, (250, 160, 300, 60), 0, 30, 30, 30, 30) # MODO NOTURNO
    pygame.draw.rect(tela, contorno, (260, 230, 125, 60), 0, 30, 30, 30, 30) # SIM
    pygame.draw.rect(tela, contorno, (415, 230, 125, 60), 0, 30, 30, 30, 30) # NÃO
    pygame.draw.rect(tela, contorno, (250, 310, 300, 60), 0, 30, 30, 30, 30) # GRADE
    pygame.draw.rect(tela, contorno, (250, 380, 200, 60), 0, 30, 30, 30, 30) # LINHAS
    pygame.draw.circle(tela, contorno, (495, 410), 30) # 3
    pygame.draw.circle(tela, contorno, (570, 410), 30) # 4
    pygame.draw.circle(tela, contorno, (645, 410), 30) # 5
    pygame.draw.rect(tela, contorno, (250, 450, 240, 60), 0, 30, 30, 30, 30) # COLUNAS
    pygame.draw.circle(tela, contorno, (535, 480), 30) # 3
    pygame.draw.circle(tela, contorno, (610, 480), 30) # 4
    pygame.draw.circle(tela, contorno, (685, 480), 30) # 5
    pygame.draw.rect(tela, contorno, (450, 530, 300, 60), 0, 0, 30, 0, 30) # VOLTAR

    tela.blit (txt_sons, (360, 30))
    tela.blit (txt_sim, (302, 100))
    tela.blit (txt_nao, (455, 100))
    tela.blit (txt_mdnot, (315, 180))
    tela.blit (txt_sim, (302, 250))
    tela.blit (txt_nao, (455, 250))
    tela.blit (txt_grade, (360, 330))
    tela.blit (txt_lin, (290, 400))
    tela.blit (txt_3, (489, 400))
    tela.blit (txt_4, (564, 400))
    tela.blit (txt_5, (639, 400))
    tela.blit (txt_col, (290, 470))
    tela.blit (txt_3, (529, 470))
    tela.blit (txt_4, (604, 470))
    tela.blit (txt_5, (679, 470))
    tela.blit (txt_voltar, (540, 550))

    if dia: 
        if som == True:
            icon_som = pygame.image.load("imagens/Som Diurno.png")
        else:
            icon_som = pygame.image.load("imagens/Mudo Diurno.png")
        

        icon_dia = pygame.image.load("imagens/Sol Diurno.png")
      
        icon_grade = pygame.image.load("imagens/Grade Diurno.png")

    else:
        if som == True:
            icon_som = pygame.image.load("imagens/Som Noturno.png")
        else:
            icon_som = pygame.image.load("imagens/Mudo Noturno.png")
        
       
        icon_dia = pygame.image.load("imagens/Lua Noturno.png")
        icon_grade = pygame.image.load("imagens/Grade Noturno.png")

    if l == 3:
        tela.blit (txt_icon3, (580, 303))
    elif l == 4:
        tela.blit (txt_icon4, (580, 303))
    else:
        tela.blit (txt_icon5, (580, 303))

    if c == 3:
        tela.blit (txt_icon3, (605, 330))
    elif c == 4:
        tela.blit (txt_icon4, (605, 330))
    else:
        tela.blit (txt_icon5, (605, 330))

    tela.blit (icon_som, (570, 25))
    tela.blit (icon_dia, (570, 175))
    tela.blit (icon_grade, (570, 325))
    
    pygame.display.update()
