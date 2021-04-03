import random

 
def convert_to_binary(number: int)->str:
    if number == 1:
        return '1'
    if number == 0:
        return '0'
    converted = ''
    exponent = 0
    result = 0
    while result <= number //2:
        exponent +=1
        result = 2**exponent
    for i in range(exponent,-1,-1):
        if 2**i >= number//2 and 2**i <= number:
            converted += '1'
            number -= (2**i)
        else:
            converted +='0'
    return converted
 
 
 
#---
# tests
print(convert_to_binary(100))
print(convert_to_binary(1000)=='1111101000')
print(convert_to_binary(100)=='1100100')
print(convert_to_binary(10)=='1010')
print(convert_to_binary(1)=='1')
print(convert_to_binary(0)=='0')
print('prime tests')
print(convert_to_binary(2)=='10')
print(convert_to_binary(3))
print(convert_to_binary(7)=='111')
print(convert_to_binary(11)=='1011')
print(convert_to_binary(1009)=='1111110001')
number = random.randint(0,10000000000000)
binary = convert_to_binary(number)
print('{0} converted to binary would read {1}'.format(number,binary))
#---'''
