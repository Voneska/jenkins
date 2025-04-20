def bitnumb_to_decimal(inp_bit_value):
    # check if not a binary number
    if len(inp_bit_value) <= 1:
        raise Exception("The value must be signed: min length = 2")

    # check that string is a binary numb
    # generate new exception (from None)
    try:
        int(inp_bit_value, 2)
    except ValueError:
        raise Exception("The value must be binary") from None

    # if input value is signed then reverse it
    if inp_bit_value[0] == "1":
        value_inv = ''
        for bit in inp_bit_value:
            value_inv += "0" if bit == "1" else "1"

        value_int = -int(value_inv, 2) - 1
    else:
        value_int = int(inp_bit_value, 2)

    return value_int


if __name__ == "__main__":
    input_value = input("Write bit number: ")
    res = bitnumb_to_decimal(input_value)
    print(res)
