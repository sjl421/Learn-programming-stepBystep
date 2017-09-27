import sys
def add_line_number(f):
    count = 1
    for line in f:
        print('%-60s # %d'%(line[:-2], count))
        count += 1

add_line_number(sys.stdin)
