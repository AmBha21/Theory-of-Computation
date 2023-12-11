from graphviz import Digraph
from pyUnit import *

# purely for testing purposes i am recreating the nfa datatype
class NFA:
    def __init__(self, nfa_dict=None):
        if nfa_dict is None:
            nfa_dict = {
                'states': [],
                'letters': [],
                'transition_function': [],
                'start_states': [],
                'final_states': []
            }
        self.nfa = nfa_dict

    def set_nfa(self, nfa_dict: dict):
        self.nfa = nfa_dict

    def nfa_to_graph(self, filename):
        dot = Digraph(comment='NFA', format='png')

        # Add states
        dot.attr('node', shape='circle')
        for state in self.nfa['states']:
            if state in self.nfa['final_states']:
                dot.attr('node', shape='doublecircle')
            dot.node(state)
            dot.attr('node', shape='circle')

        # Add transitions
        for start_state, input_symbol, end_state in self.nfa['transition_function']:
            if input_symbol == '$':  # Handling epsilon transitions
                input_symbol = 'ε'
            dot.edge(start_state, end_state, label=input_symbol)

        dot.render(filename, format='png', cleanup=True)


def epsilon_closure(states, transition_function):
    closure = set(states)
    stack = list(states)

    while stack:
        state = stack.pop()
        for start, symbol, end in transition_function:
            if start == state and symbol == '$' and end not in closure:
                closure.add(end)
                stack.append(end)

    return closure


def move(states, symbol, transition_function):
    next_states = set()
    for state in states:
        for start, sym, end in transition_function:
            if start == state and sym == symbol:
                next_states.add(end)
    return next_states


def compute_dfa(nfa):
    dfa = {
        'states': [],
        # Exclude epsilon
        'letters': [sym for sym in nfa['letters'] if sym != '$'],
        'transition_function': [],
        'start_states': [],
        'final_states': []
    }

    start_state_closure = epsilon_closure(
        nfa['start_states'], nfa['transition_function'])
    unprocessed = [start_state_closure]
    dfa['start_states'] = [start_state_closure]

    while unprocessed:
        current = unprocessed.pop()
        dfa['states'].append(current)

        for letter in dfa['letters']:
            next_state_closure = epsilon_closure(
                move(current, letter, nfa['transition_function']), nfa['transition_function'])

            if next_state_closure:
                if next_state_closure not in dfa['states']:
                    unprocessed.append(next_state_closure)

                dfa['transition_function'].append(
                    (current, letter, next_state_closure))

    for state in dfa['states']:
        if any(s in nfa['final_states'] for s in state):
            dfa['final_states'].append(state)

    return dfa


def create_dfa_graph(dfa, filename):
    graph = Digraph('finite_state_machine')
    graph.attr(rankdir='LR', size='8,5')

    # Add nodes for states
    for state in dfa['states']:
        state_name = '_'.join(state) if state else 'Ø'
        if state in dfa['final_states']:
            graph.attr('node', shape='doublecircle')
        else:
            graph.attr('node', shape='circle')

        if state_name in map(lambda s: '_'.join(s), dfa['start_states']):
            # Special style for start states (e.g., blue color)
            graph.node(state_name, style='filled', color='lightblue')
        else:
            graph.node(state_name)

    # Add edges for transitions
    for transition in dfa['transition_function']:
        start, letter, end = transition
        start_name = '_'.join(start) if start else 'Ø'
        end_name = '_'.join(end) if end else 'Ø'
        graph.edge(start_name, end_name, label=letter)

    # Save the graph to a file
    graph.render(filename, format='png', cleanup=True)


if __name__ == "__main__":
    # testing dfa for regex ab*
    _nfa = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'], 'letters': ['a', '$', 'b'], 'transition_function': [['Q1', 'a', 'Q2'], ['Q2', '$', 'Q3'], ['Q3', '$', 'Q4'], ['Q3', '$', 'Q5'], ['Q4', 'b', 'Q6'], ['Q6', '$', 'Q4'], ['Q6', '$', 'Q5']], 'start_states': ['Q1'], 'final_states': ['Q5']}
    nfa = NFA()
    nfa.set_nfa(_nfa)
    dfa = compute_dfa(nfa.nfa)
    expected = {'states': [{'Q1'}, {'Q4', 'Q3', 'Q5', 'Q2'}, {'Q4', 'Q6', 'Q5'}], 'letters': ['a', 'b'], 'transition_function': [({'Q1'}, 'a', {'Q4', 'Q3', 'Q5', 'Q2'}), ({'Q4', 'Q3', 'Q5', 'Q2'}, 'b', {'Q4', 'Q6', 'Q5'}), ({'Q4', 'Q6', 'Q5'}, 'b', {'Q4', 'Q6', 'Q5'})], 'start_states': [{'Q1'}], 'final_states': [{'Q4', 'Q3', 'Q5', 'Q2'}, {'Q4', 'Q6', 'Q5'}]}
    run_test(dfa, expected, 'dfa4')
    if display_graph('dfa4'):
        create_dfa_graph(dfa, 'dfa4')