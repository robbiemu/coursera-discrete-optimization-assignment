import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from screenname import solver

input_data = ''

def test_solver():
    result = solver.solve_it(input_data)
    assert(result == 'I_R a-N00B')