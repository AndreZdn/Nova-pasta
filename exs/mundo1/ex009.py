num = int(input('voce deseja saber a tabuda de qual numero? '))
for c in range(11):
    res = num*c
    print('{} x {} = {}'.format(num, c, res))
