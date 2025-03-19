'''
Copyright 2025 Nicolette Glut
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
                            
'''

#BSD License


def ultimatebinarywatch(num):
    
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


