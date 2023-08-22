import pandas as pd
import re

def get_matching_trucks(csv_file, keyword):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(csv_file)

    # Filter the DataFrame to get only trucks with the facility type "Truck"
    trucks = df[df["FacilityType"] == "Truck"]

    # Construct a regex pattern to match the whole word
    pattern = r'\b' + re.escape(keyword.lower()) + r'\b'

    # Filter the trucks based on the keyword using the regex pattern
    matching_trucks = trucks[trucks["FoodItems"].str.contains(pattern, case=False, na=False, regex=True)]

    # Check if any matching trucks were found
    if matching_trucks.empty:
        print(f"No 'Truck' type food trucks found containing the keyword '{keyword}'.")
    else:
        # Get the unique names of matching trucks
        matching_truck_names = set(matching_trucks["Applicant"])

        # Print the names of matching trucks
        print(f"Names of 'Truck' type food trucks containing the keyword '{keyword}':")
        for name in matching_truck_names:
            print(name)

if __name__ == "__main__":
    csv_file = "Mobile_Food_Facility_Permit.csv"

    while True:
        keyword = input("Enter a keyword to search for 'Truck' type food trucks (or type 'exit' to quit): ")
        
        if keyword.lower() == "exit":
            break
        
        get_matching_trucks(csv_file, keyword)

