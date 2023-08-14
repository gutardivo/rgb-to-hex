def convert_each(i):
    j = ((int(i)+1) % 16)
    k = (int(i)+1) / 16

    if j == 1:
        num2 = '0'
    elif j == 2:
        num2 = '1'
    elif j == 3:
        num2 = '2'
    elif j == 4:
        num2 = '3'
    elif j == 5:
        num2 = '4'
    elif j == 6:
        num2 = '5'
    elif j == 7:
        num2 = '6'
    elif j == 8:
        num2 = '7'
    elif j == 9:
        num2 = '8'
    elif j == 10:
        num2 = '9'
    elif j == 11:
        num2 = 'a'
    elif j == 12:
        num2 = 'b'
    elif j == 13:
        num2 = 'c'
    elif j == 14:
        num2 = 'd'
    elif j == 15:
        num2 = 'e'
    elif j == 0:
        num2 = 'f'

    if k > 15:
        num1 = 'f'
    elif k > 14:
        num1 = 'e'
    elif k > 13:
        num1 = 'd'
    elif k > 12:
        num1 = 'c'
    elif k > 11:
        num1 = 'b'
    elif k > 10:
        num1 = 'a'
    elif k > 9:
        num1 = '9'
    elif k > 8:
        num1 = '8'
    elif k > 7:
        num1 = '7'
    elif k > 6:
        num1 = '6'
    elif k > 5:
        num1 = '5'
    elif k > 4:
        num1 = '4'
    elif k > 3:
        num1 = '3'
    elif k > 2:
        num1 = '2'
    elif k > 1:
        num1 = '1'
    elif k > 0:
        num1 = '0'

    return f'{str(num1)}{str(num2)}'

def convert(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    red = convert_each(r)
    green = convert_each(g)
    blue = convert_each(b)

    return f'#{red}{green}{blue}'

rgb = 144,230,255
print(convert(rgb))