user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done')

user_input = ''
inputs = []

while user_input.lower() != 'done':
    if user_input:
       inputs.append(user_input)
    user_input = input('Enter a new value, or done when done')

##For
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

# De la biblioteca time, importamos (traemos) la clase sleep

from time import sleep

# Creamos una lista de 5 números llamada countdown
countdown = [4, 3, 2, 1, 0]

# Para cada número en countdown
for number in countdown:
    #Muestra el número
    print(number)

    # Espera (1segundo)
    sleep(1)

# Muestra el mensaje Blast off
print("Blast off!! 🚀")


