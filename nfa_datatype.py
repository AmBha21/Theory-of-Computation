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
            dot.attr('node', shape='circle')

        # Add transitions
        for start_state, input_symbol, end_state in self.nfa['transition_function']:
            if input_symbol == '$':  # Handling epsilon transitions
                input_symbol = 'ε'
            dot.edge(start_state, end_state, label=input_symbol)

        dot.render(filename, format='png', cleanup=True)



    # def to_dot(self):
    #     dot_str = 'digraph NFA {\n'
    #     dot_str += '    rankdir=LR;\n'
    #     dot_str += '    node [shape = doublecircle]; ' + ' '.join(str(s) for s in self.accept_states) + ';\n'
    #     dot_str += '    node [shape = circle];\n'

    #     for state, node in self.states.items():
    #         for symbol, destinations in node.transitions.items():
    #             for dest in destinations:
    #                 dot_str += f'    {state} -> {dest} [label="{symbol}"];\n'
    #         for dest in node.epsilon_transitions:
    #             dot_str += f'    {state} -> {dest} [label="ε"];\n'

    #     dot_str += '}'
    #     return dot_str

    # def generate_graphviz_file(self, filename):
    #     with open(filename, 'w') as file:
    #         file.write(self.to_dot())
    #     print(f"GraphViz file generated: {filename}")

    # def render_graph(self, filename='nfa'):
    #     dot = Digraph()

    #     for state in self.states:
    #         if state in self.accept_states:
    #             dot.node(str(state), shape='doublecircle')
    #         else:
    #             dot.node(str(state), shape='circle')

    #     for state, node in self.states.items():
    #         for symbol, destinations in node.transitions.items():
    #             for dest in destinations:
    #                 dot.edge(str(state), str(dest), label=symbol)
    #         for dest in node.epsilon_transitions:
    #             dot.edge(str(state), str(dest), label='ε')

    #     dot.render(filename, format='png', cleanup=True)
    #     print(f"Graph rendered and saved as {filename}.png")