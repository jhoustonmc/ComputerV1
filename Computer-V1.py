import sys

def reduce_equation(leftSide, rightSide):
    try:
        if (check_degree(rightSide) > check_degree(leftSide)):
            temp = rightSide
            rightSide = leftSide
            leftSide = temp
        rightSide_list = rightSide.split(" ")
        leftSide_list = leftSide.split(" ")
        i = 2
        for c in rightSide_list and leftSide_list:
            if ((i - 2) < len(rightSide_list) and (i - 2) < len(leftSide_list)):
                if (c == "X^0" or c == "X^1" or c == "X^2"):
                    temp = float(rightSide_list[i - 4]) * -1
                    leftSide_list[i - 4] = str(float(leftSide_list[i - 4]) + temp)
            i += 1
        reducedEquation = " ".join(leftSide_list)
        return(reducedEquation)
    except:
        exit("Improper Input. Please revise")

def check_degree(leftSide):
    degree = 0
    i = 0
    while (i != len(leftSide)):
        if (leftSide[i] == '^'):
            degree = int(leftSide[i + 1])
            if (degree > 2):
                exit("The polynomial degree is strictly greater than 2, I can't solve.")
        i += 1
    return(degree)

def solve_polynomial(reducedEquation):
    max_degree = check_degree(reducedEquation)
    reducedEquation_list = reducedEquation.split(" ")
    i = 0
    while (i < len(reducedEquation_list)):
        if (reducedEquation_list[i] == "X^0"):
            c = float(reducedEquation_list[i - 2])
        if (reducedEquation_list[i] == "X^1"):
            if (reducedEquation_list[i - 3] != "-"):
                b = float(reducedEquation_list[i - 2])
            else:
                b = float(reducedEquation_list[i - 2]) * -1
        if (reducedEquation_list[i] == "X^2"):
            if (reducedEquation_list[i - 3] != "-"):
                a = float(reducedEquation_list[i - 2])
            else:
                a = float(reducedEquation_list[i - 2]) * -1
        i += 1
    ans = ans1 = ans2 = ans3 = ans4 = ans5 = 0
    if (max_degree == 0):
        if (c == 0):
            print ("True for all X")
        else:
            print("No Solution")
    if (max_degree == 1):
        ans = (c * -1) / (b)
    if (max_degree == 2):
        if (a == 0):
            ans1 = 1
        elif ((b**2 - (4*a*c)) < 0):
            ans2 = (-b - ((b**2 - (4*a*c))**0.5))/(2 * a)
            ans3 = (-b + ((b**2 - (4*a*c))**0.5))/(2 * a)
        else:
            ans4 = (-b - (b**2 - (4*a*c))**0.5)/(2 * a)
            ans5 = (-b + (b**2 - (4*a*c))**0.5)/(2 * a)
    if (ans != 0):
        print("Solution: " + str(ans))
    elif (ans1 != 0):
        print("No Solution")
    elif (ans2 != 0 and ans3 != 0):
        print("Discriminant is strictly negative, the two solutions are: " + '\n' + str(ans2) + '\n' + str(ans3))
    elif (ans4 != 0 and ans5 != 0):
        print("Discriminant is strictly positive, the two solutions are: " + '\n' + str(ans4) + '\n' + str(ans5))

if (len(sys.argv) == 2):
    compound = sys.argv[1].upper().split(' = ')
    leftSide = compound[0]
    rightSide = compound[1]
    degree = check_degree("".join(leftSide))
    reducedEquation = reduce_equation(leftSide, rightSide)
    print("Reduced form: " + reducedEquation + " = 0")
    print("Polynomial degree: " + str(degree))
    solve_polynomial(reducedEquation)
else:
    print("Incorrect Formatting")
