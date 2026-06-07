import mysql.connector


def get_database_connection():
    connection = mysql.connector.connect(
        host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user = '3c7E88Vnm34xaB6.root',
        password = '7PZ3xn5h7TV39qKr',
        port = 4000,
        database = 'student_task_manager'
    )
    return connection