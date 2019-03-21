idade = input("Digite sua idade: ")
idade = int(idade)
if( idade < 0 ):
    print("Isso não é idade!")
elif( idade < 3 ):
    print("Iti! Você é um bebê!")
elif( idade <= 12 ):
    print("Não, meu celular não tem joguinhos, criança!")
elif( idade < 18 ):
    print("Você é chato, aborrecente")
elif( idade < 60 ):
    print("Parabéns, você tem boletos para pagar, adulto!")
else:
    print("Tá véio ein, idoso!")
