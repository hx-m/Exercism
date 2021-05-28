def two_fer(name = 'you'):
    if name == 'you':
        return 'One for you, one for me.'
    else:
        return f'One for {name}, one for me.'

two_fer()