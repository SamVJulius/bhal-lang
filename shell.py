import basic

while True:
    commnand = input('bhal-lang > ')
    result, error = basic.run("input file", commnand)
    if error:
        print(error.as_string())
    else:
        print(result)