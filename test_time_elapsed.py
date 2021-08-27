import timeit

from process_file import process_file

def print_runtime_for_processing(filename):
    start = timeit.timeit()
    process_file(filename)
    end = timeit.timeit()
    print(f"Processed file {filename} in {(end - start) * 1000} milliseconds")

print_runtime_for_processing('teenylines.txt')

print_runtime_for_processing('biglines.txt')