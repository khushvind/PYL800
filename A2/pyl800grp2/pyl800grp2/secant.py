from sympy import symbols, sympify
x = symbols('x')

try:
    expression_str = input("Enter a mathematical function using 'x' as the variable: ")
    expression = sympify(expression_str)
    # value_of_x = float(input("Enter a value for x: "))
    x0 = 1.0
    x1 = 2.0
    max_iter = int(input('Enter maximum iterations  '))
    error = float(input('Enter tolerance error  '))
    i = 0
    fx0 = expression.subs(x,x0)
    fx1 = expression.subs(x,x1)
    print('x0 = ',x0)
    print('x1 = ',x1)
    while(i < max_iter and abs(x1-x0)>error):
        k = x1
        fk = fx1
        x1 = x1 - ((fx1)*(x1-x0))/(fx1-fx0)
        print(f'x',i+2,' = ',x1)
        x0 = k
        fx1 = expression.subs(x,x1)
        fx0 = fk
        i+=1
    print(f'one of the root of the function is ',x1)

except Exception as e:
    print(f"Error: {e}")