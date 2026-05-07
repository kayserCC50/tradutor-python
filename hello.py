print("swiw,swiw,swiw, water falling of your skin")
portugues = "nadar, nadar, nadar, água caindo da sua pele"
espanhol = "nadar, nadar, nadar, agua cayendo de tu piel"
frances = "nager, nager, nager, eau tombant de votre peau"

while True:
        traducao = input("Traduzir para qual idioma? ( portugues, espanhol, frances) ou 'sair' : ")
        if traducao == "sair":
             print("ate mais!")
             break
        if traducao == "portugues":
            print(portugues)
        elif traducao == "espanhol":
             print(espanhol)
        elif traducao == "frances":
             print(frances)

        else:
             print("Idioma não reconhecido")

