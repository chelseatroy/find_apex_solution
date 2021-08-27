class ApexNotFoundException(Exception):
    pass

def find_apex_recursive(collection, start, end): # collection passed in initial call should already contain integers, for speed
    mid = start + ((end - start) // 2)

    if collection[mid + 1] < collection[mid] > collection[mid - 1]:
        return collection[mid], mid

    if collection[mid] > collection[mid - 1]:
        return find_apex_recursive(collection, mid + 1, end)
    else:
        return find_apex_recursive(collection, start, mid - 1)

    raise ApexNotFoundException("")


def find_apex_iterative(collection):
    collection = [int(item) for item in collection]
    start = 0
    end = len(collection)
    step = 0

    while start <= end:
        # print(f"Subcollection in step {step}: {str(collection[start:end+1])}")
        step = step + 1
        mid = start + ((end - start) // 2)

        if collection[mid] > collection[mid - 1] and collection[mid] > collection[mid + 1]:
            return collection[mid], mid

        if collection[mid] > collection[mid - 1]:
            start = mid + 1
        else:
            end = mid - 1

    raise ApexNotFoundException()

