import random
from faker import Faker
from datetime import timedelta
from datetime import datetime
# Initialize Faker
fake = Faker()

# Number of records to generate
NUM_AUTHORS = 10
NUM_PUBLISHERS = 5
NUM_BOOKS = 20
NUM_CUSTOMERS = 15
NUM_BOOK_COPIES = 50
NUM_TRANSACTIONS = 100
NUM_LIBRARIES = 3  # Number of libraries to generate

# Helper functions
def generate_authors():
    authors = []
    for _ in range(NUM_AUTHORS):
        authors.append(f"INSERT INTO Author (AuthorName) VALUES ('{fake.name()}');")
    return authors

def generate_publishers():
    publishers = []
    for _ in range(NUM_PUBLISHERS):
        publishers.append(f"INSERT INTO Publisher (PublisherName) VALUES ('{fake.company()}');")
    return publishers

def generate_books():
    books = []
    for _ in range(NUM_BOOKS):
        title = fake.sentence(nb_words=3).replace("'", "''")  # Escape single quotes
        genre = random.choice(["Fantasy", "Science Fiction", "Mystery", "Non-Fiction", "Romance"])
        pub_year = random.randint(1980, 2023)
        publisher_id = random.randint(1, NUM_PUBLISHERS)
        author_id = random.randint(1, NUM_AUTHORS)
        books.append(f"INSERT INTO Book (Title, Genre, PublicationYear, PublisherID, AuthorID) VALUES ('{title}', '{genre}', {pub_year}, {publisher_id}, {author_id});")
    return books

def generate_customers():
    customers = []
    for _ in range(NUM_CUSTOMERS):
        name = fake.name()
        contact_info = fake.phone_number()
        customers.append(f"INSERT INTO Customer (CustomerName, ContactInfo) VALUES ('{name}', '{contact_info}');")
    return customers

def generate_libraries():
    libraries = []
    for library_id in range(1, NUM_LIBRARIES + 1):  # Generate IDs starting from 1
        library_name = fake.company()  # Random library name (using company names for now)
        address = fake.address().replace("'", "''")  # Escape single quotes
        libraries.append(f"INSERT INTO Library (LibraryID, LibraryName, Address) VALUES ({library_id}, '{library_name}', '{address}');")
    return libraries

def generate_book_copies():
    book_copies = []
    for _ in range(NUM_BOOK_COPIES):
        book_id = random.randint(1, NUM_BOOKS)
        library_id = random.randint(1, NUM_LIBRARIES)  # Now linked to Library
        book_copies.append(f"INSERT INTO BookCopy (BookID, LibraryID) VALUES ({book_id}, {library_id});")
    return book_copies

def generate_transactions():
    transactions = []
    today = datetime.today().date()  # Get today's date
    
    for _ in range(NUM_TRANSACTIONS):
        copy_id = random.randint(1, NUM_BOOK_COPIES)
        customer_id = random.randint(1, NUM_CUSTOMERS)
        issue_date = fake.date_between(start_date='-1y', end_date=today)
        
        # Ensure due date is later than the issue date and before today
        due_date = issue_date + timedelta(days=random.randint(7, 30))  # Random due date between 7 and 30 days later
        if due_date > today:
            due_date = today  # Make sure due date is not in the future

        # Randomly determine if the return date is available (i.e., the book has been returned)
        return_date = None
        if random.choice([True, False]):
            # Ensure return date is after due date and not later than today
            return_date = fake.date_between(start_date=due_date, end_date=today)

        # Correct logic for return_date being after due_date or NULL
        if return_date is None:
            transactions.append(
                f"INSERT INTO Transaction (CopyID, CustomerID, IssueDate, DueDate, ReturnDate) VALUES "
                f"({copy_id}, {customer_id}, '{issue_date}', '{due_date}', NULL);"
            )
        else:
            transactions.append(
                f"INSERT INTO Transaction (CopyID, CustomerID, IssueDate, DueDate, ReturnDate) VALUES "
                f"({copy_id}, {customer_id}, '{issue_date}', '{due_date}', '{return_date}');"
            )
    
    return transactions
# Main function to generate all SQL insert commands
def generate_data():
    authors = generate_authors()
    publishers = generate_publishers()
    books = generate_books()
    customers = generate_customers()
    libraries = generate_libraries()
    book_copies = generate_book_copies()
    transactions = generate_transactions()

    with open(r"C:\Users\Akash\Desktop\Library management data using psql\in_data.sql", "w") as file:
        file.write("-- Authors\n")
        file.write("\n".join(authors) + "\n\n")
        file.write("-- Publishers\n")
        file.write("\n".join(publishers) + "\n\n")
        file.write("-- Books\n")
        file.write("\n".join(books) + "\n\n")
        file.write("-- Customers\n")
        file.write("\n".join(customers) + "\n\n")
        file.write("-- Libraries\n")
        file.write("\n".join(libraries) + "\n\n")
        file.write("-- Book Copies\n")
        file.write("\n".join(book_copies) + "\n\n")
        file.write("-- Transactions\n")
        file.write("\n".join(transactions) + "\n\n")


# Run the script
if __name__ == "__main__":
    generate_data()
