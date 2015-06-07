import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

command = input("command> ")


def list_employees():
    cursor.execute("""SELECT name,position FROM company""")
    connection.commit()
    for employee in cursor:
        print(employee)


def monthly_spending():
    cursor.execute("""SELECT monthly_salary FROM company""")
    cursor_result = 0
    for employee in cursor:
        cursor_result += sum(employee)
    connection.commit()
    print("The company The company is spending ${} every month!".format(cursor_result))


def yearly_spending():
    cursor.execute("""SELECT monthly_salary,yearly_bonus FROM company""")
    cursor_result = 0
    for employee in cursor:
        cursor_result += sum(employee)
    connection.commit()
    print("The company The company is spending ${} every year!".format(cursor_result))


def add_employee():
    name = input("name> ")
    monthly_salary = input("monthly_salary> ")
    yearly_bonus = input("yearly_bonus> ")
    position = input("position> ")
    cursor.execute("""INSERT
                      INTO company
                      (name, monthly_salary, yearly_bonus, position)
                      VALUES (?,?,?,?)
                      """).format(name, monthly_salary, yearly_bonus, position)
    connection.commit()


def delete_employee(id):
    cursor.execute("""DELETE FROM company WHERE ?""").format(id,)
    connection.commit()
# delete_employee = """ DELETE FROM company WHERE id=6"""


def update_employee(id):
    name = input("name> ")
    monthly_salary = input("monthly_salary> ")
    yearly_bonus = input("yearly_bonus> ")
    position = input("position> ")
    cursor.execute("""UPDATE company
                      SET ?, ?, ?, ?
                      WHERE ?""").format(name, monthly_salary, yearly_bonus, position, id)
    connection.commit()

# update_employee = """ UPDATE company SET yearly_bonus = 2000 WHERE id=2"""

commands = {
           "list_employees": list_employees,
           "monthly_spending": monthly_spending,
           "yearly_spending": yearly_spending,
           "add_employee": add_employee,
           "delete_employee": delete_employee,
           "update_employee": update_employee
           }


def main():
    user_command = command.split()[0]
    try:
        user_id = command.split()[1]
        commands[user_command](user_id)
        print("i deleted")
    except:
        commands[user_command]()

if __name__ == '__main__':
    main()
