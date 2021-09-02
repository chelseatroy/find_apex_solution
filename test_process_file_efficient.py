from process_file_efficient import process_file_efficient
from find_apex import ApexNotFoundException

apex, position = process_file_efficient('teenylines.txt')
assert apex == '464789283674898372468937463849837468798378'
assert position == 47

apex, position = process_file_efficient('biglines.txt')
assert apex.endswith('6894')

try:
    apex, position = process_file_efficient('only_ascending.txt')
    raise AssertionError("This should raise because the numbers only ascend in this file")
except ApexNotFoundException as e:
    if str(e) == "Numbers only ascend":
        pass
    else:
        raise AssertionError("Honestly, no idea what happened here")
try:
    apex, position = process_file_efficient('only_descending.txt')
    raise AssertionError("This should raise because the numbers only descend in this file")
except ApexNotFoundException as e:
    if str(e) == "Numbers only descend":
        pass
    else:
        raise AssertionError("Honestly, no idea what happened here")




