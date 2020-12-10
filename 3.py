#4) (3.0) Simulador de boletim escolar.
#A. Você deve perguntar ao usuário o nome do aluno e duas notas.
#B. Você deve perguntar também se o usuário deseja cadastrar mais alunos (deve ser possível
#cadastrar quantos alunos o usuário desejar).
#C. O programa deve calcular a media desse aluno.
#D. O programa deve mostrar como resultado, o nome e a média de todos os alunos cadastrados.
#E. Você também deve criar uma opção para ver apenas um aluno com as suas respectivas notas.

def cadastros():
    listaAlunos = []
    listaMedia = []
    cadastrar=0
    while cadastrar == 0:
        nome = input("nome do aluno: ")
        while(len(nome)<3):
            print ( "O nome deve conter no mínimo 3 letras " )
            nome = input("nome: ")
        nome=nome.upper()
        if nome in listaAlunos:
            print('Aluno já está Matriculado')
        else:
            listaAlunos.append(nome)
            nota1 = int(input("Qual sua 1° nota: "))
            nota2 = int(input("Qual sua 2° nota: "))
            media = (nota1 + nota2)/2
            listaMedia.append(media)
            print("O aluno ",nome,"possui média",media)
            pergunta = int(input("Deseja cadastrar um novo aluno?\n 1 - Sim\n 2 - Não"))
            if pergunta == 1: 
                cadastrar = 0
            else:
                cadastrar=1
          
    print("os alunos cadastrados foram:",listaAlunos,"\n As médias respectivamente:  \n",listaMedia)

cadastros()

#sora nao consegui fazer a media e as notas de cada aluno, apenas mostrar no geral. Faltou tempo pra pensarrrr :(. Tenho dificuldade