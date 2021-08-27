from process_file import process_file

# 'teenylines.txt' is a small file with 6 integers and a clear apex at index 2.
# This is sort of the 'smallest number of moving parts' smoke test for process_file.
item, index = process_file('teenylines.txt')
assert int(item) == 464789283674898372468937463849837468798378
assert index == 2
# The apex integer in this file is 464789283674898372468937463849837468798378 as opposed to 400
# Because I was using this file to make sure readlines() with a byte hint would never cut off
# right in the middle of a line.

# # 'biglines.txt' is a file with about 116 kb of data in seven REALLY long integers.
# # 116 kb exceeds process_file's default buffer setting of 80kb.
# # Its apex occurs at index 4 with a REALLY long integer that ends in '894.'
# # This is the 'happy path' case for files that require multiple batches of processing.
item, index = process_file('biglines.txt')
assert str(item).strip().endswith('894')
assert index == 4
# This test is how I discovered that I was failing to account for the
# size of final_items_previous_batch in calculating my output indices.

# 'inconvenient_split.txt` has a file size of 24 bytes.
# When processed with a working data limit of 10 bytes, it gets split right before the apex.
# This tests process_file's ability to identify an apex with a neighbor in a different batch.
item, index = process_file('inconvenient_split.txt', working_data_limit=10)
assert item == 110
assert index == 5
# This is how I realized I needed to convert the lines (which are strings)
# to integers in the binary search function. Strings have their own numerical
# representations, so calling inequality functions on them yields results,
# but they're not the same as the results if the same lines converted to integers.

# Same as above, except that when processed with a working data limit of 14 bytes,
# 'inconvenient_split.txt' gets split right AFTER the apex.
item, index = process_file('inconvenient_split.txt', working_data_limit=14)
assert item == 110
assert index == 5



