import datetime 
import mysql.connector

# Establish a database connection
cnx = mysql.connector.connect(user='root', password='Database123', host='localhost', database='test')
cursor = cnx.cursor()

# Define your SQL commands with host variables
queries_with_variables = {
    'query1': {
        'sql': "SELECT * FROM Flights WHERE DepartureAirport = %s UNION SELECT * FROM Flights WHERE DestinationAirport = %s",
        'params': ('JFK', 'JFK')  
    },
    'query2': {
        'sql': "SELECT Customer.*, Reservation.* FROM Customer, Reservation WHERE Customer.CustomerID = Reservation.CustomerID AND Customer.CustomerID = %s",
        'params': (5,)  
    },
    'query3': {
        'sql': "SELECT DepartureAirport FROM Flights WHERE DepartureAirport = %s UNION SELECT DestinationAirport FROM Flights WHERE DestinationAirport = %s",
        'params': ('LAX', 'FLL')  
    },
    'query4': {
        'sql': "SELECT SUM(AvailableSeats) FROM Flights WHERE FlightNumber = %s",
        'params': ('101',)  
    },
    'query5': {
        'sql': "SELECT * FROM Customer WHERE CustomerID IN (SELECT CustomerID FROM Reservation WHERE Reservationid > %s)",
        'params': ('2',)  
    },
    'query6': {
        'sql': "SELECT * FROM Reservation WHERE ReservationID IN (SELECT ReservationID FROM Payment WHERE typeofpayment > %s)",
        'params': ('PayPal',)  
    }
}

# Execute each query with its corresponding host variables
for query_name, query_info in queries_with_variables.items():
    cursor.execute(query_info['sql'], query_info['params'])  # Execute the query with host variables
    if query_name in ['query1', 'query2', 'query3', 'query5', 'query6']:
        # print results for SELECT queries
        results = cursor.fetchall()
        print(f"Results for {query_name}:")
        for row in results:
            print(row)
    elif query_name == 'query4':
        # For the aggregation query, fetch and print the result
        total_seats = cursor.fetchone()
        print(f" Results for query4:\n Total available seats for airline 'AA': {total_seats[0]}")

# Close the cursor and the database connection
cursor.close()
cnx.close()



