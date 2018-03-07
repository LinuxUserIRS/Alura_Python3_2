def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_certas = []
    for letra in palavra_secreta:
        letras_certas.append('_')
    print(letras_certas)


    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_certas[index]=letra
            index = index + 1
        print(letras_certas)
        if '_' not in letras_certas:
            acertou=True



    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
