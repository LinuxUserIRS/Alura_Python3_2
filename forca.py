def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "treta"
    palavra_secreta=palavra_secreta.lower()
    letras_certas = ['_' for letra in palavra_secreta]
    erros=0
    print(letras_certas)


    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().lower()


        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_certas[index]=letra
                index+=1
            print(letras_certas)
            if '_' not in letras_certas:
                acertou=True
        else:
            erros+=1
        enforcou=erros==6



    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
