students = [
    ["BSIT", ["irvin","paul"]],
    ["BSSW", ["kristel","keigi","gi"]]
]

for course in students:
    print(course[0])
    for student in course[1]:
        print(student)
    print()