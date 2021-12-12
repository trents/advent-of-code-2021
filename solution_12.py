''' Advent of Code 2021 Day 12 solution '''

def count_paths(path, neighbors):
    """ Solves 12a by counting paths through the graph """    
    return_value = 0
    if path[-1] == 'end':
        return_value = 1
    else: 
        for neighbor in neighbors[path[-1]]:
            if neighbor[0].isupper() or neighbor not in path:
                return_value += count_paths(path+[neighbor], neighbors)
    return return_value

def count_paths_doubler(path, neighbors):
    """ Solves 12b by counting paths through the graph in a different way """
    return_value = 0
    if path[-1] == 'end':
        return_value = 1
    else:
        for neighbor in neighbors[path[-1]]:
            if neighbor[0].isupper() or neighbor not in path:
                return_value += count_paths_doubler(path + [neighbor], neighbors)
            if neighbor[0].islower() and neighbor in path and neighbor != "start":
                return_value += count_paths(path + [neighbor], neighbors)
    return return_value

def main():
    """ driver for solution to puzzle """
    with open('12.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    edges = []
    for item in lines:
        edges.append(item.split("-"))

    nodes = set().union(*edges)

    # single hardest bit in the program ...
    # This creates a dict of node:set values, where the set contains all of the other nodes node is a neighbor to
    # spent way too long on this

    neighbors = {node:(set().union(*[edge for edge in edges if node in edge]) - {node}) for node in nodes}

    # Passing the full path to each recursive call of count_paths and count_path_neighbors
    # was essential for debugging

    print("12a ->",count_paths(["start"],neighbors))
    print("12b ->",count_paths_doubler(["start"],neighbors))

if __name__ == "__main__":
    main()
