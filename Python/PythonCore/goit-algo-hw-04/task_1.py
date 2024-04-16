from pathlib import Path


p = Path("salary_file.txt")
p.write_text("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")


def total_salary(p):
    total_salary = 0
    num_developers = 0
    try:
        with open(p, "r", encoding="utf_8") as file:
            for line in file:
                name, salary_str = line.split(',')
                salary = int(salary_str)
                total_salary += salary
                num_developers += 1
    except FileNotFoundError:
        print(f"File '{p}' not found.")
        return None

    average_salary = total_salary / num_developers if num_developers > 0 else 0

    return total_salary, average_salary


total, average = total_salary(p)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")