import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def nb_grades(grades):
    """ return the highest number of grades"""
    nb_notes = 0
    x = -1
    for i in grades:
        if x < len(i):
            x = len(i)
        nb_notes = x
    return nb_notes


def harmonize_grades(nb_notes):
    """ add None type to each lst of notes in order to make all of them contain the same number of values"""
    harmonized_grades = []
    for i in grades:
        for j in range(nb_notes - len(i)):
            i.append(None)
            harmonized_grades.append(i)
    return harmonized_grades


speed_notes = [4, 3, 8, 7, 8, 8, 9]
ds_notes = [None, 15.5]

"""speed_notes = [4, 3, 8, 7, 8, 8, 9]
ds_notes = [None, 15.5, 4, 5, 12, 5, 1, 15, 15, 20, 2, 4, 3, 6]"""

speed_notes_20 = []

for i in speed_notes:
    speed_notes_20.append(i * 2)
speed_notes_20.insert(0, None)

grades = [speed_notes_20, ds_notes]


nb_grades = nb_grades(grades)
harmonized_grades = harmonize_grades(nb_grades)

x = []
for i in range(nb_grades):
    x.append(i)

plt.ylim(0, 21)
plt.gca().yaxis.set_major_locator(MultipleLocator(1))
plt.xlim(0, nb_grades)
plt.plot(x, speed_notes_20, "o-", markersize=5, label='notes calcul rapide')
plt.plot(x, ds_notes, "o-", markersize=5, label='notes DS')
plt.xlabel('évaluation')
plt.ylabel('notes')
plt.title('Notes Mathematiques 2021-2022 T°B')
plt.grid(True)
plt.legend()
plt.show()
