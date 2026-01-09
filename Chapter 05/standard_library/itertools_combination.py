import itertools

# it = itertools.combinations(range(1, 46), 6)
# for num in it:
#     print(num)

print(len(list(itertools.combinations(range(1, 46), 6))))

print(len(list(itertools.combinations_with_replacement(range(1, 46), 6))))