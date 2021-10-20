'''exercitiul 1'''
def citireLista():
    lst = []
    givenString = input("Dati nr. separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        lst.append(float(x))
    return lst

'''exercitiul 2'''

def nr_intreg(lst):
    '''
    Afișarea părții întregi a tuturor numerelor din listă.
    :param lst:lista citita de la tastatura
    :return:rezultat -o noua lista care respecta cerinta
    '''
    rezultat=[]
    for x in lst:
        x=int(x)
        rezultat.append(x)
    return rezultat

def test_nr_intreg():
    assert nr_intreg([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert nr_intreg([2.4,5.6,3.56]) == [2,5,3]


'''exercitiul 3'''

def interval_deschis(lst,a,b):
    '''
    Se afișeaza toate numerele care aparțin unui interval deschis citit de la tastatură.
    :param lst:
    :param a: capatul stang al intervalului deschis
    :param b: capatul drept al intervalului deschis
    :return: rezultat-o noua lista care are numerele in intervalul deschis
    '''
    rezultat=[]
    for x in lst:
        if a<x and x<b:
            rezultat.append(x)
    return rezultat

def test_interval_deschis():
    assert interval_deschis([1.5, -3.3, 8, 9.8, 3.2],-4,5) == [1.5, -3.3, 3.2]
    assert interval_deschis(([2.0,4.5,5,6]),1,4) == [2.0]
    assert interval_deschis(([2.0,4.7,6.0]),2,6) == [4.7]

'''exercitiul 4'''

def parteI_divizor_parteF(lst):
    '''
    Afisarea tuturor numerelor care au partea intreaga divizor al partii fractionare.
    :param lst:
    :return: rezultat-lista de numere care respecat cerinat
    '''
    rezultat=[]
    for x in lst:
        #intreg partea intreaga a lui x
        intreg=int(x)
        aux=x
        while aux%1!=0:
            aux=aux*10
            intreg=intreg*10
        aux=aux-intreg
        aux=int(aux)
        #aux va avea valoarea numarului de dupa virgula ca numar intreg
        intreg=int(x)
        #verificam daca partea intreaga este divizor a partii fractionare
        if aux%intreg == 0 and aux!=0:
            rezultat.append(x)
    return rezultat

def test_parteI_divizor_parteF():
    assert parteI_divizor_parteF([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]
    assert parteI_divizor_parteF([2.4,5,3.6]) == [2.4, 3.6]

'''exercitiul 5'''

def lista_string(lst):
    '''
    Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din
    cuvinte care le descriu caracter cu caracter.
    :param lst:
    :return:
    '''


    






def print_main():
    print('1.Citire. ')
    print('2.Lista parte intreaga. ')
    print('3.Lista cu numerele care apartin intervalului deschis. ')
    print('4.Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare')
    print('5.Afisare lista string. ')
    print('a.Afisare ')
    print('x.Iesire. ')

def main():
    test_nr_intreg()
    test_interval_deschis()
    test_parteI_divizor_parteF()
    lst = []
    while True:
        print_main()
        op = input("Alegeti o optiune: ")
        if op == '1':
            lst = citireLista()
        if op=='2':
            print(nr_intreg(lst))
        if op=='3':
            a=float(input("Capatul stang al intervalului deschis: "))
            b=float(input("Capatul drept al intervalului deschis: "))
            print(interval_deschis(lst,a,b))
        if op=='4':
            print(parteI_divizor_parteF(lst))
        if op=='5':
            break
        elif op == 'a':
            print(lst)
        elif op == 'x':
            break
        else:
            print("Optiune gresita! Reincearca!")


main()


