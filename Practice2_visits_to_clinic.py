#Practice 2
appointments = [
    {'patient_id': 'P001', 'visit_type': 'Check-up', 'bill_amount': 250, 'doctor': 'Dr. Evans'},
    {'patient_id': 'P002', 'visit_type': 'Follow-up', 'bill_amount': 150, 'doctor': 'Dr. Smith'},
    {'patient_id': 'P003', 'visit_type': 'Check-up', 'bill_amount': 250, 'doctor': 'Dr. Evans'},
    {'patient_id': 'P004', 'visit_type': 'Emergency', 'bill_amount': 800, 'doctor': 'Dr. Chen'},
    {'patient_id': 'P005', 'visit_type': 'Follow-up', 'bill_amount': 150, 'doctor': 'Dr. Smith'},
    {'patient_id': 'P006', 'visit_type': 'Check-up', 'bill_amount': 250, 'doctor': 'Dr. Evans'},
    {'patient_id': 'P007', 'visit_type': 'Emergency', 'bill_amount': 800, 'doctor': 'Dr. Chen'},
    {'patient_id': 'P008', 'visit_type': 'Follow-up', 'bill_amount': 150, 'doctor': 'Dr. Smith'},
]

visit = ""
bill = 0
doc_count = {}

for app in appointments:
    if app["visit_type"] == "Check-up":
        bill += app["bill_amount"]
    current_doc = app['doctor']
    if current_doc in doc_count:
        doc_count[current_doc] +=1
    else:
        doc_count[current_doc] = 1

#print(doc_count)    
print(max(doc_count, key=doc_count.get))
print (f" The sum of all bills of patients that came for Check-up is {bill}")