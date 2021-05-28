def build_field(user_num):
    field = ['_'] * 5
    cross = 'X'
    for i in range(user_num):
        field[i-1] = '_'
        field[i] = cross
        print(field)
    return field


def build_field_reverse(user_num):
    field = ['_'] * user_num
    cross = 'X'
    for i in range(user_num):
        if i != 0:
            field[i-1] = '_'
            field[user_num-i] = '_'
        field[user_num-i-1] = 'X'
        field[i] = 'X'
        print(field)
    return field



build_field(5)
st = ''
print(st)
build_field_reverse(5)