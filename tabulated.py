Here is a Python program that uses the `tabulate` library to format and display factory details in a tabular format. 

First, you need to install the `tabulate` library if you haven't already:

```bash
pip install tabulate
```

Once you have the library installed, you can use the following code:

```python
from tabulate import tabulate

# Define factory details
factories = [
    {"Factory ID": 101, "Name": "Alpha Corp", "Location": "New York", "Employees": 250},
    {"Factory ID": 102, "Name": "Beta Industries", "Location": "Chicago", "Employees": 300},
    {"Factory ID": 103, "Name": "Gamma Ltd", "Location": "San Francisco", "Employees": 150},
    {"Factory ID": 104, "Name": "Delta Manufacturing", "Location": "Houston", "Employees": 400}
]

# Convert dictionaries to list of rows
table = [[f['Factory ID'], f['Name'], f['Location'], f['Employees']] for f in factories]

# Define column headers
headers = ["Factory ID", "Name", "Location", "Number of Employees"]

# Display table using tabulate
print(tabulate(table, headers, tablefmt="grid"))
```

### Explanation:
- The `factories` list contains dictionaries with details for each factory (ID, name, location, and number of employees).
- We convert the list of dictionaries into a list of lists (which `tabulate` accepts).
- Finally, the `tabulate` function displays the data in a well-formatted table with headers.

### Sample Output:
```
+-------------+---------------------+-------------------+---------------------+
|   Factory ID| Name                | Location          |   Number of Employees|
+=============+=====================+===================+=====================+
|         101 | Alpha Corp          | New York          |                   250|
+-------------+---------------------+-------------------+---------------------+
|         102 | Beta Industries     | Chicago           |                   300|
+-------------+---------------------+-------------------+---------------------+
|         103 | Gamma Ltd           | San Francisco     |                   150|
+-------------+---------------------+-------------------+---------------------+
|         104 | Delta Manufacturing | Houston           |                   400|
+-------------+---------------------+-------------------+---------------------+
```

This program will generate a clean table layout for displaying factory details.