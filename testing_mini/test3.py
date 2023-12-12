def remove_unreachable_states(dfa):
    # Convert start states to tuples
    reachable = set(tuple(state) for state in dfa['start_states'])
    new_transitions = []

    for start, letter, end in dfa['transition_function']:
        start_tuple = tuple(start)
        end_tuple = tuple(end)
        if start_tuple in reachable:
            new_transitions.append((start, letter, end))
            reachable.add(end_tuple)

    # Update the states and final states
    dfa['states'] = [state for state in dfa['states'] if tuple(state) in reachable]
    dfa['transition_function'] = new_transitions
    dfa['final_states'] = [state for state in dfa['final_states'] if tuple(state) in reachable]

def partition_states(dfa):
    # Convert states and final states to sets of tuples
    final_states_set = set(tuple(state) for state in dfa['final_states'])
    states_set = set(tuple(state) for state in dfa['states'])

    P = [final_states_set, states_set - final_states_set]
    W = [final_states_set.copy()]

    while W:
        A = W.pop()
        for c in dfa['letters']:
            X = set()
            for start, letter, end in dfa['transition_function']:
                start_tuple = tuple(start)
                end_tuple = tuple(end)
                if letter == c and any(end_state in A for end_state in map(tuple, end)):
                    X.add(start_tuple)

            for Y in P[:]:
                if Y & X and Y - X:
                    P.remove(Y)
                    P.append(Y & X)
                    P.append(Y - X)
                    if Y in W:
                        W.remove(Y)
                        W.append(Y & X)
                        W.append(Y - X)
                    else:
                        W.append(Y & X if len(Y & X) <= len(Y - X) else Y - X)

    return [list(map(list, part)) for part in P]  # Convert tuples back to lists

# ... rest of the code for minimize_dfa and main ...

def minimize_dfa(dfa):
    remove_unreachable_states(dfa)

    partitions = partition_states(dfa)

    # Flatten each partition's states into a single string
    new_states = ["_".join(sorted("_".join(state) for state in part)) for part in partitions]

    # Update final states and start state based on new partitions
    new_final_states = set()
    for part in partitions:
        part_string = "_".join(sorted("_".join(state) for state in part))
        if any(state in dfa['final_states'] for state in part):
            new_final_states.add(part_string)
    
    # Determine the new start state
    new_start_state = "_".join(sorted("_".join(state) for state in next(part for part in partitions if dfa['start_states'][0] in part)))

    # Update the transition function
    new_transitions = []
    for part in partitions:
        part_string = "_".join(sorted("_".join(state) for state in part))
        representative = next(iter(part))
        for letter in dfa['letters']:
            end_state = next((end for start, sym, end in dfa['transition_function'] if start == representative and sym == letter), None)
            if end_state is not None:
                end_part_string = "_".join(sorted("_".join(state) for state in next(p for p in partitions if end_state[0] in p)))
                new_transitions.append((part_string, letter, end_part_string))

    return {
        'states': new_states,
        'letters': dfa['letters'],
        'transition_function': new_transitions,
        'start_states': [new_start_state],
        'final_states': list(new_final_states)
    }


# Example usage
if __name__ == "__main__":
    # Assume 'dfa' is the output from your NFA to DFA conversion
    dfa = {'states': [['Q1', 'Q2', 'Q3', 'Q6', 'Q7', 'Q5'], ['Q4', 'Q8', 'Q9', 'Q5'], ['Q10', 'Q6', 'Q7', 'Q5'], ['Q8', 'Q9']], 'letters': ['a', 'b'], 'transition_function': [(['Q1', 'Q2', 'Q3', 'Q6', 'Q7', 'Q5'], 'a', ['Q4', 'Q8', 'Q9', 'Q5']), (['Q4', 'Q8', 'Q9', 'Q5'], 'b', ['Q10', 'Q6', 'Q7', 'Q5']), (['Q10', 'Q6', 'Q7', 'Q5'], 'a', ['Q8', 'Q9']), (['Q8', 'Q9'], 'b', ['Q10', 'Q6', 'Q7', 'Q5'])], 'start_states': [['Q1', 'Q2', 'Q3', 'Q6', 'Q7', 'Q5']], 'final_states': [['Q1', 'Q2', 'Q3', 'Q6', 'Q7', 'Q5'], ['Q4', 'Q8', 'Q9', 'Q5'], ['Q10', 'Q6', 'Q7', 'Q5']]}

    minimized_dfa = minimize_dfa(dfa)
    print(minimized_dfa)
