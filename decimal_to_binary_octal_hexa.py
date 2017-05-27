number = 17
p = 0
p = len(str(bin(number)))
p = p - 1
for i in range(1, (number + 1)):
    print(' ' * (p - len(str(i))) + str(i),
          ' ' * (p - len(str(oct(i)).replace('0o', ''))) + str(oct(i)).replace('0o', '') + ' ' * (
          p - len(str(hex(i)).replace('0x', ''))),
          str(hex(i)).replace('0x', '') + ' ' * (p - len(str(bin(i)).replace('0b', ''))) + (
          str(bin(i)).replace('0b', '')))