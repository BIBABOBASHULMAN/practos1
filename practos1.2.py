text = 'one two three'
a = text[:4]
b = text[4:8]
c = text[9:]
d = a + b + c
t = d.split(' ')
print(f"Moya vraza is {'-'.join(t)}")