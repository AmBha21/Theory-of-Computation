from graphviz import Digraph
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from nfa_datatype import NFA
from nfa_to_dfa import *

def test_a_star_dfa():
    # testing dfa for regex a*
    _nfa = {'states': ['Q1', 'Q2', 'Q3', 'Q4'], 'letters': ['$', 'a'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', 'a', 'Q4'], ['Q4', '$', 'Q2'], ['Q4', '$', 'Q3']], 'start_states': ['Q1'], 'final_states': ['Q3']}
    nfa = NFA()
    nfa.set_nfa(_nfa)
    dfa = compute_dfa(nfa.nfa)
    expected = {'states': [{'Q3', 'Q2', 'Q1'}, {'Q3', 'Q2', 'Q4'}], 'letters': ['a'], 'transition_function': [({'Q3', 'Q2', 'Q1'}, 'a', {'Q3', 'Q2', 'Q4'}), ({'Q3', 'Q2', 'Q4'}, 'a', {'Q3', 'Q2', 'Q4'})], 'start_states': [{'Q3', 'Q2', 'Q1'}], 'final_states': [{'Q3', 'Q2', 'Q1'}, {'Q3', 'Q2', 'Q4'}]}
    try:
        assert dfa == expected
        print("Test a*_dfa passed")
        create_dfa_graph(dfa, 'a*_dfa')
    except AssertionError as e:
        print(f"Assertion failed: a*_dfa failed. Details: {e}")
        raise

def test_a_or_b_dfa():
    # testing dfa for regex a+b
    _nfa = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'], 'letters': ['$', 'a', 'b'], 'transition_function': [['Q1', '$', 'Q2'], [
        'Q1', '$', 'Q3'], ['Q2', 'a', 'Q4'], ['Q4', '$', 'Q5'], ['Q3', 'b', 'Q6'], ['Q6', '$', 'Q5']], 'start_states': ['Q1'], 'final_states': ['Q5']}
    nfa = NFA()
    nfa.set_nfa(_nfa)
    dfa = compute_dfa(nfa.nfa)
    expected = {'states': [{'Q1', 'Q3', 'Q2'}, {'Q6', 'Q5'}, {'Q4', 'Q5'}], 'letters': ['a', 'b'], 'transition_function': [
        ({'Q1', 'Q3', 'Q2'}, 'a', {'Q4', 'Q5'}), ({'Q1', 'Q3', 'Q2'}, 'b', {'Q6', 'Q5'})], 'start_states': [{'Q1', 'Q3', 'Q2'}], 'final_states': [{'Q6', 'Q5'}, {'Q4', 'Q5'}]}
    try:
        assert dfa == expected
        print("Test a+b_dfa passed")
        create_dfa_graph(dfa, 'a+b_dfa')
    except AssertionError as e:
        print(f"Assertion failed: a+b_dfa failed. Details: {e}")
        raise

def test_ab_dfa():
    # testing dfa for regex ab
    _nfa = {'states': ['Q1', 'Q2', 'Q3', 'Q4'], 'letters': ['a', '$', 'b'], 'transition_function': [
        ['Q1', 'a', 'Q2'], ['Q2', '$', 'Q3'], ['Q3', 'b', 'Q4']], 'start_states': ['Q1'], 'final_states': ['Q4']}
    nfa = NFA()
    nfa.set_nfa(_nfa)
    dfa = compute_dfa(nfa.nfa)
    expected = {'states': [{'Q1'}, {'Q3', 'Q2'}, {'Q4'}], 'letters': ['a', 'b'], 'transition_function': [
        ({'Q1'}, 'a', {'Q3', 'Q2'}), ({'Q3', 'Q2'}, 'b', {'Q4'})], 'start_states': [{'Q1'}], 'final_states': [{'Q4'}]}
    try:
        assert dfa == expected
        print("Test ab_dfa passed")
        create_dfa_graph(dfa, 'ab_dfa')
    except AssertionError as e:
        print(f"Assertion failed: ab_dfa failed. Details: {e}")
        raise

def test_ab_star_dfa():
    # testing dfa for regex ab*
    _nfa = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'], 'letters': ['a', '$', 'b'], 'transition_function': [['Q1', 'a', 'Q2'], ['Q2', '$', 'Q3'], [
        'Q3', '$', 'Q4'], ['Q3', '$', 'Q5'], ['Q4', 'b', 'Q6'], ['Q6', '$', 'Q4'], ['Q6', '$', 'Q5']], 'start_states': ['Q1'], 'final_states': ['Q5']}
    nfa = NFA()
    nfa.set_nfa(_nfa)
    dfa = compute_dfa(nfa.nfa)
    expected = {'states': [{'Q1'}, {'Q4', 'Q3', 'Q5', 'Q2'}, {'Q4', 'Q6', 'Q5'}], 'letters': ['a', 'b'], 'transition_function': [({'Q1'}, 'a', {'Q4', 'Q3', 'Q5', 'Q2'}), (
        {'Q4', 'Q3', 'Q5', 'Q2'}, 'b', {'Q4', 'Q6', 'Q5'}), ({'Q4', 'Q6', 'Q5'}, 'b', {'Q4', 'Q6', 'Q5'})], 'start_states': [{'Q1'}], 'final_states': [{'Q4', 'Q3', 'Q5', 'Q2'}, {'Q4', 'Q6', 'Q5'}]}
    try:
        assert dfa == expected
        print("Test ab*_dfa passed")
        create_dfa_graph(dfa, 'ab*_dfa')
    except AssertionError as e:
        print(f"Assertion failed: ab*_dfa failed. Details: {e}")
        raise

def test_ab_dot_ab_star_dfa():
    # testing dfa for regex ab*
    _nfa = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10'], 'letters': ['a', '$', 'b'], 'transition_function': [['Q1', 'a', 'Q2'], ['Q2', '$', 'Q3'], ['Q3', 'b', 'Q4'], ['Q4', '$', 'Q5'], ['Q5', '$', 'Q6'], ['Q5', '$', 'Q7'], ['Q6', 'a', 'Q8'], ['Q8', '$', 'Q9'], ['Q9', 'b', 'Q10'], ['Q10', '$', 'Q6'], ['Q10', '$', 'Q7']], 'start_states': ['Q1'], 'final_states': ['Q7']}
    nfa = NFA()
    nfa.set_nfa(_nfa)
    dfa = compute_dfa(nfa.nfa)
    expected = {'states': [{'Q1'}, {'Q2', 'Q3'}, {'Q4', 'Q6', 'Q5', 'Q7'}, {'Q9', 'Q8'}, {'Q6', 'Q10', 'Q7'}], 'letters': ['a', 'b'], 'transition_function': [({'Q1'}, 'a', {'Q2', 'Q3'}), ({'Q2', 'Q3'}, 'b', {'Q4', 'Q6', 'Q5', 'Q7'}), ({'Q4', 'Q6', 'Q5', 'Q7'}, 'a', {'Q9', 'Q8'}), ({'Q9', 'Q8'}, 'b', {'Q6', 'Q10', 'Q7'}), ({'Q6', 'Q10', 'Q7'}, 'a', {'Q9', 'Q8'})], 'start_states': [{'Q1'}], 'final_states': [{'Q4', 'Q6', 'Q5', 'Q7'}, {'Q6', 'Q10', 'Q7'}]}
    try:
        assert dfa == expected
        print("Test ab.(ab)*_dfa passed")
        create_dfa_graph(dfa, 'ab*_dfa')
    except AssertionError as e:
        print(f"Assertion failed: ab.(ab)*_dfa failed. Details: {e}")
        raise

if __name__ == "__main__":
    print("\nRunning tests 1/4 => ▮▯▯▯▯")
    test_a_star_dfa()
    print("\nRunning tests 2/4 => ▮▮▯▯▯")
    test_a_or_b_dfa()
    print("\nRunning tests 3/4 => ▮▮▮▯▯")
    test_ab_dfa()
    print("\nRunning tests 4/4 => ▮▮▮▮▯")
    test_ab_star_dfa()
    print("\nRunning tests 5/5 => ▮▮▮▮▮")
    test_ab_dot_ab_star_dfa()
    print("\nAll tests passed (4/4)")
