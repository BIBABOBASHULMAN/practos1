from string import Template
name = 'Daniil'
age = '18'
city = 'Minsk'
s = Template('Menya zovut $name. Mne $age let. Ya iz $city.')
print(s.substitute((name=name, age=age, city=city)))