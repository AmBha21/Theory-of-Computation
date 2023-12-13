# Conversion from Regex to NFA
from graphviz import Digraph
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from regexp_to_nfa import *

def test_a_star_nfa():
    reg = 'a*'
    
    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)
    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4'], 'letters': ['$', 'a'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', 'a', 'Q4'], ['Q4', '$', 'Q2'], ['Q4', '$', 'Q3']], 'start_states': ['Q1'], 'final_states': ['Q3']}
    try:
        assert nfa == expected
        print("Test a*_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render('a*_nfa')
    except AssertionError as e:
        print(f"Assertion failed: a*_nfa failed. Details: {e}")
        raise

def test_a_or_b_nfa():    
    reg = 'a+b'
    
    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)
    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'], 'letters': ['$', 'a', 'b'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', 'a', 'Q4'], ['Q4', '$', 'Q5'], ['Q3', 'b', 'Q6'], ['Q6', '$', 'Q5']], 'start_states': ['Q1'], 'final_states': ['Q5']}
    try:
        assert nfa == expected
        print("Test a+b_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render('a+b_nfa')
    except AssertionError as e:
        print(f"Assertion failed: a+b_nfa failed. Details: {e}")
        raise
    
def test_ab_nfa():
    reg = 'ab'

    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)
    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4'], 'letters': ['a', '$', 'b'], 'transition_function': [
        ['Q1', 'a', 'Q2'], ['Q2', '$', 'Q3'], ['Q3', 'b', 'Q4']], 'start_states': ['Q1'], 'final_states': ['Q4']}
    try:
        assert nfa == expected
        print("Test ab_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render('ab_nfa')
    except AssertionError as e:
        print(f"Assertion failed: ab_nfa failed. Details: {e}")
        raise
    

def test_ab_star_nfa():
    reg = "ab*"
    
    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)
    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'], 'letters': ['a', '$', 'b'], 'transition_function': [['Q1', 'a', 'Q2'], ['Q2', '$', 'Q3'], [
        'Q3', '$', 'Q4'], ['Q3', '$', 'Q5'], ['Q4', 'b', 'Q6'], ['Q6', '$', 'Q4'], ['Q6', '$', 'Q5']], 'start_states': ['Q1'], 'final_states': ['Q5']}
    try:
        assert nfa == expected
        print("Test ab*_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render('ab*_nfa')
    except AssertionError as e:
        print(f"Assertion failed: ab*_nfa failed. Details: {e}")
        raise

def test_ab_dot_ab_star_nfa():
    reg = "ab.(ab)*"
    
    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)

    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10'], 'letters': ['a', '$', 'b'], 'transition_function': [['Q1', 'a', 'Q2'], ['Q2', '$', 'Q3'], ['Q3', 'b', 'Q4'], ['Q4', '$', 'Q5'], ['Q5', '$', 'Q6'], ['Q5', '$', 'Q7'], ['Q6', 'a', 'Q8'], ['Q8', '$', 'Q9'], ['Q9', 'b', 'Q10'], ['Q10', '$', 'Q6'], ['Q10', '$', 'Q7']], 'start_states': ['Q1'], 'final_states': ['Q7']}
    try:
        assert nfa == expected
        print("Test ab.(ab)*_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render('ab.(ab)*_nfa')
    except AssertionError as e:
        print(f"Assertion failed: ab.(ab)*_nfa failed. Details: {e}")
        raise


if __name__ == "__main__":
    print("\nRunning tests 1/5 => ▮▯▯▯")
    test_a_star_nfa()
    print("\nRunning tests 2/5 => ▮▮▯▯")
    test_a_or_b_nfa()
    print("\nRunning tests 3/5 => ▮▮▮▯")
    test_ab_nfa()
    print("\nRunning tests 4/5 => ▮▮▮▮▯")
    test_ab_star_nfa()
    print("\nRunning tests 5/5 => ▮▮▮▮▮")
    test_ab_dot_ab_star_nfa()

