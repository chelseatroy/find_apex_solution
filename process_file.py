from find_apex import find_apex_iterative, ApexNotFoundException

def process_file(filename, working_data_limit=80000):
    with open(filename, 'r') as cursor:
        index = 0
        final_items_previous_batch = [0]

        while True:
            batch = cursor.readlines(working_data_limit)
            if batch:
                if len(batch) == 1:
                    #edge case: one line in this batch
                    if batch[0] > final_items_previous_batch[-1]:
                        raise ApexNotFoundException("Numbers only increase")
                    else:
                        item, local_index = find_apex_iterative(final_items_previous_batch + batch)
                        return item, index + local_index - len(final_items_previous_batch)
                else:
                    if int(batch[-1]) > int(batch[-2]):
                        index += (len(batch))
                        final_items_previous_batch = batch[-2:]
                        continue
                    else:
                        item, local_index = find_apex_iterative(final_items_previous_batch + batch)
                        return item, index + local_index - len(final_items_previous_batch)
