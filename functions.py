import psycopg2
# IF ALL LETTERS ARE UPPERCASE - THEN ITS A CONSTANT (not meant to change)
DBNAME = "Job_Tracker_DataBase"
USER = "postgres"  # postgres
PASSWORD = "5859"  # <YOUR POSTGRES PASSWORD>
HOST = "localhost"
PORT = "5432"

connection = psycopg2.connect(
    dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
)

# 2. Create a cursor (tool to run queries)
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
        query = f"insert into contacts(company, contact_date, action, job_title, job_link, contact_name) values(%s, %s, %s, %s, %s, %s);"
        cursor.execute(query,(self.company, self.contact_date, self.action, self.job_title, self.job_link, self.contact_name))
        connection.commit()  # apply all changes from cursor through the connection
    
    def delete_application_by_id(self, id):
        query = f"delete from contacts where id = %s;"
        cursor.execute(query,(id,))
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

    
    def select_all(self) -> list[tuple]:
        query = "select * from contacts;"
        cursor.execute(query)
        rows = (cursor.fetchall())
        return rows
    
    def sort_by_date(self) -> list:
        query = "SELECT * FROM contacts ORDER BY contact_date;"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows