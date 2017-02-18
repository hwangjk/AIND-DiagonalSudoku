File: README.md
Authors: Joseph Hwang & Udacity AIND Staff


				--Diagonal Sudoku AI Agent Project--


----------
Objectives
----------
Implement Naked Twins constraint propagation and modify a Sudoku AI Agent
to solve Diagonal Sudokus

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?
A: *Student should provide answer here*

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?
A: *Student should provide answer here*

--------------------------------------------
Sub-Modules and Components
--------------------------------------------
solution.py
pygame visualization

solution_test.py # for tests

-------------------------
INSTALL & RUN Information
-------------------------
*From Project Requirements Udacity AIND

"
	### Install

	This project requires **Python 3**.

	We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
	Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

	##### Optional: Pygame

	Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

	If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

	### Code

	* `solutions.py` - You'll fill this in as part of your solution.
	* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
	* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
	* `visualize.py` - Do not modify this. This is code for visualizing your solution.

	### Visualizing

	To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

	### Data

	The data consists of a text file of diagonal sudokus for you to solve.
"

--------------------
Command Line Input
--------------------

		solution.py

Command Input:  python solution.py [optional diagonal sudoku string]
Example:  python solution.py .45...63.2...1...59..8.5..7..9...3...3.....7...8...5..8..5.3..15...2...3.26...95.
.45...63.2...1...59..8.5..7..9...3...3.....7...8...5..8..5.3..15...2...3.26...95.

if no optional argument - will solve hardcoded diagonal string in solution.py

--------------------------------------------
Testing
--------------------------------------------
To test the Diagonal Solver, I ran solution_test.py for unit tests created by
Udacity AIND staff.

		solution_test.py

Command Input:  python solution_test.py

--------------------------------------------
Design & Strategy Decisions
--------------------------------------------
*Please see Design Spec for more information




==============================================================================
						   Data Flow - Block Diagram
==============================================================================


1.       |------------------|       AMInit       |-----------------|
   	     |    AMStartup     |      =======>      |     SERVER      |   ==>
	     |------------------|			         |-----------------|

2.       |------------------|     AM_Init_OK     |-----------------|
     ==> |    SERVER        |      ======>       |     AMStartup   |   ==>
         |------------------|	   MazePort	     |-----------------|


3.       |------------------|      AM_Avatar     |-----------------|
   	 ==> |    AMStartup     |       ======>      |     AMAvatar    |   ==>
         |------------------|	     CALL        |-----------------|


4	     |------------------|  AM_Avatar_Ready   |-----------------|
	 ==> |    AMAvatar      |      =======>    	 |     SERVER      |   ==>
	     |------------------|	         	     |-----------------|

5. nAvatar x times
	     |------------------|    AM_Avatar_Turn  |-----------------|
	 ==> |    SERVER        |      =======>    	 |     AMAvatar    |   ==>
    	 |------------------|	   MazePort	     |-----------------|

6. nAvatar x times
	     |------------------|   AM_Avatar_Move   |-----------------|
	 ==> |    SERVER        |      =======>    	 |     AMStartup   |   ==>
    	 |------------------|	   			     |-----------------|


7.	     |------------------|      AMInitOK      |-----------------|
	 ==> |    SERVER        |      =======>    	 |     AMStartup   | ==>
    	 |------------------|	   			     |-----------------|

loop 5-7 until a) solved or b) socket broken c) wait time exceeded d) server max moves exceeded

8.
	     |------------------|    AM_MAZE_SOLVED  |-----------------|
	 ==> |    SERVER        |      =======>    	 |     AM_AVATAR   | ==>
    	 |------------------|	   			     |-----------------|


8.
	     |------------------|  Write to Logfile  |-----------------|
	 ==> |    AM_Avatar     |      =======>    	 |     AM_AVATAR   | ==>
    	 |------------------|	  FREE MEMORY 	 |-----------------|








contact info: joseph.c.hwang.17@dartmouth.edu
			  hwangjk012@hotmail.com
Linkedin:	  https://www.linkedin.com/in/joseph-hwang-8400b271
