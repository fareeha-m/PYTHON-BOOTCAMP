#THE CHALLENGE
I am a data analyst at a clinic. I have been given a list of patient's visit record. Each record is a dictionary containing information about a single visit.
## Tasks:
    1. Take list of dictionary as input
    2. Calculate the avg age of all patients in the list
    3. Find the oldest patient in the list
    4. Return both of these values
## Data Set:
patient_visits = [
    {'patient_id': 'P001', 'name': 'Alice', 'age': 45, 'visit_date': '2024-05-10'},
    {'patient_id': 'P002', 'name': 'Bob', 'age': 62, 'visit_date': '2024-05-11'},
    {'patient_id': 'P003', 'name': 'Charlie', 'age': 38, 'visit_date': '2024-05-12'},
    {'patient_id': 'P004', 'name': 'Diana', 'age': 71, 'visit_date': '2024-05-13'},
    {'patient_id': 'P005', 'name': 'Eve', 'age': 55, 'visit_date': '2024-05-14'}
]

#SOLUTION
    1. scan through data set and find the age key 
    2. create a loop
    3. use "patients" as items in the list i.e "patient_visits"
    4. add all ages
    5. divide by len() of the list
    6.