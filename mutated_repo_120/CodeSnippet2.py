"""THE FOLLOWING CODE IS PROPERTY OF ANDREW SASS Copyright © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""

'''this code solves the "platforme" problem from https://open.kattis.com/ in a unique and non-trivial way'''

import operator

def platforme()
    nums = int(input())

    plats =[]

    for i in range (nums):
        plat = [int(x) for x in input().split()]
        plats.append(plat)



    height_sorted = sorted(plats, key=operator.itemgetter(0))

    total = 0

    covered_spots = {}

    for plat in height_sorted:
        
        heightL = covered_spots.get(plat[1], 0)
        heightR = covered_spots.get(plat[2]-1, 0)
        total += plat[0]-heightL

        total += plat[0]-heightR

        for i in range(plat[1],plat[2]):
            covered_spots.update({i: plat[0]})

    print(total)


"""END OF COPYRIGHTED CODE © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""