import basic

while True:
    commnand = input('bhal-lang > ')
    if commnand.strip() == "":
        continue
    result, error = basic.run("input file", commnand)
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
