import sys
sys.path.insert(0, '../')
from nfa_datatype import NFA
from regex_datatype import RegexPattern


def test_set_nfa():
    # Create an instance of NFA
    nfa = NFA()

    # Define a sample NFA dictionary
    nfa_dict = {
        'states': ['q0', 'q1', 'q2'],
        'letters': ['a', 'b'],
            'transition_function': [('q0', 'a', 'q1'), ('q1', 'b', 'q2')],
            'start_states': ['q0'],
            'final_states': ['q2']
        }

    # Set the NFA using the set_nfa method
    nfa.set_nfa(nfa_dict)

    # Assert that the NFA instance has been properly set
    try:
        assert nfa.nfa == nfa_dict
        print("Test set_nfa passed")
    except AssertionError as e:
        print(f"Assertion failed: set_nfa failed. Details: {e}")
        raise
    
def test_set_regex():
    # Create an instance of RegexPattern
    regex = RegexPattern()

    # Set a pattern using set_pattern method
    regex.set_pattern("a*")

    # Assert that the pattern has been properly set
    try:
        assert regex.pattern == "a*"
        print("Test set_regex passed")
    except AssertionError as e:
        print(f"Assertion failed: set_regex failed. Details: {e}")
        raise

if __name__ == "__main__":
        
    print("\nRunning tests 1/2 => ▮▯")
    test_set_nfa()
    print("\nRunning tests 2/2 => ▮▮")
    test_set_regex()
    print("\nAll tests passed (2/2)")
