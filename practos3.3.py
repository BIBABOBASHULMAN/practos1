#from string import Template
#name = input('Vvodim imya: ')
#age = input('Vvodim vozrast: ')
#city = input('Vvodim gorod: ')
#s = Template('Menya zovut $name. Mne $age let. Ya iz $city.')
#print(s.substitute((name=name, age=age, city=city)))
s = input()

i = 0
while s[i] == ' ':
    i += 1
s = s[i:]

i = len(s)
while s[i - 1] == ' ':
    i -= 1
s = s[:i]

s_new = s[0]
i = 1
while i < len(s):
    if s[i] != ' ':
        s_new += s[i]
    elif s[i - 1] != ' ':
        s_new += '-'
    i += 1
print(s_new )