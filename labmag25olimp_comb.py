def read_file(filename):
    try:       
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.readlines()
            surnames = {}
        for line in data:
            line = line.strip()
            if line:
                parts = line.split()
                surname = parts[0]
                if len(parts) > 1:  
                    place = parts[1]  
                else:
                    place = None
                surnames[surname] = place
        return surnames
    except Exception:
        print("Ошибка при чтении файла")
        return {}

def searching_students(olympiad1, olympiad2):
    results = {}
    olympiad1_names = read_file(olympiad1)
    olympiad2_names = read_file(olympiad2)
    students = set(olympiad1_names.keys()) | set(olympiad2_names.keys())   
    
    for student in sorted(students):
        place1 = olympiad1_names.get(student)
        place2 = olympiad2_names.get(student)

        prize1 = place1 in ["1", "2", "3"] 
        prize2 = place2 in ["1", "2", "3"] 

        part1 = student in olympiad1_names
        part2 = student in olympiad2_names       
        
        if part1 and part2:
            if prize1 and prize2:
                grade = "5"
            elif prize1 or prize2:
                grade = "4"
            else:
                grade = "3"
        else:
            grade = "д"
        
        results[student] = grade  

    with open("result_olimp.txt", 'w', encoding='utf-8') as result_file:
        for student, grade in results.items():
            result_file.write(f"{student} «{grade}»\n")
    print("Результаты сохранены в файл")
    return results

results = searching_students('Olimpiada_1.txt', 'Olimpiada_2.txt')
