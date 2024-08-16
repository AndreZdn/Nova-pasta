from datetime import date
datu = date.today().year
nasc= int(input('em que ano voce nasceu '))
idade = datu - nasc
if idade<=9:
    print('voce esta na categoria MIRIM')
elif idade<=14:
    print('voce esta na categoria INFANTIL')
elif idade<=19:
    print('voce esta na categoria JUNIOR')
elif idade<=25:
    print('voce esta na categoria SENIOR')
else:
    print('voce esta na categoria MASTER')