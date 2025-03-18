print("Hello World!")
"""THE FOLLOWING CODE IS PROPERTY OF ANDREW SASS Copyright © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER
MIT License

Copyright (c) 2023 Anna

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

'''this code adds three numbers together in a unique, non-trivial, stupid, and very overcomplicated way'''
def AndrewsAwesomeAdditionAchiever(x,y,z):
    starter = 0

    if x>y:
        for i in range(x-y):
            starter+=1
        for i in range(2*y):
            starter+=1
    else:
        for i in range (y-x):
            starter+=1
        for i in range(2*x):
            starter+=1


    middle = 0
    biz = bin(z)
    biz = biz[2:]
    biy = bin(y)
    biy = biy[2:]

    biggerlen = max(len(biz),len(biy))
    if  len(biz) >len(biy):
        for i in range(biggerlen-len(biy)):
            biy= '0'+biy
    else:
        for i in range(biggerlen-len(biz)):
            biz= '0'+biz



   
    carier = 0
    result = ""


    for i in range(biggerlen-1,-1,-1):
        temp = carier
        temp +=1 if biz[i] == '1' else 0
        temp +=1 if biy[i] == '1' else 0
        result = ('1' if temp%2 ==1 else '0') +result
        carier = 0 if temp <2 else 1
    
    middle = result
    if carier !=0:
        middle = '1'+middle
    middle = int(middle,2)
    
    
    if middle > starter:
        while starter >x:
            starter-=1
        return(middle+starter)
    else:
        return middle+starter-y


"""END OF COPYRIGHTED CODE © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER""""""THE FOLLOWING CODE IS PROPERTY OF ANDREW SASS Copyright © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""

'''this code adds three numbers together in a unique, non-trivial, stupid, and very overcomplicated way'''
def AndrewsAwesomeAdditionAchiever(x,y,z):
    starter = 0

    if x>y:
        for i in range(x-y):
            starter+=1
        for i in range(2*y):
            starter+=1
    else:
        for i in range (y-x):
            starter+=1
        for i in range(2*x):
            starter+=1


    middle = 0
    biz = bin(z)
    biz = biz[2:]
    biy = bin(y)
    biy = biy[2:]

    biggerlen = max(len(biz),len(biy))
    if  len(biz) >len(biy):
        for i in range(biggerlen-len(biy)):
            biy= '0'+biy
    else:
        for i in range(biggerlen-len(biz)):
            biz= '0'+biz



   
    carier = 0
    result = ""


    for i in range(biggerlen-1,-1,-1):
        temp = carier
        temp +=1 if biz[i] == '1' else 0
        temp +=1 if biy[i] == '1' else 0
        result = ('1' if temp%2 ==1 else '0') +result
        carier = 0 if temp <2 else 1
    
    middle = result
    if carier !=0:
        middle = '1'+middle
    middle = int(middle,2)
    
    
    if middle > starter:
        while starter >x:
            starter-=1
        return(middle+starter)
    else:
        return middle+starter-y


"""END OF COPYRIGHTED CODE © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""