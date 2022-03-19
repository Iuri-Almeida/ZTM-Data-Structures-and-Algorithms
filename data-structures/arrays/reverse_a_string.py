def reverse_a_string(s):
    if s is None or type(s) != str or len(s) < 2:
        return 'Not so good input'
    return s[-1::-1]


print(reverse_a_string('hello, my name is Iuri'))


def reverse_a_string2(s):
    if s is None or type(s) != str or len(s) < 2:
        return 'Not so good input'

    reversed_list = []
    for i in range(len(s) - 1, -1, -1):
        reversed_list.append(s[i])
    return ''.join(reversed_list)


print(reverse_a_string2('hello, my name is Iuri'))


def reverse_a_string3(s):
    reversed_list = list(s)
    reversed_list.reverse()
    return ''.join(reversed_list)


print(reverse_a_string3('hello, my name is Iuri'))
