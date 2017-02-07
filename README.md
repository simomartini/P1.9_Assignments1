# P1.9_Assignments1

Assignments P1.9 - Part 1
Python Function Tabulation/Plot Project
Create an empty git repository and write a small plain python script (no subprograms, no
classes, compatible with python2 and python3) that creates two lists (xval, yval) and populates
xval with evenly spaced numbers between -5.0 and 5.0 (inclusive, 0.1 apart) and yval with the
corresponding y=f(x) values. The resulting two lists shall be visualized with matplotlib as a plot
with x and y values. The program shall take a number as command line argument and
depending on that number, yval will be filled from a different function. Implement this basic
program with support for only f(x) = x as function number 1. Write this program in stages (handle
command line, fill lists, plot lists) and commit after each step is complete and the program is
working this far.

Now create a branch “polynomial” off the trunk (aka “master”) and implement two additional
functions: f(x) = x**2, f(x) = x**3 as number 2 and number 3. Then create a second branch
“trigonometric” off the trunk and implement three additional functions: f(x) = sin(x), f(x) = cos(x),
f(x) = tan(x) as number 2, 3 and 4.

Finally, create a branch “development” off of “master” and add support for printing a “Usage: ...“
message with a list of the supported functions and the corresponding numbers, if no arguments
are given. Create a third branch “irrational” off this “development” branch and implement the
functions: exp(x), and sqrt(|x|) and update the usage message accordingly.

Switch to branch “polynomial” and merge in the changes from “development”. Then update the
usage message. Now switch to “trigonometric”, also merge from “development”, and update the
usage message as well. Now switch back to “development” and and change the plot interval
from [-5.0; 5.0] to [-3.0; 3.0]. Merge this change to the three other branches.

Create a branch “release_candidate” from “development” and merge in “polynomial”,
“trigonometric”, and then “irrational” and resolve any conflicts in between. Update the usage
message as needed. Test this version thoroughly, make corrections as needed and finally
merge “release_candidate” to “development” and “master”. Delete all branches except “development”.
Add a tag “release_v1” to “master” when done.
