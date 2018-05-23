File: README.md

Authors: Joseph Hwang & Udacity Staff (AIND)


				--Project: Diagonal Sudoku AI Agent--


----------
Objectives
----------
Implement Naked Twins constraint propagation and implement a modified Sudoku AI Agent to solve Diagonal Sudoku

DETECTS AND SOLVES BOTH REGULAR AND DIAGONAL SUDOKU (DEFAULT)

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?

A: Constraint propagation is used to make the search space of a problem smaller by using knowledge of certain definitions like Only One choice for a digit in a unit is in a box in Sudoku means that that the only value for the box is the "only choice". Another example of constraint propagation is the eliminate(values) function which follows the Sudoku definition that a digit 1-9 can only appear once in a unit, thus eliminating any digits (that should be the only choice for certain boxes) from peers. Naked Twins definition is boxes which have twin possibilities can only exist in those boxes and must be rejected from any other boxes in the peers of the twins. I used constraint propagation as follows for my naked twins implementation:

"
	if len(values[box]) == 2:
		doubles.append(box)
"

Here I am only considering the boxes with 2 possible values and saving them in a list for this unit in the unitlist. Making problem space smaller.

"
	if len(doubles) > 1:
"

Here I am only proceeding to naked twins eliminations if the doubles list for this unit is greater than 1 otherwise there cannot be any twins. Making problem space smaller.

"
	same_dict = dict()
	for x in doubles:
		if not (values[x] in same_dict.keys()):
			same_dict[values[x]] = x
		else:
			twin = same_dict[values[x]]
			#eliminate twin values from peers
"

Here I created a dictionary to hash values to check in O(1) if there any of the doubles boxes are twins by searching if the string possibility is in the same_dict key (aka entered already).
If not, then I enter string, box as key,value pair.
If yes, then we have a twin. Then proceed to eliminate pairs. Making problem space smaller.

"
	twin = same_dict[values[x]]
	for peer in peers[x]:
		if peer in peers[twin]
"

Here I check only proceed with the following if the box is a peer of both twins pruning all the other possible peers to eliminate values from. Making problem space smaller.

And in the big picture, I used naked twins functionality as a constraint propagation in the reduce(values) function to reduce the problem space like eliminate(values) and only_choice(values) functions in every call to reduce_puzzle(values)

	"
		values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
	"

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?

A: The definition of a diagonal sudoku is the addition of a constraint to regular sudoku which forces solvers to account the A1 - I9 and A9 - I1 main diagonals as a sudoku unit.
Simply implementing this definition is a constraint propagation. I achieved this by creating a helper function:
	def create_diag(rows, cols):
which returns the two main diagonal units as a list.
Then I added this diag_units list to the "unitlist" which the rest of the python script iterates through to search for a solution, which effectively calls the solver to only consider diagonal sudoku and return False/not solvable if not a diagonal sudoku.


--------------------------------------------
Sub-Modules and Components
--------------------------------------------
solution.py

pygame visualization files: PySudoku.py, visualize.py

solution_test.py # unit test

-------------------------
INSTALL & RUN Information
-------------------------
*From Project Requirements Udacity AIND

"
	### Install

	This project requires **Python 3**.

	##### Optional: Pygame

	Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

	If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

"

--------------------
Command Line Input
--------------------

		solution.py

Command Input:  python solution.py [optional sudoku string]
Example: 

python solution.py .45...63.2...1...59..8.5..7..9...3...3.....7...8...5..8..5.3..15...2...3.26...95.

if no optional argument - will solve hardcoded diagonal string in solution.py

--------------------------------------------
Testing
--------------------------------------------
To test the Diagonal Solver, I ran solution_test.py for unit tests created by
Udacity AIND staff.

		solution_test.py

Command Input:  python solution_test.py

and also searched random diagonal puzzles ranging in difficulty and manually entered them as command line arguments.
