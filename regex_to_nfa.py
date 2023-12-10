from parse import parse
from fsm import *
from nfa_datatype import NFA
from charclass import DOT

# Simple regular expression
regex = r'a*|b|c*'

# Parse the regular expression
parsed_regex = parse(regex)

# Convert to FSM
fsm = parsed_regex.to_fsm()

def fsm_to_nfa(fsm: Fsm) -> NFA:
    nfa = NFA()

    # Add states
    for state in fsm.states:
        nfa.add_state(state)

    # Set start and accept states
    nfa.set_start_state(fsm.initial)
    for final_state in fsm.finals:
        nfa.add_accept_state(final_state)

    # Add transitions
    for state, transitions in fsm.map.items():
        for charclass, dest_state in transitions.items():
            if charclass == DOT:  # DOT represents all characters
                label = 'ALL'  # This label can be changed as needed
            else:
                # Convert Charclass to a readable format (or handle it as needed)
                label = str(charclass)  # This is a simplification
            nfa.add_transition(state, label, dest_state)

    return nfa

# Convert the parsed FSM to NFA
nfa = fsm_to_nfa(fsm)

# Now you can generate the Graphviz file or render the graph
nfa.generate_graphviz_file('nfa.dot')
# or
nfa.render_graph('nfa_graph')

