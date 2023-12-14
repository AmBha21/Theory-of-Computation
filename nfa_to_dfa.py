# Conversion from NFA to DFA
from graphviz import Digraph

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
        dfa['states'].append(current)

        for letter in dfa['letters']:
            next_state_closure = epsilon_closure(move(current, letter, nfa['transition_function']), nfa['transition_function'])

            if next_state_closure:
                if next_state_closure not in dfa['states']:
                    unprocessed.append(next_state_closure)

                dfa['transition_function'].append((current, letter, next_state_closure))

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