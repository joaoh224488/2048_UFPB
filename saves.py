import shutil
import tempfile


def find_best(grade):
    arq = 'saves/best.txt'  # Lê o arquivo
    linhas = len(grade)
    colunas = len(grade[0])
    with open(arq, 'r') as arquivo:
        for i in arquivo:
            if int(i[5]) == linhas and int(i[7]) == colunas:
                numero = i[11:]
                best_score = int(numero)
                return best_score

def save_best(grade, best):
    arq = 'saves/best.txt'
    linhas = len(grade)
    colunas = len(grade[0])
    with open(arq, 'r') as arquivo, \
     tempfile.NamedTemporaryFile('w', delete=False) as out: # Cria um arquivo temporário onde será escrito conteúdo original e o novo, se necessário
        for i in arquivo:
            if int(i[5]) == linhas and int(i[7]) == colunas:
                numero = i[11:]
                anterior = int(numero)
                if best > anterior:
                    line = i[0:10] + ' ' + str(best) + '\n'
                    out.write(line)
                else:
                    out.write(i)
            else:
                out.write(i)
    shutil.move(out.name, arq) #substitui o conteúdo do arquivo orginal pelo conteúdo do temporário

def find_grade(linhas, colunas):
    arq = 'saves/saves.txt'
    with open(arq, 'r') as arquivo:
        for i in arquivo:
            if int(i[6]) == linhas and int(i[8]) == colunas:
                grade_salva = eval(i[12:])     #Eval transforma uma string com forma de lista de volta em lista
                return grade_salva


def save_grade(grade):
    arq = 'saves/saves.txt'
    linhas = len(grade)
    colunas = len(grade[0])
    with open(arq, 'r') as arquivo, \
     tempfile.NamedTemporaryFile('w', delete=False) as out:
        for i in arquivo:
            if int(i[6]) == linhas and int(i[8]) == colunas:
                line = i[0:11]+ ' ' + str(grade) + '\n'
                out.write(line)
            else: 
                out.write(i)
    shutil.move(out.name, arq)

def find_gesq(l, c):
    arq = 'saves/saves_versus.txt'
    with open(arq, 'r') as arquivo, \
     tempfile.NamedTemporaryFile('w', delete=False) as out:
     for i in arquivo:
         if i[0:3] == 'esq' and int(i[3]) == l and int(i[5]) == c:
             grade_esq = eval(i[8:])
             return grade_esq


def save_gesq(gesq):
    arq = 'saves/saves_versus.txt'
    linhas = len(gesq)
    colunas = len(gesq[0])
    with open(arq, 'r') as arquivo, \
     tempfile.NamedTemporaryFile('w', delete=False) as out:
        for i in arquivo:
            if i[0:3] == 'esq' and int(i[3]) == linhas and int(i[5]) == colunas:
                line = i[0:8]+ ' ' + str(gesq) + '\n'
                out.write(line)
            else: 
                out.write(i)
    shutil.move(out.name, arq)


def find_gdir(l, c):
    arq = 'saves/saves_versus.txt'
    with open(arq, 'r') as arquivo, \
     tempfile.NamedTemporaryFile('w', delete=False) as out:
     for i in arquivo:
         if i[0:3] == 'dir' and int(i[3]) == l and int(i[5]) == c:
             grade_dir = eval(i[8:])
             return grade_dir

def save_gdir(gdir):
    arq = 'saves/saves_versus.txt'
    linhas = len(gdir)
    colunas = len(gdir[0])
    with open(arq, 'r') as arquivo, \
     tempfile.NamedTemporaryFile('w', delete=False) as out:
        for i in arquivo:
            if i[0:3] == 'dir' and int(i[3]) == linhas and int(i[5]) == colunas:
                
                line = i[0:8]+ ' ' + str(gdir) + '\n'
                out.write(line)
            else: 
                out.write(i)
    shutil.move(out.name, arq)

def find_pt(grade):
    arq = 'saves/pt.txt'
    linhas = len(grade)
    colunas = len(grade[0])
    with open(arq, 'r') as arquivo:
        for i in arquivo:
            if int(i[3]) == linhas and int(i[5]) == colunas:
                numero = i[9:]
                pont = int(numero)
                return pont


def save_pt(grade, pt):
    arq = 'saves/pt.txt'
    linhas = len(grade)
    colunas = len(grade[0])
    with open(arq, 'r') as arquivo, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
            for i in arquivo:
                if int(i[3]) == linhas and int(i[5]) == colunas:
                    line = i[0:8]+ ' ' + str(pt) + '\n'
                    out.write(line)
                else: 
                    out.write(i)
    shutil.move(out.name, arq)




def find_dia():
    arq = 'saves/opc.txt'
    with open(arq, 'r') as arquivo:
        for i in arquivo:
            if i[0:3] == 'dia':
                cond = eval(i[6:])
                return cond


def change_dia(cond):
    arq = 'saves/opc.txt'
    with open(arq, 'r') as arquivo, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
            for i in arquivo:
                if i[0:3] == 'dia':
                   
                    if 'True' in i[6:]:
                        line = 'dia = ' + str(cond) + '\n'
                        
                        out.write(line)
                    elif 'False' in i[6:]:
                        line = 'dia = ' + str(cond) + '\n'
                        
                        out.write(line)
                else: 
                    out.write(i)
    shutil.move(out.name, arq)

def find_l():
    arq = 'saves/opc.txt'
    with open(arq, 'r') as arquivo:
        for i in arquivo:
            
            if 'l' in str(i[0:1]):
                cond = int(i[4])
                return cond
def find_c():
    arq = 'saves/opc.txt'
    with open(arq, 'r') as arquivo:
        for i in arquivo:
            if 'c' in str(i[0:1]):
                cond = int(i[4])
                return cond

def save_l(l):

    arq = 'saves/opc.txt'
    with open(arq, 'r') as arquivo, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
            for i in arquivo:
                if i[0] == 'l':
                    line = 'l = ' + str(l) + '\n'
                    out.write(line)
                else: 
                    out.write(i)
    shutil.move(out.name, arq)

def save_c(c):

    arq = 'saves/opc.txt'
    with open(arq, 'r') as arquivo, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
            for i in arquivo:
                if i[0] == 'c':
                    line = 'c = ' + str(c) + '\n'
                    out.write(line)
                else: 
                    out.write(i)
    shutil.move(out.name, arq)



def change_som(cond):
    arq = 'saves/opc.txt'
    with open(arq, 'r') as arquivo, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
            for i in arquivo:
                if i[0:3] == 'som':
                   
                    if 'True' in i[6:]:
                        line = 'som = ' + str(cond) + '\n'
                        
                        out.write(line)
                    elif 'False' in i[6:]:
                        line = 'som = ' + str(cond) + '\n'
                        
                        out.write(line)
                else: 
                    out.write(i)
    shutil.move(out.name, arq)

def find_som():
    arq = 'saves/opc.txt'
    with open(arq, 'r') as arquivo:
        for i in arquivo:
            if i[0:3] == 'som':
                cond = eval(i[6:])
                return cond

