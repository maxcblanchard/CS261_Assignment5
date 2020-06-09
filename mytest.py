from hash_map import *

student_map = HashMap(10, hash_function_1)
test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20),
                       ("set", 10), ("anotha_one", -7), ("completely_different", 5), ("getting_there", -1)]
for key, val in test_values:
    student_map.put(key, val)
print(student_map)
print(student_map.size)