# **Dontrey Concert Ticket Management Application**

## Prerequisites
Before you begin, ensure you have the following software installed on your machine:

### Applications
* Python 3.x
* MySQL Server
* MySQL Workbench

### Packages
* pathlib
* pymysql.cursors
* re
* tkinter
* PIL

### Others
The GUI uses Poppins Font Family

## Setup Instructions
### 1. Configure Database Credentials
First, update the credentials in the credentials.py file.

* Open the credentials.py file.
* Locate the get_creds function and update it with your MySQL database password
* Locate the get_admin_pw function and set your admin account password
* Locate the get_staff_pw function and set your staff account password

```
def get_creds():
    return "Enter Your MYSQL Password Here"

def get_admin_pw():
    return "Enter Your Admin Password Here"

def get_staff_pw():
    return "Enter Your Staff Password Here"
```

### 2. Create the Database and Tables
Next, use MySQL Workbench to set up the database and tables required for the project.

* Open MySQL Workbench and connect to your MySQL Server.
* Copy and paste the following SQL commands into a new SQL script:
```
create database csa;
use csa;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerName VARCHAR(50),
    PhoneNumber VARCHAR(15),
    Concert VARCHAR(50),
    ConcertDate DATE,
    Section VARCHAR(50),
    cost float
);

CREATE TABLE concerts (
    Concert VARCHAR(50),
    ConcertDate DATE,
    ConcertSection VARCHAR(20),
    SectionAvailableSeats INT,
    Price float
);

CREATE TABLE membership (
    memberID INT PRIMARY KEY AUTO_INCREMENT,
    memberName VARCHAR(50),
    memberPhoneNumber VARCHAR(15)
);
```
* Run the script to create the csa database and its tables.
## Usage and Features
Once the application is running, you can start using it to manage concerts and tickets.
* Set up admin and staff accounts

### As admin:
* Add and Remove concert
* Upload Concert Poster

### As staff:
* Make ticket purchase by selecting concert name, concert date, seat section, fill in customer name and phone number, and save receipt ticket
* Register membership for customers that will get 10% discount for purchase
* Search for past ticket reciepts

**If you encounter any issues or have any questions, feel free to open an issue in the repository.**

**Happy coding!**
