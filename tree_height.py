# python3
#221REB054 Marija Tulovska 13.grupa
import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0 

    def height(i):
        if  node_tree[i] != 0:
            return node_tree[i]
        if parents[i] != -1:
            node_tree[i] = height(parents[i]) + 1
        if parents[i] == -1:
            node_tree[i] = 1

        return node_tree[i]

    # Your code here
    node_tree = numpy.zeros(n)
    for i in range(n):
        height(i)
        
    max_height = int(max(node_tree))
    return max_height


def main():
    # implement input form keyboard and from files
    test = input("F or I : ")

    if "I" in test:
        # input number of elements
        n = int(input("The number of nodes: "))
        # input values in one variable, separate with space, split these values in an array
        parents = (list(map(int, input("Nodes: ").split())))
        print(compute_height(n, parents))
        

    if "F" in test:
        fails = "test/" + input("File: ")
        # let user input file name to use, don't allow file names with letter a
        if not "a" in fails:
            with open(fails, "r") as file:
                
                n = int(file.readline())
                parents = (list(map(int, file.readline().split())))

        
                print(compute_height(n, parents))

    
    # account for github input inprecision
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
