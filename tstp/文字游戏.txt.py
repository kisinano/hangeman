qs = ['请输入你姓名\n',
      '请输入你电话\n',
      '请输入你身份证\n',
      '输入电话号码前三位乘以身份证前三位即可退出\n']
n = 0
i = 1
while True:
    a = input(qs[n])
    if a == '188*411'or a == '7708':
        print('恭喜你答对了')
        break
    n = (n+1) %4
    print('按q键退出')
    i = i +1
    if i>20:
        continue


