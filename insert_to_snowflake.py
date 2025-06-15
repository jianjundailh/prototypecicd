import os
import snowflake.connector
from datetime import datetime

def insert_data():
    # Load Snowflake credentials from environment variables
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE")  # Optional
    )

    cursor = conn.cursor()

    try:
        # Define your insert SQL
        insert_sql = """
        INSERT INTO ppln.public.test001 (col1, col2, col3)
        VALUES (%s, %s, %s)
        """
        # Example data
        data = (101, 102, 'Inserted from CodeBuild pipeline')

        # Execute the insert
        cursor.execute(insert_sql, data)
        print("Insert successful.")

    except Exception as e:
        print("Error during insert:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insert_data()
