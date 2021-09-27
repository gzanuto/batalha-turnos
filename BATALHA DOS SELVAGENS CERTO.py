# Player Stats
import random
danox = 1
danoy = 1
agilidadex = 1
agilidadey = 1
atributosx = 1
atributosy = 1
ataquex = 1
ataquey = 1
defesax = 1
defesay = 1
criticox = 1
criticoy = 1
vidax = 1
viday = 1

# Personagem 1 - Martol

atributos1 = []
ataque1 = 95
defesa1 = 87
agilidade1 = 70
vida1 = 100
atributos1.append(ataque1)
atributos1.append(defesa1)
atributos1.append(agilidade1)
atributos1.append(vida1)

# Personagem 2 - Lass

atributos2 = []
ataque2 = 77
defesa2 = 82
agilidade2 = 95
vida2 = 100
atributos2.append(ataque2)
atributos2.append(defesa2)
atributos2.append(agilidade2)
atributos2.append(vida2)

# Menu

resp1 = str(input('Olá, você gostaria de jogar "Batalha dos Selvagens"? [S/N]')).upper().strip()
if resp1 == 'S':
    print('Escolha seu personagem')
    print('Martol')
    print('Ata', 'Def', 'Agi', 'Vida')
    print(atributos1)
    print('Lass')
    print('Ata', 'Def', 'Agi', 'Vida')
    print(atributos2)
    resp2 = int(input('Digite [1] para Martol e [2] para Lass.'))
    if resp2 == 1:
        print('Você escolheu Martol!')
        print('Ata', 'Def', 'Agi', 'Vida')
        ataquex = ataque1
        defesax = defesa1
        agilidadex = agilidade1
        vidax = vida1
        ataquey = ataque2
        defesay = defesa2
        agilidadey = agilidade2
        viday = vida2
        atributosx = atributos1
        atributosy = atributos2
        print(atributosx)
    else:
        print('Você escolheu Lass!')
        ataquex = ataque2
        defesax = defesa2
        agilidadex = agilidade2
        vidax = vida2
        ataquey = ataque1
        defesay = defesa1
        agilidadey = agilidade1
        viday = vida1
        atributosx = atributos2
        atributosy = atributos1
        print(atributosx)
else:
    exit()

# Batalha - PlayerX vs ComputerY

while vidax > 0 and viday > 0:
    print(input('Digite [D] para rodar o dado!').upper().strip())
    dadox = random.randint(1, 6)
    print(dadox)
    if dadox >= 5:
        criticox = (ataquex + agilidadex*2 / 2) * 10/100
        viday = (viday - criticox)
        if viday < 0:
            viday = 0
            print(f'Você causou um dano crítico de {criticox}!')
        print(f'Agora a vida de seu adversário é de {viday}.')
        if viday > 0:
            viday = viday + (5/100 * defesay)
            print('Seu adversário recupera 5% de sua vida.')
        else:
            break
        print(f'Agora a vida de seu adversário é de {viday}.')
    elif dadox == 2 or dadox == 3 or dadox == 4:
        danox = 10/100 * ataquex
        viday = (viday - danox)
        if viday < 0:
            viday = 0
            print(f'Você acertou o ataque e tirou um dano de {danox}!')
        print(f'Agora a vida de seu adversário é de {viday}.')
        if viday > 0:
            viday = viday + (5/100 * defesay)
            print('Seu adversário recupera 5% de sua vida.')
        else:
            break
        print(f'Agora a vida de seu adversário é de {viday}.')
    else:
        print(f'Você não conseguiu atingir seu adversário, e sua vida segue em {viday}.')

    print('Agora é a vez de seu adversário!')
    dadoy = random.randint(1, 6)
    print(dadoy)
    if dadoy >= 5:
        criticoy = (ataquey + agilidadey*2 / 2) * 10/100
        vidax = (vidax - criticoy)
        if vidax < 0:
            vidax = 0
        print(f'Seu adversário causou um dano crítico de {criticoy}!')
        if vidax > 0:
            vidax = vidax + (5/100 * defesax)
            print('Você recupera 5% de vida.')
        print(f'Agora a sua vida é de {vidax}.')
    elif dadoy == 2 or dadoy == 3 or dadoy == 4:
        danoy = 10/100 * ataquey
        vidax = (vidax - danoy)
        print(f'Seu adversário acertou o ataque e tirou um dano de {danoy}!')
        if vidax > 0:
            vidax = vidax + (5/100 * defesax)
            print('Você recupera 5% de vida.')
        print(f'Agora a sua vida é de {vidax}.')
    else:
        print(f'Seu adversário não te atingiu, e a sua vida segue em {vidax}.')
if viday <= 0:
    print('A batalha dos selvagens chegou ao fim e você saiu como vencedor!')
elif vidax <= 0:
    print('A batalha dos selvagens chegou ao fim e você saiu derrotado.')
