import datetime 
import mysql.connector

# Establish a database connection
cnx = mysql.connector.connect(user='root', password='Database123', host='localhost', database='test')
cursor = cnx.cursor()

# Each query has a set of parameters that will be passed through the actual query. %s is the placeholder and will be replaced by whats in the params
queries_with_variables = { 
    #Query to find all flights departing from or arriving at JFK airport
    'query1': {
        'sql': "SELECT * FROM Flights WHERE DepartureAirport = %s UNION SELECT * FROM Flights WHERE DestinationAirport = %s",
        'params': ('JFK', 'JFK')  
    },
    #Query to retrieve all customer and reservation details for a specific customer ID
    'query2': {
        'sql': "SELECT Customer.*, Reservation.* FROM Customer, Reservation WHERE Customer.CustomerID = Reservation.CustomerID AND Customer.CustomerID = %s",
        'params': (5,)  
    },
     # Query to get a list of unique airports for departures and arrivals, specifically for LAX and FLL
    'query3': {
        'sql': "SELECT DepartureAirport FROM Flights WHERE DepartureAirport = %s UNION SELECT DestinationAirport FROM Flights WHERE DestinationAirport = %s",
        'params': ('LAX', 'FLL')  
    },
    # Query to calculate the total number of available seats for a specific flight number
    'query4': {
        'sql': "SELECT SUM(AvailableSeats) FROM Flights WHERE FlightNumber = %s",
        'params': ('101',)  
    },
    # Query to select all customers who have made a reservation with a reservation ID greater than a given value
    'query5': {
        'sql': "SELECT * FROM Customer WHERE CustomerID IN (SELECT CustomerID FROM Reservation WHERE Reservationid > %s)",
        'params': ('2',)  
    },
    # Query to select all reservations made with a type of payment greater than a specified value (e.g., 'PayPal')
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
        # For the aggregation query, obtain and print the result
        total_seats = cursor.fetchone()
        print(f" Results for query4:\n Total available seats for airline 'AA': {total_seats[0]}")

# Close the cursor and the database connection
cursor.close()
cnx.close()



