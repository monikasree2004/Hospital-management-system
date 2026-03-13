import mysql.connector
# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@456",
    database="hospital"
)

cursor = db.cursor()

# Add patient
def add_patient():
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")

    sql = "INSERT INTO patients (name, age, disease) VALUES (%s, %s, %s)"
    values = (name, age, disease)

    cursor.execute(sql, values)
    db.commit()

    print("Patient Added Successfully")

# View patients
def view_patients():
    cursor.execute("SELECT * FROM patients")

    result = cursor.fetchall()

    print("\nPatient List")
    print("----------------------")

    for row in result:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("Disease:", row[3])
        print("----------------------")

# Update patient
def update_patient():
    pid = int(input("Enter Patient ID to update: "))
    new_disease = input("Enter New Disease: ")

    sql = "UPDATE patients SET disease=%s WHERE id=%s"
    values = (new_disease, pid)

    cursor.execute(sql, values)
    db.commit()

    print("Patient Updated Successfully")

# Delete patient
def delete_patient():
    pid = int(input("Enter Patient ID to delete: "))

    sql = "DELETE FROM patients WHERE id=%s"
    values = (pid,)

    cursor.execute(sql, values)
    db.commit()

    print("Patient Deleted Successfully")

# Main menu
while True:

    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        update_patient()

    elif choice == "4":
        delete_patient()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")