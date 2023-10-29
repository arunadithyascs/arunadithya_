class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    # Create a list of Student objects
    students = [
        Student("Logesh", "A101", 3.8),
        Student("Karthik", "B102", 4.5),
        Student("Bharath", "C103", 4.0),
        Student("Praveen", "D104", 3.9),
    ]

    # Sort students by CGPA in descending order
    sorted_students = sort_students(students)

    # Print the sorted list
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
