def find_employee_age(employee_dict, target_id):
    # Check if the current employee is the target
    if employee_dict["id"] == target_id:
        return employee_dict["age"]
    
    # Recursively search in subordinates
    for subordinate in employee_dict.get("subordinates", {}).values():
        age = find_employee_age(subordinate, target_id)
        if age is not None:  # If the age is found, return it
            return age
    
    return None  # Return None if the target_id is not found

# Example usage:
target_id = "3"
age = find_employee_age(employees["1"], target_id)
if age is not None:
    print(f"The age of employee with ID {target_id} is {age}.")
else:
