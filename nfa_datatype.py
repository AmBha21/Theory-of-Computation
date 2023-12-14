from graphviz import Digraph


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

    def set_nfa(self, nfa_dict : dict):
        self.nfa = nfa_dict

    def nfa_to_graph(self, filename):
        dot = Digraph(comment='NFA', format='png')

        # Add states
        dot.attr('node', shape='circle')
        for state in self.nfa['states']:
            if state in self.nfa['final_states']:
                dot.attr('node', shape='doublecircle')
            dot.node(state)

        # Add transitions
        for start_state, input_symbol, end_state in self.nfa['transition_function']:
            if input_symbol == '$':  # Handling epsilon transitions
                input_symbol = 'ε'
            dot.edge(start_state, end_state, label=input_symbol)

        dot.render(filename, format='png', cleanup=True)