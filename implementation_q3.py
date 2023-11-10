import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='Zona.44.riccione', host='localhost', database='P2_Schema')
cursor = cnx.cursor()

def search_criteria():
    round_trip = input("Round trip (yes/no): ")
    if round_trip == "yes":
        DepartureDateTime = input("Departure date (YYYY-MM-DD): ")
        return_date = input("Return date (YYYY-MM-DD): ")
    elif round_trip == "no":
        DepartureDateTime = input("Departure date (YYYY-MM-DD): ")
    DepartureAirport = input("Departure airport: ")
    DestinationAirport = input("Destination airport: ")
    num_passengers = int(input("Number of passengers: "))  # Convert to integer
    
    #SQL query to search for flights
    query = "SELECT * FROM Flights WHERE DepartureDateTime = %s AND DepartureAirport = %s AND DestinationAirport = %s"
    cursor.execute(query, (DepartureDateTime, DepartureAirport, DestinationAirport))
    flights = cursor.fetchall()
    print(flights)
    
    print("\nAvailable Flights:\n")
    for flight in flights:
        FlightNumber, FlightClass, DepartureAirport, DestinationAirport, DepartureDateTime, FlightDuration, Price = flight
        print(f"Flight Number: {FlightNumber}")  
        print(f"Departure Date and Time: {DepartureDateTime}")  
        print(f"Departure Airport: {DepartureAirport}")  
        print(f"Destination Airport: {DestinationAirport}") 
        print(f"Cabin Class: {FlightClass}")   
        print(f"Price: {Price}")  
    print("="*50)  # Separator for better readability

    
    # Add more code to handle round trip, return date, etc.

def seat_selection():
    choose_seat = input("\n\nDo you want to choose a seat (yes/no): ")
    cabin_class = input("Cabin class (economy/business/first): ")
    
    if choose_seat.lower() == 'yes':
        # Add code for seat selection
        seat_number = input("Enter seat number: ")
        print(f"Seat {seat_number} selected in {cabin_class} class\n\n.")
    else:
        print(f"You have chosen {cabin_class} class without seat selection.\n\n")
    print("="*50)  # Separator for better readability
    
def customer_details():
    name = input("Full name: ")
    email = input("Email address: ")
    phone = input("Phone number: ")
    flightPurchased = 1

    
    # SQL query to save customer details
    query = "INSERT INTO Customer (CustomerName, Email, PhoneNumber, FlightPurchased) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, phone, flightPurchased))
    cnx.commit()
    print("Customer details saved successfully.")

# Example usage:
search_criteria()
seat_selection()
customer_details()

# Close the database connection
cursor.close()
cnx.close()

