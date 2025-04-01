import psycopg2


DB_NAME = "postgres"
DB_USER = "postgres.qovbkwtooljrahkeofdl"
DB_PASSWORD = "cQ&ijnr6DCRN$jy"
DB_HOST = "aws-0-ap-south-1.pooler.supabase.com"
DB_PORT = "5432"


def db_connection():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print("Connected to the database")
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        return None


def create_table():
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teacher (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Table created successfully")


def insert_teacher(name, age):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teacher (name, age) VALUES (%s, %s) RETURNING id", (name, age))
        conn.commit()
        cursor.close()
        conn.close()
        print("Value inserted")


def delete_teacher(id):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("Delete from teacher WHERE id = %s RETURNING id", (id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Deleted successfully")


def update_teacher(id, name, age):
    conn = db_connection()
    if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE teacher SET name = %s, age = %s WHERE id = %s RETURNING id", (name, age, id))
            conn.commit()
            cursor.close()
            conn.close()
            print(" updated successfully.")



if __name__ == "__main__":
    create_table()
    update_teacher(4, 'Shreya', 27)


