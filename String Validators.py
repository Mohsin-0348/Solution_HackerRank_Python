if __name__ == "__main__":
    s = input()
    methods = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    for method in methods:
        print(any(method(x) for x in s))
