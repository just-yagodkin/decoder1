answer = ''
with open('data.txt') as string:

    x = []
    temp = 0

    for i in string:
        x += i


    for i in range(len(x)):
        if ord(x[i]) >= 48 and ord(x[i]) <= 58: # если это цифра
            temp = temp*10 + int(x[i])
            if i == len(x) - 1:
                for count in range(temp):
                    answer += x[number]
                temp = 0
        else:                               # Если это буква.
            if temp == 0:                   # Если счетчик равен нулю -
                number = i                  # - запоминаем номер буквы
            else:
                for count in range(temp):
                    answer += x[number]
                temp = 0
                number = i

enigma = open('enigma.txt', 'w')
for c in answer:
    enigma.write(c)