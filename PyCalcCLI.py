from time import sleep
import math
def addition_f():
    while 3 > 2:
        print("Enter first number")
        fn = input()
        if fn == "":
            continue
        else:
             while 3 > 2:
                print("Enter second number")
                sn = input()
                if sn == "":
                    continue
                else:
                    ans = float(fn) + float(sn)
                    print("Answer = " + str(ans))
                    break
        break
def subtraction_f():
    while 3 > 2:
        print("Enter first number(larger number)")
        fn = input()
        if fn == "":
            continue
        else:
            while 3 > 2:
                print("Enter second number(smaller number)")
                sn = input()
                if sn == "":
                    continue
                else:
                    ans = float(fn) - float((sn))
                    print("Answer = " + str(ans))
                    break
        break
def multiplication_f():
    while 3 > 2:
        print("ENter first number")
        fn = input()
        if fn == "":
            continue
        else:
            while 3 > 2:
                print("Enter second number")
                sn = input()
                if sn == "":
                    continue
                else:
                    ans = float(fn) * float(sn)
                    print("Product = " + str(ans))
                    break
        break
def division_f():
    while 3 > 2:
        print("Enter any number for dividend(except 0)")
        fn = input()
        if fn == "" or fn == "0":
            continue
        else:
            while 3 > 2:
                print("Enter second number for divisor(except 0)")
                sn = input()
                if sn == "" or sn == "0":
                    continue
                else:
                    ans = float(fn) / float(sn)
                    print("Quotient = " + str(ans))
                    break
        break
def exponents_f():
    while 3 > 2:
        print("Enter any number")
        num = input()
        if num == "":
            continue
        else:
            while 3 > 2:
                print("Enter any number for power")
                pwr = input()
                if pwr == "":
                    continue
                else:
                    ans = float(num) ** float(pwr)
                    print("Answer = " + str(ans))
                    break
        break
def squareroots_f():
    while 3 > 2:
        print("Enter any number whose square root do you want to find?")
        sqrt = input()
        if sqrt == "":
            continue
        else:
            ans = math.sqrt(float(sqrt))
            print("Answer = " + str(ans))
            break
        break
def cuberoots_f():
    while 3 > 2:
        print("enter any number whose cube root do you want to find?")
        cubt = input()
        if cubt == "":
            continue
        else:
            ans = float(cubt) ** (1./3)
            print("Answer = " + str(ans))
        break
def atan_f():
    while 3 > 2:
        print("Which numbers atan do you want to find?")
        num = input()
        if num == "":
            continue
        else:
            ans = math.atan(float(num))
            print("Answer = " + str(ans))
        break
def asin_f():
    while 3 > 2:
        print("Which numbers asin do you want to find?")
        num = input()
        if num == "":
            continue
        else:
            ans = math.asin(float(num))
            print("Answer = " + str(ans))
        break
def acos_f():
    while 3 > 2:
        print("Which numbers acos do you want to find?")
        acos = input()
        if acos == "":
            continue
        else:
            ans = math.acos(float(num))
            print("Answer = " + str(ans))
            break
def cos_f():
    while 3 > 2:
        print("Which numbers cos do you want to find?")
        num = input()
        if num == "":
            continue
        else:
            ans = math.cos(float(num))
            print("Answer = " + str(ans))
            break
def sin_f():
    while 3 > 2:
        print("Which numbers sin do you want to find?")
        num = input()
        if num == "":
            continue
        else:
            ans = math.sin(float(num))
            print("Answer = " + str(ans))
            break
def tan_f():
    while 3 > 2:
        print("Which numbers tan do you want to find?")
        num = input()
        if num == "":
            continue
        else:
            ans = math.tan(x)(float(num))
            print("Answer = " + str(ans))
            break
def abs_f():
    while 3 > 2:
        print("Which numbers absolute value do you want to find?")
        num = input()
        if num == "":
            continue
        else:
            ans = abs(float(num))
            print("Answer = " + str(ans))
            break
def log_f():
    while 3 > 2:
        print("Which numbers logarithm do you want to find?")
        num = input()
        if num == "":
            continue
        else:
            while 3 > 2:
                print("Enter the base you want to use or put e for defualt")
                bse = input()
                if bse == "":
                    continue
                elif bse == "e":
                    ans = math.log(float(num))
                    print("Answer = " + str(ans))
                    break
                else:
                    ans = math.log(float(num) , float(bse))
                    print("Answer = " + str(ans))
                    break
        break

print("Welcome to PyCalc 1.1")
while 3 > 2:
    modes = ["1.Basic Mode" , "2.Advanced Mode"]
    for x in modes:
        print(x)
    mod = input()
    if mod == "1":
        opera = ["1.Addition" , "2.Subtraction" , "3.Multiplication" , "4.Division" , "5.Exponents" , "6.Square Roots" , "7.Cube Roots"]
        for x in opera:
            print(x)
        opr = input()
        if opr == "1":
            addition_f()
        elif opr == "2":
            subtraction_f()
        elif opr == "3":
            multiplication_f()
        elif opr == "4":
            division_f()
        elif opr == "5":
            exponents_f()
        elif opr == "6":
            squareroots_f()
        elif opr == "7":
            cuberoots_f()

        sleep(2.5)
        print("Want to change mode?(Y/n)")
        yn = input()
        if yn == "Y" or yn == "y":
            continue
        elif yn == "N" or yn == "n":
            print("Thank You for using PyCalc CLI")
            exit()

    elif mod == "2":
        opr2 = ["1.ABS(Finding absolute value of any numbers)" , "2.ACOS" , "3.Addition" , "4.ASIN" , "5.ATAN" , "6.COS" , "7.Cube Root" , "8.Division" , "9.Exponents" , "10.Logarithm" , "11.Multiplication" , "12.SIN" , "13.Square Root" , "14.Subtraction" , "15.TAN" ]
        for x in opr2:
            print(x)
        opr2s = input()
        if opr2s == "1":
            abs_f()
        elif opr2s == "2":
            acos_f()
        elif opr2s == "3":
            addition_f()
        elif opr2s == "4":
            asin_f()
        elif opr2s == "5":
            atan_f()
        elif opr2s == "6":
            cos_f()
        elif opr2s == "7":
            cuberoots_f()
        elif opr2s == "8":
            division_f()
        elif opr2s == "9":
            exponents_f()
        elif opr2s == "10":
            log_f()
        elif opr2s == "11":
            multiplication_f()
        elif opr2s == "12":
            sin_f()
        elif opr2s == "13":
            squareroots_f()
        elif opr2s == "14":
            subtraction_f()
        elif opr2s == "15":
            tan_f()

        sleep(2.5)
        print("Want to change mode?(Y/n)")
        yn = input()
        if yn == "Y" or yn == "y":
            continue
        elif yn == "N" or yn == "n":
            print("Thank You for using PyCalc CLI")
            exit()
    else:
        continue
