alphabet = {
    'A' : [0,0],
    'B' : [0,1],
    'C' : [0,2],
    'D' : [0, 3],
    'E' : [1,0],
    'F' : [1,1],
    'G' : [1,2],
    'H' : [1,3],
    'I' : [2,0],
    'J' : [2, 1],
    'K' : [2,2],
    'L' : [2,3],
    'M' : [3,0],
    'N' : [3,1],
    'O' : [3,2],
    '.' : [3,3]
}

scatter = 0

mtx = []

for i in range (4):
    line = input()
    n = 0
    for letter in line:
        #print(letter)
        if letter == '.':
            n+=1
            continue
        else:
            #print(letter)
            coords = alphabet[letter]
            # print("right x: ", coords[0])
            # print("right y: ", coords[1])
            # print("curr x: ", i)
            # print("curr y: ", n)
            scatter += abs(coords[0]-i)
            # print(letter, ": ", scatter)
            scatter += abs(coords[1] - n)
            # print(letter, ": ", scatter)
            # print("n", " = ", n)
            n+=1

<<<<<<< HEAD
print(scatter)"""THE FOLLOWING CODE IS PROPERTY OF ANDREW SASS Copyright © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""

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