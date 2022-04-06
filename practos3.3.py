from string import Template
name = input('Vvodim imya: ')
age = input('Vvodim vozrast: ')
city = input('Vvodim gorod: ')
s = Template('Menya zovut $name. Mne $age let. Ya iz $city.')
print(s.substitute((name, age, city)))