def task2(number, own_base, format_to_convert):
    def char_to_value(char):
        return int(char) if char.isdigit() else ord(char.upper()) - ord('A') + 10

    def to_decimal(number, own_base):
        if "." in str(number):
            integer_part, float_part = str(number).split(".")[0][::-1], str(number).split(".")[1]

            return sum([char_to_value(integer_part[i]) * (own_base ** i) for i in range(len(integer_part))]) + sum([char_to_value(float_part[i]) * (own_base ** -(i + 1)) for i in range(len(float_part))])
        else:
            number = str(number)[::-1]
            return sum([char_to_value(number[i]) * (own_base ** i) for i in range(len(number))])

    def to_user_format(decimal_num, supposed_format):
        integer_part = int(decimal_num)
        fractional_part = decimal_num - integer_part
        res = ""

        while integer_part > 0:
            res += str(integer_part % supposed_format)
            integer_part //= supposed_format

        res = res[::-1]

        if fractional_part > 0:
            res += "."
            while fractional_part > 0 and len(res) < 20: 
                fractional_part *= supposed_format
                digit = int(fractional_part)
                res += str(digit)
                fractional_part -= digit

        return res if res else "0"

    decimal_number = to_decimal(number, own_base)
    res = to_user_format(decimal_number, format_to_convert)
    print(f"Turned base {own_base} number: {number}, into new base - {format_to_convert} and got result:\n{res}")

# Test cases
task2(691, 16, 10)
task2(691, 8, 2)
task2("AAA123", 12, 5)
task2(691, 20, 4)
task2("FFFFFFAAA10101", 22, 11)
task2("AAABBBCCCHHEEQQQ", 36, 10)
task2("1E14D", 16, 10)
task2(123213, 10, 16)