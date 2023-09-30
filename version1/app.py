from flask import Flask, request, jsonify,render_template
import csv

app = Flask(__name__)

# Assuming your CSV data is in a file named "data.csv" with a header row.

# Define the indices for the columns you want to search and return.
search_column_index = 1 # Second column (0-based index)
return_column_index = 2 # Third column (0-based index)
retu = 3
rame = 0
column_index = 2
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search_roll_number():
    roll_number = request.args.get("rollNumber")
    #roll_number="160121729039"
    # Initialize the result as None (not found)
    result = None

    # Open and read the CSV file
    with open("data.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        #next(reader)  # Skip the header row
        for row in reader:
            if row[search_column_index] == roll_number:
                result = row[return_column_index] + row[retu] + row[rame]
                break  # Stop searching once a match is found

    # Return the result as JSON
    if result is not None:
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Roll Number not found"})
    '''values_array = []

    # Open and read the CSV file
    with open("data.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            values_array.append(row[column_index])

    # Sort the values array
    values_array.sort()

    # Return the sorted array as JSON
    return jsonify({"result": values_array})'''
    '''value_dict_list = []

    # Open and read the CSV file
    with open("data.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            value = row[search_column_index]
            corresponding_value = row[return_column_index]
            value_dict_list.append({"value": value, "corresponding_value": corresponding_value})

    # Sort the list of dictionaries based on the "value" key
    sorted_value_dict_list = sorted(value_dict_list, key=lambda x: x["value"])

    # Return the sorted list of dictionaries as JSON
    return jsonify({"result":sorted_value_dict_list})'''

if __name__ == "__main__":
    app.run(port=5000, debug=False)
