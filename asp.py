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

def solve_nqueens(locations):
    n = len(locations[0])
    control = clingo.Control()

    # Define the N-Queens program
    program = ''

    for i in range(n):
        program += f'row({i}). '
    program += '\n'
    for i in range(n):
        program += f'col({i}). '
    program += '\n'
    for x_index in range(n):
        for y_index in range(n):
            if(locations[x_index][y_index] != 0):
                program += f'illegal_location({x_index},{y_index}). '
    program += '\n'
    program += 'pit(X, Y) :- row(X), col(Y), illegal_location(X, Y).\n'
    program += 'has_pit(X) :- pit(X, Y), row(X), col(Y).\n'
    program += ':- row(X), not has_pit(X).\n'
    # program += ':- q(0,0).\n'
    # program += 'not_q(X, Y) :- not q(X, Y), row(X), col(Y).\n'
    # program += 'q(X, Y):- row(X), col(Y), not not_q(X, Y), not illegal_location(X, Y).\n'
    # program += 'has_q(X) :- q(X, Y), row(X), col(Y).\n'
    # program += ':- row(X), not has_q(X).\n'
    # program += ':- q(X, Y), q(X, Y+1).\n'
    # program += ':- q(X, Y), q(X+1, Y+1).\n'
    # program += ':- q(X, Y), q(X+1, Y).\n'
    # program += ':- q(X, Y), q(X+1, Y-1).\n'
    # program += ':- q(X, Y), q(X, Y-1).\n'
    # program += ':- q(X, Y), q(X-1, Y-1).\n'
    # program += ':- q(X, Y), q(X-1, Y).\n'
    # program += ':- q(X, Y), q(X-1, Y+1).\n'

   
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
    with control.solve(yield_=True) as handle:
        print('Starting model call')
        for model in handle:
            final_locations = on_model(model, locations_copy)

    # for row in final_locations:
    #     for cell in row:
    #         print(cell, end='')
    #     print()

    return locations_copy

