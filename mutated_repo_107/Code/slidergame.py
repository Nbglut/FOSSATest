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

print(scatter)
