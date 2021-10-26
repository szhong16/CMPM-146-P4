Sijia Zhong szhong16@ucsc.edu
Rob Lodes rlodes@ucsc.edu

Our heuristic strategy was to implement a method that would check to see if the current tool needed had previously been made. If the tool had been made, then we would not need to make another, or get caught in a loop of checking for the tool.
 
This check was direct to implement. We simply check within our current task if it was already in our list of tasks. If it was we returned false, and if it wasn't we returned true to prune the branch.
 
Also, we presorted our incoming data from the json file such that when the methods and the operators were added to our list they were already in the preferred order of use which was sorted based on time to produce. 