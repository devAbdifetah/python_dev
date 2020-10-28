students = {
           "male": ["Tom", "charles", "dhoore", "osman dhoore"],
           "female":["xalimo", " kadra", "amina", "sacda"]
           }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(key)
