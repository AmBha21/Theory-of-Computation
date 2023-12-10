import json
import sys
from graphviz import Digraph

def epsilon_closure(state, transition_function):
    closure = {state}
    states_to_process = [state]
    while states_to_process:
        current_state = states_to_process.pop()
        for transition in transition_function:
            if transition[0] == current_state and transition[1] == '$':
                if transition[2] not in closure:
                    closure.add(transition[2])
                    states_to_process.append(transition[2])
    return closure

def compute_dfa(nfa):
    dfa = {'states': [], 'letters': nfa['letters'], 'transition_function': [], 'start_states': [], 'final_states': []}
    unprocessed_dfa_states = [frozenset(epsilon_closure(nfa['start_states'][0], nfa['transition_function']))]
    dfa['start_states'].append(unprocessed_dfa_states[0])

    while unprocessed_dfa_states:
        current_dfa_state = unprocessed_dfa_states.pop()
        if current_dfa_state not in dfa['states']:
            dfa['states'].append(current_dfa_state)

            for letter in nfa['letters']:
                if letter != '$':  # Skip epsilon
                    new_state = frozenset(
                        state for nfa_state in current_dfa_state
                        for trans in nfa['transition_function']
                        if trans[0] == nfa_state and trans[1] == letter
                        for state in epsilon_closure(trans[2], nfa['transition_function'])
                    )

                    if new_state:
                        dfa['transition_function'].append((current_dfa_state, letter, new_state))
                        if new_state not in dfa['states']:
                            unprocessed_dfa_states.append(new_state)

    # Add final states
    for state in dfa['states']:
        if any(nfa_state in nfa['final_states'] for nfa_state in state):
            dfa['final_states'].append(state)

    return dfa

def create_dfa_graph(dfa, filename):
    graph = Digraph('finite_state_machine', filename=filename)
    graph.attr(rankdir='LR', size='8,5')

    for state in dfa['states']:
        state_name = '_'.join(sorted(state)) if state else 'Ø'
        if state in dfa['final_states']:
            graph.attr('node', shape='doublecircle')
        else:
            graph.attr('node', shape='circle')
        graph.node(state_name)

    for start, letter, end in dfa['transition_function']:
        start_name = '_'.join(sorted(start)) if start else 'Ø'
        end_name = '_'.join(sorted(end)) if end else 'Ø'
        graph.edge(start_name, end_name, label=letter)

    graph.view()

if __name__ == "__main__":
    nfa = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10'], 'letters': ['$', 'a', 'b'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', '$', 'Q4'], ['Q2', '$', 'Q5'], ['Q4', 'a', 'Q6'], ['Q6', '$', 'Q4'], ['Q6', '$', 'Q5'], ['Q5', '$', 'Q7'], ['Q3', 'a', 'Q8'], ['Q8', '$', 'Q9'], ['Q9', 'b', 'Q10'], ['Q10', '$', 'Q7']], 'start_states': ['Q1'], 'final_states': ['Q7']}
    
    dfa = compute_dfa(nfa)
    create_dfa_graph(dfa, 'dfa_graph')
