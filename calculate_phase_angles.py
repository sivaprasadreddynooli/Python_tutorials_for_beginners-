import cmath
a = input().split('+')
r = int(a[0])
i = int(a[1].replace('j',''))
print(abs(complex(r,i)))
print(cmath.phase(complex(r,i)))