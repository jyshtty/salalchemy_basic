import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = db_name)
    except Exception as e:
        print(e)

def add_new_project(cursor, project_title, project_description, task_descriptions):
    project_data = (project_title, project_description)
    cursor.execute("""Insert into projects(title, description)
        values (%s, %s)""", project_data)

    project_id  = cursor.lastrowid # this will grab the project id of the last row we inserted

    tasks_data = []

    for description in task_descriptions:
        task_data_tuple = (project_id, description)
        tasks_data.append(task_data_tuple)

    cursor.executemany("""Insert into tasks(project_id, description)
        values (%s, %s)""", tasks_data)

if __name__ == "__main__":
    db = connect("projects")
    cursor = db.cursor()
    tasks = ["clean bathroom", "clean living room", "clean kitchen"]
    add_new_project(cursor, "Clean House", "CLean house by room", tasks)
    db.commit()
    db.close()