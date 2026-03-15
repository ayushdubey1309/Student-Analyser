# mini project 1 student analyser


student=[

{"name": "Ayush" , "marks" : 87 },
{"name": "Rahul" , "marks" : 65 },
{"name": "Athrav" , "marks": 97},
{"name": "Ayushi" , "marks": 100},
{"name": "Udit" , "marks":87},
{"name": "Anjali", "marks":34},
{"name": "Neha" , "marks":45},
{"name": "Vikash" , "marks":67},
{"name": "Priya" , "marks":78},


]
#print all student
print("All Students")
for a in student:
    print(f"{a['name']} {a['marks']}")

# Find Topper

topper = max ( student , key= lambda x: x['marks'])
print(f"\nTopper:{topper['name']} with {topper['marks']}")

#student who pased 

passed = [s for s in student if s['marks']>50]
print (f"\n Paseed: {len(passed)}student")

#avrage marks

avg=sum(s['marks']for s in student)/ len(student)
print (f"\nClass Average:{avg:.2f}")




