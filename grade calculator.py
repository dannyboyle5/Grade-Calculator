import json

def spring_26_classes():
    try:
        with open(r'C:\Users\danny\OneDrive\Desktop\project\grade calculate\spring_26_classes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Warning: classes.json not found. Proceeding with manual entry only.")
        return {}

def get_grades():
    preloaded_data = spring_26_classes()
    grades = {}
    num_of_classes = int(input("How many classes are you taking? ").strip())

    for _ in range(num_of_classes):
        class_name = input("What is the name of the class (Input class code if you have *cap sensitive*): ").strip().upper()
        class_total = 0

        if class_name in preloaded_data:
            weights = preloaded_data[class_name]

            for cat_name, weight_val in weights.items():
                try:
                    score = float(input(f"What is your grade for {cat_name}?: "))
                    class_total += score*weight_val
                except ValueError:
                    print("Error, try again")
        else:
            i = 1
            while True:
                    cat_name = input(f"Name of category {i} (TYPE \"STOP\" to stop this): ").strip().upper()
                    if cat_name.strip().upper() == "STOP":
                        break
                    try:
                        weight = float(input(f"Weight % for {cat_name}? ")) / 100
                        score = float(input(f"What is your current grade in {cat_name}? "))
                        class_total += score*weight
                        i += 1
                    except ValueError:
                        print(f"Error, try again.")
        
        grades[class_name] = class_total
    return grades
final_grades = get_grades()
def displayed_grades(grades):
    for class_name, total in grades.items():
        print(f"{class_name}: {total:.2f}%")
displayed_grades(final_grades)