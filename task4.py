# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def Compression(text):
    compressdata = ''
    i = 0
    while i < len(text):
        count = 1
        while i < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        compressdata += str(count) + text[i]
        i += 1
    return compressdata

def Recovery(text):
    datarecovery = ''
    i = 0
    while i < len(text):
        datarecovery += str(text[i+1]) * int(text[i])
        i += 2
    return datarecovery

with open('text1.txt', 'r') as t1:
    t1 = t1.read()
with open('text2.txt', 'w+') as t2:
    t2.write(Compression(t1))
    t2.seek(0)
    t2 = t2.read()
with open('text3.txt', 'w') as t3:
    t3.write(Recovery(t2))
