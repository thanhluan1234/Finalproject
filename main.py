# Read number of set
number_of_sets = int(input("Enter the number of sets: "))
list_of_sets = []

# Read sets
for i in range(number_of_sets):
    input_set = set(input("Enter elements in set, seprated by a space: ").split())
    list_of_sets.append(input_set)

"""
Set Operations
"""

while True:
    # User guide
    print()
    print("- Set Operations -")
    print("1 Difference")
    print("2 Intersection")
    print("3 Symmetric Difference")
    print("4 Union")
    print("5 View your sets")
    print("0 Exit")
    print()

    choose = input("Choose the function: ")

    # Difference operation
    if choose == "1":
        [s1, s2] = input("Choose 2 sets to operate (Enter its number seprated by a space): ").split()

        first = set(list_of_sets[int(s1)-1])
        second = set(list_of_sets[int(s2)-1])

        print("The first set is", first)
        print("The second set is", second)
        print("The difference result is", first.difference(second))
    
    # Intersection operation
    elif choose == "2":
        [s1, s2] = input("Choose 2 sets to operate (Enter its number seprated by a space): ").split()

        first = set(list_of_sets[int(s1)-1])
        second = set(list_of_sets[int(s2)-1])

        print("The first set is", first)
        print("The second set is", second)
        print("The Intersection result is", first.intersection(second))

    # Symmetric Difference operation
    elif choose == "3":
        [s1, s2] = input("Choose 2 sets to operate (Enter its number seprated by a space): ").split()

        first = set(list_of_sets[int(s1)-1])
        second = set(list_of_sets[int(s2)-1])

        print("The first set is", first)
        print("The second set is", second)
        print("The symmetric differencet is", first.symmetric_difference(second))

    # Union operation
    elif choose == "4":
        [s1, s2] = input("Choose 2 sets to operate (Enter its number seprated by a space): ").split()

        first = set(list_of_sets[int(s1)-1])
        second = set(list_of_sets[int(s2)-1])

        print("The first set is", first)
        print("The second set is", second)
        print("The union result is", first.union(second))

    # View all of sets
    elif choose == "5":
        print("Your sets are")
        for i in list_of_sets:
            print(list_of_sets.index(i), end="\t")
            print(i)

    # Exit
    elif choose == "0":
        print("Good bye")
        break
    
    # Catch invalid choose operation
    else:
        print("Your choose is wrong! Please try again")