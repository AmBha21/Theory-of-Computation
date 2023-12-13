from graphviz import Digraph
from disjoint_set import DisjointSet

dfa = {}
reachable_states = []
split_needed = None
dis_set = None

def reachable_dfs(node, dfa, reachable_states):
    for start, inp, end in dfa['transition_function']:
        if start == node and end not in reachable_states:
            reachable_states.append(end)
            reachable_dfs(end, dfa, reachable_states)

def remove_unreachable_states(dfa):
    reachable_states = []
    for st in dfa['start_states']:
        if st not in reachable_states:
            reachable_states.append(st)
            reachable_dfs(st, dfa, reachable_states)

    dfa['states'] = [state for state in dfa['states'] if state in reachable_states]
    dfa['final_states'] = [state for state in dfa['final_states'] if state in reachable_states]
    dfa['transition_function'] = [val for val in dfa['transition_function'] if val[0] in reachable_states]

def get_to_state(start, inp, dfa):
    for val in dfa['transition_function']:
        if start == val[0] and inp == val[1]:
            return val[2]
    return None

def minimiseDFA(dfa):
    remove_unreachable_states(dfa)
    split_needed = True
    sorted_states = sorted(dfa['states'])
    group = {(st1, st2): (st1 in dfa['final_states']) == (st2 in dfa['final_states']) 
             for i, st1 in enumerate(sorted_states) 
             for st2 in sorted_states[i+1:]}

    while split_needed:
        split_needed = False
        for i, st1 in enumerate(sorted_states):
            for st2 in sorted_states[i+1:]:
                if not group[(st1, st2)]:
                    continue
                for letter in dfa['letters']:
                    to1 = get_to_state(st1, letter, dfa)
                    to2 = get_to_state(st2, letter, dfa)
                    if to1 and to2 and to1 != to2:
                        is_same_grp = group[(min(to1, to2), max(to1, to2))]
                        split_needed = split_needed or not is_same_grp
                        group[(st1, st2)] = is_same_grp
                        if not is_same_grp:
                            break

    dis_set = DisjointSet(dfa['states'])
    for st_pair, is_same_grp in group.items():
        if is_same_grp:
            dis_set.union(st_pair[0], st_pair[1])

    dfa_new_states = []
    for state in dfa['states']:
        new = dis_set.find(state)
        new_state = "_".join(sorted(new))  # Convert list of states to string immediately
        if new_state not in dfa_new_states:
            dfa_new_states.append(new_state)
    dfa['states'] = dfa_new_states

    dfa_new_transition = []
    for val in dfa['transition_function']:
        start, inp, end = val
        new_state1 = dis_set.find(start)
        new_state2 = dis_set.find(end)
        transition = [new_state1[0], inp, new_state2[0]]
        if transition not in dfa_new_transition:
            dfa_new_transition.append(transition)
    dfa['transition_function'] = dfa_new_transition

    final_states = []
    for fi_state in dfa['final_states']:
        fi_set = dis_set.find(fi_state)
        # Add only the representative state of the equivalence class to the final states
        rep_state = fi_set[0]  # The representative state is the first element
        if rep_state not in final_states:
            final_states.append(rep_state)
    dfa['final_states'] = final_states
    

    start_states = []
    for st_state in dfa['start_states']:
        st_set = dis_set.find(st_state)
        if st_set not in start_states:
            start_states.append(st_set[0])
    dfa['start_states'] = start_states

    return dfa

def output_dfa_to_graphviz(dfa, filename='dfa_graph'):
    dot = Digraph(comment='The Minimized DFA')

    # Add states to the graph
    for state in dfa['states']:
        # Apply styling based on whether a state is final or not
        if state in dfa['final_states']:
            dot.node(state, state, shape='doublecircle')  # Final state
        else:
            dot.node(state, state, shape='circle')  # Normal state

    # Add transitions to the graph
    for start, input_char, end in dfa['transition_function']:
        dot.edge(start, end, label=input_char)

    # Open the rendered PNG directly without saving the dot file
    dot.format = 'png'
    dot.render(filename, cleanup=True)  # cleanup=True will remove the intermediary files

    return dot



def update_transition_function(dfa):
    # Create a mapping from old state names to the merged state names
    state_mapping = {state: state for state in dfa['states']}

    for state in dfa['states']:
        if '_' in state:
            # If the state is a merged state, split and map each individual state to the merged state
            for substate in state.split('_'):
                state_mapping[substate] = state
        else:
            # If the state is not a merged state, it maps to itself
            state_mapping[state] = state

    # Update the transition function using the state_mapping
    updated_transition_function = []
    for start, input_char, end in dfa['transition_function']:
        # Use the merged state name if it exists, otherwise the original
        new_start = state_mapping.get(start, start)
        new_end = state_mapping.get(end, end)
        updated_transition_function.append([new_start, input_char, new_end])

    return updated_transition_function


# Call the function with the example DFA
if __name__ == "__main__":
    dfa = {
    "states": ["a", "b", "c", "d", "e", "f"],
    "letters": ["0", "1"],
    "transition_function": [
        ["a", "0", "b"],
        ["a", "1", "c"],
        ["b", "0", "a"],
        ["b", "1", "d"],
        ["c", "0", "e"],
        ["c", "1", "f"],
        ["d", "0", "e"],
        ["d", "1", "f"],
        ["e", "0", "e"],
        ["e", "1", "f"],
        ["f", "0", "f"],
        ["f", "1", "f"]
    ],
    "start_states": ["a"],
    "final_states": ["c", "d", "e"]
}
    
    
    # dfa from hw2
#     dfa = dfa = {
#     "states": ["0", "1", "2", "3", "4", "5", "6"],
#     "letters": ["a", "b", "c"],
#     "transition_function": [
#         ["0", "a", "1"],
#         ["0", "c", "0"],
#         ["0", "b", "6"],
#         ["1", "a", "2"],
#         ["1", "b", "3"],
#         ["1", "c", "4"],
#         ["2", "a", "3"],
#         ["2", "b", "5"],
#         ["2", "c", "5"],
#         ["3", "a", "4"],
#         ["3", "b", "5"],
#         ["3", "c", "6"],
#         ["4", "a", "2"],
#         ["4", "b", "5"],
#         ["4", "c", "6"],
#         ["5", "a", "5"],
#         ["5", "b", "5"],
#         ["5", "c", "6"],
#         ["6", "a", "6"],
#         ["6", "b", "6"],
#         ["6", "c", "6"]
#     ],
#     "start_states": ["0"],
#     "final_states": ["5", "6"]
# }

    minimized_dfa = minimiseDFA(dfa)
    # After minimization, before calling output_dfa_to_graphviz


    minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)
    # output_dfa_to_graphviz(minimized_dfa, 'minimized_dfa_graph')
    print("Minimized DFA:", minimized_dfa)