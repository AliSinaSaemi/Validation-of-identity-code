

def code_identity():
    user_code = None
    # get the code from user
    try:
        user_code = int(input(">"))
    except ValueError:
        print('SORRY, You can only enter numbers in this field.')
    # inalize the code
    # it must be 10 numbers
    if len(str(user_code)) == 10:
        print('COOL! Our program is inalizing your code...')
        # program has to read all of them especialy first and second number because they might be zero
        position = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        list_user_code = [int(x) for x in str(user_code)]
        control_number = list_user_code[9]
        # control number created by some operations on first 9 numbers of code
        total = 0
        for i in range(10):
            # number (code) x its position = result
            row = list_user_code[i] * position[i]
            total += row
        # result % 11
        remainder = total % 11
        # if 'remainder < 2' -> remainder = control code
        if remainder < 2 and remainder == control_number:
            print('Your identity code is availble')
        elif remainder >= 2:
            # else 11 - remainder then if total wasn't the control number so your code is unvalid
            remainder = 11 - remainder
            if remainder == control_number:
                print('Your identity code is availble')
            else:
                print('Your code is not valid')
        
    elif len(str(user_code)) < 10:
        print('Entered number {} is lower than 10.')
        code_identity()
    elif len(str(user_code)) > 10:
        print('Entered number {} is higher than 10.')
        code_identity()
    else:
        print('Program doesn\'t undrestand!')
        code_identity()

print("Please Enter your identity code below for access.")
code_identity()
