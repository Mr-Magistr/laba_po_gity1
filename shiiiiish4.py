file = open('Mashinki.txt').readlines()
masssiv=['Модель:','Цвет:','Объём двигателя:','Фары:']
class Car:
    def __init__(self,model = None,color= None,obem_dvig = None,fary = 'Выкл',dveri = 'Закрыты'):
        self.model = model
        self.color  = color
        self.obem_dvig = obem_dvig
        self.fary = fary
        self.dveri = dveri

class Dvery:
    dvop='Открыта'
    dvcl='Закрыта'
    def __init__(self,dv1='Закрыта',dv2='Закрыта',dv3='Закрыта',dv4='Закрыта'):
        self.dv1 = dv1
        self.dv2 = dv2
        self.dv3 = dv3
        self.dv4 = dv4



znach_dver=[]
prikol=[]
for i in range(0,len(file)):
    lupa = file[i].split(' ')
    znach_dver.append(lupa[9])
    prikol.append(Car(lupa[1],lupa[3],lupa[6],lupa[8],lupa[10]))
lupa=None
file=None

class peremen:
    per1 = '0'
    per2 = '0'
    per3 = '0'
    per4 = '0'
    per5 = '0'
    proverka = None
a = peremen()
class start():

    def pynkt1(self):
        def aboba():
            a.proverka=5
            a.per1 = int(input("Что вы хотите сделать\n1)Добавить новую конфигурацию машинки\n2)Изменить какую-нибудь конфигурацию\n3)Завершить программу\n"))
            start.proverkainf(b,a.per1) 
            if a.per1 == 1:
                start.debil(b)
                #print(len(prikol))
                file4 = open('Mashinki.txt').readlines()
                pip=len(file4)-1
                #print(file4)
                #print(file4[pip])
                #print(f'{masssiv[0]} {prikol[pip].model} {masssiv[1]} {prikol[pip].color} {masssiv[2]} {prikol[pip].obem_dvig} {masssiv[3]} {prikol[pip].fary} {znach_dver[pip]} {prikol[pip].dveri}\n')
                if file4[pip] == str(f'{masssiv[0]} {prikol[pip].model} {masssiv[1]} {prikol[pip].color} {masssiv[2]} {prikol[pip].obem_dvig} {masssiv[3]} {prikol[pip].fary} {znach_dver[pip]} {prikol[pip].dveri}'):
                    print('Конфигурация сохранена в файле')
                start.pynkt1(b)
            elif a.per1 == 2:
                start.vibor(b)



            elif a.per1 == 3:
                print('Программа сломана')
            else:
                #print('выбранноео число выходет за пределы допустимого')
                #print('Ты дебил?')
                aboba()
        aboba()

    def vibor(self):
        start.dva2(b)
        a.per2 = int(input((f'Выберите номер из {len(prikol)}\n')))
        a.proverka=len(prikol)+1
        start.proverkainf(b,a.per2)
        start.vibranoecilo(b)

    def vibranoecilo(self):
        a.proverka=9
        if (a.per2 <= len(prikol)) and (a.per2 > 0):
            i = int(a.per2) - 1
            

            print(f'{masssiv[0]} {prikol[i].model} {masssiv[1]} {prikol[i].color} {masssiv[2]} {prikol[i].obem_dvig} {masssiv[3]} {prikol[i].fary} {znach_dver[i]} {prikol[i].dveri}')
            if prikol[i].fary == 'Выкл':
                a.per3 = int(input("Что хотите изменить?\n1)Модель\n2)Цвет\n3)Объём двигателя\n4)Включить Фары\n5)Двери\n6)Удалить конфигурацию\n7)Выбрать другую конфигурацию\n8)В начало\n"))
            if prikol[i].fary == 'Вкл':
                a.per3 = int(input("Что хотите изменить?\n1)Модель\n2)Цвет\n3)Объём двигателя\n4)Выключить Фары\n5)Двери\n6)Удалить конфигурацию\n7)Выбрать другую конфигурацию\n8)В начало\n"))
            start.proverkainf(b, a.per3)
            if a.per3 == 1:
                prikol[i].model = input('Введите новое название:\n').replace(' ', '_')
                start.zapis(b)

                file4 = open('Mashinki.txt').readlines()
                if file4[i] == str(f'{masssiv[0]} {prikol[i].model} {masssiv[1]} {prikol[i].color} {masssiv[2]} {prikol[i].obem_dvig} {masssiv[3]} {prikol[i].fary} {znach_dver[i]} {prikol[i].dveri}'):
                    print('модель правильно изменилась')
                start.vibranoecilo(b)
            elif a.per3 == 2:
                prikol[i].color = input('Введите новый цвет:\n').replace(' ', '_')
                start.zapis(b)
                start.vibranoecilo(b)
            elif a.per3 == 3:
                prikol[i].obem_dvig = input('Введите новый объём:\n').replace(' ', '_')
                start.zapis(b)
                start.vibranoecilo(b)
            elif a.per3 == 4:
                if prikol[i].fary == 'Выкл':
                    prikol[i].fary = 'Вкл';print('Фары включены')
                    start.zapis(b)
                    start.vibranoecilo(b)
                else:
                    prikol[i].fary = 'Выкл';print('Фары выключены')
                    start.zapis(b)
                    start.vibranoecilo(b)

            elif a.per3 == 5:
                start.knopdv(b)

            elif a.per3 == 6:
                del (prikol[i])
                print('Конфигурация удлена')
                start.zapis(b)

                file4 = open('Mashinki.txt').readlines()
                if len(file4) == len(prikol):
                    print('Проверка прошла успешно и в файле удалилась конфигурация')

                start.pynkt1(b)
            elif a.per3 == 7:
                start.vibor(b)
            elif a.per3 == 8:
                start.pynkt1(b)
            else:
                #print('Ты дебил?');
                start.vibranoecilo(b)
        else:
            #print(f'Ты выбрал число больше {len(prikol)}, выбели другое')
            start.vibor(b)



    def dva2(self):
        for i in range(len(prikol)):
            vvvvvp = prikol[i].dveri.replace('\n', '')
            print(f'{i + 1}){masssiv[0]} {prikol[i].model} {masssiv[1]} {prikol[i].color} {masssiv[2]} {prikol[i].obem_dvig} {masssiv[3]} {prikol[i].fary} {znach_dver[i]} {vvvvvp}')

    def debil(self):
        pyrpyr = Car(input('Напишите модель\n').replace(' ', '_'), input('Напишите цвет\n').replace(' ', '_'),input('Напишите объём двигателя\n').replace(' ', '_'))
        file3 = open('Mashinki.txt', 'a+')
        file3.write(f'Модель: {pyrpyr.model} Цвет: {pyrpyr.color} Объём двигателя: {pyrpyr.obem_dvig} Фары: {pyrpyr.fary} Двери: {pyrpyr.dveri}\n')
        file3.close()
        prikol.append(Car(pyrpyr.model,pyrpyr.color,pyrpyr.obem_dvig,'Выкл','Закрыты\n'))
        znach_dver.append('Двери:')

    def zapis(self):
        file2 = open('Mashinki.txt', 'w')
        for i in range(0, len(prikol)):
            file2.write(f'{masssiv[0]} {prikol[i].model} {masssiv[1]} {prikol[i].color} {masssiv[2]} {prikol[i].obem_dvig} {masssiv[3]} {prikol[i].fary} {znach_dver[i]} {prikol[i].dveri}')
        file2.close()

    def knopdv(self):
        i = int(a.per2) - 1
        dver = Dvery()
        def dvery(stroch,chislo,nom):
            if stroch in znach_dver[i]:print(f'{nom}){chislo}',end=' '); return chislo
            else:chislo = 'Открыта';print(f'{nom}){chislo}', end=' '); return chislo

        dver.dv1 = dvery('в', dver.dv1, '1')
        dver.dv2 = dvery('е', dver.dv2, '2')
        dver.dv3 = dvery('р', dver.dv3, '3')
        dver.dv4 = dvery('и', dver.dv4, '4')

        a.per4 = int(input('\nВыхотите открыть или закрыть двери?\n1)открыть\n2)закрыть\n3)выбрать другую конфигурацию\n'))

        op = 'открыт'
        cl = 'закрыт'
        def openclose(nomdv, opcl, znach, bukv1, bukv2):
            if nomdv == opcl:
                print(f'Дверь и так {znach}а')
                start.knopdv(b)
                return nomdv
            else:
                znach_dver[i] = znach_dver[i].replace(bukv1, bukv2)
                print(f'Дверь теперь {znach}а')
                nomdv = opcl
                return nomdv

        def slova(znach, opcl):
            if (dver.dv1 == dver.dv2 == dver.dv3 == dver.dv4 == opcl):
                prikol[i].dveri = f'{znach}ы\n'.capitalize()
            else:
                prikol[i].dveri = f'Частично_открыты\n'
            start.zapis(b)
            start.knopdv(b)

        if a.per4 == 1:
            a.per5 = int(input('какую дверь из четырёх открыть?\n'))
            if a.per5 == 1:
                dver.dv1 = openclose(dver.dv1, dver.dvop, op, 'в', 'В')
                slova(op, dver.dvop)

            if a.per5 == 2:
                dver.dv2 = openclose(dver.dv2, dver.dvop, op, 'е', 'Е')
                slova(op, dver.dvop)

            if a.per5 == 3:
                dver.dv3 = openclose(dver.dv3, dver.dvop, op, 'р', 'Р')
                slova(op, dver.dvop)

            if a.per5 == 4:
                dver.dv4 = openclose(dver.dv4, dver.dvop, op, 'и', 'И')
                slova(op, dver.dvop)

        elif a.per4 == 2:
            a.per5 = int(input('какую дверь из четырёх закрыть?\n'))
            if a.per5 == 1:
                dver.dv1 = openclose(dver.dv1, dver.dvcl, cl, 'В', 'в')
                slova(cl, dver.dvcl)

            if a.per5 == 2:
                dver.dv2 = openclose(dver.dv2, dver.dvcl, cl, 'Е', 'е')
                slova(cl, dver.dvcl)

            if a.per5 == 3:
                dver.dv3 = openclose(dver.dv3, dver.dvcl, cl, 'Р', 'р')
                slova(cl, dver.dvcl)

            if a.per5 == 4:
                dver.dv4 = openclose(dver.dv4, dver.dvcl, cl, 'И', 'и')
                slova(cl, dver.dvcl)


        elif a.per4 == 3:
            start.vibor(b)
        else:
            print('Ты дебил?');start.pynkt1(b)
        return()

    def proverkainf(self,pro):
        if pro in range(1,a.proverka):
                print('выбранноео число не выходит за пределы допустимого')
        else:
                print('выбранноео число выходит за пределы допустимого')


b=start()
b.pynkt1()


#print(len(prikol))
#print(len(znach_dver))
#print(prikol[0].__dict__,f'{masssiv[0]} {prikol[0].model} {masssiv[1]} {prikol[0].color} {masssiv[2]} {prikol[0].obem_dvig} {masssiv[3]} {prikol[0].fary} {znach_dver[0]} {prikol[0].dveri}')
#print(prikol[1].__dict__)
#print(prikol[2].__dict__)
#print(prikol[3].__dict__)
#print(prikol[4].__dict__)
#print(prikol[5].__dict__)
#print(prikol[6].__dict__)
#print(prikol[7].__dict__)
#print(prikol[8].__dict__)
