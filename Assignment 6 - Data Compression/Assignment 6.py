'''
Created on 3/29/22
@author: Akshatha Vasant Hegde & Punjal Kumari
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
import functools
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5
K = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#USED FOR COMPRESS

def convo(x, a = [], zeros = 0):
    "Counts the 0s and puts the number in the list a, x is og string"
    if len(x) == 0 :
        return a + [zeros]
    elif (zeros < 31):
        if x[0] == '0' :
            zeros = zeros + 1
            return convo(x[1:], a, zeros)
        elif x[0] == '1' :
            return convl(x, a = a + [zeros], ones = 0)
        else :
            return "error"
    else:
        return convl(x, a = a + [zeros], ones = 0)

def convl(x, a, ones = 0):
    "Counts the 1s and puts the number in the list a, x is og string"
    if len(x) == 0:
        return a + [ones]
    elif (ones < 31):
        if x[0] == '1' :
            ones = ones + 1
            return convl(x[1:], a, ones)
        elif x[0] == '0' :
            return convo(x, a = a + [ones], zeros = 0)
        else :
            return "error"
    else:
        return convo(x, a = a + [ones], zeros = 0)

def padding(Pix_Num):
    '''Padding each binary number to K binary numbers. Have made K global'''
    if len(Pix_Num) == K :
        return Pix_Num
    elif len(Pix_Num) < K :
        L = K - len(Pix_Num)
        Zs = '0'*L
        return Zs + Pix_Num
    else :
        return "Pixel number is longer than the block size. Check padding func"

def binary(Num_List):
    ''' converts a number into binary '''
    Num_List = bin(Num_List).replace("0b","")
    Num_List = padding(Num_List)
    return Num_List

#USED FOR UNCOMPRESS

def sepList(code, a = [], pos = 0):
    '''Seperate the code into groups of K'''
    if len(code) <= pos :
        return a
    else:
        return sepList(code, a = a + [code[pos : K+pos]], pos = K+pos)

def binaryToNum(s):
    '''converts the binary to int '''
    if s == "" :
        return 0
    else:
        if s[0] == '1':
            return binaryToNum(s[1:]) + 2**(len(s)-1)
        else:
            return binaryToNum(s[1:])

def Mult(IntList, a = 0, NewList = []):
    '''Multiplies even index num with 0 and odd index num with 1'''
    if IntList == [] :
        return NewList
    else :
        if (a%2 == 0) :
            return Mult(IntList[1:], a+1, NewList = NewList + [IntList[0]*'0'])
        else :
            return Mult(IntList[1:], a+1, NewList = NewList + [IntList[0]*'1'])


#MAIN FUNCTIONS

def compress(incode) :
    "Main Compress Function"
    ''' the largest number of bits that the compress algorithm could
    possibly use to encode a 64-bit string/image is 320'''
    pix_list = convo(incode, a = [], zeros = 0)  
    Bin_pix_list = list(map(binary, pix_list))
    Single_string = functools.reduce(lambda x,y : x + y , Bin_pix_list)
    return Single_string

def uncompress(outcode) :
    "Main decompress Function"
    Seperated_List = sepList(outcode)  #seperate the string into graups of 5
    Int_List = list(map(binaryToNum, Seperated_List)) #Conv bin to int
    New_List = Mult(Int_List)  
    Uncomp_List = functools.reduce(lambda x,y : x + y , New_List)
    return Uncomp_List

def compression(incode) :
    "Ratio b/w compressed size and uncompressed size"
    outcode = compress(incode)
    ratio = round(len(outcode)/len(incode),6)
    return ratio

#ANSWERS TO QUESTIONS

Penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
Smile= "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110"+ "0"*8
Five= "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"

#Your compress function may sometimes give output that is actually longer than
#its input. In a comment, explain what is the largest number of bits that your
#compress algorithm could possibly use to encode a 64-bit string/image.
'''The largest number of bits that the compress algorithm could possibly use
    to encode a 64-bit string/image is 320
    This is the number of bits in the compressed algorithmwhen there is the
    highest amount of varience with wvery bit encoded induvidually'''

#describe the tests that you conducted and the compression ratios that you
#found. You may find it useful to write some additional functions to help
#automate the testing of your compress algorithm.
''' Peguin ratio = 1.48475 '''
''' Smile ratio = 1.328125 '''
''' Five ratio = 1.015625 '''
''' ('0' * 64) ratio = 0.390625 '''
''' ('000' * 4 + '110'*4 +'1'*30 +'0'*10) ratio = 0.859375 '''

#Laicompress(S) that takes a 64-bit string and always outputs a shorter string
#that represents that image.
''' Such an algorithm cannot exist
    As you can see from the above examples, often the compressed code is longer
    than the original code.
    as every substring of 0s and 1s is converted into a binary code of some
    length ( here 5-bits long ), this means that when there is a high amount of
    varience (b/w 0s and 1s) there is more code that is generated
    For example, in our program a single variation 01 will generate 10-bits of
    code.
    If perchance the binary numbers are reduced so that the code that varies
    produces less code. This would make the input code with long stretches of
    the same number much longer in return as the binary code can contain only a
    set amount of code (ex in this program - 31 bits is the limit)
    Thus - an algorithm that always outputs a shorter string that represents
    the image is impossible.
'''

