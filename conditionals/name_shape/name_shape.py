
shapes = ['Invalid number of sides', 'Invalid number of sides', 'Invalid number of sides', 'Triangle', 'Quadrilateral',
'Pentagon', 'Hexagon', 'Heptagon', 'Octagon', 'Nonagon', 'Decagon']

n = int(input())

if n > 10 or n < 0:
    print('Invalid number of sides')
else:
    print(shapes[n])