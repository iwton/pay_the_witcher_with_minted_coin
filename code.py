money = int(input('Enter the number: '))
x = money // 25
y = money % 25 // 10
z = money % 25 % 10 // 5
n = money % 25 % 10 % 5 // 1

print('You need ' + str(x + y + z + n) + ' coins' )
