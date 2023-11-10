import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='Database123', host='localhost', database='test')
cursor = cnx.cursor()

# Call the stored procedure
try:
    cursor.callproc('GetTotalSeats')
    for result in cursor.stored_results():
        print("Total available seats from stored procedure:", result.fetchone()[0])
except mysql.connector.Error as err:
    print("An error occurred: {}".format(err))

# Call the function
try:
    cursor.execute("SELECT AverageFlightPrice()")
    average_price = cursor.fetchone()[0]
    print("Average flight price:", average_price)
except mysql.connector.Error as err:
    print("Error occurred: {}".format(err))

# Close the cursor and database connection
cursor.close()
cnx.close()



################ Below is the actual SQL script that was used for the procedure and function ###################

# DELIMITER //

# CREATE PROCEDURE GetTotalSeats()
# BEGIN
#     SELECT SUM(AvailableSeats) AS TotalSeats FROM Flights;
# END //

# DELIMITER ;



#DELIMITER //

# CREATE FUNCTION AverageFlightPrice() RETURNS DECIMAL(10,2)
# DETERMINISTIC
# READS SQL DATA
# BEGIN
#     DECLARE result DECIMAL(10,2);
#     SELECT AVG(Price) INTO result FROM Flights;
#     RETURN result;
# END //

# DELIMITER ;



