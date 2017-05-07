#git - Проверка
# удаляет в текстовом файле источнике "my_file1.txt" все вхождения ссылок на литературу,
# а результат записывает в новый файл "my_file2.txt".
def DelLitRefFile():
    DelLitRefFile_ (4)

# Перебирает строки файла "file1" - все найденные блоки [1...n] удаляются
# Результат записывает в фйл "file2"
# n - максимальное количество цифр ссылки на литературу внутри скобок [1...n]
#def DelLitRefFile (file1, file2, n):
def DelLitRefFile_ (n):
    from time import clock
    tbegin=clock()
    f1 = open('my_file1.txt', 'r')# открыт файл для чтения
    f2 = open('my_file2.txt', 'w')# открыт файл для записи
    i=1
    while True:
        line = f1.readline()
        if line == "":
            break
        line = LineDelFrag (line, n)
        f2.write(line)
        i=i+1
    dt=clock()-tbegin
    #line = "\n"+" = Число обработанных строк в файле = "+str(i) # строка итога
    line = "\n"+" = Число обработанных строк в файле = "+str(i)+"\n Время: "+str(round(dt, 2))+" сек." # строка итога
    f2.write(line) # запись строки итога
    f1.close()
    f2.close()
    print ('Готово!')

# Обработка всей строки - все найденные блоки [1...n] с n цифрами удаляются
# IFL - список параметров интерфейса между LineDelFrag (str, n) и FindBlok (str, n)
# [False, -1, -1] - блок не найден
# [True, left, right] - блок не найден, left :right - индексы для '[' и ']'
def LineDelFrag (str, n):
    IFL=[False, -1, -1]
    while True:
        if str ==  "":
            break
        else:
            IFL=FindBlok (str, n)
            if IFL[0]:
                i_left=IFL[1]
                i_right=IFL[2]
                str=str[:i_left] + str[i_right+1:]
                continue
            else:
                break
    IFL=[False, -1, -1]
    return (str)

# Ищет первое вхождение блока [1...n] в строке str
# Возвращает: (False, -1, -1) - нет блоков, (True, i_left, i_right) - блок найден 
def FindBlok (str, n): # n - максимальное количество цифр в блоке [1...n]
    ch1=r'['
    ch2=r']'
    nlen=len(str) # nlen - длина str 
    for i in range(nlen): 
        if str[i] == ch1:
            left_=i # индекс для '['
            s=str[left_+1:]
            nlen_=nlen-left_-1 # длина строки s
            if n > nlen_: # nb - конец обзора поиска конца блока цифр
                nb=nlen_
            else:
                nb=n
            nn=NumFrag (s, nb)			
            if nn > 0:
                right_=left_+nn+1 # индекс для ']'
                if str[right_] == ch2:
                    return ([True, left_, right_])
                else:
                    continue                                
            else:
                continue
        else:
            continue
    return([False, -1, -1])

# Проверка фрагмента цифр длинной n от начала строки str (нужна для FindBlok).
def NumFrag (str, n):
    nlen=len(str)
    if n > nlen:
        nb=nlen
    else:
        nb=n
    w=str[0 : nb]
    for i in range(nb):
        if w.isdigit():
            return(nb-i)
        w=w[0:nb-i-1]
    return(0)
	
DelLitRefFile()