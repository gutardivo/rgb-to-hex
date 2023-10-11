def decimal_to_hex_digit(n):
    return hex(n)[2:]

def convert_each(i):
    j = (int(i) + 1) % 16
    k = (int(i) + 1) // 16

    num2 = decimal_to_hex_digit(j)
    num1 = decimal_to_hex_digit(k) if k > 0 else '0'

    return f'{num1}{num2}'

def convert(rgb):
    r, g, b = rgb
    red = convert_each(r)
    green = convert_each(g)
    blue = convert_each(b)

    return f'#{red}{green}{blue}'

rgb = 144, 230, 255
print(convert(rgb))
