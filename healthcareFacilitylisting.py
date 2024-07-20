import requests 
import pandas as pd 

url = 'https://data.chhs.ca.gov/dataset/59d9abe7-2664-407a-a5aa-f89a866f3381/resource/641c5557-7d65-4379-8fea-6b7dedbda40b/download/current-healthcare-facility-listing.csv'

response = requests.get(url)


# Check if the request was successful
if response.status_code == 200:
    # Save the content of the response to a CSV file
    with open('current-healthcare-facility-listing.csv', 'wb') as file:
        file.write(response.content)
    print("CSV file downloaded successfully.")
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('current-healthcare-facility-listing.csv')
    
    # Display the first few rows of the DataFrame
    print(df.head())
else:
    print(f"Failed to download the file. Status code: {response.status_code}")