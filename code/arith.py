import sys

def main():
    if  len(sys.argv) != 4:
        print 'Need exactly 3 arguments'
    else:
        operator = sys.argv[1]
        if not operator in ['add', 'subtract', 'multiply', 'divide']:
           print 'Operator is not one of add, subtract, multiply, or divide: bailing out' 
        else:
            try:
                operand1, operand2 = float(sys.argv[2]), float(sys.argv[3])
            except ValueError:
                print 'cannot convert input to a number: bailing out'
                return
        
            do_arithmetic(operand1, operator, operand2)

def do_arithmetic(operand1, operator, operand2):

    if operator == 'add':
        value = operand1 + operand2
    elif operator == 'subtract':
        value = operand1 - operand2
    elif operator == 'multiply':
        value = operand1 * operand2
    elif operator == 'divide':
        value = operand1 / operand2
    print value

main()
