import clingo
from config import *
import copy

def on_model(model, locations):
    print('In on_model')
    for atom in model.symbols(atoms=True):
        print(atom)

        if atom.name == 'pit':
            row = atom.arguments[0].number
            col = atom.arguments[1].number
            locations[row - 1][col - 1] = 2
    return locations

def solve_nqueens(locations, destination):
    # for row in locations:
    #     for cell in row:
    #         print(cell, end='')
    #     print()

    n = len(locations[0])
    control = clingo.Control()

    program = ''

    for i in range(n):
        program += f'row({i+1}). '
    program += '\n'
    for i in range(n):
        program += f'col({i+1}). '
    program += '\n'
    # Programming in walls
    for col in range(n):
        for row in range(n):
            if(locations[row][col] != 0):
                program += f'illegal_location({row+1},{col+1}). '
    #Making maze boundaries into illegal locations
    for index in range(n):
        program += f'illegal_location({0},{index+1}). '
        program += f'illegal_location({n+1},{index+1}). '
        program += f'illegal_location({index+1},{0}). '
        program += f'illegal_location({index+1},{n+1}). '

    program += '\n'
    # Testing
    program += 'not_pit(X, Y) :- not pit(X, Y), row(X), col(Y).\n'
    program += 'pit(X, Y) :- row(X), col(Y), not not_pit(X, Y), not illegal_location(X, Y).\n'
    program += 'has_pit(X) :- pit(X, Y), row(X), col(Y).\n'
    program += ':- row(X), not has_pit(X).\n'
    program += ':- pit(1,1).\n'
    program += f':- pit({destination[1]+1}, {destination[0]+1}).\n'
    program += 'not_block(X,Y) :- not pit(X, Y), not illegal_location(X, Y), row(X), col(Y).\n'
    program += 'block(X, Y) :- row(X), col(Y), not not_block(X, Y).\n'
    program += ':- pit(X,Y), block(X, Y+1), block(X, Y-1).\n'
    program += ':- pit(X,Y), block(X+1, Y), block(X-1, Y).\n'
    program += ':- pit(X,Y), block(X+1, Y+1), block(X-1, Y-1).\n'
    program += ':- pit(X,Y), block(X-1, Y+1), block(X+1, Y-1).\n'
    program += ':- pit(X,Y), block(X-1, Y), block(X+1, Y-1).\n'
    program += ':- pit(X,Y), block(X-1, Y), block(X+1, Y+1).\n'
    program += ':- pit(X,Y), block(X+1, Y), block(X-1, Y-1).\n'
    program += ':- pit(X,Y), block(X+1, Y), block(X-1, Y+1).\n'

    #New
    program += ':- pit(X,Y), block(X, Y-1), block(X-1, Y+1).\n'
    program += ':- pit(X,Y), block(X, Y-1), block(X+1, Y+1).\n'
    program += ':- pit(X,Y), block(X, Y+1), block(X-1, Y-1).\n'
    program += ':- pit(X,Y), block(X, Y+1), block(X+1, Y-1).\n'

    # Below is temporarily working
    # program += ':- pit(X,Y), pit(X+1, Y).\n'
    # program += ':- pit(X,Y), pit(X, Y+1).\n'
    # program += ':- pit(X,Y), pit(X+1, Y+1).\n'
    # program += ':- pit(X,Y), pit(X-1, Y-1).\n'
    # program += ':- pit(X,Y), pit(X+1, Y-1).\n'

    # Good code above

   
    print(program)
    # Create a deep copy of the locations array
    locations_copy = copy.deepcopy(locations)
    control.add("base", [], program)
    control.ground([("base", [])])

    final_locations = []
    # Define the observer function
    def on_model_wrapper(model):
        on_model(model, locations_copy)

    # Register the observer function
    control.register_observer(on_model_wrapper)

    # Solve the program
    try:
        with control.solve(yield_=True) as handle:
            print('Starting model call')
            for model in handle:
                print('In the for loop')
                final_locations = on_model(model, locations_copy)
    except clingo.SolveError as e:
        print('No models found')
        print(e)



    return locations_copy

