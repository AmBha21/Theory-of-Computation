# Conversion from NFA to DFA
import json
import sys
from graphviz import Digraph

dfa = {}
nfa = {}
nfa_states = []
dfa_states = []

def create_dfa_graph(dfa):
    graph = Digraph('finite_state_machine')
    graph.attr(rankdir='LR', size='8,5')

    # Add nodes for states
    for state in dfa['states']:
        state_name = '_'.join(state) if state else 'Ø'
        if state in dfa['final_states']:
            graph.attr('node', shape='doublecircle')
        else:
            graph.attr('node', shape='circle')
        graph.node(state_name)

    # Add edges for transitions
    for transition in dfa['transition_function']:
        start, letter, end = transition
        start_name = '_'.join(start) if start else 'Ø'
        end_name = '_'.join(end) if end else 'Ø'
        graph.edge(start_name, end_name, label=letter)

    # Display the graph
    graph.view()

def get_power_set(nfa_st):
    powerset = [[]]
    for i in nfa_st:
        for sub in powerset:
            powerset = powerset + [list(sub) + [i]]
    return powerset

def load_nfa():
    global nfa
    with open(sys.argv[1], 'r') as inpjson:
        nfa = json.loads(inpjson.read())

def out_dfa():
    global dfa
    with open(sys.argv[2], 'w') as outjson:
        outjson.write(json.dumps(dfa, indent = 4))

if __name__ == "__main__":
    nfa = {
    "states": [
        "Q0",
        "Q1",
        "Q2"
    ],
    "letters": [
        "0",
        "1"
    ],
    "transition_function": [
        [
            "Q0",
            "0",
            "Q0"
        ],
        [
            "Q0",
            "1",
            "Q1"
        ],
        [
            "Q1",
            "0",
            "Q0"
        ],
        [
            "Q1",
            "1",
            "Q1"
        ],
        [
            "Q1",
            "0",
            "Q2"
        ],
        [
            "Q2",
            "0",
            "Q2"
        ],
        [
            "Q2",
            "1",
            "Q2"
        ],
        [
            "Q2",
            "1",
            "Q1"
        ]
    ],
    "start_states": [
        "Q0"
    ],
    "final_states": [
        "Q2"
    ]
}
    
    dfa['states'] = []
    dfa['letters'] = nfa['letters']
    dfa['transition_function'] = []
    
    for state in nfa['states']:
        nfa_states.append(state)

    dfa_states = get_power_set(nfa_states)


    dfa['states'] = []
    for states in dfa_states:
        temp = []
        for state in states:
            temp.append(state)
        dfa['states'].append(temp)

    for states in dfa_states:
        for letter in nfa['letters']:
            q_to = []
            for state in states:
                for val in nfa['transition_function']:
                    start = val[0]
                    inp = val[1]
                    end = val[2]
                    if state == start and letter == inp:
                        if end not in q_to:
                            q_to.append(end)
            q_states = []
            for i in states:
                q_states.append(i)
            dfa['transition_function'].append([q_states, letter, q_to])

    dfa['start_states'] = []
    for state in nfa['start_states']:
        dfa['start_states'].append([state])
    dfa['final_states'] = []
    for states in dfa['states']:
        for state in states:
            if state in nfa['final_states'] and states not in dfa['final_states']:
                dfa['final_states'].append(states)
    
    create_dfa_graph(dfa)
