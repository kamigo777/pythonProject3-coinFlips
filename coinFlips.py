import random
print('Яподброшу монетку 1000 раз. Угадай сколько раз выпадет Орел(Нажми клавишу Enter ЧТобы начать)')
input()
flips = 0
heads = 0
while flips <1000:
    if random.randint(0,1) ==1:
        heads = heads + 1
    flips = flips+1

    if flips == 900:
        print('900 подкидываний и Орел выпал ' + str(heads) + 'раз')
    if flips ==100:
        print('100 подкидываний и Орел выпал ' + str(heads) + 'раз')
    if flips == 500:
        print('500 подкидываний и Орел выпал ' + str(heads) + 'раз')

print()
print('из 1000 подкидываний  монетки, Орел выпал ' + str(heads) + 'раз')
print('насколько вы близки к правильному ответу?')