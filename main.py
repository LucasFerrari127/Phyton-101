#Importo una biblioteca que tiene el metodo random
import random

#armo una tupla con los valores posibles de las opciones
options = ('piedra', 'papel', 'tijera')

#inicializo el numero de victorias
computer_wins = 0
user_wins = 0

#inicializo el numero de round
rounds = 1

#mientras sea verdadero. el corte lo produce el break de cuando alguien gana 2 partidas.
while True:

    #Imprimo el numero de rounds y las victorias de cada  uno.
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    #le pido al usuario que ingrese piedra papel o tijera.
    user_option = input('piedra, papel o tijera => ')
    #lo paso a lower case para que la igualdad se pueda comparar.
    user_option = user_option.lower()

    #compruebo que la opción sea válidad, hasta que no sea validad no avanzamos.
    while not user_option in options:
     print('esa opcion no es valida')
     user_option = input('piedra, papel o tijera => ')
     continue

    #sumo un round  
    rounds += 1

    #Hago el random para sacar la opcion de la compu
    computer_option = random.choice(options)

    #muestro las 2 opciones.
    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    #Hago todas las comparaciones posibles para saber quien gana. Si hay empate repito la pregunta, si hay un ganador incremento el numero de rondas ganadas.
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1
    #Cuando la compu llega a 2 rondas ganadas, gana y salgo del jugo.
    if computer_wins == 2:
      print('El ganador es la computadora')
      break
    #Lo mismo pero para el usuario.
    if user_wins == 2:
      print('El ganador es el usuario')
      break
