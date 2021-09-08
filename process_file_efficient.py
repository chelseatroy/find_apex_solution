import os

def process_file_efficient(filename):
    start, end = 0, os.path.getsize(filename)

    def is_smaller(maybe_smaller, comparator):
        if len(maybe_smaller) != len(comparator):
            return len(maybe_smaller) < len(comparator)
        return maybe_smaller < comparator

    with open(filename, 'rb') as cursor:
        while True:
            bytes_position = start + (end - start) // 2
            print("Looking at %d" % bytes_position)
            cursor.seek(bytes_position)
            if bytes_position > 0:
                cursor.readline()  # this could be halfway through a line so we throw it out except if first line

            # strip removes newlines on the end, otherwise in two numeric strings
            # with the same number of chars, the one with the newline looks 'greater than'
            # the other one to this implementation of 'is_smaller'
            left = cursor.readline().strip()
            maybe_apex = cursor.readline().strip()

            # I define 'position' as my cursor position in bytes at the end of the apical line
            maybe_apex_position = cursor.tell()
            right = cursor.readline().strip()
            if left and maybe_apex and right:
                if is_smaller(left, maybe_apex) and is_smaller(right, maybe_apex):
                    return maybe_apex, maybe_apex_position
                if is_smaller(right, maybe_apex):
                    # Descending
                    end = bytes_position
                else:
                    # Ascending
                    start = bytes_position
            else:
                end = bytes_position

import cProfile
import pstats
from pstats import SortKey

cProfile.run('process_file_efficient("biglines.txt")', 'profiling.txt')

p = pstats.Stats('profiling.txt')
p.strip_dirs().sort_stats(-1).print_stats()

print("MOST CUMULATIVE TIME SPENT")
p.sort_stats(SortKey.CUMULATIVE).print_stats(10)

print("MOST TIME PER CALL")
p.sort_stats(SortKey.TIME).print_stats(10)

