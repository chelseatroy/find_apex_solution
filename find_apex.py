class ApexNotFoundException(Exception):
    # I want to be EXPLICIT when something didn't work as expected
    # So no client can accidentally proceed with a non-nominal result.
    pass

# We don't use this in the solution, but I included it to compare
# the effect of a recursive vs an iterative binary search strategy
# on the stack (Python doesn't have tail call optimization). See video for details.
def find_apex_recursive(collection, start, end): # Collection passed in initial call should already contain integers, for speed
    mid = start + ((end - start) // 2)

    if collection[mid + 1] < collection[mid] > collection[mid - 1]:
        return collection[mid], mid

    if collection[mid] > collection[mid - 1]:
        return find_apex_recursive(collection, mid + 1, end)
    else:
        return find_apex_recursive(collection, start, mid - 1)

    raise ApexNotFoundException("")


def find_apex_iterative(collection):
    start = 0
    end = len(collection)
    step = 0

    while start <= end:
        step = step + 1
        mid = start + ((end - start) // 2) # See Alberto Savoia's explanation in 'Beautiful Tests' of why we do it this way

        before = int(collection[mid + 1])
        maybe_apex = int(collection[mid])
        after = int(collection[mid - 1])

        if before < maybe_apex > after:
            return maybe_apex, mid

        if maybe_apex > after:
            start = mid + 1
        else:
            end = mid - 1

    raise ApexNotFoundException()

