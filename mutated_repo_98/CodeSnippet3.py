"""THE FOLLOWING CODE IS PROPERTY OF ANDREW SASS Copyright © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""

'''this code solves the "Ultimate Binary Watch" problem from https://open.kattis.com/ in a unique and non-trivial way'''

import operator

def ultimatebinarywatch():
    num = input()
    first = ""
    second = ""
    third = ""
    fourth = ""

    for n in num:
        numb = int(n)
        if numb >= 8:
            numb-=8
            first+= "* "
        else:
            first +=". "

        if numb >= 4:
            numb-=4
            second+= "* "
        else:
            second +=". "

        if numb >= 2:
            numb-=2
            third+= "* "
        else:
            third +=". "

        if numb == 1:
            numb-= 1
            fourth+= "* "
        else:
            fourth += ". "
    print(first[0:4]+"  "+first[4:-1])
    print(second[0:4]+"  "+second[4:-1])
    print(third[0:4]+"  "+third[4:-1])
    print(fourth[0:4]+"  "+fourth[4:-1])


"""END OF COPYRIGHTED CODE © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""