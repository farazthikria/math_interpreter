import juffy

while True:
    text = input('juffy > ')
    result, error = juffy.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)