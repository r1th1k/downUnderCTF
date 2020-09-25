file = open('ilovescomo.jpg.out', 'r').read().split('\n')

binary = ['0'] * len(file)

for i in range(len(file)):
    if file[i] == '':
        continue
    if file[i][-1] == ' ':
        binary[i] = '1'

flag = ""
for i in range(0, len(binary), 8):
    flag += chr(int("".join(binary[i:i + 8]), 2))

print(flag)
