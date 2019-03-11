#!/usr/bin/env python3

ones = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

def numtostr(num):
    num_len = len(str(num))
    if num_len == 1 and num != 0:
        print(ones[num], end='')
    elif num_len == 2:
        if num in tens:
            print(tens[num], end='')
        else:
            print(tens[(num//10)*10]+' '+ones[num%10], end='')
    elif num_len == 3:
        print(ones[num//100]+' hundred ', end='')
        num = num%100
        numtostr(num)
    elif num_len >= 4 and num_len <= 6:
        numtostr(num//1000)
        print(' thousand ', end='')
        num = num%1000
        numtostr(num)
    elif num_len >= 7 and num_len <= 9:
        numtostr(num//1000000)
        print(' million ', end='')
        num = num%1000000
        numtostr(num)
    elif num_len >= 10 and num_len <= 12:
        numtostr(num//1000000000)
        print(' billion ', end='')
        num = num%1000000000
        numtostr(num)
    elif num_len >= 13 and num_len <= 15:
        numtostr(num//1000000000000)
        print(' trillion ', end='')
        num = num%1000000000000
        numtostr(num)

if __name__ == '__main__':
    num = int(input("Enter any number: "))
    if num == 0:
        print('zero')
    else:
        numtostr(num)
    print()
