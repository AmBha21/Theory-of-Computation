Authors:
- Amol Bhagavathi
- Liao Zhu
- Ilya Tataurov
All members completed the course evaluation as per extra credit requirements
All hawkids can be found in partner.txt

Tooling:
    - Python 2.7.18 or greater can be used to run
    - GraphViz is used to generate the pdf graph visualization seen in nfa_graph.png
    Please refer to requirements.txt for further details

All Sources:

All files ending with .py are needed to run the program. The python files are as listed:
    1. main.py: this is the entry to the program and creates an nfa from a desired regex, the ability to convert nfa -> dfa is also available
    2. regexp_to_nfa.py: converts a regex expression to nfa graphical form ===Outputs===> nfa.png
    3. nfa_to_dfa.py: converts nfa from main.py into dfa graphical form ====Outputs====> dfa.png
    4. nfa_datatype.py + regex_datatype.py: define our two datatypes needed to handle both regex and nfas

All test files are located in pyTests (a test suite directory)
    - TESTING.txt highlights certain test cases of different regex patterns
    - For each test case, a simple overview of how the test is ran as well as a high level overview of what we are expected of each test is given
    Further documentation can be found in TESTING.txt

Though all methods are important, some ones worth mentioning are:
    1. make_exp_tree: found in regexp_to_nfa.py and handles creating an expression tree which is later converted to an nfa
    2. create_dfa_graph: found in nfa_to_dfa.py and handles the conversion of nfa to dfa

    *Note the pyTests directory holds our python test files and are not part of the source files needed

Runner Source:
To run the program, run `python3 main.py` in the root directory of this project (note that '|' should be replaced by '+' if testing 'or')
    - two graphs are then generated
        1. nfa.png
        2. dfa.png
    - both of these graphs show the nfa and dfa representation of the regex

To test the program, cd into pyTests and run any of the (dfa|nfa)*.py test cases
    
*Note: State colored in blue is assumed to be the starting state for DFA, and Q1 is the start state for NFA