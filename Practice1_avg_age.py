patient_visits = [
    {'patient_id': 'P001', 'name': 'Alice', 'age': 45, 'visit_date': '2024-05-10'},
    {'patient_id': 'P002', 'name': 'Bob', 'age': 62, 'visit_date': '2024-05-11'},
    {'patient_id': 'P003', 'name': 'Charlie', 'age': 38, 'visit_date': '2024-05-12'},
    {'patient_id': 'P004', 'name': 'Diana', 'age': 71, 'visit_date': '2024-05-13'},
    {'patient_id': 'P005', 'name': 'Eve', 'age': 55, 'visit_date': '2024-05-14'}
]

total_age= 0
max_age = 0
oldest_pt_name = ""

for patient in patient_visits:
    age = patient['age']
    total_age += age
    # print(total_age)
    if age > max_age:
        max_age = age
        oldest_pt_name = patient["name"]
        # print(oldest_pt_name)
print(f"The name of oldest patient is {oldest_pt_name}")


    
num_pt= len(patient_visits)
avg = total_age/num_pt

print(f"The average age of patients in the given data set is {avg} years")

