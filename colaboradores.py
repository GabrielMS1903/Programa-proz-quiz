while(True):
    try:   
     bemVindo = int(input("Seja bem-vindo. Você deseja jogar um quiz hoje ? 1 = Sim ou 2 = Não"))
     print(bemVindo)

     if bemVindo not in (1, 2):
            print("Digite 1 ou 2")
            
     elif(bemVindo == 2):
            print("Você saiu do programa")
            break
     else:
          while True:
            print("1: historia")
            print("2: geografia")
            print("3: ciencia")
            
         
    except: 
        print("Digite apenas 1 para sim ou 2 para não")


        perguntas = ["Geografia", "Pergunta Qual país está situado na Europa ?", "1 - Colombia", "2 - Inglaterra", "2 - Correto"
        ["Historia", "Pergunta Quando acabou a segunda guerra mundial ? ", "1- 1943", "2-1945", "2- Correto"
        ["Matematica", "Pergunta Quanto é 2x2 ?" "1- 4 " , "2 - 6", "1- Correto"]] ]




#certo
perguntas = [("Geografia", "Pergunta Qual país está situado na Europa ?", "1 - Colombia", "2 - Inglaterra", "2 - Correto")
("Historia", "Pergunta Quando acabou a segunda guerra mundial ? ", "1- 1943", "2-1945", "2- Correto")
("Matematica", "Pergunta Quanto é 2x2 ?" "1- 4 " , "2 - 6", "1- Correto")]

#Nicolas Assis 
#Matheus Henrique
#Diego Silva
#Mauricio Junior
#Gabriel Martins