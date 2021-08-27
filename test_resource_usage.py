from resource import getrusage, RUSAGE_SELF

from process_file import process_file

def print_resource_usage_for_processing(filename):
    process_file(filename)
    print(f"Resource report for processing {filename}:")
    print(getrusage(RUSAGE_SELF))

print_resource_usage_for_processing('teenylines.txt')

print_resource_usage_for_processing('biglines.txt')