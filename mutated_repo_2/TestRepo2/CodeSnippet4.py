"""THE FOLLOWING CODE IS PROPERTY OF ANDREW SASS Copyright © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""

'''this code solves the "Building Pyramids" problem from https://open.kattis.com/ in a unique and non-trivial way'''

import operator

def pyramids()
    blocks = int(input())

    if blocks == 0:
        print (0)
    else:
        blocks-=1
        layers = 1
        layerside = 1
        while(blocks >= (layerside+2)*(layerside+2)):
            blocks -=(layerside+2)*(layerside+2)
            layers +=1
            layerside +=2
        print(layers)

"""END OF COPYRIGHTED CODE © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER"""