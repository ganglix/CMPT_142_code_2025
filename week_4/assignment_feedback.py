
# a2q3
# clean_grades()
# These changes should be done by modifying the input list itself. No new lists should be created and this
# function has no return value.

# reduced example:

student_grades = [1, 1, 1, 1]

def clean_grades(grade_list):
    """
    add two to all grades in the input list (no new list is returned)
    :param grade_list: list, a list of grades
    :return: None
    """
    for i in range(len(grade_list)):
        grade_list[i] += 2

print('before cleaning:', student_grades)
clean_grades(student_grades)
print(student_grades)


def clean_grades(grade_list):
    """
    add two to all grades in the input list and return it as a new list
    :param grade_list: list, a list of grades
    :return: None
    """
    new_grades = []
    for grade in grade_list:
        new_grades.append(grade + 2)
    return new_grades