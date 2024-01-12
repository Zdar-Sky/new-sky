print('1 - Comedy')
print('2 - Fantasy')
print('3 - Horror')
genre = int(input('What genre are you interested in? '))
match genre:
    case 1 | 2:
        print('One house')
    case 2:
        print('Guardians of the galaxy')
    case 3:
        print('Astral')
    case 4:
        print('no')