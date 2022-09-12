import time
def LI(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite apenas número inteiro, ex: 1, 2, 3')
        except KeyboardInterrupt:
            print('Você preferiu deixar vazio.')
            return 0
        else:
            return n


def linha(tam=42):
    return '~' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def cardápio(lista):
    cabeçalho('MENU PRIMÁRIO')
    c = 1
    for item in lista:
        print(f'\033[30m{c}\033[m - \033[32m{item}\033[m')
        c += 1
    print(linha())
    opc = LI('\033[32mEscolha uma das opções: \033[m')
    return opc

def arquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do aquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except Exception as error:
        print(f'Erro: {error.__class__}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Deesconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro!'*3)
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro! Ao introduzir os dados no  arquivo .txt')
        else:
            print('Arquivos gerados com sucesso!')
            print(f'Nome da pessoa: {nome}, idade {idade} anos')
            a.close()

arq = 'mini-project.txt'
if not arquivo(arq):
    criararquivo(arq)
# Principal program
while True:
    resp = cardápio(['Ver Pessoas cadastradas', 'Cadastrar mais pessoas', 'Sair'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome da pessoa:   '))
        idade = LI('Idade da pessoa:        ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('««««FINALIZADO»»»»')
        break
    else:
        print('Erro! Digite novamente!')
    time.sleep(3)
