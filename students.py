import numpy as np


# PART 1: A Python list of student names
students = ["Amina", "Brian", "Carol", "David"]

print("STUDENT LIST")
print(students)


# PART 2: A NumPy array of student names
student_names = np.array(students)

print("\nSTUDENT NAMES ARRAY")
print(student_names)


# PART 3: A Python list of student ages
# Each age matches the student in the same position.
student_ages = [20, 21, 19, 22]

print("\nSTUDENT AGES LIST")
print(student_ages)


# PART 4: A NumPy array showing ages in two years
ages_array = np.array(student_ages)
ages_in_two_years = ages_array + 2

print("\nAGES IN TWO YEARS")
print(ages_in_two_years)

for name, age, future_age in zip(
    students, student_ages, ages_in_two_years
):
    print(f"{name}: now {age}, in two years {future_age}")


# PART 5: Create, edit, add to, and delete from a 2D array
# Each row contains two example marks.
marks_2d = np.array([
    [70, 80],
    [65, 75]
])

print("\nORIGINAL 2D ARRAY")
print(marks_2d)
print("Dimensions:", marks_2d.ndim)
print("Shape:", marks_2d.shape)

# Edit the value in the first row, second column.
marks_2d[0, 1] = 85

print("\n2D ARRAY AFTER EDITING")
print(marks_2d)

# Add a new row.
marks_2d = np.append(marks_2d, [[90, 95]], axis=0)

print("\n2D ARRAY AFTER ADDING A ROW")
print(marks_2d)

# Delete the second row, which has index 1.
marks_2d = np.delete(marks_2d, 1, axis=0)

print("\n2D ARRAY AFTER DELETING A ROW")
print(marks_2d)


# PART 6: Create, edit, add to, and delete from a 3D array
# This array contains two layers.
# Each layer has two rows and two columns.
marks_3d = np.array([
    [
        [70, 80],
        [65, 75]
    ],
    [
        [85, 90],
        [78, 88]
    ]
])

print("\nORIGINAL 3D ARRAY")
print(marks_3d)
print("Dimensions:", marks_3d.ndim)
print("Shape:", marks_3d.shape)

# Edit the first layer, first row, second column.
marks_3d[0, 0, 1] = 82

print("\n3D ARRAY AFTER EDITING")
print(marks_3d)

# Create and add a new layer.
new_layer = np.array([
    [
        [91, 92],
        [93, 94]
    ]
])

marks_3d = np.append(marks_3d, new_layer, axis=0)

print("\n3D ARRAY AFTER ADDING A LAYER")
print(marks_3d)

# Delete the second layer, which has index 1.
marks_3d = np.delete(marks_3d, 1, axis=0)

print("\n3D ARRAY AFTER DELETING A LAYER")
print(marks_3d)


# PART 7: A dictionary containing student records
# The outer dictionary uses student IDs as keys.
# Each value is another dictionary holding student details.
student_data = {
    "S001": {
        "Name": "Amina",
        "Age": 20,
        "DOB": "2006-01-15",
        "Location": "Nairobi"
    },
    "S002": {
        "Name": "Brian",
        "Age": 21,
        "DOB": "2005-03-22",
        "Location": "Mombasa"
    },
    "S003": {
        "Name": "Carol",
        "Age": 19,
        "DOB": "2007-07-10",
        "Location": "Kisumu"
    },
    "S004": {
        "Name": "David",
        "Age": 22,
        "DOB": "2004-09-05",
        "Location": "Nakuru"
    }
}

print("\nSTUDENT DICTIONARY")

for student_id, details in student_data.items():
    print(student_id, details)

print("\nNAME OF STUDENT S001")
print(student_data["S001"]["Name"])