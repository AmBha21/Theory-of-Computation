def run_test(actual, expected, test_name):
    if actual == expected:
        print("Test " + test_name + " passed")
    else:
        print("Test " + test_name + " failed")
        print("Expected: " + str(expected))
        print("Actual: " + str(actual))

def display_graph(test_name):
    show_graph = input(f'Show graph for test {test_name}? (y/n): ')
    if show_graph.lower() == 'y':
        print("Graph created in " + test_name + ".png")
        return True
    return False