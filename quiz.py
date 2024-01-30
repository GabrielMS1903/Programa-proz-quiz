quiz = {'historia': [{'Em que ano a segunda guerra mundial acabou?': 1945, 'A ONU foi criada para impedir outro conflito como a segunda guerra mundial?': "Sim" }],
        'geografia': [{'A Inglaterra é um país situado na Europa?': "Sim", 'A agropecuária está ligada com atividades de produção animal?': "Sim"}],
        'ciencia': [{'Como são chamados os seres que causam efeitos no ecossistema situados em vida?': "bioticos", 'Quem é conhecido como o pai da genética?': "Gregor Mendel"}],
}  #Aqui estamos usando um dicionario com 3 materias e duas questoes cada

#for materia, questao in quiz.items():   Para conhecimento, considerem que se nós declarassemos um for dessa maneira, a materia receberia como resposta os subdicionarios e a questao no que em cada um condiz
  #print(materia)  Seria printado historia, geografia, ciencia
  #print(questao)   Seria printado as perguntas juntos com as respostas
#Ou seja, primeiro pegamos a materia e depois as questoes

#Como chamamos as respostas ou perguntas isoladas?


#for materia, questao in quiz.items():  materia esta recebendo as materias dando abertura para oq esta dentro da nateria
    #print()
    #for todas in questao[0].items(): #todas esta percorrendo em questao acima que esta com os submodulos
      #pergunta, resposta = todas  #pergunta esta caindo no primeiro item dos submodulos e a resposta na segunda que recebem o valor de todas que estava percorrendo todos os items da questao
      #print({resposta})


#respostas = quiz[materia_atual][0] nesse caso o for não é necessário , pois já estamos em um while 

while True:
    bemVindo = input("Seja bem-vindo. Escolha a sua matéria: 1 - 'historia'  2 - 'geografia'  3 - 'ciencia' ou pressione ENTER para sair")
#o input acima será ativado para a escolha das materias 
    if bemVindo == "1":   #comparação da var com o param da escolha
        materia_atual = 'historia'     #recebimento da resposta  
    elif bemVindo == "2":
        materia_atual = 'geografia'
    elif bemVindo == "3":
        materia_atual = 'ciencia'
    elif('\nPRESSIONE "ENTER" PARA SAIR'):  #para sair do programa
        break
    else:
        print("Opção incorreta")  #opção incorreta se o user colocar algo que não seja 1,2,3 ou tecla ENTER
        continue

    if materia_atual == 'historia':  #aqui está sendo locado a materia atual da escolha do user
        respostas = quiz[materia_atual][0] #respostas esta recebendo o dicionario com o seu array atual e a materia
        pergunta1 = float(input('Em que ano a segunda guerra mundial acabou? Responda com 1945 ou outro ano: '))
        
        if respostas['Em que ano a segunda guerra mundial acabou?'] == pergunta1:
            print("Acertou!!")
        else:
            print("Poxa, não é essa a resposta!")

        pergunta2 = input('A ONU foi criada para impedir outro conflito como a segunda guerra mundial? Responda com Sim ou Não: ')
        if respostas['A ONU foi criada para impedir outro conflito como a segunda guerra mundial?'] == pergunta2:
            print("Ae, sim!")
        else: 
            print("Tente mais uma vez!")

    elif materia_atual == 'geografia':  #um elif como outros abaixo para separar as meterias atuais, evitando conflito 
        respostas = quiz[materia_atual][0]
        pergunta3 = input('A Inglaterra é um país situado na Europa? Responda com Sim ou Não: ')
        if 'Sim' in pergunta3 and respostas['A Inglaterra é um país situado na Europa?'] == pergunta3:   # if 'Sim' in pergunta3 and respostas   explicação: se tiver "Sim" como resposta no param pergunta3 que esta recebendo respostas do dicionario,
            print("aeeeeeeeeeeeeee") # cairá no acerto
        else: 
            print("hum...não foi dessa vez") #senão..

        pergunta4 = input('A agropecuária está ligada com atividades de produção animal? Responda com Sim ou Não: ')
        if 'Sim' in pergunta4 and respostas['A agropecuária está ligada com atividades de produção animal?'] ==  pergunta4:
            print("Acertou mais uma!")
        else: 
            print("errado")

    elif materia_atual == 'ciencia':
        respostas = quiz[materia_atual][0]
        pergunta5 = input('Como são chamados os seres que causam efeitos no ecossistema situados em vida? Responda com seres bioticos ou abioticos: ')
        if 'bioticos' in pergunta5 and respostas['Como são chamados os seres que causam efeitos no ecossistema situados em vida?'] == pergunta5:
            print("Que conhecimento!")
        else: 
            print("não foi dessa vez :(")

        pergunta6 = input('Quem é conhecido como o pai da genética? Responda com Gregor Mendel ou Charles Darwin: ')
        if 'Gregor Mendel' in pergunta6 and respostas['Quem é conhecido como o pai da genética?'] == pergunta6:
            print("Correto!")
        else: 
            print("Infelizmente está errado")

            #não foi adicionado um loop para retornar corretamente as perguntas, porém o programa é reiniciado