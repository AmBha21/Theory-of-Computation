# Minimise DFA

import json 
from graphviz import Digraph
import sys

dfa = {}
reachable_states = []
split_needed = None
dis_set = None

class DisjointSet(object):

	def __init__(self,items):

		self._disjoint_set = list()

		if items:
			for item in set(items):
				self._disjoint_set.append([item])

	def _get_index(self,item):
		for s in self._disjoint_set:
			for _item in s:
				if _item == item:
					return self._disjoint_set.index(s)
		return None

	def find(self,item):
		for s in self._disjoint_set:
			if item in s:
				return s
		return None

	def find_set(self, item):

		s = self._get_index(item)

		return s+1 if s is not None else None 

	def union(self,item1,item2):
		i = self._get_index(item1)
		j = self._get_index(item2)

		if i != j:
			self._disjoint_set[i] += self._disjoint_set[j]
			del self._disjoint_set[j]
	
	def get(self):
		return self._disjoint_set


def reachable_dfs(node):
    global dfa, reachable_states
    for val in dfa['transition_function']:
        start = val[0]
        inp = val[1]
        end = val[2]
        
        if start == node:
            if end not in reachable_states:
                reachable_states.append(end)
                reachable_dfs(end)


def remove_unreachable_states():
    global dfa, reachable_states

    for st in dfa['start_states']:
        reachable_states.append(st)
        reachable_dfs(st)

    dfa['states'] = [state for state in dfa['states'] if state in reachable_states]
    
    dfa['final_states'] = [state for state in dfa['final_states'] if state in reachable_states]

    temp = []

    for val in dfa['transition_function']:
        if val[0] in reachable_states:
            temp.append(val)

    dfa['transition_function'] = temp

def order_tuple(a,b):
	return (a,b) if a < b else (b,a)

def get_to_state(start, inp):
    global dfa
    for val in dfa['transition_function']:
        if val[0] == start and val[1] == inp:
            return val[2]
    return []  # Return an empty list instead of None

def minimiseDFA():
    global dfa, split_needed, dis_set
    split_needed = True
    dis_set = DisjointSet([tuple(state) for state in dfa['states']])

    while split_needed:
        split_needed = False
        new_groups = []

        # Convert states in DFA to tuples for hashing and comparison
        tuple_states = [tuple(sorted(state)) for state in dfa['states']]
        tuple_final_states = [tuple(sorted(state)) for state in dfa['final_states']]

        for state1 in tuple_states:
            for state2 in tuple_states:
                if state1 != state2:
                    # Compare transitions for all input symbols
                    all_match = True
                    for letter in dfa['letters']:
                        to_state1 = get_to_state(list(state1), letter)
                        to_state2 = get_to_state(list(state2), letter)
                        if to_state1 != to_state2 or ((state1 in tuple_final_states) != (state2 in tuple_final_states)):
                            all_match = False
                            break

                    if all_match:
                        dis_set.union(state1, state2)

        # Check if new groups are different from old groups
        if set(map(frozenset, dis_set.get())) != set(map(frozenset, new_groups)):
            split_needed = True

    # Reconstruct DFA with minimized states
    minimized_states = [set(group) for group in dis_set.get()]
    dfa['states'] = minimized_states

    # Update transition function
    new_transition_function = []
    for start, letter, end in dfa['transition_function']:
        new_start = find_new_state(start, minimized_states)
        new_end = find_new_state(end, minimized_states)
        if (new_start, letter, new_end) not in new_transition_function:
            new_transition_function.append((new_start, letter, new_end))
    dfa['transition_function'] = new_transition_function

    # Update final states
    dfa['final_states'] = [find_new_state(state, minimized_states) for state in dfa['final_states']]

def find_new_state(old_state, new_states):
    """ Find the new state corresponding to an old state. """
    old_state_tuple = tuple(sorted(old_state))
    for state in new_states:
        if old_state_tuple in [tuple(sorted(s)) for s in state]:
            return state
    return None

# Rest of the DFA minimization code...


def create_minimized_dfa_graph(dfa):
    graph = Digraph('finite_state_machine')
    graph.attr(rankdir='LR', size='8,5')

    # Add nodes for states
    for state in dfa['states']:
        state_name = ''.join(state) if isinstance(state, list) else state
        if state in dfa['final_states']:
            graph.attr('node', shape='doublecircle')
        else:
            graph.attr('node', shape='circle')
        graph.node(state_name)

    # Add edges for transitions
    for transition in dfa['transition_function']:
        start, letter, end = transition
        start_name = ''.join(start) if isinstance(start, list) else start
        end_name = ''.join(end) if isinstance(end, list) else end
        graph.edge(start_name, end_name, label=letter)

    # Display the graph
    graph.view()
    
# def load_dfa():
#     global dfa
#     with open(sys.argv[1], 'r') as inpjson:
#         dfa = json.loads(inpjson.read())

# def out_min_dfa():
#     global dfa
#     with open(sys.argv[2], 'w') as outjson:
#         outjson.write(json.dumps(dfa, indent = 4))


if __name__ == "__main__":
    # load_dfa()
    dfa = {'states': [['Q1', 'Q2', 'Q3', 'Q6', 'Q7', 'Q5'], ['Q4', 'Q8', 'Q9', 'Q5'], ['Q10', 'Q6', 'Q7', 'Q5'], ['Q8', 'Q9']], 'letters': ['a', 'b'], 'transition_function': [(['Q1', 'Q2', 'Q3', 'Q6', 'Q7', 'Q5'], 'a', ['Q4', 'Q8', 'Q9', 'Q5']), (['Q4', 'Q8', 'Q9', 'Q5'], 'b', ['Q10', 'Q6', 'Q7', 'Q5']), (['Q10', 'Q6', 'Q7', 'Q5'], 'a', ['Q8', 'Q9']), (['Q8', 'Q9'], 'b', ['Q10', 'Q6', 'Q7', 'Q5'])], 'start_states': [['Q1', 'Q2', 'Q3', 'Q6', 'Q7', 'Q5']], 'final_states': [['Q1', 'Q2', 'Q3', 'Q6', 'Q7', 'Q5'], ['Q4', 'Q8', 'Q9', 'Q5'], ['Q10', 'Q6', 'Q7', 'Q5']]}
    remove_unreachable_states()
    minimiseDFA()
    create_minimized_dfa_graph(dfa)
    # out_min_dfa()