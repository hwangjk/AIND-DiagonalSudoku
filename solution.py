"""* ========================================================================== */
/* File: solution.py
 *
 * Project name: Diagonal Sudoku AI Agent
 * Authors: Joseph Hwang & Udacity Staff (AIND)
 * Mentor: Khushboo Tiwari
 *
 * Description: This python script defines functionality of a Sudoku agent capable of
 *     solving regular and diagonal sudokus using Eliminate,Only Choice, Naked Twins
 *     contraint propagations, solves both Regular and Diagonal Sudoku using Recursive Depth First Search
 *     , and shows ASCII and Pygame visualization
 *
 * Usage:
 *
 *         python solution.py
 *
 *                 or
 *
 *         python solution.py 2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3
 *
 * 		   Run using Anaconda package env listed in UNIX and Windows aind-environment yml files included
 *
 * Input: (optional) starting sudoku string
 *         otherwise - solves hardcoded starting sudoku string in body of script
 *
 * Output: Terminal Display of Solved Sudoku and if Pygame is installed then visualization
 *
 * Citation: Some definitions were implemented during lectures or cited from lecture notes in Udacity's AIND program.
 *
 */
/* ========================================================================== */
"""
import sys  #command line options

assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

def create_diag(rows, cols):
    """
    creates a diagonal units list
    Args:
        rows list and cols list
    Returns:
        list of diagonal units """
    l = []
    s1 = []
    s2 = []
    n = len(rows)

    for i in range(n):
        s1.append(rows[i] + cols[i])
        s2.append(rows[i] + cols[(n-1) - i])
    l.append(s1)
    l.append(s2)

    return l


boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diag_units = create_diag(rows, cols)
unitlist = row_units + column_units + square_units + diag_units
reg_unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)



def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    #TODO::

    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

    for l in unitlist:
        doubles = []      #keep track of boxes wth 2
        for box in l:
            if len(values[box]) == 2:
                doubles.append(box)
        if len(doubles) > 1:
            # check for twins
            same_dict = dict()    #hashing to check if doubles are twins
            for x in doubles:
                if not (values[x] in same_dict.keys()):
                    # print(values[x])
                    same_dict[values[x]] = x
                else:
                    twin = same_dict[values[x]]
                    #eliminate twin values from peers
                    for peer in peers[x]:
                        if peer in peers[twin]:
                            #check others in twins
                            if peer == twin:
                                pass
                            else:
                                #eliminate values from twin peers
                                for m in values[x]:
                                    if m in values[peer]:
                                        new_string = values[peer].replace(m,'')
                                        assign_value(values, peer, new_string)
                                    else:
                                        pass
                        else:
                            pass
    return values




def grid_values(grid):
    """
    * Cited from Udacity-AIND Lectures
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    * Cited from Udacity-AIND Lectures
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print


def eliminate(values):
    """
    * Cited from Udacity-AIND Lectures
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            r_value = values[peer].replace(digit,'')
            # values[peer] = values[peer].replace(digit,'')
            values = assign_value(values, peer, r_value)
    return values

def only_choice(values):
    """
    * Cited from Udacity-AIND Lectures
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], digit)
                # values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    """
    * Cited from Udacity-AIND Lectures
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)  #added naked_twins
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    """
    * Cited from Udacity-AIND Lectures
    Using depth-first search and propagation, create a search tree and solve the sudoku."
    First, reduce the puzzle using the previous function
    """
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

    return search(grid_values(grid))


#----------SCRIPT----------#

if __name__ == '__main__':

    if len(sys.argv) > 1:
        sudoku_grid = sys.argv[1]
    else:
        sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    # TRY DIAGONAL SUDOKU SOLVE - DEFAULT
    d_display = solve(sudoku_grid)

    if d_display:
    	display(d_display)
    else:
        # TRY REGULAR SUDOKU SOLVE - CHANGE VARIABLE DEPENDENCIES to REG SETTINGS

        unitlist = reg_unitlist
        units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
        peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

        r_display = solve(sudoku_grid)

        if r_display:
        	display(r_display)
        else:
        	sys.exit("Not Solvable as a Diagonal or Regular Sudoku")
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('Pygame not installed/working. No visualization.')
