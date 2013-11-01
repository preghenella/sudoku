import random

coordinates = tuple((i, j, (i / 3) * 3 + j / 3) for j in range(0, 9) for i in range(0, 9))
numbers = set(range(1, 10))

def print_scheme(scheme):
    for i in range(0, 9):
        if i % 3 == 0: print '-' * 25
        for j in range(0, 9):
            if j % 3 == 0: print '|',
            print scheme[(i, j, (i / 3) * 3 + j / 3)],
        print '|'
    print '-' * 25

def get_available(scheme, coo):
    row = {scheme[x] for x in scheme if x[0] == coo[0]}
    col = {scheme[x] for x in scheme if x[1] == coo[1]}
    sqr = {scheme[x] for x in scheme if x[2] == coo[2]}
    return list(numbers - row - col - sqr)

def generate_scheme():
    scheme = {coo : 'X' for coo in coordinates}
    for coo in coordinates:
        available = get_available(scheme, coo)
        if len(available) == 0: return None
        scheme[coo] = random.choice(available)
    return scheme

def empty_scheme(scheme):
    coord = [x for x in scheme if scheme[x] != ' ']
    while len(coord) > 0:
        coo = random.choice(coord)
        X = scheme[coo]
        available = get_available(scheme, coo)
        # check whether any of the available numbers
        # would break the scheme if inserted here
        # at the place of the current number
        for case in available:
            scheme[coo] = case
            empty = [x for x in scheme if scheme[x] == ' ']
            for coo2 in empty:
                if len(get_available(scheme, coo2)) == 0:
                    available.remove(case)
                    break
        # no other numbers but this one is allowed here
        if len(available) == 0:
            scheme[coo] = ' '
        # other numbers are allowed here
        else:
            scheme[coo] = 'X'
            empty_row = {x for x in scheme if scheme[x] == ' ' and x[0] == coo[0]}
            empty_col = {x for x in scheme if scheme[x] == ' ' and x[1] == coo[1]}
            empty_sqr = {x for x in scheme if scheme[x] == ' ' and x[2] == coo[2]}

#            print '*' * 40
#            print X
#            print_scheme(scheme)

            gotrow = True
#            print 'row:'
            for coo2 in empty_row:
#                print coo2, get_available(scheme, coo2)
                if X in get_available(scheme, coo2):
                    gotrow = False
                    break

            gotcol = True
#            print 'col:'
            for coo2 in empty_col:
#                print coo2, get_available(scheme, coo2)
                if X in get_available(scheme, coo2):
                    gotcol = False
                    break

            gotsqr = True
#            print 'sqr:'
            for coo2 in empty_sqr:
#                print coo2, get_available(scheme, coo2)
                if X in get_available(scheme, coo2):
                    gotsqr = False
                    break

            if gotrow or gotcol or gotsqr:
#                print 'gotit'
                scheme[coo] = ' '
            else:
                scheme[coo] = X
                
#            print '*' * 40
        coord.remove(coo)

while True:

    scheme = generate_scheme()
    while scheme == None: scheme = generate_scheme()
    fullscheme = scheme.copy()

    empty_scheme(scheme)
    empty = [x for x in scheme if scheme[x] == ' ']
    
    if len(empty) > 51:
        print_scheme(fullscheme)
        print 'original scheme'
        print_scheme(scheme)
        print 'scheme with', len(empty), 'numbers to be found'
        break
