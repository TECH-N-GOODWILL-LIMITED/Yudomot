from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

# Create a Flask app instance
app = Flask(__name__)

try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
    if conn:
        print("Database Connected!!!")
    else:
        print("Database Not Connected")
except mysql.connector.Error as err:
    print("Error:", err)


# Define a route and a view function
@app.route('/', methods=['GET'])
def index():
    return "Welcome To Our API"

# Define a route and a view function
@app.route('/country_list', methods=['GET'])
def country_list():
    country = request.args.get('country')
    city = request.args.get('city')

    if country is not None and city is not None:
        try:
            # Create a cursor object
            cursor = conn.cursor()

            # Execute a SELECT query with a prepared statement
            query = "SELECT * FROM country_list WHERE country = %s AND city = %s"
            cursor.execute(query, (country, city))  # replace user_input with your actual input
            # cursor.execute(query)
            # Fetch the results
            rows = cursor.fetchall()

            return jsonify({'result': rows})

        except mysql.connector.Error as cursor_err:
            print("Error executing query:", cursor_err)
        finally:
            # Close the cursor
            if 'cursor' in locals():
                cursor.close()

    elif country is not None:
        try:
            # Create a cursor object
            cursor = conn.cursor()

            # Execute a SELECT query with a prepared statement
            query = "SELECT * FROM country_list WHERE country = %s"
            cursor.execute(query, (country,))  # replace user_input with your actual input
            # cursor.execute(query)
            # Fetch the results
            rows = cursor.fetchall()

            return jsonify({'result': rows})

        except mysql.connector.Error as cursor_err:
            print("Error executing query:", cursor_err)
        finally:
            # Close the cursor
            if 'cursor' in locals():
                cursor.close()

    elif city is not None:
        try:
            # Create a cursor object
            cursor = conn.cursor()

            # Execute a SELECT query with a prepared statement
            query = "SELECT * FROM country_list WHERE city = %s"
            cursor.execute(query, (city,))  # replace user_input with your actual input
            # cursor.execute(query)
            # Fetch the results
            rows = cursor.fetchall()

            return jsonify({'result': rows})

        except mysql.connector.Error as cursor_err:
            print("Error executing query:", cursor_err)
        finally:
            # Close the cursor
            if 'cursor' in locals():
                cursor.close()

    else:
        try:
            # Create a cursor object
            cursor = conn.cursor()

            # Execute a SELECT query with a prepared statement
            query = "SELECT * FROM country_list"
            cursor.execute(query)  # replace user_input with your actual input
            # cursor.execute(query)
            # Fetch the results
            rows = cursor.fetchall()

            return jsonify({'result': rows})

        except mysql.connector.Error as cursor_err:
            print("Error executing query:", cursor_err)
        finally:
            # Close the cursor
            if 'cursor' in locals():
                cursor.close()


@app.route('/country_list/add', methods=['POST'])
def country_list_add():
    data = request.get_json()
    country = data.get('country')
    city = data.get('city')
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Define the INSERT query with placeholders for values
        insert_query = "INSERT INTO country_list (country, city, date_created) VALUES (%s, %s, %s)"

        # Define the values to be inserted (replace these with your actual values)
        values = (country, city, current_date)

        # Execute the INSERT query with the values
        cursor.execute(insert_query, values)

        # Commit the transaction
        conn.commit()

        return jsonify({'result': 'Data inserted successfully!'})
    except mysql.connector.Error as cursor_err:
        return jsonify({'result': cursor_err})
    finally:
        # Close the cursor
        if 'cursor' in locals():
            cursor.close()


@app.route('/country_list/update', methods=['POST'])
def country_list_update():
    data = request.get_json()
    country = data.get('country')
    city = data.get('city')
    country_id = data.get('country_id')

    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Define the UPDATE query with placeholders for values
        update_query = "UPDATE country_list SET country = %s, city = %s WHERE id = %s"

        # Define the values to be updated (replace these with your actual values)
        values = (country, city, country_id)

        # Execute the UPDATE query with the values
        cursor.execute(update_query, values)

        # Commit the transaction
        conn.commit()

        return jsonify({'result': 'Data updated successfully!'})
    except mysql.connector.Error as cursor_err:
        return jsonify({'result': cursor_err})
    finally:
        # Close the cursor
        if 'cursor' in locals():
            cursor.close()


@app.route('/country_list/delete', methods=['POST'])
def country_list_delete():
    data = request.get_json()
    country_id = data.get('country_id')

    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Define the UPDATE query with placeholders for values
        update_query = "DELETE FROM country_list WHERE id = %s"

        # Define the values to be updated (replace these with your actual values)
        values = (country_id,)

        # Execute the UPDATE query with the values
        cursor.execute(update_query, values)

        # Commit the transaction
        conn.commit()

        return jsonify({'result': 'Data deleted successfully!'})
    except mysql.connector.Error as cursor_err:
        return jsonify({'result': cursor_err})
    finally:
        # Close the cursor
        if 'cursor' in locals():
            cursor.close()


# @app.route('/calculator', methods=['GET'])
# def calculator():
#     result = 0.00
#     first_value = request.args.get('first_value')
#     second_value = request.args.get('second_value')
#     operator = request.args.get('operator')
#     if operator == "add":
#         result = float(first_value) + float(second_value)
#     elif operator == "subtract":
#         result = float(first_value) - float(second_value)
#     elif operator == "divide":
#         result = float(first_value) / float(second_value)
#     elif operator == "multiply":
#         result = float(first_value) * float(second_value)
#
#     return jsonify({'result': result})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
