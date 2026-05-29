import basic

while True:
    command = input('bhal-lang > ')
    if command.strip() == "":
        continue
    result, error = basic.run("input file", command)
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
