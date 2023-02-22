import os
import random

cor = {'verm':'\033[1;31m',
       'verd':'\033[1;32m',
       'amar':'\033[1;33m',
       'azul':'\033[1;36m',
       'bran':'\033[m\033[1m',
       'norm':'\033[m'}

def block123():
    tecla = 't'
    while(tecla != '1' and tecla != '2' and tecla != '3'):
        tecla = input('')
    print('você selecionou: {}'.format(tecla))
    return tecla

def block12():
    tecla = 't'
    while(tecla != '1' and tecla != '2'):
        tecla = input('')
    print('você selecionou: {}'.format(tecla))
    return tecla

def print_bat_temp(turno, v, vi, e, ei):

    print('{}turno:{}'.format(cor['bran'], turno))
    print('{}()*****************************************************()'.format(cor['verm']))
    print(' * {}gota de agua{}            * temperatura               *'.format(cor['azul'], cor['verm']))
    print(' * {}vida:{}{}                  * {}vida:{}{}                    *'.format(cor['verd'], v, cor['verm'], cor['verd'], vi, cor['verm']))
    print(' * {}energia:{}{}               * {}energia:{}{}                 *'.format(cor['amar'], e, cor['verm'], cor['amar'], ei, cor['verm']))
    print(' *                         *                           *')
    print(' *        {}(){}               *            )(             *'.format(cor['azul'], cor['verm']))
    print(' *        {}(  ){}             *           ) (             *'.format(cor['azul'], cor['verm']))
    print(' *       {}(    ){}            *          )   (            *'.format(cor['azul'], cor['verm']))
    print(' *      {}(  *  *){}           *         )# #  (           *'.format(cor['azul'], cor['verm']))
    print(' *      {}/(    ){}            *         <)   ( >          *'.format(cor['azul'], cor['verm']))
    print(' *        {}----{}             *            *              *'.format(cor['azul'], cor['verm']))
    print('()*****************************************************(){}'.format(cor['bran']))
    print('decida sua açao perante o inimigo, usando 1, 2 ou 3:')
    print('{}1-atacar'.format(cor['verm']))
    print('{}2-defender'.format(cor['verd']))
    print('{}3-recarregar energia(+1){}'.format(cor['amar'], cor['bran']))

def print_bat_press(turno, v, vi, e, ei):

    print('{}turno:{}'.format(cor['bran'], turno))
    print('{}()*****************************************************()'.format(cor['amar']))
    print(' * {}gota de agua{}            * pressão atmosférica       *'.format(cor['azul'], cor['amar']))
    print(' * {}vida:{}{}                  * {}vida:{}{}                    *'.format(cor['verd'], v, cor['amar'], cor['verd'], vi, cor['amar']))
    print(' * {}energia:{}{}               * {}energia:{}{}                 *'.format(cor['bran'], e, cor['amar'], cor['bran'], ei, cor['amar']))
    print(' *                         *                           *')
    print(' *        {}(){}               *       *     []     *      *'.format(cor['azul'], cor['amar']))
    print(' *        {}(  ){}             *       * [[[[[]]]]] *      *'.format(cor['azul'], cor['amar']))
    print(' *       {}(    ){}            *       * [] ^  ^ [] *      *'.format(cor['azul'], cor['amar']))
    print(' *      {}(  *  *){}           *       ##-[] @  []-##      *'.format(cor['azul'], cor['amar']))
    print(' *      {}/(    ){}            *       ^   [][][]   ^      *'.format(cor['azul'], cor['amar']))
    print(' *        {}----{}             *           []  []          *'.format(cor['azul'], cor['amar']))
    print('()*****************************************************(){}'.format(cor['bran']))
    print('decida sua açao perante o inimigo, usando 1, 2 ou 3:')
    print('{}1-atacar'.format(cor['verm']))
    print('{}2-defender'.format(cor['verd']))
    print('{}3-recarregar energia(+1){}'.format(cor['amar'], cor['bran']))

def batalha(tipo):

    bat = 1
    v = 3
    e = 2
    ei = 2
    vezj = 1
    vezi = 1
    atk = 0
    atki = 0
    defe = 0
    defei = 0
    jog = 0
    turno = 1

    os.system('clear')
    print('\n')
    if(tipo == 1):
        vi = 3
    else:
        vi = 5

    while(bat == 1):
        if(atk == defei):
            atk = 0
        if(atki == defe):
            atki = 0
        v -= atki
        vi -= atk
        if(v == 0):
            os.system('clear')
            print('{}você perdeu!!!{}\n'.format(cor['verm'], cor['bran']))
            bat = 0
            vitoria = 0
            break
        if(vi == 0):
            os.system('clear')
            print('{}você venceu!!!{}'.format(cor['verd'], cor['bran']))
            bat = 0
            vitoria = 1
            break
        vezj = 1
        vezi = 1
        atk = 0
        atki = 0
        defe = 0
        defei = 0
        while(vezj == 1):
            if(tipo == 1):
                print_bat_temp(turno, v, vi, e, ei)
            else:
                print_bat_press(turno, v, vi, e, ei)
            jog = block123()
            if(jog == '1'):
                if(e == 0):
                    os.system('clear')
                    print('sem energia...')
                    continue
                else:
                    os.system('clear')
                    print('{}você atacou!{}'.format(cor['verm'], cor['bran']))
                    atk = 1
                    e -= 1
                    vezj = 0
            elif(jog == '2'):
                os.system('clear')
                print('{}você defendeu!{}'.format(cor['verd'], cor['bran']))
                defe = 1
                vezj = 0
            elif(jog == '3'):
                if(e < 3):
                    os.system('clear')
                    print('{}você recarregou!{}'.format(cor['amar'], cor['bran']))
                    e += 1
                    vezj = 0
                else:
                    os.system('clear')
                    print('energia máxima, escolha outra opção')
                    continue
            if vezi == 1:
                if ei == 0:
                    resp = random.randrange(1, 3)
                    if resp == 1:
                        ei += 1
                        print('{}o inimigo recarregou!{}'.format(cor['amar'], cor['bran']))
                        vezi = 0
                    else:
                        defi = 1
                        print('{}o inimigo defendeu!{}'.format(cor['verm'], cor['bran']))
                        vezi = 0
                elif e == 0:
                    resp = random.randrange(1, 3)
                    if resp == 1:
                        atki = 1
                        ei -= 1
                        print('{}o inimigo atacou!{}'.format(cor['verm'], cor['bran']))
                        vezi = 0
                    else:
                        ei += 1
                        print('{}o inimigo recarregou!{}'.format(cor['amar'], cor['bran']))
                        vezi = 0
                elif ei <= 1:
                    resp = random.randrange(1, 3)
                    if resp == 1:
                        ei += 1
                        print('{}o inimigo recarregou!{}'.format(cor['amar'], cor['bran']))
                        vezi = 0
                    else:
                        atki = 1
                        ei -= 1
                        print('{}o inimigo atacou!{}'.format(cor['verm'], cor['bran']))
                        vezi = 0
                elif ei == 3:
                    resp = random.randrange(1, 4)
                    if resp > 1:
                        atki = 1
                        ei -= 1
                        print('{}o inimigo atacou!{}'.format(cor['verm'], cor['bran']))
                        vezi = 0
                    else:
                        defi = 1
                        print('{}o inimigo defendeu!{}'.format(cor['verm'], cor['bran']))
                        vezi = 0
                else:
                    resp = random.randrange(0, 4)
                    if resp <= 1:
                        atki = 1
                        ei -= 1
                        print('{}o inimigo atacou!{}'.format(cor['verm'], cor['bran']))
                        vezi = 0
                    elif resp == 2:
                        ei += 1
                        print('{}o inimigo recarregou!{}'.format(cor['amar'], cor['bran']))
                        vezi = 0
                    else:
                        defi = 1
                        print('{}o inimigo defendeu!{}'.format(cor['verm'], cor['bran']))
                        vezi = 0

            # if(vezi == 1):
            #     if(turno == 1 or turno % 3 == 0 and turno < 10):
            #         defei = 1
            #         print('{}o inimigo defendeu!{}'.format(cor['verm'], cor['bran']))
            #         vezi = 0
            #     elif(ei > 0):
            #         atki = 1
            #         ei -= 1
            #         print('{}o inimigo atacou!{}'.format(cor['verm'], cor['bran']))
            #         vezi = 0
            #     else:
            #         ei += 1
            #         print('{}o inimigo recarregou!{}'.format(cor['amar'], cor['bran']))
            #         vezi = 0
        turno += 1
    print('{}{}{} a '.format(cor['azul'], v, cor['bran']), end='')
    if(tipo == 1):print('{}{}{}'.format(cor['verm'], vi, cor['bran']))
    else:print('{}{}{}'.format(cor['amar'], vi, cor['bran']))
    return vitoria

def rota_do_carro():
    resp = 0
    pont = 0
    print('{}'.format(cor['bran']))
    print('_____________________________________________')
    print('|Você caiu em cima de um carro!             |')
    print('|Com as opções restritas a fazer resistência|')
    print('|para permanecer no carro ou simplesmente se|')
    print('|largar e cair, você escolhe:               |')
    print('---------------------------------------------')
    print('')
    print('1- pular do carro')
    print('2-permanecer no carro')
    resp = block12()
    if(resp == '1'):
        print('__________________________________________________________')
        print('|Após cair do carro você parou no asfalto!               |')
        print('|Isso com que sua temperatura aumente.                   |')
        print('|Com as circunstâncias atuais é possível tentar evaporar:|')
        print('|Você quer tentar evaporar?                              |')
        print('----------------------------------------------------------')
        print('')
        print('1-sim')
        print('2-não')
        resp = block12()
        if(resp == '1'):
            pont = batalha(1)
            pont += 3
        else:
            print('_________________________________________________')
            print('|Depois de um tempo sua massa diminui ainda mais|')
            print('|Você deseja tentar evaporar agora?             |')
            print('-------------------------------------------------')
            print('')
            print('1-sim')
            print('2-não')
            if(resp == '1'):
                pont = batalha(1)
                pont += 4
            else:
                print('________________________________________________')
                print('|Agora a pressão atmosférica pode fazer você ir|')
                print('|para casa, tente vencê-la para que sua energia|')
                print('|cinética seja o suficiente para voltar        |')
                print('------------------------------------------------')
                pont = 4
    else:
        print('{}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'.format(cor['verm']))
        print('!Infelizmente o carro foi parar em uma garagem!')
        print('!e as suas chances de evaporar são nulas.     !')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{}'.format(cor['bran']))
    return pont

def historia():
    pont = 0
    resp = 0

    os.system('clear')
    print('{}_________________________________________________'.format(cor['bran']))
    print('|Era uma vez uma gota, de maneira preciptada e  |')
    print('|indesejada ela saiu de casa,  participando de  |')
    print('|um enorme despejo, oque chamaram de "chuva".   |')
    print('|Enquanto caia ela obsevou lugares promissores  |')
    print('|para que tentasse voltar para sua casa,o céu,em|')
    print('|segurança, pegando uma carona com os ventos ela|')
    print('|tem a opção de cair num lugar sólido ou aquoso:|')
    print('-------------------------------------------------')
    print('')
    print('Decida as ações da gota em sua jornada para ')
    print('que ela consiga evaporar e voltar para casa.')
    print('')
    print('1-cair em algo solido')
    print('2-cair em algo aquoso')
    resp = block12()
    if(resp == '1'):
        pont = rota_do_carro()
    else:
        print('_____________________________________________')
        print('|Você caiu em uma poça de água!             |')
        print('|Nessa circunstância é possível ficar nela  |')
        print('|ou ir na direção de um bueiro, acompanhando|')
        print('|o fluxo da correnteza.                     |')
        print('---------------------------------------------')
        print('1-ir na direção do bueiro')
        print('2-ficar onde está')
        resp = block12()
        if(resp == '1'):
            print('{}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'.format(cor['verm']))
            print('!Infelizmente você foi completamente consumido !')
            print('!pelas águas sujas da cidade, e suas chances de!')
            print('!voltar para o céu foram jogadas no bueiro.    !')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{}'.format(cor['bran']))
        else:
            print('_______________________________________________')
            print('|Esperando uma oportunidade, surge um gigante |')
            print('|automotivo que quando passa por poças lança  |')
            print('|tudo para cima, e com uma sorte celestial a  |')
            print('|gota é jogada novamente aos ventos, assim tem|')
            print('|a opção de jogar-se em cima do gigante ou    |')
            print('|ir na direção de uma fogueira com gigantescos|')
            print('|pedaços de carne em cima.                    |')
            print('-----------------------------------------------')
            print('')
            print('1-pular em cima do carro')
            print('2-pular na churrasqueira')
            resp = block12()
            if(resp == '1'):
                pont = rota_do_carro()
            else:
                print('____________________________________')
                print('|Ao cair em uma churrasqueira acesa|')
                print('|sua temperatura interna subia com |')
                print('|uma velocidade muito grande, assim|')
                print('|a iniciando um processo de vapori-|')
                print('|zação.                            |')
                print('------------------------------------')
                print('aperte qualquer tecla para continuar')
                resp = input('')
                pont = batalha(1)
                pont += 4
    if(pont != 0):
        print('____________________________________________')
        print('|Você pode agora duelar contra a pressão   |')
        print('|sobre seu corpo, para aumentar sua energia|')
        print('|cinética, dando-o a habilidade de virar um|')
        print('|gás e conseguir voltar para casa.         |')
        print('--------------------------------------------')
        print('deseja aceitar o duelo?')
        print('1-sim')
        print('2-não')
        resp = block12()
        if(resp == '1'):
            pont += batalha(2)
        while(pont == 4):
            print('__________________________________________________')
            print('|infelizmente você ainda não conseguiu evaporar, |')
            print('|mas a pressão em cima do seu corpo é tão grande |')
            print('|que entrar em uma batalha contra a pressão nova-|')
            print('|mente é possível, mas vc deseja continuar?      |')
            print('--------------------------------------------------')
            print('1-sim')
            print('2-não')
            resp = block12()
            if(resp == '2'):
                os.system('clear')
                print('{}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'.format(cor['verm']))
                print('!Você não conseguiu evaporar: derrota. !')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'.format(cor['bran']))
                break
            pont += batalha(2)
        if(pont < 4):
            print('{}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'.format(cor['verm']))
            print('!Você não conseguiu evaporar: derrota. !')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'.format(cor['bran']))
        if(pont > 4):
            print('                                                                  ')
            print('                                                   _              ')
            print('                   _                         (           )        ')
            print('             (           )                  (    ^   ^    )       ')
            print('            (    ^   ^    )                 (        >    )       ')
            print('            (        >    )                  (     --    )        ')
            print('             (     --    )                      *    *            ')
            print('                *                                 *      *        ')
            print('               *    *  *                      *       *           ')
            print('                 *     *                           *              ')
            print('               *    *                           *    *    *       ')
            print('                                                                  ')
            print('                                                                  ')
            print('~~~_~~___~______~~~~~_____~~~_~~~__~~~______~~~~~~_________~~~~~~~')
            print('   ~  ~~      ~  ~  ~~       ~      ~    ~~~    ~  ~~~~~   ~~~~  ~')
            print('             ####################################                 ')
            print('             #                                  #                 ')
            print('             # Voce conseguiu voltar para casa! #                 ')
            print('             # Parabens!                        #                 ')
            print('             #                                  #                 ')
            print('             ####################################                 ')
            print('                                                    pontuacao:{}'.format(pont))

def pos_game():
    print('\n\nVocê deseja recomeçar?')
    print('1-sim')
    print('2-não')
    resp = block12()
    return resp

def main():
    jogando = '1'
    while(jogando == '1'):
        historia()
        jogando = pos_game()
main()