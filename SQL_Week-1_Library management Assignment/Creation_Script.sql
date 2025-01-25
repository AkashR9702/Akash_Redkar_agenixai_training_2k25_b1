-- Create the Author table
CREATE TABLE author (
    AuthorID SERIAL PRIMARY KEY,
    AuthorName VARCHAR(255) NOT NULL
);

-- Create the Publisher table
CREATE TABLE publisher (
    PublisherID SERIAL PRIMARY KEY,
    PublisherName VARCHAR(255) NOT NULL
);

-- Create the Library table
CREATE TABLE library (
    LibraryID SERIAL PRIMARY KEY,
    LibraryName VARCHAR(255) NOT NULL,
    Address TEXT NOT NULL
);

-- Create the Book table
CREATE TABLE book (
    BookID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Genre VARCHAR(50),
    PublicationYear INT NOT NULL,
    PublisherID INT NOT NULL,
    AuthorID INT NOT NULL,
    FOREIGN KEY (PublisherID) REFERENCES Publisher (PublisherID) ON DELETE CASCADE,
    FOREIGN KEY (AuthorID) REFERENCES Author (AuthorID) ON DELETE CASCADE
);

-- Create the Customer table
CREATE TABLE customer (
    CustomerID SERIAL PRIMARY KEY,
    CustomerName VARCHAR(255) NOT NULL,
    ContactInfo VARCHAR(255) UNIQUE NOT NULL
);

-- Create the BookCopy table
CREATE TABLE bookCopy (
    CopyID SERIAL PRIMARY KEY,
    BookID INT NOT NULL,
    LibraryID INT NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID) ON DELETE CASCADE,
    FOREIGN KEY (LibraryID) REFERENCES Library (LibraryID) ON DELETE CASCADE
);

-- Create the Transaction table
CREATE TABLE transaction (
    TransactionID SERIAL PRIMARY KEY,
    CopyID INT NOT NULL,
    CustomerID INT NOT NULL,
    IssueDate DATE NOT NULL,
    DueDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (CopyID) REFERENCES BookCopy (CopyID) ON DELETE CASCADE,
    FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID) ON DELETE CASCADE
);
