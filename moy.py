import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

cmd = str(input("test (y/n) :"))
if cmd == 'y':
    test = True
else:
    test = False


def attribute_data():
    """ return test data if test == True and T°B one otherwise """
    if test:
        # add all new set of test data
        data_set = [math_speed_test, math_ds_test, co_anglais_test, ce_anglais_test]
    else:
        # add all new set of T°B data
        data_set = [math_speed, math_ds, co_anglais, ce_anglais]
    return data_set


def nb_grades(grades):
    """ return the highest number of grades"""
    nb_notes = 0
    x = -1
    for i in grades:
        z = 0
        for j in i:
            if isinstance(j, (int, float)):
                z += 1
        if x < z:
            x = z
        nb_notes = x
    return nb_notes


def harmonize_grades(nb_notes):
    """ add None type to each lst of notes in order to make all of them contain the same number of values"""
    for i in grades:
        i.insert(0, None)
        z = 0
        for j in i:
            if isinstance(j, (int, float)):
                z += 1
        for k in range(nb_notes - z):
            i.append(None)


def display_values(x, data_set):
    for i in data_set:
        plt.ylim(0, 21)
        plt.gca().yaxis.set_major_locator(MultipleLocator(1))
        plt.xlim(0, nb_grades+1)
        plt.xlabel('évaluation')
        plt.ylabel('notes')
        plt.title('Notes Mathematiques 2021-2022 T°B')
        plt.grid(True)

        if i[2]:
            plt.plot(x, i[0], "o-", markersize=5, label=i[1])
    plt.legend()
    plt.show()


# -----------------------------------------------------------------------------------------------------------------------
# T°B values
math_speed = [[],
              "math rapide", False]
math_ds = [[], "math Ds", False]
co_anglais = [[],
              "anglais Co", False]
ce_anglais = [[],
              "anglais Ce", False]

# -----------------------------------------------------------------------------------------------------------------------
# [0] grades
# [1] description
# [2] display (True/False)
# test values
math_speed_test = [[8, 6, 16, 14, 16, 16, 18],
                   "math rapide", True]
math_ds_test = [[15.5, 4, 5, 12, 5, 1, 15, 15, 20, 2, 4, 3, 6],
                "math Ds", True]
co_anglais_test = [[17, 15, 18, 6, 20, 13],
                   "anglais Co", True]
ce_anglais_test = [[12, 19, 5, 20, 1, 15, 13, 13, 16, 3, 8, 3, 6],
                   "anglais Ce", True]

# -----------------------------------------------------------------------------------------------------------------------

data_set = attribute_data()

grades = []
for i in data_set:
    grades.append(i[0])

nb_grades = nb_grades(grades)
harmonize_grades(nb_grades)

x = []
for i in range(nb_grades+1):
    x.append(i)

print("test = {}".format(test))
display_values(x, data_set=data_set)
