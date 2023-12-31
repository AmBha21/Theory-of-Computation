from regexp_to_nfa import *
from regex_datatype import RegexPattern
from nfa_datatype import NFA
from nfa_to_dfa import *


#entry to the program
if __name__ == "__main__":
    #setting the regex pattern
    regex = RegexPattern()
    regex.set_pattern("ab.(ab)*")
    showGraph = input("Show graph? (y/n): ")
    
    #converting the regex pattern to nfa
    pr = polish_regex(regex.pattern)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    _nfa = arrange_nfa(fa)
    print("===============> NFA <===============")
    print(_nfa)

    nfa = NFA()
    nfa.set_nfa(_nfa)

    #converting the nfa to dfa
    dfa = compute_dfa(nfa.nfa)
    print("===============> DFA <===============")
    print(dfa)
    if (showGraph == 'y'):
        nfa.nfa_to_graph('nfa')
        create_dfa_graph(dfa, 'dfa')
        print("Graphs created.")