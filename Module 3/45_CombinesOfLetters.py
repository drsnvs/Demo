# 45. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# o Sample data: {'1': ['a','b'], '2': ['c','d']}
# o Expected Output:
# o ac ad bc bd

sample_data = {'1': ['a','b'], '2': ['c','d']}

for i in sample_data['1']:
    for j in sample_data['2']:
        print(i+j)