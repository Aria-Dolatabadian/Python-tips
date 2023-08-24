# Define a dictionary to represent blood types and their compatibility
blood_types = {
    'A+': ['A+', 'AB+'],
    'A-': ['A+', 'A-', 'AB+', 'AB-'],
    'B+': ['B+', 'AB+'],
    'B-': ['B+', 'B-', 'AB+', 'AB-'],
    'AB+': ['AB+'],
    'AB-': ['AB+', 'AB-'],
    'O+': ['A+', 'B+', 'AB+', 'O+'],
    'O-': ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']
}

# Function to check if two individuals have compatible blood types for transfusion
def are_blood_types_compatible(person1_blood_type, person2_blood_type):
    return person1_blood_type in blood_types.get(person2_blood_type, [])

# Input blood types of two individuals
person2_blood_type = input("Enter the blood type of the donor person (e.g., B-): ").upper()
person1_blood_type = input("Enter the blood type of the recipient person (e.g., A+): ").upper()

# Check compatibility
if are_blood_types_compatible(person1_blood_type, person2_blood_type):
    print(f"The two individuals have compatible blood types for transfusion.")
else:
    print(f"The two individuals have incompatible blood types for transfusion.")
