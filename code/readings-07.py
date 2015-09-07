import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    if not action in ['-n', '-m', '-x']:
        print 'Action is not one of -n, -m, or -x: '
    else:
        if len(filenames) == 0:
            process(sys.stdin, action)
        else:
            for f in filenames:
                process(f, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')

    if action == '-n':
        values = data.min(axis=1)
    elif action == '-m':
        values = data.mean(axis=1)
    elif action == '-x':
        values = data.max(axis=1)

    for m in values:
        print m

main()
