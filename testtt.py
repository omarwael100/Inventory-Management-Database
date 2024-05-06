# Import libraries
import pymongo

# Replace these with your actual values
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Inventory"]
collection = database["COGS"]

# Get user input
beg_inv_dm = float(input("Begining inventory of direct material: "))

# Create document
document = {
    "Begining inventory DM": beg_inv_dm,
    # Add other fields and their values here
}

# Insert document
collection.insert_one(document)

# Close connection
client.close()
