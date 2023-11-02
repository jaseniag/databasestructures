import datetime 
import mysql.connector 

# connect with your mysql database
# assume your database nname 'test'
cnx = mysql.connector.connect(user='root', password='Database123', host='localhost', database='test') 

# create cursor
cursor = cnx.cursor() 

'''
You can use your own SQL commands below
'''

query = 'SELECT * FROM Flights WHERE DepartureAirport = "JFK" UNION SELECT * FROM Flights WHERE DestinationAirport = "JFK"'
query = 'SELECT Customer.*, Reservation.* FROM Customer, Reservation WHERE Customer.CustomerID = Reservation.CustomerID;'
query = 'SELECT DepartureAirport FROM Flights UNION SELECT DestinationAirport FROM Flights;'
query = 'SELECT SUM(AvailableSeats) FROM Flights;'
query = 'SELECT * FROM Customer WHERE CustomerID IN (SELECT CustomerID FROM Reservation);'
query = ' SELECT *FROM Reservation WHERE ReservationID IN (SELECT ReservationID FROM Payment);'



# run SQL command in mysql and
# cursor now points to the first record of results from SQL
cursor.execute(query) 

# fetch record one by one by using cursor
for data in cursor:
    print(data) 
    # print("{}, {} was hired on {:%d %b %Y}".format( last_name, first_name, hire_date))

# close the connection with mtsql
cursor.close()
cnx.close() 