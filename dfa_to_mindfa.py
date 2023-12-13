
dfa = {}
reachable_states = []
split_needed = None
dis_set = None

class DisjointSet(object):
    def __init__(self, items):
        self._disjoint_set = list()
        if items:
            for item in set(items):
                self._disjoint_set.append([item])

    def _get_index(self, item):
        for s in self._disjoint_set:
            for _item in s:
                if _item == item:
                    return self._disjoint_set.index(s)
        return None

    def find(self, item):
        for s in self._disjoint_set:
            if item in s:
                return s
        return None

    def find_set(self, item):
        s = self._get_index(item)
        return s+1 if s is not None else None 

    def union(self, item1, item2):
        i = self._get_index(item1)
        j = self._get_index(item2)
        if i != j:
            self._disjoint_set[i] += self._disjoint_set[j]
            del self._disjoint_set[j]
    
    def get(self):
        return self._disjoint_set
    

# Assume the DisjointSet class definition here, as previously provided.

def reachable_dfs(node, dfa, reachable_states):
    for start, inp, end in dfa['transition_function']:
        if start == node and end not in reachable_states:
            reachable_states.append(end)
            reachable_dfs(end, dfa, reachable_states)

def remove_unreachable_states(dfa):
    reachable_states = []
    for st in dfa['start_states']:
        if st not in reachable_states:
            reachable_states.append(st)
            reachable_dfs(st, dfa, reachable_states)

    dfa['states'] = [state for state in dfa['states'] if state in reachable_states]
    dfa['final_states'] = [state for state in dfa['final_states'] if state in reachable_states]
    dfa['transition_function'] = [val for val in dfa['transition_function'] if val[0] in reachable_states]

def get_to_state(start, inp, dfa):
    for val in dfa['transition_function']:
        if start == val[0] and inp == val[1]:
            return val[2]
    return None

def minimiseDFA(dfa):
    remove_unreachable_states(dfa)
    split_needed = True
    sorted_states = sorted(dfa['states'])
    group = {(st1, st2): (st1 in dfa['final_states']) == (st2 in dfa['final_states']) 
             for i, st1 in enumerate(sorted_states) 
             for st2 in sorted_states[i+1:]}

    while split_needed:
        split_needed = False
        for i, st1 in enumerate(sorted_states):
            for st2 in sorted_states[i+1:]:
                if not group[(st1, st2)]:
                    continue
                for letter in dfa['letters']:
                    to1 = get_to_state(st1, letter, dfa)
                    to2 = get_to_state(st2, letter, dfa)
                    if to1 and to2 and to1 != to2:
                        is_same_grp = group[(min(to1, to2), max(to1, to2))]
                        split_needed = split_needed or not is_same_grp
                        group[(st1, st2)] = is_same_grp
                        if not is_same_grp:
                            break

    dis_set = DisjointSet(dfa['states'])
    for st_pair, is_same_grp in group.items():
        if is_same_grp:
            dis_set.union(st_pair[0], st_pair[1])

    dfa_new_states = []
    for state in dfa['states']:
        new = dis_set.find(state)
        if new not in dfa_new_states:
            dfa_new_states.append(new)
    dfa['states'] = dfa_new_states

    dfa_new_transition = []
    for val in dfa['transition_function']:
        start, inp, end = val
        new_state1 = dis_set.find(start)
        new_state2 = dis_set.find(end)
        transition = [new_state1[0], inp, new_state2[0]]
        if transition not in dfa_new_transition:
            dfa_new_transition.append(transition)
    dfa['transition_function'] = dfa_new_transition

    final_states = []
    for fi_state in dfa['final_states']:
        fi_set = dis_set.find(fi_state)
        if fi_set not in final_states:
            final_states.append(fi_set[0])
    dfa['final_states'] = final_states
    

    start_states = []
    for st_state in dfa['start_states']:
        st_set = dis_set.find(st_state)
        if st_set not in start_states:
            start_states.append(st_set[0])
    dfa['start_states'] = start_states

    return dfa

# Call the function with the example DFA
if __name__ == "__main__":
#     dfa = {
#     "states": ["a", "b", "c", "d", "e", "f"],
#     "letters": ["0", "1"],
#     "transition_function": [
#         ["a", "0", "b"],
#         ["a", "1", "c"],
#         ["b", "0", "a"],
#         ["b", "1", "d"],
#         ["c", "0", "e"],
#         ["c", "1", "f"],
#         ["d", "0", "e"],
#         ["d", "1", "f"],
#         ["e", "0", "e"],
#         ["e", "1", "f"],
#         ["f", "0", "f"],
#         ["f", "1", "f"]
#     ],
#     "start_states": ["a"],
#     "final_states": ["c", "d", "e"]
# }
    #dfa from hw2
    dfa = dfa = {
    "states": ["0", "1", "2", "3", "4", "5", "6"],
    "letters": ["a", "b", "c"],
    "transition_function": [
        ["0", "a", "1"],
        ["0", "c", "0"],
        ["0", "b", "6"],
        ["1", "a", "2"],
        ["1", "b", "3"],
        ["1", "c", "4"],
        ["2", "a", "3"],
        ["2", "b", "5"],
        ["2", "c", "5"],
        ["3", "a", "4"],
        ["3", "b", "5"],
        ["3", "c", "6"],
        ["4", "a", "2"],
        ["4", "b", "5"],
        ["4", "c", "6"],
        ["5", "a", "5"],
        ["5", "b", "5"],
        ["5", "c", "6"],
        ["6", "a", "6"],
        ["6", "b", "6"],
        ["6", "c", "6"]
    ],
    "start_states": ["0"],
    "final_states": ["5", "6"]
}

    minimized_dfa = minimiseDFA(dfa)

    print("Minimized DFA:", minimized_dfa)