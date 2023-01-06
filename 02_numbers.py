name = input('¿Cuál es tu nombre? => ')
print(name)
last_name = input('¿Cuál es tu apellido? => ')
print(last_name)
age = input('¿Cuál es tu edad? => ')
print(age)
total = age + 10
total = str(total)
age = str(age)

template = f"Hola mi nombre es {name} {last_name}, tengo {age} años y en 10 años tendré {total} años"
print(template)