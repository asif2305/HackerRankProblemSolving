if __name__ == '__main__':
    s = input()

    print(any(ss.isalnum() for ss in s))
    print(any(ss.isalpha() for ss in s))
    print(any(ss.isdigit() for ss in s))
    print(any(ss.islower() for ss in s))
    print(any(ss.isupper() for ss in s))