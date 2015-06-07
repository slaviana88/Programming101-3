import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

create_company_table = """
CREATE TABLE IF NOT EXISTS 
company(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER,yearly_bonus INTEGER, position TEXT)
"""

cursor.execute(create_company_table)


cursor.execute("""INSERT 
                  INTO company(name, monthly_salary, yearly_bonus, position)
                  VALUES("Ivan Ivanov", 5000, 10000, "Software Developer")
""")


cursor.execute("""INSERT 
                  INTO company(name, monthly_salary, yearly_bonus, position)
                  VALUES("Rado Rado", 500, 0, "Technical Support intern")
""")

cursor.execute("""INSERT 
                  INTO company(name, monthly_salary, yearly_bonus, position)
                  VALUES("Ivo Ivo", 10000, 100000, "CEO")
""")

cursor.execute("""INSERT 
                  INTO company(name, monthly_salary, yearly_bonus, position)
                  VALUES("Petar Petrov", 3000, 1000, "Marketing Manager")
""")

cursor.execute("""INSERT 
                  INTO company(name, monthly_salary, yearly_bonus, position)
                  VALUES("Maria Georgieva", 8000, 10000, "COO")
""")

connection.commit()