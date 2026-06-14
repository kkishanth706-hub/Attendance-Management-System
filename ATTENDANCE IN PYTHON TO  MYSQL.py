import mysql.connector
from datetime import date

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="attendance_db"
)

cursor = conn.cursor()

print("=== Attendance Management System ===")

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    print(f"\nStudent {i+1}")

    name = input("Enter student name: ")
    status = input("Attendance (P/A): ").upper()

    if status == "P":
        status = "Present"
    else:
        status = "Absent"

    sql = """
    INSERT INTO attendance
    (student_name, attendance_date, status)
    VALUES (%s, %s, %s)
    """

    values = (name, date.today(), status)

    cursor.execute(sql, values)

conn.commit()

print("\nAttendance saved successfully!")

# Display records
print("\nAttendance Records:")
cursor.execute("SELECT * FROM attendance")

records = cursor.fetchall()

for row in records:
    print(row)

cursor.close()
conn.close()
