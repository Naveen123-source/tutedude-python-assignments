students = {"Mike":80,"Nick":90,"Alice":100}
studentName = input("Enter the student's name:")
if studentName in students:
    print(f"{studentName}'s marks: {students[studentName]}")
else:
    print("Student not found.")