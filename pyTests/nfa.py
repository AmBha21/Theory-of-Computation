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

def p_a_or_b_p_or_c_star_nfa():
    reg = '(a+b)+c*'
    
    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)

    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12'], 'letters': ['$', 'a', 'b', 'c'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', '$', 'Q4'], ['Q2', '$', 'Q5'], ['Q4', 'a', 'Q6'], ['Q6', '$', 'Q7'], ['Q7', '$', 'Q8'], ['Q5', 'b', 'Q9'], ['Q9', '$', 'Q7'], ['Q3', '$', 'Q10'], ['Q3', '$', 'Q11'], ['Q10', 'c', 'Q12'], ['Q12', '$', 'Q10'], ['Q12', '$', 'Q11'], ['Q11', '$', 'Q8']], 'start_states': ['Q1'], 'final_states': ['Q8']}
    try:
        assert nfa == expected
        print("Test (a+b)+c*_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render('(a+b)+c*_nfa')
    except AssertionError as e:
        print(f"Assertion failed: (a+b)+c*_nfa failed. Details: {e}")
        raise
    
def stress_test_1_nfa():
    reg = "(ab+cd)+(x*y)*"
    
    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)

    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20'], 'letters': ['$', 'a', 'b', 'c', 'd', 'x', 'y'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', '$', 'Q4'], ['Q2', '$', 'Q5'], ['Q4', 'a', 'Q6'], ['Q6', '$', 'Q7'], ['Q7', 'b', 'Q8'], ['Q8', '$', 'Q9'], ['Q9', '$', 'Q10'], ['Q5', 'c', 'Q11'], ['Q11', '$', 'Q12'], ['Q12', 'd', 'Q13'], ['Q13', '$', 'Q9'], ['Q3', '$', 'Q14'], ['Q3', '$', 'Q15'], ['Q14', '$', 'Q16'], ['Q14', '$', 'Q17'], ['Q16', 'x', 'Q18'], ['Q18', '$', 'Q16'], ['Q18', '$', 'Q17'], ['Q17', '$', 'Q19'], ['Q19', 'y', 'Q20'], ['Q20', '$', 'Q14'], ['Q20', '$', 'Q15'], ['Q15', '$', 'Q10']], 'start_states': ['Q1'], 'final_states': ['Q10']}
    try:
        assert nfa == expected
        print(f"Test {reg}_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render(f'{reg}_nfa')
    except AssertionError as e:
        print(f"Assertion failed: {reg}_nfa failed. Details: {e}")
        raise
    
def stress_test_2_nfa():
    reg = "(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z)*"
    
    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)
    
    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30', 'Q31', 'Q32', 'Q33', 'Q34', 'Q35', 'Q36', 'Q37', 'Q38', 'Q39', 'Q40', 'Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50', 'Q51', 'Q52', 'Q53', 'Q54', 'Q55', 'Q56', 'Q57', 'Q58', 'Q59', 'Q60', 'Q61', 'Q62', 'Q63', 'Q64', 'Q65', 'Q66', 'Q67', 'Q68', 'Q69', 'Q70', 'Q71', 'Q72', 'Q73', 'Q74', 'Q75', 'Q76', 'Q77', 'Q78', 'Q79', 'Q80', 'Q81', 'Q82', 'Q83', 'Q84', 'Q85', 'Q86', 'Q87', 'Q88', 'Q89', 'Q90', 'Q91', 'Q92', 'Q93', 'Q94', 'Q95', 'Q96', 'Q97', 'Q98', 'Q99', 'Q100', 'Q101', 'Q102', 'Q103', 'Q104'], 'letters': ['$', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', '$', 'Q4'], ['Q2', '$', 'Q5'], ['Q4', '$', 'Q6'], ['Q4', '$', 'Q7'], ['Q6', '$', 'Q8'], ['Q6', '$', 'Q9'], ['Q8', '$', 'Q10'], ['Q8', '$', 'Q11'], ['Q10', '$', 'Q12'], ['Q10', '$', 'Q13'], ['Q12', '$', 'Q14'], ['Q12', '$', 'Q15'], ['Q14', '$', 'Q16'], ['Q14', '$', 'Q17'], ['Q16', '$', 'Q18'], ['Q16', '$', 'Q19'], ['Q18', '$', 'Q20'], ['Q18', '$', 'Q21'], ['Q20', '$', 'Q22'], ['Q20', '$', 'Q23'], ['Q22', '$', 'Q24'], ['Q22', '$', 'Q25'], ['Q24', '$', 'Q26'], ['Q24', '$', 'Q27'], ['Q26', '$', 'Q28'], ['Q26', '$', 'Q29'], ['Q28', '$', 'Q30'], ['Q28', '$', 'Q31'], ['Q30', '$', 'Q32'], ['Q30', '$', 'Q33'], ['Q32', '$', 'Q34'], ['Q32', '$', 'Q35'], ['Q34', '$', 'Q36'], ['Q34', '$', 'Q37'], ['Q36', '$', 'Q38'], ['Q36', '$', 'Q39'], ['Q38', '$', 'Q40'], ['Q38', '$', 'Q41'], ['Q40', '$', 'Q42'], ['Q40', '$', 'Q43'], ['Q42', '$', 'Q44'], ['Q42', '$', 'Q45'], ['Q44', '$', 'Q46'], [
        'Q44', '$', 'Q47'], ['Q46', '$', 'Q48'], ['Q46', '$', 'Q49'], ['Q48', '$', 'Q50'], ['Q48', '$', 'Q51'], ['Q50', '$', 'Q52'], ['Q50', '$', 'Q53'], ['Q52', 'a', 'Q54'], ['Q54', '$', 'Q55'], ['Q55', '$', 'Q56'], ['Q56', '$', 'Q57'], ['Q57', '$', 'Q58'], ['Q58', '$', 'Q59'], ['Q59', '$', 'Q60'], ['Q60', '$', 'Q61'], ['Q61', '$', 'Q62'], ['Q62', '$', 'Q63'], ['Q63', '$', 'Q64'], ['Q64', '$', 'Q65'], ['Q65', '$', 'Q66'], ['Q66', '$', 'Q67'], ['Q67', '$', 'Q68'], ['Q68', '$', 'Q69'], ['Q69', '$', 'Q70'], ['Q70', '$', 'Q71'], ['Q71', '$', 'Q72'], ['Q72', '$', 'Q73'], ['Q73', '$', 'Q74'], ['Q74', '$', 'Q75'], ['Q75', '$', 'Q76'], ['Q76', '$', 'Q77'], ['Q77', '$', 'Q78'], ['Q78', '$', 'Q79'], ['Q79', '$', 'Q2'], ['Q79', '$', 'Q3'], ['Q53', 'b', 'Q80'], ['Q80', '$', 'Q55'], ['Q51', 'c', 'Q81'], ['Q81', '$', 'Q56'], ['Q49', 'd', 'Q82'], ['Q82', '$', 'Q57'], ['Q47', 'e', 'Q83'], ['Q83', '$', 'Q58'], ['Q45', 'f', 'Q84'], ['Q84', '$', 'Q59'], ['Q43', 'g', 'Q85'], ['Q85', '$', 'Q60'], ['Q41', 'h', 'Q86'], ['Q86', '$', 'Q61'], ['Q39', 'i', 'Q87'], ['Q87', '$', 'Q62'], ['Q37', 'j', 'Q88'], ['Q88', '$', 'Q63'], ['Q35', 'k', 'Q89'], ['Q89', '$', 'Q64'], ['Q33', 'l', 'Q90'], ['Q90', '$', 'Q65'], ['Q31', 'm', 'Q91'], ['Q91', '$', 'Q66'], ['Q29', 'n', 'Q92'], ['Q92', '$', 'Q67'], ['Q27', 'o', 'Q93'], ['Q93', '$', 'Q68'], ['Q25', 'p', 'Q94'], ['Q94', '$', 'Q69'], ['Q23', 'q', 'Q95'], ['Q95', '$', 'Q70'], ['Q21', 'r', 'Q96'], ['Q96', '$', 'Q71'], ['Q19', 's', 'Q97'], ['Q97', '$', 'Q72'], ['Q17', 't', 'Q98'], ['Q98', '$', 'Q73'], ['Q15', 'u', 'Q99'], ['Q99', '$', 'Q74'], ['Q13', 'v', 'Q100'], ['Q100', '$', 'Q75'], ['Q11', 'w', 'Q101'], ['Q101', '$', 'Q76'], ['Q9', 'x', 'Q102'], ['Q102', '$', 'Q77'], ['Q7', 'y', 'Q103'], ['Q103', '$', 'Q78'], ['Q5', 'z', 'Q104'], ['Q104', '$', 'Q79']], 'start_states': ['Q1'], 'final_states': ['Q3']}
    try:
        assert nfa == expected
        print(f"Test {reg}_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render(f'{reg}_nfa')
    except AssertionError as e:
        print(f"Assertion failed: {reg}_nfa failed. Details: {e}")
        raise

def stress_test_3_nfa():
    reg = "(a*)+(b* + c*)*"
    
    pr = polish_regex(reg)
    et = make_exp_tree(pr)
    fa = compute_regex(et)
    arrange_nfa(fa)

    expected = {'states': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22'], 'letters': ['$', 'a', 'b', ' ', 'c'], 'transition_function': [['Q1', '$', 'Q2'], ['Q1', '$', 'Q3'], ['Q2', '$', 'Q4'], ['Q2', '$', 'Q5'], ['Q4', 'a', 'Q6'], ['Q6', '$', 'Q4'], ['Q6', '$', 'Q5'], ['Q5', '$', 'Q7'], ['Q3', '$', 'Q8'], ['Q3', '$', 'Q9'], ['Q8', '$', 'Q10'], ['Q8', '$', 'Q11'], [
        'Q10', '$', 'Q12'], ['Q10', '$', 'Q13'], ['Q12', 'b', 'Q14'], ['Q14', '$', 'Q12'], ['Q14', '$', 'Q13'], ['Q13', '$', 'Q15'], ['Q15', ' ', 'Q16'], ['Q16', '$', 'Q17'], ['Q17', '$', 'Q8'], ['Q17', '$', 'Q9'], ['Q9', '$', 'Q7'], ['Q11', ' ', 'Q18'], ['Q18', '$', 'Q19'], ['Q19', '$', 'Q20'], ['Q19', '$', 'Q21'], ['Q20', 'c', 'Q22'], ['Q22', '$', 'Q20'], ['Q22', '$', 'Q21'], ['Q21', '$', 'Q17']], 'start_states': ['Q1'], 'final_states': ['Q7']}
    try:
        assert nfa == expected
        print(f"Test {reg}_nfa passed")
        nfa_graph = nfa_to_graphviz(nfa)
        nfa_graph.render(f'{reg}_nfa')
    except AssertionError as e:
        print(f"Assertion failed: {reg}_nfa failed. Details: {e}")
        raise
    
def stress_test_4_nfa():
    pass

if __name__ == "__main__":
    total_tests = 10
    print(f"\nRunning tests 1/{total_tests} => {'▮' * (total_tests-9)}{'▯' * (total_tests-1)}")
    test_a_star_nfa()
    print(f"\nRunning tests 2/{total_tests} => {'▮' * (total_tests-8)}{'▯' * (total_tests-2)}")
    test_a_or_b_nfa()
    print(f"\nRunning tests 3/{total_tests} => {'▮' * (total_tests-7)}{'▯' * (total_tests-3)}")
    test_ab_nfa()
    print(f"\nRunning tests 4/{total_tests} => {'▮' * (total_tests-6)}{'▯' * (total_tests-4)}")
    test_ab_star_nfa()
    print(f"\nRunning tests 5/{total_tests} => {'▮' * (total_tests-5)}{'▯' * (total_tests-5)}")
    test_ab_dot_ab_star_nfa()
    print(f"\nRunning tests 6/{total_tests} => {'▮' * (total_tests-4)}{'▯' * (total_tests-6)}")
    p_a_or_b_p_or_c_star_nfa()
    print(f"\nRunning tests 7/{total_tests} => {'▮' * (total_tests-3)}{'▯' * (total_tests-7)}")
    stress_test_1_nfa()
    print(f"\nRunning tests 8/{total_tests} => {'▮' * (total_tests-2)}{'▯' * (total_tests-8)}")
    stress_test_2_nfa()
    print(f"\nRunning tests 9/{total_tests} => {'▮' * (total_tests-1)}{'▯' * (total_tests-9)}")
    stress_test_3_nfa()
    print(f"\nRunning tests 10/{total_tests} => {'▮' * (total_tests-0)}{'▯' * (total_tests-10)}")
    stress_test_4_nfa()
    
    print(f"\nAll tests passed ({total_tests}/{total_tests})")