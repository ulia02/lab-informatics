import math


def calc(virashenie):
    s = virashenie.replace(" ", "")
    i = [0]
    return sravnenie(s, i)



def sravnenie(s, i):
    c = slosh(s, i)
    while i[0] < len(s) and s[i[0]] == '>':
        i[0] += 1
        v = slosh(s, i)    
        c = 1 if c > v else 0
    return c


def slosh(s, i):
    c = umnosh(s, i)
    while i[0] < len(s) and s[i[0]] in '+-':
        znak = s[i[0]]
        i[0] += 1
        v = umnosh(s, i)
        if znak == '+':
            c += v
        else:
            c -= v
    return c


def umnosh(s, i):
    c = chislo(s, i)
    while i[0] < len(s) and s[i[0]] in '*/':
        znak = s[i[0]]
        i[0] += 1
        v = chislo(s, i)
        if znak == '*':
            c *= v
        else:
            c /= v
    return c


def chislo(s, i):
    if i[0] >= len(s):
        raise ValueError()
    c = s[i[0]]
    if c == '-':
        i[0] += 1
        return -chislo(s, i)
    if c == '+':
        i[0] += 1
        return chislo(s, i)
    if c == '(':
        i[0] += 1
        ch = sravnenie(s, i)          
        if i[0] < len(s) and s[i[0]] == ')':
            i[0] += 1
        else:
            raise ValueError()
        return ch
    if c.isalpha():
        imya = ''
        while i[0] < len(s) and s[i[0]].isalpha():
            imya += s[i[0]]
            i[0] += 1

        if imya == 'cos':
            if i[0] >= len(s) or s[i[0]] != '(':
                raise ValueError()
            i[0] += 1                       
            argument = sravnenie(s, i)     
            if i[0] >= len(s) or s[i[0]] != ')':
                raise ValueError()
            i[0] += 1                      
            return math.cos(argument)
        else:
            raise ValueError()               
    num = ''
    while i[0] < len(s) and s[i[0]] in '0123456789.':
        num += s[i[0]]
        i[0] += 1
    if num == '':
        raise ValueError()
    if '.' in num:
        return float(num)
    else:
        return int(num)



print("Введите выражение (когда нажмёте Enter на пустой строке, программа завершится):")

while True:
    e = input(">>> ")
    if e.strip() == "":
        print("Вот и конец)")
        break
    try:
        print("=", calc(e))
    except Exception:
        print("Ошибка, проверьте выражение и попробуйте снова")