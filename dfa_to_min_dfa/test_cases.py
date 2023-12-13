from main import minimiseDFA, update_transition_function, output_dfa_to_graphviz
from graphviz import Digraph
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from nfa_datatype import NFA
from nfa_to_dfa import *


def test1():
	# testing dfa for regex a*
	dfa = {
		"states": ["a", "b", "c", "d", "e", "f"],
		"letters": ["0", "1"],
		"transition_function": [
			["a", "0", "b"],
			["a", "1", "c"],
			["b", "0", "a"],
			["b", "1", "d"],
			["c", "0", "e"],
			["c", "1", "f"],
			["d", "0", "e"],
			["d", "1", "f"],
			["e", "0", "e"],
			["e", "1", "f"],
			["f", "0", "f"],
			["f", "1", "f"]
		],
		"start_states": ["a"],
		"final_states": ["c", "d", "e"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['a_b', 'c_d_e', 'f'], 'letters': ['0', '1'], 'transition_function': [['a_b', '0', 'a_b'], ['a_b', '1', 'c_d_e'], ['c_d_e', '0', 'c_d_e'], ['c_d_e', '1', 'f'], ['f', '0', 'f'], ['f', '1', 'f']], 'start_states': ['a'], 'final_states': ['c']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test1_mini')
		print("Test 1 passed")
	except AssertionError as e:
		print(f"Assertion failed: 1 failed. Details: {e}")
		raise

def test2():
	dfa = {
		"states": ["a", "b"],
		"letters": ["0", "1"],
		"transition_function": [
		["a", "0", "b"],
		["a", "1", "b"],
		["b", "0", "b"],
		["b", "1", "b"]
		],
		"start_states": ["a"],
		"final_states": ["b"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['a', 'b'], 'letters': ['0', '1'], 'transition_function': [['a', '0', 'b'], ['a', '1', 'b'], ['b', '0', 'b'], ['b', '1', 'b']], 'start_states': ['a'], 'final_states': ['b']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test2_mini')
		print("Test 2 passed")
	except AssertionError as e:
		print(f"Assertion failed: 2 failed. Details: {e}")
		raise

def test3():
	# testing dfa for regex (a+b)*
	dfa = {
		"states": ["q0", "q1", "q2"],
		"letters": ["a", "b"],
		"transition_function": [
			["q0", "a", "q1"],
			["q0", "b", "q1"],
			["q1", "a", "q2"],
			["q1", "b", "q2"],
			["q2", "a", "q1"],
			["q2", "b", "q1"]
		],
		"start_states": ["q0"],
		"final_states": ["q0", "q2"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['q0_q2', 'q1'], 'letters': ['a', 'b'], 'transition_function': [['q0_q2', 'a', 'q1'], ['q0_q2', 'b', 'q1'], ['q1', 'a', 'q0_q2'], ['q1', 'b', 'q0_q2']], 'start_states': ['q0'], 'final_states': ['q0']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test3_mini')
		print("Test 3 passed")
	except AssertionError as e:
		print(f"Assertion failed: 3 failed. Details: {e}")
		raise


def test4():
	# testing dfa for regex a*b
	dfa = {
		"states": ["q0", "q1", "q2"],
		"letters": ["a", "b"],
		"transition_function": [
			["q0", "a", "q1"],
			["q1", "b", "q2"]
		],
		"start_states": ["q0"],
		"final_states": ["q2"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['q0_q1', 'q2'], 'letters': ['a', 'b'], 'transition_function': [['q0_q1', 'a', 'q0_q1'], ['q0_q1', 'b', 'q2']], 'start_states': ['q0'], 'final_states': ['q2']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test4_mini')
		print("Test 4 passed")
	except AssertionError as e:
		print(f"Assertion failed: Test 4 failed. Details: {e}")
		raise

def test5():
	# testing dfa for regex (a|b)*
	dfa = {
		"states": ["q0", "q1", "q2"],
		"letters": ["a", "b"],
		"transition_function": [
			["q0", "a", "q1"],
			["q0", "b", "q2"],
			["q1", "a", "q1"],
			["q1", "b", "q2"],
			["q2", "a", "q2"],
			["q2", "b", "q2"]
		],
		"start_states": ["q0"],
		"final_states": ["q0", "q1", "q2"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['q0_q1_q2'], 'letters': ['a', 'b'], 'transition_function': [['q0_q1_q2', 'a', 'q0_q1_q2'], ['q0_q1_q2', 'b', 'q0_q1_q2']], 'start_states': ['q0'], 'final_states': ['q0']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test5_mini')
		print("Test 5 passed")
	except AssertionError as e:
		print(f"Assertion failed: Test 5 failed. Details: {e}")
		raise


def test6():
	# testing dfa for regex (a|b)*
	dfa = {
		"states": ["q0", "q1", "q2", "q3"],
		"letters": ["a", "b"],
		"transition_function": [
			["q0", "a", "q1"],
			["q0", "b", "q2"],
			["q1", "a", "q3"],
			["q1", "b", "q2"],
			["q2", "a", "q1"],
			["q2", "b", "q3"],
			["q3", "a", "q3"],
			["q3", "b", "q3"]
		],
		"start_states": ["q0"],
		"final_states": ["q0", "q1", "q2", "q3"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['q0_q1_q2_q3'], 'letters': ['a', 'b'], 'transition_function': [['q0_q1_q2_q3', 'a', 'q0_q1_q2_q3'], ['q0_q1_q2_q3', 'b', 'q0_q1_q2_q3']], 'start_states': ['q0'], 'final_states': ['q0']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test6_mini')
		print("Test 6 passed")
	except AssertionError as e:
		print(f"Assertion failed: Test 6 failed. Details: {e}")
		raise

def test7():
	# testing dfa for regex (a|b)*
	dfa = {
		"states": ["q0", "q1", "q2"],
		"letters": ["a", "b"],
		"transition_function": [
			["q0", "a", "q1"],
			["q0", "b", "q2"],
			["q1", "a", "q1"],
			["q1", "b", "q2"],
			["q2", "a", "q2"],
			["q2", "b", "q2"]
		],
		"start_states": ["q0"],
		"final_states": ["q0", "q1", "q2"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['q0_q1_q2'], 'letters': ['a', 'b'], 'transition_function': [['q0_q1_q2', 'a', 'q0_q1_q2'], ['q0_q1_q2', 'b', 'q0_q1_q2']], 'start_states': ['q0'], 'final_states': ['q0']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test7_mini')
		print("Test 7 passed")
	except AssertionError as e:
		print(f"Assertion failed: Test 7 failed. Details: {e}")
		raise

	
def test8():
	dfa = {
		"states": ["q0"],
		"letters": ["a"],
		"transition_function": [
			["q0", "a", "q0"]
		],
		"start_states": ["q0"],
		"final_states": ["q0"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['q0'], 'letters': ['a'], 'transition_function': [['q0', 'a', 'q0']], 'start_states': ['q0'], 'final_states': ['q0']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test8_mini')
		print("Test 8 passed")
	except AssertionError as e:
		print(f"Assertion failed: Test 8 failed. Details: {e}")
		raise


def test9():
	# testing dfa minimization
	dfa = {
		"states": ["q0", "q1", "q2"],
		"letters": ["a", "b"],
		"transition_function": [
			["q0", "a", "q1"],
			["q0", "b", "q2"],
			["q1", "a", "q1"],
			["q1", "b", "q2"],
			["q2", "a", "q2"],
			["q2", "b", "q2"]
		],
		"start_states": ["q0"],
		"final_states": ["q0", "q1", "q2"]
	}
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	expected = {'states': ['q0_q1_q2'], 'letters': ['a', 'b'], 'transition_function': [['q0_q1_q2', 'a', 'q0_q1_q2'], ['q0_q1_q2', 'b', 'q0_q1_q2']], 'start_states': ['q0'], 'final_states': ['q0']}
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test9_mini')
		print("Test 9 passed")
	except AssertionError as e:
		print(f"Assertion failed: Test 9 failed. Details: {e}")
		raise

# ...

def test10():
	# testing complex dfa

	dfa = {
		"states": ["q0", "q1", "q2", "q3", "q4", "q5", "q6"],
		"letters": ["a", "b"],
		"transition_function": [
			["q0", "a", "q1"],
			["q0", "b", "q2"],
			["q1", "a", "q3"],
			["q1", "b", "q4"],
			["q2", "a", "q5"],
			["q2", "b", "q6"],
			["q3", "a", "q3"],
			["q3", "b", "q4"],
			["q4", "a", "q3"],
			["q4", "b", "q4"],
			["q5", "a", "q5"],
			["q5", "b", "q6"],
			["q6", "a", "q5"],
			["q6", "b", "q6"]
		],
		"start_states": ["q0"],
		"final_states": ["q3", "q4", "q5", "q6"]
	}

	expected = {'states': ['q0', 'q1_q2', 'q3_q4_q5_q6'], 'letters': ['a', 'b'], 'transition_function': [['q0', 'a', 'q1_q2'], ['q0', 'b', 'q1_q2'], ['q1_q2', 'a', 'q3_q4_q5_q6'], ['q1_q2', 'b', 'q3_q4_q5_q6'], ['q3_q4_q5_q6', 'a', 'q3_q4_q5_q6'], ['q3_q4_q5_q6', 'b', 'q3_q4_q5_q6']], 'start_states': ['q0'], 'final_states': ['q3']}

	# Minimize the DFA
	minimized_dfa = minimiseDFA(dfa)
	minimized_dfa['transition_function'] = update_transition_function(minimized_dfa)

	print(minimized_dfa)

	# Check if the minimized DFA matches the expected output
	try:
		assert minimized_dfa == expected
		create_dfa_graph(dfa, 'test10_mini')
		print("Test 10 passed")
	except AssertionError as e:
		print(f"Assertion failed: Test 10 failed. Details: {e}")
		raise

# ...

if __name__ == "__main__":
	# ...
	print("\nRunning tests 10/10 => ▮▮▮▮▮▮▮▮▮")
	test10()




if __name__ == "__main__":
	print("\nRunning tests 1/10 => ▮▯▯▯▯▯▯▯▯▯")
	test1()

	print("\nRunning tests 2/10 => ▮▮▯▯▯▯▯▯▯▯")
	test2()

	print("\nRunning tests 3/10 => ▮▮▮▯▯▯▯▯▯▯")
	test3()

	print("\nRunning tests 4/10 => ▮▮▮▮▯▯▯▯▯▯")
	test4()

	print("\nRunning tests 5/10 => ▮▮▮▮▮▯▯▯▯▯")
	test5()

	print("\nRunning tests 6/10 => ▮▮▮▮▮▮▯▯▯▯")
	test6()

	print("\nRunning tests 7/10 => ▮▮▮▮▮▮▮▯▯▯")
	test7()

	print("\nRunning tests 8/10 => ▮▮▮▮▮▮▮▮▯▯")
	test8()

	print("\nRunning tests 9/10 => ▮▮▮▮▮▮▮▮▮▯")
	test9()

	print("\nRunning tests 10/10 => ▮▮▮▮▮▮▮▮▮")
	test10()

