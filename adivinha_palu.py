import random
chute = 101
escolha_real = random.randrange(101)
tentativa = 1

print("\nBEM VINDO AO JOGO DA ADIVINHAÇÃO")
print("\nTente adivinhar o valor do número sorteado entre 0 e 100")

while (chute!=escolha_real):
    
    chute = int(input("\nDigite o valor que você acredita ser\n"))
    
    if(chute>escolha_real):
        print("O valor sorteado é MENOR!")
        print("Tentativa número %i" %tentativa)
        tentativa = tentativa + 1
        
    elif(chute<escolha_real):
        print("O valor sorteado é MAIOR!")
        print("Tentativa número %i" %tentativa)
        tentativa = tentativa + 1
        
    else:
        if(tentativa == 1):
            print("\nParabéns! Você acertou!")
            print("Foi necessária apenas uma tentativa! MONSTRO!!")
            
        else:
            print("\nParabéns! Você acertou!")
            print("Foram necessárias %i tentativas!" %tentativa)
                
    
    
    