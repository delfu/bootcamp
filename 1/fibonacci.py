number_of_characters = 20
stack = []
stack.append(int(0))
stack.append(int(1))

def fibonacci_function(number): #Je comprends toujours pas c'est quoi que je dois mettre dans le "()"; si je met rien ça marche pas; je peux mettre n'importe quoi et ça va marcher
    current_stack_size = int(len(stack))
    new_number = stack[current_stack_size - 1] + stack[current_stack_size - 2]
    stack.append(int(new_number))

while len(stack) < number_of_characters:
    fibonacci_function(number_of_characters)

print (stack)