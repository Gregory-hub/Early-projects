from sqlite3 import *


class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay


con = connect('testdb.db')
cur = con.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS employees (
# 				first text,
# 				last text,
# 				pay integer
# 			)""")

# emp1 = Employee('Martin', 'Scorsese', '60000000')

# cur.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp1.first, 'last': emp1.last, 'pay': emp1.pay})

# cur.execute()
cur.execute("SELECT * FROM employees")

print(*cur.fetchall(), sep='\n')

con.commit()

con.close()