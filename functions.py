import psycopg2

# Constants for database connection
DBNAME = "JOB_TRACKER"
USER = "postgres"
PASSWORD = "Levinak2000"
HOST = "localhost"

# Establishing the connection
connection = psycopg2.connect(
    dbname=DBNAME, user=USER, password=PASSWORD, host=HOST
)

# Creating a cursor object to interact with the database
cursor = connection.cursor()

class Application:
    def __init__(self, company:str, contact_date, action:str, job_title:str, job_link:str, contact_name=None) -> None:
        self.company = company
        self.contact_date = contact_date
        self.action = action
        self.job_title = job_title
        self.job_link = job_link
        self.contact_name = contact_name
    
    def add_new_application(self):
        query = "INSERT INTO contacts(company, contact_date, action, job_title, job_link, contact_name) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (self.company, self.contact_date, self.action, self.job_title, self.job_link, self.contact_name))
        connection.commit()
    
    def delete_application_by_id(self, id):
        query = "DELETE FROM contacts WHERE id = %s;"
        cursor.execute(query, (id,))
        connection.commit()

    def update_application_by_job_title_and_company(self, new_data: dict):
        query = "UPDATE contacts SET contact_date = %s, action = %s, job_title = %s, job_link = %s, contact_name = %s WHERE job_title = %s AND company = %s;"
        cursor.execute(query, (
            new_data.get("contact_date"),
            new_data.get("action"),
            new_data.get("job_title"),
            new_data.get("job_link"),
            new_data.get("contact_name"),
            new_data.get("old_job_title"),
            new_data.get("old_company")
        ))
        connection.commit()

    def select_all(self) -> list:
        query = "SELECT * FROM contacts;"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def sort_by_date(self) -> list:
        query = "SELECT * FROM contacts ORDER BY contact_date;"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows