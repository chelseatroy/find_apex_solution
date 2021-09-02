import os
from find_apex import ApexNotFoundException


def is_smaller(maybe_smaller, comparator):
    if len(maybe_smaller) != len(comparator):
        return len(maybe_smaller) < len(comparator)
    return maybe_smaller < comparator

print(is_smaller('', '1'))

def process_file_efficient(filename):
    size = os.path.getsize(filename)
    proportion_through_file = 0.5

    def is_smaller(maybe_smaller, comparator):
        if len(maybe_smaller) != len(comparator):
            return len(maybe_smaller) < len(comparator)
        return maybe_smaller < comparator

    with open(filename, 'r') as cursor:
        while True:
            bytes_position = size * proportion_through_file
            if bytes_position < 1:
                raise ApexNotFoundException("Numbers only descend")
            cursor.seek(bytes_position)
            cursor.readline() # this could be halfway through a line so we throw it out

            # strip removes newlines on the end, otherwise in two numeric strings
            # with the same number of chars, the one with the newline looks 'greater than'
            # the other one to this implementation of 'is_smaller'
            left = cursor.readline().strip()
            maybe_apex = cursor.readline().strip()
            maybe_apex_position = cursor.tell()
            right = cursor.readline().strip()

            if is_smaller(left, maybe_apex):
                if(is_smaller(right, maybe_apex)):
                    if right == '':
                        raise ApexNotFoundException("Numbers only ascend")
                    return maybe_apex, maybe_apex_position # I define 'position' as my cursor position in bytes at the end of the apical line
                else:
                    #update the indices to do the right half and run again
                    proportion_through_file = proportion_through_file + ((size - proportion_through_file) / 2)
            elif is_smaller(right, maybe_apex):
                #update the indices to do the left half and run again
                proportion_through_file = 0.0 + ((proportion_through_file - 0.0) / 2)