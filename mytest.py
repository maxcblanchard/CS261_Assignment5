from hash_map import *

""" EMPTY BUCKETS """
print("\n\n********   EMPTY_BUCKETS()   ********")
print("--- EXAMPLE 1 ---")
m = HashMap(100, hash_function_1)
print(m.empty_buckets(), m.size, m.capacity)
m.put('key1', 10)
print(m.empty_buckets(), m.size, m.capacity)
m.put('key2', 20)
print(m.empty_buckets(), m.size, m.capacity)
m.put('key1', 30)
print(m.empty_buckets(), m.size, m.capacity)
m.put('key4', 40)
print(m.empty_buckets(), m.size, m.capacity)

print("--- EXAMPLE 2 ---")
m = HashMap(50, hash_function_1)
for i in range(150):
    m.put('key' + str(i), i * 100)
    if i % 30 == 0:
        print(m.empty_buckets(), m.size, m.capacity)