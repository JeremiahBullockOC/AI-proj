import clingo
from config import *
import copy

def on_model(model, locations):
    for atom in model.symbols(atoms=True):
        print(atom)

        if atom.name == 'q':
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
        program += f'row({i}).'
    program += '\n'
    for i in range(n):
        program += f'col({i}).'
    program += '\n'

    program += 'not_q(X, Y) :- not q(X, Y), row(X), col(Y).\n'
    program += 'q(X, Y) :- row(X), col(Y), not not_q(X, Y).\n'
    program += 'not_q(Z, Y) :- q(X, Y), row(X), col(Y), row(Z), X != Z.\n'
    program += 'not_q(X, Z) :- q(X, Y), row(X), col(Y), col(Z), Y != Z.\n'
    program += ':- row(X1), row(X2), col(Y1), col(Y2), X1 < X2, Y1 < Y2, q(X1, Y1), q(X2, Y2), X2 - X1 == Y2 - Y1.\n'
    program += ':- row(X1), row(X2), col(Y1), col(Y2), X1 < X2, Y1 > Y2, q(X1, Y1), q(X2, Y2), X2 - X1 == Y1 - Y2.\n'
    program += 'has_q(X) :- q(X, Y), row(X), col(Y).\n'
    program += ':- row(X), not has_q(X).\n'
    program += ':- q(0,0).\n'

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
        for model in handle:
            final_locations = on_model(model, locations_copy)
            # access the atoms of the model
            atoms = set(model.symbols(atoms=True))
            print("Atoms: {}".format(atoms))

    for row in final_locations:
        for cell in row:
            print(cell, end='')
        print()

    return locations_copy