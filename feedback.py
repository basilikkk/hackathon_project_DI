# App helps to job seekers track their job applications, allows to show, add, delete and change applications. 
# All the data is saved to the Database	"Project is working, made with tkinter. Look like you did a great job, guys! 
# 
# I like how the app is working and how usefull it is. You used OOP, classes, modules, and made userfriendly GUI with tkinter. 

# The only thing I could mention is that it was not easy to test your DB since you skip table creating in the code. 
# I know you tested it localy with created table, but I needed to see this table and its columns :) What I mean is that:

def create_tables():
    commands = (
        """"""
        CREATE TABLE IF NOT EXISTS reports (
            id SERIAL PRIMARY KEY,
            username VARCHAR NOT NULL,
            topic TEXT NOT NULL,
            link TEXT NOT NULL,
            clicks INTEGER DEFAULT 0,
            report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """""",
    )

    conn = create_connection()
    cursor = conn.cursor()
    try:
        for command in commands:
            cursor.execute(command)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# But very good job anyway! 

# Python OOP: 10/10
# Modules: 10/10
# Database:8/10
# Overall: 9