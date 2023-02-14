from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

if __name__ == '__main__':
    print("The cartesian product using repeat:")
    print(list(product([1, 2], repeat=2)))
    print()

    print("The cartesian product of the containers:")
    print(list(product(['geeks', 'for', 'geeks'], '2')))
    print()

    print("The cartesian product of the containers:")
    print(list(product('AB', [3, 4])))

    print("All the permutations of the given list is:")
    print(list(permutations([1, 'geeks'], 2)))
    print()

    print("All the permutations of the given string is:")
    print(list(permutations('AB')))
    print()

    print("All the permutations of the given container is:")
    print(list(permutations(range(3), 2)))

    print("All the combination of list in sorted order(without replacement) is:")
    print(list(combinations(['A', 2], 2)))
    print()

    print("All the combination of string in sorted order(without replacement) is:")
    print(list(combinations('AB', 2)))
    print()

    print("All the combination of list in sorted order(without replacement) is:")
    print(list(combinations(range(2), 1)))

    print("All the combination of string in sorted order(with replacement) is:")
    print(list(combinations_with_replacement("AB", 2)))
    print()

    print("All the combination of list in sorted order(with replacement) is:")
    print(list(combinations_with_replacement([1, 2], 2)))
    print()

    print("All the combination of container in sorted order(with replacement) is:")
    print(list(combinations_with_replacement(range(2), 1)))
