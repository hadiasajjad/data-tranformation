import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host= "localhost",
  user="root",
  password="1password2@",
  database="practice"
)
# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Execute the first SQL query (select all columns from the employees table)
mycursor.execute("SELECT * FROM employeess")
result1 = mycursor.fetchall()

# Execute the second SQL query (select the first name, last name, and salary of employees who make more than $50,000 per year)
mycursor.execute("SELECT first_name, last_name, salary FROM employeess WHERE salary > 50000")
result2 = mycursor.fetchall()

# Execute the third SQL query (select the average salary of employees in each department)
mycursor.execute("SELECT department, AVG(salary) FROM employeess GROUP BY department")
result3 = mycursor.fetchall()

# Display the results of the third query in a bar chart using matplotlib
df = pd.DataFrame(result3, columns=['department', 'average_salary'])
plt.bar(df['department'], df['average_salary'])
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()

# Execute the fourth SQL query (select the number of employees hired each year)
mycursor.execute("SELECT YEAR(hire_date), COUNT(*) FROM employeess GROUP BY YEAR(hire_date)")
result4 = mycursor.fetchall()

# Display the results of the fourth query in a line chart using matplotlib
df = pd.DataFrame(result4, columns=['year', 'count'])
plt.plot(df['year'], df['count'])
plt.xlabel('Year')
plt.ylabel('Number of Employees Hired')
plt.show()

# Execute the fifth SQL query (select the first name, last name, and hire date of employees who were hired in the last year)
mycursor.execute("SELECT first_name, last_name, hire_date FROM employeess WHERE hire_date >= DATE_SUB(NOW(), INTERVAL 1 YEAR)")
result5 = mycursor.fetchall()

# Display the results of the fifth query in a table using pandas
df = pd.DataFrame(result5, columns=['First Name', 'Last Name', 'Hire Date'])
print(df)
