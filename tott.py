import pymysql
import json
from decimal import Decimal

# Set the database credentials
host = ''
port = 3306
user = 'admin'
password = 'AHAD0978*ahad'
database = 'superstore'

# Connect to the database
connection = pymysql.connect(
host=host,
port=port,
user=user,
password=password,
database=database
)

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
cursor.execute('select customerID, sum(Sales) total_sales from orders group by 1 order by 2 desc limit 10;')

# Fetch the results
results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
connection.close()

# Convert results to list of dictionaries
json_data = []
for result in results:
  print(result)
  customerID = result[0]
  total_sales = float(result[1]) # Convert Decimal to float
  json_data.append({'customerID': customerID, 'total_sales': total_sales})

# Save the results as a JSON file
with open('results.json', 'w') as json_file:
  json.dump(json_data, json_file)

print("Results saved to 'results.json' file.")
