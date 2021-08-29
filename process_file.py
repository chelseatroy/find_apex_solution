from find_apex import find_apex_iterative, ApexNotFoundException

# working_data_limit represents the resource limitations of the machine the code is running on.
# I have made it artificially tiny (80kb) to force the behavior of batching up a file
# Without putting X00+ GB data files on my machine for a one hour code challenge :).
def process_file(filename, working_data_limit=80000):
    # I say 'cursor' here to communicate that the object
    # captures and uses our program's position WITHIN the file
    # If we were processing the whole file at once, line by line,
    # I'd probably do the more conventional 'with open(...) as file`
    with open(filename, 'r') as cursor:
        index = 0
        final_items_previous_batch = [0] # To handle finding apexes right before or after a batch break

        while True:
            batch = cursor.readlines(working_data_limit)
            if batch: # At the end of a file, readlines will give []. bool([]) is falsy in Python.
                if len(batch) == 1:
                    #Edge case: there's just one line in this batch
                    if int(batch[0]) > final_items_previous_batch[-1]:
                        raise ApexNotFoundException("Numbers only increase")
                    else:
                        # Did not extract this into a function, despite duplication on lines 32/33,
                        # because I try to wait for three occurrences before abstracting.
                        # It helps avoid prefactors that end up inaccurately modeling the
                        # processes they perform.
                        item, local_index = find_apex_iterative(final_items_previous_batch + batch)
                        return item, index + local_index - len(final_items_previous_batch)
                else:
                    last_in_batch = int(batch[-1])
                    second_last_in_batch = int(batch[-2])

                    if last_in_batch > second_last_in_batch: # then integers are still ascending
                        index += (len(batch))
                        final_items_previous_batch = [second_last_in_batch, last_in_batch]
                        continue
                    else: # integers have begun descending. Since we're evaluating batches sequentially, that means that this batch contains the apex.
                        item, local_index = find_apex_iterative(final_items_previous_batch + batch)
                        return item, index + local_index - len(final_items_previous_batch)
