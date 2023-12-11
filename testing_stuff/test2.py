import json
import sys
from graphviz import Digraph

def epsilon_closure(states, transition_function):
    closure = states.copy()
    stack = states.copy()

    while stack:
        state = stack.pop()
        for start, symbol, end in transition_function:
            if start == state and symbol == '$' and end not in closure:
                closure.append(end)
                stack.append(end)

    return closure

def move(states, symbol, transition_function):
    next_states = []
    for state in states:
        for start, sym, end in transition_function:
            if start == state and sym == symbol and end not in next_states:
                next_states.append(end)
    return next_states

def compute_dfa(nfa):
    dfa = {
        'states': [],
        'letters': [sym for sym in nfa['letters'] if sym != '$'],  # Exclude epsilon
        'transition_function': [],
        'start_states': [],
        'final_states': []
    }

    start_state_closure = epsilon_closure(nfa['start_states'], nfa['transition_function'])
    unprocessed = [start_state_closure]
    dfa['start_states'] = [start_state_closure]

    while unprocessed:
        current = unprocessed.pop()
        if current not in dfa['states']:
            dfa['states'].append(current)

        for letter in dfa['letters']:
            next_state_closure = epsilon_closure(move(current, letter, nfa['transition_function']), nfa['transition_function'])

            if next_state_closure and next_state_closure not in dfa['states']:
                unprocessed.append(next_state_closure)

            if next_state_closure:
                dfa['transition_function'].append((current, letter, next_state_closure))

    for state in dfa['states']:
        if any(s in nfa['final_states'] for s in state):
            dfa['final_states'].append(state)

    return dfa

# Rest of the code remains the same


def create_dfa_graph(dfa):
    graph = Digraph('finite_state_machine')
    graph.attr(rankdir='LR', size='8,5')

    for state in dfa['states']:
        state_name = '_'.join(state)
        if state in dfa['start_states']:
            # Highlight start states with a different color and a label
            graph.node(state_name, shape='circle', color='blue', style='filled', fillcolor='lightblue')
            graph.node("start_" + state_name, label="start", shape="plaintext")
            graph.edge("start_" + state_name, state_name, style="dashed")
        elif state in dfa['final_states']:
            graph.node(state_name, shape='doublecircle')
        else:
            graph.node(state_name)

    for start, letter, end in dfa['transition_function']:
        graph.edge('_'.join(start), '_'.join(end), label=letter)

    graph.view()


if __name__ == "__main__":
    nfa = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10'], 'letters': ['$', 'a', 'b'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', 'a', 'Q4'], ['Q4', '$', 'Q5'], ['Q3', '$', 'Q6'], ['Q3', '$', 'Q7'], ['Q6', 'a', 'Q8'], ['Q8', '$', 'Q9'], ['Q9', 'b', 'Q10'], ['Q10', '$', 'Q6'], ['Q10', '$', 'Q7'], ['Q7', '$', 'Q5']], 'start_states': ['Q1'], 'final_states': ['Q5']}

    dfa = compute_dfa(nfa)
    print(dfa)
    create_dfa_graph(dfa)
