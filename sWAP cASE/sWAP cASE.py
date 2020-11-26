def swap_case(s):
    L = []
    for i in s:
        if i.islower():
            L.append(i.upper())
        elif i.isupper():
            L.append(i.lower())
        else:
            L.append(i)

    return list_to_String(L)

def list_to_String(s):
    str=""
    return (str.join(s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)