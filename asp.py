import clingo
from config import *
import copy


def on_model(model, locations):
    # print('In on_model')
    for atom in model.symbols(atoms=True):
        # print(atom)

        if atom.name == 'pit':
            row = atom.arguments[0].number
            col = atom.arguments[1].number
            locations[row - 1][col - 1] = 2
    return locations

# TODO Add splitting into sub arrays. In this case 4 of them

def handle_pit_creation(locations, destination):
    length = len(locations[0])

    if length == 10:
        return create_pits(locations, destination)
    else:
        upperLeft = [[0 for _ in range(10)] for _ in range(10)]
        upperRight = [[0 for _ in range(10)] for _ in range(10)]
        lowerLeft = [[0 for _ in range(10)] for _ in range(10)]
        lowerRight = [[0 for _ in range(10)] for _ in range(10)]

        for col in range(length):
            for row in range(length):
                if(col < 10):
                    if(row < 10):
                        upperLeft[col % 10][row % 10] = locations[col][row]
                    else:
                        lowerLeft[col % 10][row % 10] = locations[col][row]
                else:
                    if(row < 10):
                        upperRight[col % 10][row % 10] = locations[col][row]
                    else:
                        lowerRight[col % 10][row % 10] = locations[col][row]

        modifiedDestination = (destination[0]%10, destination[1]%10)
        # print(str(destination))
        # print(str(modifiedDestination))
        if(destination[0] < 10):
            if(destination[1] < 10):
                    upperLeft = create_pits(upperLeft, modifiedDestination)
                    upperRight = create_pits(upperRight, None)
                    lowerLeft = create_pits(lowerLeft, None)
                    lowerRight = create_pits(lowerRight, None)
            else:
                upperLeft = create_pits(upperLeft, None)
                upperRight = create_pits(upperRight, None)
                lowerLeft = create_pits(lowerLeft, modifiedDestination)
                lowerRight = create_pits(lowerRight, None)
        else:
            if(destination[1] < 10):
                upperLeft = create_pits(upperLeft, None)
                upperRight = create_pits(upperRight, modifiedDestination)
                lowerLeft = create_pits(lowerLeft, None)
                lowerRight = create_pits(lowerRight, None)
            else:
                upperLeft = create_pits(upperLeft, None)
                upperRight = create_pits(upperRight, None)
                lowerLeft = create_pits(lowerLeft, None)
                lowerRight = create_pits(lowerRight, modifiedDestination)


        updatedArray = [[0 for _ in range(20)] for _ in range(20)]

        for col in range(length):
            for row in range(length):
                if(col < 10):
                    if(row < 10):
                        updatedArray[col][row] = upperLeft[col % 10][row % 10]
                    else:
                        updatedArray[col][row] = lowerLeft[col % 10][row % 10]
                else:
                    if(row < 10):
                        updatedArray[col][row] = upperRight[col % 10][row % 10]
                    else:
                        updatedArray[col][row] = lowerRight[col % 10][row % 10]
        return updatedArray



def create_pits(locations, destination):

    if(destination is None):
        destination = (0,0)
    n = len(locations[0])
    control = clingo.Control()

    # print('The n used is: ' + str(n))

    program = ''

    #Defining the rows and cols in the maze
    for i in range(n):
        program += f'row({i+1}). '
    program += '\n'
    for i in range(n):
        program += f'col({i+1}). '
    program += '\n'

    # Programming in maze walls
    for col in range(n):
        for row in range(n):
            if(locations[row][col] != 0):
                program += f'illegal_location({row+1},{col+1}). '

    #Making maze boundaries into illegal locations
    program += f'illegal_location({0},{0}). '
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
    program += 'not_block(X,Y) :- not pit(X, Y), not illegal_location(X, Y), not block(X, Y), row(X), col(Y).\n'
    program += 'block(X, Y) :- row(X), col(Y), not not_block(X, Y).\n'

    # Handles having 3 blocking cells in a line
    # Vertical and horizontal
    program += ':- pit(X,Y), block(X, Y+1), block(X, Y-1).\n'
    program += ':- pit(X,Y), block(X+1, Y), block(X-1, Y).\n'
    # Diagonal
    program += ':- pit(X,Y), block(X+1, Y+1), block(X-1, Y-1).\n'
    program += ':- pit(X,Y), block(X-1, Y+1), block(X+1, Y-1).\n'

    # Handles 3 disjoint cells that still block
    program += ':- pit(X,Y), block(X-1, Y), block(X+1, Y-1).\n'
    program += ':- pit(X,Y), block(X-1, Y), block(X+1, Y+1).\n'
    program += ':- pit(X,Y), block(X+1, Y), block(X-1, Y-1).\n'
    program += ':- pit(X,Y), block(X+1, Y), block(X-1, Y+1).\n'
    program += ':- pit(X,Y), block(X, Y-1), block(X-1, Y+1).\n'
    program += ':- pit(X,Y), block(X, Y-1), block(X+1, Y+1).\n'
    program += ':- pit(X,Y), block(X, Y+1), block(X-1, Y-1).\n'
    program += ':- pit(X,Y), block(X, Y+1), block(X+1, Y-1).\n'
   
    #TODO: Try subdividing into size that is 10x10 or less.

    # print(program)
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
            for model in handle:
                # print('In the for loop')
                final_locations = on_model(model, locations_copy)
            # print('Starting model call')
            # print('Exhausted: ' + str(handle.get().exhausted))
            # print('Interrupted: ' + str(handle.get().interrupted))
            # print('Unknown: ' + str(handle.get().unknown))
            # print('Satisfiable: ' + str(handle.get().satisfiable))
    except clingo.SolveError as e:
        print('No models found')
        print(e)



    return locations_copy

