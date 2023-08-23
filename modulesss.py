import keyword as key


def contains_keyword(*args):
    for arg in args:
        if key.iskeyword(arg) == True:
            print(True)
    print(False)


contains_keyword("etc", "def")
