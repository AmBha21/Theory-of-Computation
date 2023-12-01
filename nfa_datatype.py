class StateNode:
    def __init__(self, state_id):
        self.state_id = state_id
        self.transitions = {}
        self.epsilon_transitions = set()

    def add_transition(self, symbol, state):
        if symbol not in self.transitions:
            self.transitions[symbol] = set()
        self.transitions[symbol].add(state)

    def add_epsilon_transition(self, state):
        self.epsilon_transitions.add(state)

class NFA:
    def __init__(self):
        self.states = {}
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state_id):
        if state_id not in self.states:
            self.states[state_id] = StateNode(state_id)

    def set_start_state(self, state_id):
        self.start_state = state_id

    def add_accept_state(self, state_id):
        self.accept_states.add(state_id)

    def add_transition(self, from_state, symbol, to_state):
        self.states[from_state].add_transition(symbol, to_state)

    def add_epsilon_transition(self, from_state, to_state):
        self.states[from_state].add_epsilon_transition(to_state)

    # TODO, maybe additional methods for simulating the NFA, checking input strings, etc.


# def test_nfa_structure():
#     # Create a new NFA instance
#     nfa = NFA()

#     # Add states
#     nfa.add_state(1)
#     nfa.add_state(2)
#     nfa.add_state(3)

#     # Set start state and accept states
#     nfa.set_start_state(1)
#     nfa.add_accept_state(3)

#     # Add transitions
#     nfa.add_transition(1, 'a', 2)
#     nfa.add_transition(2, 'b', 3)

#     # Add epsilon transition
#     nfa.add_epsilon_transition(1, 3)

#     # Check if states and transitions are set up correctly
#     assert nfa.start_state == 1
#     assert 3 in nfa.accept_states
#     assert 'a' in nfa.states[1].transitions
#     assert 2 in nfa.states[1].transitions['a']
#     assert 'b' in nfa.states[2].transitions
#     assert 3 in nfa.states[2].transitions['b']
#     assert 3 in nfa.states[1].epsilon_transitions

#     print("All tests passed.")

# # Run the test
# test_nfa_structure()
