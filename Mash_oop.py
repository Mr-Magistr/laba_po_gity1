import os
import time


def kluchi():
    Ldoor = '[ ]'
    Rdoor = '[ ]'
    Lights = '[ ]'
    Lwind = '[ ]'
    Rwind = '[ ]'
    while True:
        print(
            '1.Фары: ' + Lights + '\n'
                                  '2.Левая дверь: ' + Ldoor + '\n'
                                                              '3.Правая дверь: ' + Rdoor + '\n'
                                                                                           '4.Левое окно: ' + Lwind + '\n'
                                                                                                                      '5.Правое окно: ' + Rwind + '\n'
                                                                                                                                                  '0 для выхода \n')
        breloque = int(input())

        if breloque == 1:
            if Lights == '[ ]':
                Lights = '[X]'
            else:
                Lights = '[ ]'

        if breloque == 2:
            if Ldoor == '[ ]':
                Ldoor = '[X]'
            else:
                Ldoor = '[ ]'
        if breloque == 3:
            if Rdoor == '[ ]':
                Rdoor = '[X]'
            else:
                Rdoor = '[ ]'
        if breloque == 4:
            if Lwind == '[ ]':
                Lwind = '[X]'
            else:
                Lwind = '[ ]'
        if breloque == 5:
            if Rwind == '[ ]':
                Rwind = '[X]'
            else:
                Rwind = '[ ]'
        if breloque == 0:
            menufunc(int(input('что нужно?\n'
                               '1.новая конфигурация\n'
                               '2.удалить конфигурацию\n'
                               '3.изменить конфигурацию\n'
                               '4.просмотр конфигураций\n'
                               '5.Брелок\n')))
def sborka():
    car1 = Jelezo(str(input('Введите имя тачки: ')), str(input('Введите название движка: ')),
                  str(input('объем движка: ')), str(input('мощность движка: ')), str(input('акум?: ')),
                  str(input('ток акума: ')),
                  str(input('Введите имя коробки: ')), str(input('Введите цвет тачки: ')))
    saves.write(
        car1.name + ',' + car1.Cengine + ',' + car1.CEvolume + ' (см3),' + car1.CEpower + ' (л.с.),' + car1.Cakum + ',' + car1.CAtok + ' А,' +
        car1.Ckorob + ',' + car1.Ccolor + '\n')
    return print('Ваша конфигурация сохранена как: ' + car1.name)
def prosmotr():
    print('укажите номер конфигурации(для выхода нажмите 0)')
    cnt = 0
    for i in range(len(a)):
        q = str(a[i])
        q = q.split(',')
        if len(q[0]) > 1:
            cnt += 1
            print(cnt, q[0])
        else:
            continue
    se = int(input())
    if se == 0:
        menufunc(int(input('что нужно?\n'
                           '1.новая конфигурация\n'
                           '2.удалить конфигурацию\n'
                           '3.изменить конфигурацию\n'
                           '4.просмотр конфигураций\n'
                           '5.Брелок\n')))
    if se>cnt:
        print('Выход из диапазона')
        menufunc(int(input('что нужно?\n'
                           '1.новая конфигурация\n'
                           '2.удалить конфигурацию\n'
                           '3.изменить конфигурацию\n'
                           '4.просмотр конфигураций\n'
                           '5.Брелок\n')))
    else:
        cnt = 0
        for i in range(len(a)):
            q = str(a[i])
            q = q.split(',')
            if len(q[0]) > 1:
                cnt += 1
                if cnt == se:
                    messi2 = q[0]
                    for j in range(len(a)):
                        q1 = str(a[j])
                        q1 = q1.split(',')
                        if q1[0] == messi2:
                            return (print('Название авто: ' + q[0] + '\n'
                                                             'Двигатель: ' + q[1] + '\n'
                                                                                    '    Объём: ' + q[2] + '\n'
                                                                                                           '    Мощность: ' +
                                  q[3] + '\n'
                                         'Аккумулятор: ' + q[4] + '\n'
                                                                  '    Напряжение: 12 В\n'
                                                                  '    Ток: ' + q[5] + '\n'
                                                                                       '    Ёмкость: 60 А*ч\n'
                                                                                       'Коробка передач: ' + q[6] + '\n'
                                                                                                                    'Цвет авто: ' +
                                  q[7] + '\n'))

def izmena():
    print('укажите номер конфигурации(для выхода нажмите 0)')
    cnt = 0
    for i in range(len(a)):
        q = str(a[i])
        q = q.split(',')
        if len(q[0]) > 1:
            cnt += 1
            print(cnt, q[0])
        else:
            continue
    chg = int(input())
    if chg == 0:
        menufunc(int(input('что нужно?\n'
                           '1.новая конфигурация\n'
                           '2.удалить конфигурацию\n'
                           '3.изменить конфигурацию\n'
                           '4.просмотр конфигураций\n'
                           '5.Брелок\n')))
    if chg>cnt:
        print('Выход из диапазона')
        menufunc(int(input('что нужно?\n'
                    '1.новая конфигурация\n'
                    '2.удалить конфигурацию\n'
                    '3.изменить конфигурацию\n'
                    '4.просмотр конфигураций\n'
                    '5.Брелок\n')))
    else:
        cnt = 0
        for i in range(len(a)):
            q = str(a[i])
            q = q.split(',')
            if len(q[0]) > 1:
                cnt += 1
                if cnt == chg:
                    messi3 = q[0]
                    for j in range(len(a)):
                        q1 = str(a[j])
                        q1 = q1.split(',')
                        if q1[0] == messi3:
                            print('Выберите позицию для изменения: ' + '\n'
                                                                       '1.Двигатель\n'
                                                                       '2.Аккумулятор\n'
                                                                       '3.Коробка передач\n'
                                                                       '4.Цвет\n'
                                                                       '5.Название\n'
                                                                       '0 для выхода\n')
                            chang = int(input())
                            if chang == 0:
                                menufunc(int(input('что нужно?\n'
                                                   '1.новая конфигурация\n'
                                                   '2.удалить конфигурацию\n'
                                                   '3.изменить конфигурацию\n'
                                                   '4.просмотр конфигураций\n'
                                                   '5.Брелок\n')))
                            elif chang < 0 or chang > 5:
                                print('Выход из диапазона')
                                menufunc(int(input('что нужно?\n'
                                                   '1.новая конфигурация\n'
                                                   '2.удалить конфигурацию\n'
                                                   '3.изменить конфигурацию\n'
                                                   '4.просмотр конфигураций\n'
                                                   '5.Брелок\n')))
                            elif chang == 1 or chang == 2 or chang == 3 or chang == 4 or chang == 5:
                                dc = j
                                for z in range(len(a)):
                                    if z != dc:
                                        deletes.write(a[z])
                                    else:
                                        if chang == 1:
                                            cnt = 0
                                            for t in range(len(engmas)):
                                                p = str(engmas[t])
                                                p = p.split(',')
                                                if len(p[0]) > 1:
                                                    cnt += 1
                                                    print(cnt, p[0])
                                                else:
                                                    continue
                                            eng2 = int(input())
                                            if (eng2 > cnt) or (eng2 < 1):
                                                print('Выход из диапазона')
                                                menufunc(int(input('что нужно?\n'
                                                                   '1.новая конфигурация\n'
                                                                   '2.удалить конфигурацию\n'
                                                                   '3.изменить конфигурацию\n'
                                                                   '4.просмотр конфигураций\n'
                                                                   '5.Брелок\n')))
                                            cnt = 0
                                            for t in range(len(engmas)):
                                                p = str(engmas[t])
                                                p = p.split(',')
                                                if len(p[0]) > 1:
                                                    cnt += 1
                                                    if cnt == eng2:
                                                        messi = p[0]
                                                        for t1 in range(len(engmas)):
                                                            p1 = str(engmas[t1])
                                                            p1 = p1.split(',')
                                                            if p1[0] == messi:
                                                                engine_name = p[0]
                                                                volume = p[1]
                                                                power = p[2]
                                            deletes.write(
                                                q[0] + ',' + engine_name + ',' + volume + ',' + power + ',' + q[
                                                    4] + ',' + q[5] + ',' + q[6] + ',' + q[7])
                                        if chang == 2:
                                            cnt = 0
                                            for t in range(len(akmas)):
                                                p = str(akmas[t])
                                                p = p.split(',')
                                                if len(p[0]) > 1:
                                                    cnt += 1
                                                    print(cnt, p[0])
                                                else:
                                                    continue
                                            eng2 = int(input())
                                            if (eng2 > cnt) or (eng2 < 1):
                                                print('Выход из диапазона')
                                                menufunc(int(input('что нужно?\n'
                                                                   '1.новая конфигурация\n'
                                                                   '2.удалить конфигурацию\n'
                                                                   '3.изменить конфигурацию\n'
                                                                   '4.просмотр конфигураций\n'
                                                                   '5.Брелок\n')))
                                            cnt = 0
                                            for t in range(len(akmas)):
                                                p = str(akmas[t])
                                                p = p.split(',')
                                                if len(p[0]) > 1:
                                                    cnt += 1
                                                    if cnt == eng2:
                                                        messi = p[0]
                                                        for t1 in range(len(akmas)):
                                                            p1 = str(akmas[t1])
                                                            p1 = p1.split(',')
                                                            if p1[0] == messi:
                                                                ak_name = p[0]
                                                                tok = p[1]
                                            deletes.write(q[0] + ',' + q[1] + ',' + q[2] + ',' + q[
                                                3] + ',' + ak_name + ',' + tok + ',' + q[6] + ',' + q[7])
                                        if chang == 3:
                                            cnt = 0
                                            for t in range(len(kormas)):
                                                p = str(kormas[t])
                                                p = p.split(',')
                                                if len(p[0]) > 1:
                                                    cnt += 1
                                                    print(cnt, p[0])
                                                else:
                                                    continue
                                            eng2 = int(input())
                                            if (eng2 > cnt) or (eng2 < 1):
                                                print('Выход из диапазона')
                                                menufunc(int(input('что нужно?\n'
                                                                   '1.новая конфигурация\n'
                                                                   '2.удалить конфигурацию\n'
                                                                   '3.изменить конфигурацию\n'
                                                                   '4.просмотр конфигураций\n'
                                                                   '5.Брелок\n')))
                                            cnt = 0
                                            for t in range(len(kormas)):
                                                p = str(kormas[t])
                                                p = p.split(',')
                                                if len(p[0]) > 1:
                                                    cnt += 1
                                                    if cnt == eng2:
                                                        messi = p[0]
                                                        for t1 in range(len(kormas)):
                                                            p1 = str(kormas[t1])
                                                            p1 = p1.split(',')
                                                            if p1[0] == messi:
                                                                ko_name = p[0]
                                            deletes.write(
                                                q[0] + ',' + q[1] + ',' + q[2] + ',' + q[3] + ',' + q[4] + ',' + q[
                                                    5] + ',' + ko_name + ',' + q[7])
                                        if chang == 4:
                                            cnt = 0
                                            for t in range(len(clrmas)):
                                                p = str(clrmas[t])
                                                p = p.split(',')
                                                if len(p[0]) > 1:
                                                    cnt += 1
                                                    print(cnt, p[0])
                                                else:
                                                    continue
                                            eng2 = int(input())
                                            if (eng2 > cnt) or (eng2 < 1):
                                                print('Выход из диапазона')
                                                menufunc(int(input('что нужно?\n'
                                                                   '1.новая конфигурация\n'
                                                                   '2.удалить конфигурацию\n'
                                                                   '3.изменить конфигурацию\n'
                                                                   '4.просмотр конфигураций\n'
                                                                   '5.Брелок\n')))
                                            cnt = 0
                                            for t in range(len(clrmas)):
                                                p = str(clrmas[t])
                                                p = p.split(',')
                                                if len(p[0]) > 1:
                                                    cnt += 1
                                                    if cnt == eng2:
                                                        messi = p[0]
                                                        for t1 in range(len(clrmas)):
                                                            p1 = str(clrmas[t1])
                                                            p1 = p1.split(',')
                                                            if p1[0] == messi:
                                                                clr_nameq = p[0]
                                            deletes.write(
                                                q[0] + ',' + q[1] + ',' + q[2] + ',' + q[3] + ',' + q[4] + ',' + q[
                                                    5] + ',' + q[6] + ',' + clr_nameq)
                                        if chang == 5:
                                            namere = str(input('Введите желаемое имя\n'))
                                            deletes.write(
                                                namere + ',' + q[1] + ',' + q[2] + ',' + q[3] + ',' + q[4] + ',' + q[
                                                    5] + ',' + q[6] + ',' + q[7])
                                        saves.close()
                                        deletes.close()
                                        os.remove('Saves.txt')
                                        os.rename('Saves1.txt', 'Saves.txt')
def udalenka():
    print('укажите номер удаляемого сохранения(для выхода нажмите 0)?')
    cnt = 0
    for i in range(len(a)):
        q = str(a[i])
        q = q.split(',')
        if len(q[0]) > 1:
            cnt += 1
            print(cnt, q[0])
        else:
            continue
    dele = int(input())
    if dele == 0:
        menufunc(int(input('что нужно?\n'
                    '1.новая конфигурация\n'
                    '2.удалить конфигурацию\n'
                    '3.изменить конфигурацию\n'
                    '4.просмотр конфигураций\n'
                    '5.Брелок\n')))
    if dele>cnt:
        print('Выход из диапазона')
    else:
        cnt = 0
        for i in range(len(a)):
            q = str(a[i])
            q = q.split(',')
            if len(q[0]) > 1:
                cnt += 1
                if cnt == dele:
                    messi = q[0]
                    for j in range(len(a)):
                        q1 = str(a[j])
                        q1 = q1.split(',')
                        if q1[0] == messi:
                            dc = j
                            for z in range(len(a)):
                                if z != dc:
                                    deletes.write(a[z])
                                else:
                                    continue
                            saves.close()
                            deletes.close()
                            os.remove('Saves.txt')
                            os.rename('Saves1.txt', 'Saves.txt')
def test1():
    k=4
    for a1 in range(k):
        for a2 in range(k):
            for a3 in range(k):
                for a4 in range(k):
                    for a5 in range(k):
                        for a6 in range(k):
                            for a7 in range(k):
                                for a8 in range(k):
                                    car1=Jelezo(str(a1)*3,str(a2)*3,str(a3)*3,str(a4)*3,str(a5)*3,str(a6)*3,str(a7)*3,str(a8)*3)
                                    saves.write(
                                        car1.name + ',' + car1.Cengine + ',' + car1.CEvolume + ' (см3),' + car1.CEpower + ' (л.с.),' + car1.Cakum + ',' + car1.CAtok + ' А,' +
                                        car1.Ckorob + ',' + car1.Ccolor + '\n')
                                    print('Ваша конфигурация сохранена как: ' + car1.name)
    deletes.close()
    saves.close()
    return(print('Выполнено',k**8,'операций'))
def test2():
    deletes.close()
    saves.close()
    os.remove('Saves.txt')
    os.rename('Saves1.txt', 'Saves.txt')
def test3():


    starttime=time.time()
    k = 4
    for a1 in range(k):
        for a2 in range(k):
            for a3 in range(k):
                for a4 in range(k):
                    for a5 in range(k):
                        for a6 in range(k):
                            for a7 in range(k):
                                for a8 in range(k):
                                    car1 = Jelezo(str(a1), str(a2), str(a3), str(a4), str(a5), str(a6), str(a7),
                                                  str(a8))
                                    saves.write(
                                        car1.name + ',' + car1.Cengine + ',' + car1.CEvolume + ' (см3),' + car1.CEpower + ' (л.с.),' + car1.Cakum + ',' + car1.CAtok + ' А,' +
                                        car1.Ckorob + ',' + car1.Ccolor + '\n')
                                    # print('Ваша конфигурация сохранена как: ' + car1.name)

    elapsed_time = time.time()-starttime
    print('Время затрачено на все операции:\n')
    print(elapsed_time)
    print('Среднее время на операцию:\n')
    print(elapsed_time/(k**8))
    print('-----')
    deletes.close()
    saves.close()

def menufunc(b):
    if b==1:
        return sborka()
    if b==2:
        return udalenka()
    if b==3:
        return izmena()
    if b==4:
        return prosmotr()
    if b==5:
        return kluchi()
    if b==6:
        return test1()
    if b==7:
        return test2()
    if b==8:
        return test3()
    else:
        print('Выход из диапазона')
        menuque = int(input('что нужно?\n'
                            '1.новая конфигурация\n'
                            '2.удалить конфигурацию\n'
                            '3.изменить конфигурацию\n'
                            '4.просмотр конфигураций\n'
                            '5.Брелок\n'
                            '6.Test1\n'
                            '7.Test2\n'
                            '8.Test3\n'
                            ))
        menufunc(menuque)


class Jelezo:
    def __init__(self,name,Cengine,CEvolume,CEpower,Cakum,CAtok,Ckorob,Ccolor):
        self.name=name
        self.Cengine=Cengine
        self.CEvolume=CEvolume
        self.CEpower=CEpower
        self.Cakum=Cakum
        self.CAtok=CAtok
        self.Ckorob=Ckorob
        self.Ccolor=Ccolor
while True:
    deletes = open('Saves1.txt', 'w', encoding='UTF-8')
    saves = open('Saves.txt', 'a', encoding='UTF-8')
    a = list(map(str, open('Saves.txt', encoding='UTF-8')))
    englist = open('enginelist.txt', 'a', encoding='UTF-8')
    engmas = list(map(str, open('enginelist.txt', encoding='UTF-8')))
    aklist = open('akkumlist.txt', 'a', encoding='UTF-8')
    akmas = list(map(str, open('akkumlist.txt', encoding='UTF-8')))
    korlist = open('koroblist.txt', 'a', encoding='UTF-8')
    kormas = list(map(str, open('koroblist.txt', encoding='UTF-8')))
    clrlist = open('colorlist.txt', 'a', encoding='UTF-8')
    clrmas = list(map(str, open('colorlist.txt', encoding='UTF-8')))
    menuque = int(input('что нужно?\n'
                        '1.новая конфигурация\n'
                        '2.удалить конфигурацию\n'
                        '3.изменить конфигурацию\n'
                        '4.просмотр конфигураций\n'
                        '5.Брелок\n'
                        '6.Test1\n'
                        '7.Test2\n'
                        '8.Test3\n'
                        ))
    menufunc(menuque)

