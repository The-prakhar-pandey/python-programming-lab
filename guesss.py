
# guess the number
import random
num = random.randrange(1, 101)
count = 0
while 1:
    n = int(input('guess the number '))
    count += 1
    if n < num:
        print('isse bada hoga ')
    elif n > num:
        print('isse chhota hoga')
    else:
        print('You Win score/', count)
        break
