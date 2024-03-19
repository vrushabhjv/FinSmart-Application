from django.db import connection

def get_transaction(transaction_id):
    # Define the SQL query for calling the stored procedure
    query = f"CALL GetTransaction({transaction_id})"

    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            # If the row is found, return the transaction details
            transaction = {
                'id': row[0],
                'date': row[1],
                'description': row[2],
                'amount': row[3],
                'category_id': row[4],
                'user_id': row[5],
                'type': row[6]
            }
            return transaction
        else:
            # If no row is found, return None
            return None
