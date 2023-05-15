from heapq import heappop, heappush

# Define the heuristic function

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Define the A* path planning function

def astar(maze, start, goal):
    # Initialize the open list and the closed list
    open_list = []
    closed_list = set()
    # Add the starting node to the open list
    heappush(open_list, (0, start))

    # Initialize the cost and came_from dictionaries
    cost = {start: 0}
    came_from = {}

    # Loop through the open list
    while open_list:
        # Get the node with the lowest cost
        current_cost, current_node = heappop(open_list)

        # Check if we've reached the goal node
        if current_node == goal:
            # Reconstruct the path
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path

        # Add the current node to the closed list
        closed_list.add(current_node)

        # Loop through the neighbors of the current node
        for neighbor in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor_node = (current_node[0] + neighbor[0], current_node[1] + neighbor[1])

            # Check if the neighbor is inside the maze and not in the closed list
            if neighbor_node[0] < 0 or neighbor_node[0] >= len(maze[0]) or neighbor_node[1] < 0 or neighbor_node[1] >= len(maze) or maze[neighbor_node[1]][neighbor_node[0]] == 1 or neighbor_node in closed_list:
                continue

            # Calculate the cost of the neighbor node
            new_cost = cost[current_node] + 1

            # Check if the neighbor is already in the open list or not
            if neighbor_node not in cost or new_cost < cost[neighbor_node]:
                # Update the cost and came_from dictionaries
                cost[neighbor_node] = new_cost
                priority = new_cost + heuristic(goal, neighbor_node)
                heappush(open_list, (priority, neighbor_node))
                came_from[neighbor_node] = current_node

    # If we can't reach the goal node, return None
    return None

def dfs(maze, start, goal):
    # Initialize the stack and the visited set
    stack = [(start, [start])]
    visited = set()

    # Loop through the stack
    while stack:
        current_node, path = stack.pop()

        # Check if we've reached the goal node
        if current_node == goal:
            return path

        # Add the current node to the visited set
        visited.add(current_node)

        # Loop through the neighbors of the current node in reverse order
        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_node = (current_node[0] + neighbor[0], current_node[1] + neighbor[1])

            # Check if the neighbor is inside the maze, not a wall, and not visited
            if (
                neighbor_node[0] >= 0 and neighbor_node[0] < len(maze[0]) and
                neighbor_node[1] >= 0 and neighbor_node[1] < len(maze) and
                maze[neighbor_node[1]][neighbor_node[0]] == 0 and
                neighbor_node not in visited
            ):
                # Push the neighbor node and path to the stack
                stack.append((neighbor_node, path + [neighbor_node]))

    # If we can't reach the goal node, return None
    return None




def ucs(maze, start, goal):
    return

