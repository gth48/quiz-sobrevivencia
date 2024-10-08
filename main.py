import random as rd
import picture2 as picture
import time

p1 = "\nMÉDIO\nQual animal seria o mais útil para domesticar após um apocalipse para ajudar na agricultura?\nA) Leão\nB) Galinha\nC) Cavalo\nD) Cachorro"
r1 = "C"
p2 = "\nMÉDIO\nQual dessas plantas seria essencial cultivar para obter uma fonte contínua de proteínas?\nA) Trigo\nB) Batata\nC) Soja\nD) Tomate"
r2 = "C"
p3 = "\nFÁCIL\nQual tecnologia seria mais crucial recuperar primeiro para reconstruir a sociedade?\nA) Internet\nB) Energia elétrica\nC) Telefone\nD) Televisão"
r3 = "B"
p4 = "\nDIFÍCIL\nQual destes métodos seria mais eficaz para purificar água em um cenário pós-apocalíptico para consumo imediato?\nA) Filtragem com panos\nB) Uso de iodo\nC) Fervura\nD) Exposição ao sol"
r4 = "C"
p5 = "\nDIFÍCIL\nQual dessas plantas seria a mais útil para fins medicinais após um apocalipse?\nA) Aloe vera\nB) Rosa\nC) Dente-de-leão\nD) Samambaia"
r5 = "A"
p6 = "\nFÁCIL\nQual dessas habilidades seria mais valiosa para sobreviver após um apocalipse?\nA) Programação de computadores\nB) Dirigir Tratores\nC) Escrever de relatórios\nD) Carpintaria"
r6 = "D"
p7 = "\nDIFÍCIL\nQual destes métodos seria mais eficaz e mais fácil para preservar alimentos após um apocalipse?\nA) Congelamento em bolsa térmica\nB) Secagem ao sol\nC) Fermentação\nD) Uso de sal"
r7 = "D"
p8 = "\nFÁCIL\nQual dessas redes de comunicação seria mais fácil de restabelecer primeiro após um apocalipse?\nA) Rede de telefonia celular\nB) Rádio amador\nC) Televisão a cabo\nD) Internet via satélite"
r8 = "B"
p9 = "\nDIFÍCIL\nQual desses alimentos seria mais eficiente para estocar devido à sua longa vida útil e valor nutricional?\nA) Frutas\nB) Macarrão instantâneo\nC) Mel\nD) Leite"
r9 = "C"
p10 = "\nMÉDIO\nQual dessas técnicas seria mais eficiente e fácil para criar uma fonte de calor?\nA) Geração eólica\nB) Queima de papéis\nC) Queima de madeira\nD) Queima de carvão"
r10 = "C"
p11 = "\nFÁCIL\nQual desses livros seria mais útil ter em uma biblioteca pós-apocalíptica?\nA) Um guia de plantas medicinais\nB) Um romance de ficção\nC) Um livro de culinária gourmet\nD) Um manual de etiqueta social"
r11 = "A"
p12 = "\nMÉDIO\nQual dessas fontes de proteína animal seria mais prática para criar em um cenário pós-apocalíptico?\nA) Gado\nB) Peixes\nC) Galinhas\nD) Porcos"
r12 = "C"
p13 = "\nMÉDIO\nQual desses materiais seria mais essencial para a construção de abrigos após um apocalipse?\nA) Vidro\nB) Areia\nC) Madeira\nD) Plástico"
r13 = "C"
p14 = "\nFÁCIL\nQual dessas tecnologias de comunicação teria a maior probabilidade de ser restaurada primeiro?\nA) Correio\nB) Internet \nC) E-mails\nD) Telefone"
r14 = "A"
p15 = "\nMÉDIO\nQual dessas estratégias seria mais eficaz para manter a saúde mental em uma comunidade pós-apocalíptica?\nA) Comer\nB) Isolamento individual\nC) Uso de medicamentos\nD) Atividades recreativas"
r15 = "D"
p16 = "\nFÁCIL\nQual dessas habilidades médicas seria mais valiosa em um cenário pós-apocalíptico?\nA) Cirurgia plástica\nB) Primeiros socorros\nC) Oftalmologia\nD) Dermatologia"
r16 = "B"
p17 = "\nMÉDIO\nQual dessas formas de transporte seria mais viável em um mundo pós-apocalíptico?\nA) Carros elétricos\nB) Barcos a motor\nC) Motos a gasolina\nD) Bicicletas"
r17 = "D"
p18 = "\nFÁCIL\nQual dessas habilidades de cozinha seria mais importante para garantir a segurança alimentar após um apocalipse?\nA) Cozinhar pratos gourmet\nB) Fazer sobremesas\nC) Preparar conservas\nD) Decoração de pratos"
r18 = "C"
p19 = "\nMÉDIO\nQual dessas práticas seria mais eficaz para proteger uma comunidade de doenças transmissíveis após um apocalipse?\nA) Vacinação em massa\nB) Quarentena e isolamento\nC) Uso de máscaras\nD) Higiene pessoal rigorosa"
r19 = "B"
p20 = "\nFÁCIL\nQual dessas fontes de energia seria mais prática para cozinhar em um cenário pós-apocalíptico?\nA) Fogueira\nB) Fogão a gás\nC) Forno elétrico\nD) Micro-ondas"
r20 = "A"

pontos = 0
quantas_perg_precisou = 0
lista_perg = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]
lista_resp = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20]
lista_rand = []
facil = [3,6,8,11,14,16,18,20]
medio = [1,2,10,12,13,15,17,19]
dificil = [4,5,7,9]
facil_ja_foram = 0
medio_ja_foram = 0
dificil_ja_foram = 0

print("\n\n\nBem-vindo ao Quiz de Sobrevivência.\nO sistema de inteligência artificial do Oásis foi comprometido por um vírus.\nPara encontrar o código de restauração, é necessário passar pelos desafios.\nEsse desafio é um quiz que possui perguntas ligadas a como sobreviver em um ambiente pós-apocalíptico.\nVocê escolherá se quer uma pergunta fácil, média ou difícil.\nQuanto maior o grau de dificuldade, mais pontos você ganha em caso de acerto, ou perde em caso de erro.\nSerá enviada uma pergunta aleatória da dificuldade escolhida.\n\nVocê precisa alcançar 10 pontos para receber a parte do código de restauração desse desafio.\n")
_ = input("Começar? (pressione Enter)")

while True:
    print("\nDigite 'fácil' para uma pergunta fácil, 'médio' para uma pergunta média, 'difícil' para uma pergunta difícil ou 'aleatório' para uma pergunta aleatória.")
    
    fal = input()
    
    if str.lower(fal) == "fácil" or str.lower(fal) == "f":
        if facil_ja_foram == 8:
            print("\nVocê já respondeu a todas as perguntas fáceis. Escolha outra dificuldade.")
            _ = input("Avançar (pressione Enter)")
            continue
        else:
            while True:
                rand = rd.randint(0, 19)
                if rand + 1 not in lista_rand and rand + 1 in facil:
                    facil_ja_foram += 1
                    diff = "fácil"
                    pontosdiff = 1
                    break
    elif str.lower(fal) == "médio" or str.lower(fal) == "m":
        if medio_ja_foram == 8:
            print("\nVocê já respondeu a todas as perguntas médias. Escolha outra dificuldade.")
            _ = input("Avançar (pressione Enter)")
            continue
        else:
            while True:
                rand = rd.randint(0, 19)
                if rand + 1 not in lista_rand and rand + 1 in medio:
                    medio_ja_foram += 1
                    diff = "média"
                    pontosdiff = 2
                    break
    elif str.lower(fal) == "difícil" or str.lower(fal) == "d":
        if dificil_ja_foram == 4:
            print("\nVocê já respondeu a todas as perguntas difíceis. Escolha outra dificuldade.")
            _ = input("Avançar (pressione Enter)")
            continue
        else:
            while True:
                rand = rd.randint(0, 19)
                if rand + 1 not in lista_rand and rand + 1 in dificil:
                    dificil_ja_foram += 1
                    diff = "difícil"
                    pontosdiff = 3
                    break
    elif str.lower(fal) == "aleatório" or str.lower(fal) == "a":
        while True:
            rand = rd.randint(0, 19)
            if rand + 1 not in lista_rand:
                if rand + 1 in facil:
                    facil_ja_foram += 1
                    diff = "fácil"
                    pontosdiff = 1
                    break
                elif rand + 1 in medio:
                    medio_ja_foram += 1
                    diff = "média"
                    pontosdiff = 2
                    break
                elif rand + 1 in dificil:
                    dificil_ja_foram += 1
                    diff = "difícil"
                    pontosdiff = 3
                    break
            elif len(lista_rand) == 20:
                print("\nVocê já respondeu a todas as perguntas. Encerre o programa e inicie novamente.")
                time.sleep(5)
                continue
    else:
        print("\nNão entendi. Você pode repetir?")
        continue

    print(lista_perg[rand])
    input('Aperte "Enter" e mostre a alternativa para a câmera.')
    resp0 = picture.capture_and_analyze_image()
    print("Sua resposta:", resp0)
    resp = str.upper(resp0)
    if lista_resp[rand] in resp:
        print(f"\nParabéns! Você acertou! Como a pergunta era {diff}, você ganhou", pontosdiff, "ponto(s).")
        pontos += pontosdiff
    else:
        print(f"\nResposta incorreta. A resposta correta era a letra {lista_resp[rand]}. Como a pergunta era {diff}, você perdeu", pontosdiff, "ponto(s).")
        pontos -= pontosdiff
    print("Você tem", pontos, "ponto(s).")
    lista_rand.append(rand + 1)
    quantas_perg_precisou += 1
    _ = input("Avançar (pressione Enter)")

    if pontos >= 10:
        break

print("\n\n\n")
for i in range(5): 
    print("\nVocê alcançou 10 pontos. Foram precisas", quantas_perg_precisou, "perguntas para isso.\nA parte do código é '?'")
print("\n\n\n")
