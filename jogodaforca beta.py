from time import sleep
import random

o1 = int(input('[0] INICIAR JOGO DA FORCA\n\n'))
if o1 == 0:
    print('……………▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('…………▄▄█▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▄▄')
    print('………▄▀▀▓▒░░░░░░░░░░░░░░░░▒▓▓▀▄')
    print('……▄▀▓▒▒░░░░░░░░░░░░░░░░░░░▒▒▓▀▄')
    print('…..█▓█▒░░░░░░░░░░░░░░░░░░░░░▒▓▒▓█')
    print('..▌▓▀▒░░░░░░░░░░░░░░░░░░░░░░░░▒▀▓█')
    print('..█▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█')
    print('▐█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌')
    print('█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█')
    print('█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓')
    print('█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▌▓█')
    print('█▓▓█▒░░░░▒█▄▒▒░░░░░░░░░▒▒▄█▒░░░░▒█▓▓█')
    print('█▓█▒░▒▒▒▒░░▀▀█▄▄░░░░░▄▄█▀▀░░▒▒▒▒░▒█▓█')
    print('█▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░░█▀▒▒▒▄▄▄▓▓▓▓▒▒▐▓█')
    print('██▌▒▓███▓█████▓▒▐▌░░▐▌▒▓████▓████▓▒▐██')
    print('.██▒▒▓███▓▓▓████▓▄░░░▄▓████▓▓▓███▓▒▒██')
    print('.█▓▒▒▓██████████▓▒░░░▒▓██████████▓▒▒▓█')
    print('..█▓▒░▒▓███████▓▓▄▀░░▀...▄▓▓███████▓▒▒▓█')
    print('....█▓▒░▒▒▓▓▓▓▄▄▄▀▒░░░░░▒▀▄▄▄▓▓▓▓▒▒░▓█')
    print('......█▓▒░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░▒▓█')
    print('........█▓▓▒▒▒░░██░░▒▓██▓▒░░██░░▒▒▒▓▓█')
    print('........▀██▓▓▓▒░░▀░▒▓████▓▒░▀░░▒▓▓▓██▀')
    print('............░▀█▓▒▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀░')
    print('...........█░░██▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██░░█')
    print('............█▄░░▀█▓▒░░░░░░░░░░▒▓█▀░░▄█')
    print('.............█▓█░░█▓▒▒▒░░░░░▒▒▒▓█░░█▓█')
    print('.............▐█▓█░░█▀█▓▓▓▓▓▓█▀░░█░█▓█▌')
    print('...............█▓▓█░█░█░█▀▀▀█░█░▄▀░█▓█')
    print('.............. █▓▓█░░▀█▀█░█░█▄█▀░░█▓▓█')
    print('................█▓▓█░░░░▀▀▀▀░░░░░█▓▓█')
    sleep(3)





elif o1 != 0:
    while o1 != 0:
        print('ESSA OPÇÃO NÃO EXISTE')
        o1 = int(input('[0] INICIAR JOGO DA FORCA\n\n'))

print('CARREGANDO JOGO\n█▒▒▒▒▒▒▒▒▒')
sleep(2)
print('███▒▒▒▒▒▒▒10%')
sleep(2)
print('█████▒▒▒▒▒30%')
sleep(2)
print('███████▒▒▒50%')
sleep(2)
print('██████████100%\n')
sleep(2)

tema = int(input('ESCOLHA UM TEMA: \n[1] ANIMAIS \n[2] FRUTAS (em breve) \n[3] OBJETOS (em breve)\n\n '))
if tema == 1:
    an1 = 'cachorro'
    an2 = 'gato'
    an3 = 'macaco'
    an4 = 'lagarto'
    ltan = [an1,an2,an3,an4]
    print('INICIANDO PARTIDA COM TEMA ANIMAIS AGUARDE\n')
    sleep(2)
    ps = random.choice(ltan)
    #print(ps)
    if ps == an1:
        while ps == an1:
            cl1an= input('\nCHUTE UMA LETRA: ')
            if cl1an == 'c':
                print('C-C-----')
                chtan1 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan1 == 's':
                    rpdan1 = input('DIGITE A RESPOSTA: ')
                    if rpdan1 == an1:
                        print('PARABENS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan1 != an1:
                        print('RESPOTA ERRADA')
                        exit()


            elif cl1an == 'a':
                print('-A------')
                chtan1 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan1 == 's':
                    rpdan1 = input('DIGITE A RESPOSTA: ')
                    if rpdan1 == an1:
                        print('PARABENS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan1 != an1:
                        print('RESPOTA ERRADA')


            elif cl1an == 'h':
                print('---H----')
                chtan1 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan1 == 's':
                    rpdan1 = input('DIGITE A RESPOSTA: ')
                    if rpdan1 == an1:
                        print('PARABENS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan1 != an1:
                        print('RESPOTA ERRADA')


            elif cl1an == 'o':
                print('----O--O')
                chtan1 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan1 == 's':
                    rpdan1 = input('DIGITE A RESPOSTA: ')
                    if rpdan1 == an1:
                        print('PARABENS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan1 != an1:
                        print('RESPOTA ERRADA')


            elif cl1an == 'r':
                print('-----RR-')
                chtan1 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan1 == 's':
                    rpdan1 = input('DIGITE A RESPOSTA: ')
                    if rpdan1 == an1:
                        print('PARABENS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan1 != an1:
                        print('RESPOTA ERRADA')


            else:
                print('NÃO TEM ESSA LETRA')

    elif ps == an2:
        while ps == an2:
            cl2an = input('\nCHUTE UMA LETRA: ')
            if cl2an == 'g':
                print('G---')
                chtan2 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan2 == 's':
                    rpdan2 = input('DIGITE A RESPOSTA: ')
                    if rpdan2 == an2:
                        print('PARABENS VOCÊ ACERTOU')
                        exit()
                    elif rpdan2 != an2:
                        print('RESPOSTA ERRADA VOCÊ PERDEU')
                        exit()


            elif cl2an == 'a':
                print('-A--')
                chtan2 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan2 == 's':
                    rpdan2 = input('DIGITE A RESPOSTA: ')
                    if rpdan2 == an2:
                        print('PARABENS VOCÊ ACERTOU')
                        exit()
                    elif rpdan2 != an2:
                        print('RESPOSTA ERRADA VOCÊ PERDEU')
                        exit()


            elif cl2an == 't':
                print('--T-')
                chtan2 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan2 == 's':
                    rpdan2 = input('DIGITE A RESPOSTA: ')
                    if rpdan2 == an2:
                        print('PARABENS VOCÊ ACERTOU')
                        exit()
                    elif rpdan2 != an2:
                        print('RESPOSTA ERRADA VOCÊ PERDEU')
                        exit()


            elif cl2an == 'o':
                print('---O')
                chtan2 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan2 == 's':
                    rpdan2 = input('DIGITE A RESPOSTA: ')
                    if rpdan2 == an2:
                        print('PARABENS VOCÊ ACERTOU')
                        exit()
                    elif rpdan2 != an2:
                        print('RESPOSTA ERRADA VOCÊ PERDEU')
                        exit()


            else:
                print('NÃO TEM ESSA LETRA')


    elif ps == an3:
        while ps == an3:
            cl3an = input('CHUTE UMA LETRA: ')
            if cl3an == 'm':
                print('M-----')
                chtan3 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan3 == 's':
                    rpdan3 = input('DIGITE A RESPOSTA: ')
                    if rpdan3 == an3:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan3 != an3:
                        print('RESPOSTA ERRADA VOCÊ PERDEU')
                        exit()



            elif cl3an == 'a':
                print('-A-A--')
                chtan3 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan3 == 's':
                    rpdan3 = input('DIGITE A RESPOSTA: ')
                    if rpdan3 == an3:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan3 != an3:
                        print('RESPOSTA ERRADA VOCÊ PERDEU')
                        exit()




            elif cl3an == 'c':
                print('--C-C-')
                chtan3 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan3 == 's':
                    rpdan3 = input('DIGITE A RESPOSTA: ')
                    if rpdan3 == an3:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan3 != an3:
                        print('RESPOSTA ERRADA VOCÊ PERDEU')
                        exit()



            elif cl3an == 'o':
                print('-----O')
                chtan3 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan3 == 's':
                    rpdan3 = input('DIGITE A RESPOSTA: ')
                    if rpdan3 == an3:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan3 != an3:
                        print('RESPOSTA ERRADA VOCÊ PERDEU')
                        exit()

            else:
                print('NÃO TEM ESSA LETRA')


    elif ps == an4:
        while ps == an4:
            cl4an = input('CHUTE UMA LETRA: ')
            if cl4an == 'l':
                print('L------')
                chtan4 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan4 == 's':
                    rpdan4 = input('DIGITE A RESPOSTA: ')
                    if rpdan4 == an4:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan4 != an4:
                        print('RESPOTA ERRADA VOCÊ PERDEU')
                        exit()


            elif cl4an == 'a':
                print('-A-A---')
                chtan4 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan4 == 's':
                    rpdan4 = input('DIGITE A RESPOSTA: ')
                    if rpdan4 == an4:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan4 != an4:
                        print('RESPOTA ERRADA VOCÊ PERDEU')
                        exit()


            elif cl4an == 'g':
                print('--G----')
                chtan4 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan4 == 's':
                    rpdan4 = input('DIGITE A RESPOSTA: ')
                    if rpdan4 == an4:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan4 != an4:
                        print('RESPOTA ERRADA VOCÊ PERDEU')
                        exit()


            elif cl4an == 'r':
                print('----R--')
                chtan4 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan4 == 's':
                    rpdan4 = input('DIGITE A RESPOSTA: ')
                    if rpdan4 == an4:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan4 != an4:
                        print('RESPOTA ERRADA VOCÊ PERDEU')
                        exit()


            elif cl4an == 't':
                print('-----T-')
                chtan4 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan4 == 's':
                    rpdan4 = input('DIGITE A RESPOSTA: ')
                    if rpdan4 == an4:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan4 != an4:
                        print('RESPOTA ERRADA VOCÊ PERDEU')
                        exit()


            elif cl4an == 'o':
                print('------O')
                chtan4 = input('DESEJA CHUTAR A RESPOSTA? S/N: ')
                if chtan4 == 's':
                    rpdan4 = input('DIGITE A RESPOSTA: ')
                    if rpdan4 == an4:
                        print('PARABÉNS VOCÊ ACERTOU!!!')
                        exit()
                    elif rpdan4 != an4:
                        print('RESPOTA ERRADA VOCÊ PERDEU')
                        exit()


            else:
                print('NÃO TEM ESSA LETRA')













