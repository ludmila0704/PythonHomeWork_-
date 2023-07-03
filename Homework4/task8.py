
cars = 'BMW'
s = 50
computers = "LENOVO"
tables = ''
car, computer, table = 0, 0, 0


def change_user_variable():
    glob_dict = globals()
    for key, value in glob_dict.items():

        if key.endswith('s') and len(key) != 1:
            temp = key[:-1]
            glob_dict[temp] = value
            glob_dict[key] = None


if __name__ == "__main__":
    change_user_variable()
    print(globals().items())
