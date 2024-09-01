import csv

def read_csv(file_path):
    """Read and print the contents of a CSV file."""
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read the header row
            print("Header:", header)
            print("Data:")
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")

if __name__ == "__main__":
    file_path = 'data.csv'  # Enter your path
    read_csv(file_path)
