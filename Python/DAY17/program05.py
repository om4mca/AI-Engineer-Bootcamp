#--------------------------------------------
# AI Engineer Bootcamp
# Day 17
# Program: Dictionary Iterator
# Author: Om Roy
# Date: 22-07-2026
#--------------------------------------------

patient = {"id": 101, "name": "Om", "age": 42, "bill": 5000}

# 1. Default Iteration (Iterates over KEYS)
key_iter = iter(patient)
print(type(key_iter))  # <class 'dict_keyiterator'>
print(next(key_iter))  # 'id'
print(next(key_iter))  # 'name'

# 2. Iterating over VALUES
val_iter = iter(patient.values())
print(type(val_iter))  # <class 'dict_valueiterator'>
print(next(val_iter))  # 101
print(next(val_iter))  # 'Om'

# 3. Iterating over ITEMS (Key-Value Tuples)
item_iter = iter(patient.items())
print(type(item_iter))  # <class 'dict_itemiterator'>
print(next(item_iter))  # ('id', 101)
print(next(item_iter))  # ('name', 'Om')