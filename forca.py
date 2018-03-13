from random import randint
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

#Abre o arquivo com a palvra secreta e lê a palavra
    archive = open('secret_word.txt', 'r')
    palavra_secreta = []
#Salva todas as palavras em uma lista
    with open('secret_word.txt', 'r') as archive:
        for line in archive:
            linha = line.strip()
            palavra_secreta.append(linha)
#Escolhe aleatoriamente qual palavra vai ser usada
    chosen_word = randint(0, len(palavra_secreta))

    tentativas = len(palavra_secreta)
#Põe todas as letras em minúsculo para facilitar a leitura
    secret_word = palavra_secreta[chosen_word].lower()
#Cria uma lista preenchida com underscores para fins estéticos
    letras_certas = ['_' for letra in secret_word]
    erros=0
    print(letras_certas)

#Variáveis para controle do loop
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().lower()

#Checa se chute está presente na string
        if chute in secret_word:
            index = 0
#Checa em quais posições a letra faz parte da string e substitui na lista de underscores na posição adequada
            for letra in secret_word:
                if(chute == letra):
                    letras_certas[index]=letra
                index+=1
            if '_' not in letras_certas:
                acertou=True
        else:
            erros+=1
        enforcou=erros==tentativas
        print(letras_certas)


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
