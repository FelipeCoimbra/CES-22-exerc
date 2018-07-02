
stack = []

finput = open("exerc13_1.in", "r")

while True:
    line = finput.readline()
    if len(line) == 0:
        break
    stack.append(line)

finput.close()
foutput = open("exerc13_1.out", "w")

while len(stack) > 0:
    foutput.write(stack[len(stack)-1])
    stack.pop()

foutput.close()
