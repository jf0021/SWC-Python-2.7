import sys
import glob

def main():
    '''prints names of all files with sys.argv as suffix'''
    if len(sys.argv) < 2:
        print 'Argument list cannot be empty'
    else:
        suffix = sys.argv[1] # NB: behaviour is not as you'd expect if sys.argv[1] is *
        glob_input = '*.' + suffix # construct the input
        glob_output = glob.glob(glob_input) # call the glob function
        for item in glob_output: # print the output
            print item
        return

main()