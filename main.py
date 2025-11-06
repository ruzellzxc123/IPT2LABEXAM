# this is the connector module
# allows the python to talk to MYSQL database ( like logging, reading data etc.)
import mysql.connector 


"""
this imports the Error class from the same module
used to handle problems? ( like wrong password, or server not found) when trying to
connect to the database
"""
from mysql.connector import Error



"""
Create a connection to MySQL Database

"""

def create_connection():
  
    """
    The function create_connection() tries to connect your python program
    to MYSQL database. if the connection works it prints the Mysql version and
    returns the connection object, if its fails it prints the error and returns NONE
    """
    
    try:
      connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='iptfinals'
        
      )
      if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected {db_info}")
      return connection
    except Error as e:
      print(f"Error while connecting to mysql: {e}")
      return None
    
def create_table(connection):
    """
    create a simple table in the database
    """
    
    try:
      cursor = connection.cursor()
      
      #SQL query to create a table
      
      create_table_query = """
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(10) NOT NULL,
        age INT,
        address VARCHAR(255) NOT NULL,
        phone VARCHAR(11),
        email VARCHAR(10) NOT NULL,
        jobtitle VARCHAR(20) NOT NULL,
        professionalsummary VARCHAR(100) NOT NULL,
        experience VARCHAR(100),
        education VARCHAR(100),
        skills VARCHAR(100)
      )
      """
      
      #  CREATE TABLE IF NOT EXISTS users create a table named users only if it doesnt
      #already exist, prevents error if the the table is already there.
      
      cursor.execute(create_table_query)
      connection.commit()
      print("table users created successfully")
      cursor.close()
    except Error as e:
      print(f"Error creating table: {e}")

def get_user_input():
    """
    Get user input from terminal
    """
    print("=" * 40)
    print("Enter User Information")
    print("=" * 40)
    
    name = input("Enter Full Name: ").strip()
    
    # Validate age input
    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Please enter a valid number for age")
    
    address = input("Enter Address: ").strip()
    
    while True:
        try:
            phone = int(input("Phone: "))
            break
        except ValueError:
            print("Please enter a valid format for phone number")

    email = input("Enter Email: ").strip()

    jobtitle = input("Enter Job Title: ").strip()

    professionalsumarry = input("Enter Job Title: ").strip()

    experience = input("Enter Job Title: ").strip()

    education = input("Enter Job Title: ").strip()

    skills = input("Enter Job Title: ").strip()

    return name, age, address, phone, email, jobtitle, professionalsumarry, experience, education, skills


def insert_user_data(connection, name, age, address, phone, email, jobtitle, professionalsummary, experience, education, skills):
    # ... (This is almost identical to our old insert_data function) ...
    try:
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO users (name, age, address, phone, email, jobtitle, professionalsumarry, experience, education, skills) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        user_data = (name, age, address, phone, email, jobtitle, professionalsummary, experience, education, skills)
        
        cursor.execute(insert_query, user_data)
        connection.commit()
        print(f"\n✓ Record inserted successfully for {name}\n")
        cursor.close()
    
    except Error as e:
        print(f"Error inserting data: {e}")
    
def retrieve_data(connection):
    # ... (execute query is the same) ...
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    
    if records:
        print("\n" + "=" * 60)
        print("All Users in Database")
        print("=" * 60)
        for record in records:
            print(f"ID: {record[0]}")
            print(f"  Name: {record[1]}")
            print(f"  Age: {record[2]}")
            print(f"  Address: {record[3]}")
            print(f"  Phone: {record[4]}")
            print(f"  Email: {record[5]}")
            print(f"  Job Title: {record[6]}")
            print(f"  Professional Summary: {record[7]}")
            print(f"  Experience: {record[8]}")
            print(f"  Education: {record[9]}")
            print(f"  Skills: {record[10]}")
            print("-" * 60)
    else:
        print("\nNo users found in database\n")
    
    cursor.close()
    # ... (try/except is the same) ...

    """
    Retrieve and display all data from the users table
    """
    try:
      cursor = connection.cursor()
      
      select_query = "SELECT * FROM users"
      cursor.execute(select_query)
      
      #Fetch all records
      
      records = cursor.fetchall() #get all the results and store them in a variable called records
      
      print("\n ---- Users Data ------")
      for record in records: #loop through each row one by one
          print(f"ID: {record[0]}, Name: {record[1]}, Email: {record[2]}, Age: {record[3]}, Phone: {record[4]}, Email: {record[5]}, Job Title: {record[6]}, Professional Summary: {record[7]}, Experience: {record[8]}, Education: {record[9]}, Skills: {record[10]}")
      cursor.close()
    except Error as e:
      print(f"Error retrieving data: {e}")
    
    
def main_menu(connection):
    """
    Display menu and handle user choices
    """
    while True:
        print("\n" + "=" * 40)
        print("User Management System")
        # ... (more print statements for menu) ...
        print("3. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            name, age, address  = get_user_input()
            insert_user_data(connection, name, age, address)
        
        elif choice == "2":
            retrieve_data(connection)
        
        elif choice == "3":
            print("\nThank you for using the system!")
            break
        
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3")

  #cursor it is like a pointer or pen that executes SQL Commands.
  
def close_connection(connection):
    """
    Close the database connection
    """
    if connection.is_connected():
      connection.close()
      print("\n MYSQL connection is closed")

if __name__ == "__main__":
    # Step 1: Create connection
    conn = create_connection()
    
    if conn:
        # Step 2: Create table
        create_table(conn)
        
        # Step 3: Show menu and handle user interactions
        main_menu(conn)
        
        # Step 4: Close connection
        close_connection(conn)