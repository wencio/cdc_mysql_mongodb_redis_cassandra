# README

This repository contains a Python script (`container.py`) designed to manage Docker containers for various database systems including MySQL, MongoDB, Redis, and Cassandra. The script provides functionalities for creating, deleting containers, initializing database schemas, and performing data operations.

## Prerequisites
- Docker installed on your system

## Usage

### Setup
1. Clone this repository to your local machine.
2. Ensure Docker is running on your system.

### Running the Script
The script `container.py` accepts command-line arguments to perform different operations:

- **Create Containers**: Use the `-create` argument to create Docker containers for MySQL, MongoDB, Redis, and Cassandra.
    ```bash
    python container.py -create
    ```

- **Delete Containers**: Use the `-delete` argument to delete Docker containers for MySQL, MongoDB, Redis, and Cassandra.
    ```bash
    python container.py -delete
    ```

- **Initialize Databases**: Use the `-init` argument to initialize the MySQL and Cassandra databases.
    ```bash
    python container.py -init
    ```

- **Clear Database Data**: Use the `-clear` argument to delete all data from MySQL, MongoDB, Redis, and Cassandra databases.
    ```bash
    python container.py -clear
    ```

### Running Data Operations
The script performs data operations such as writing and reading data from different databases in a loop.

- **Writing Data**: The script continuously writes data to the MySQL database.
- **Change Data Capture (CDC)**: After writing data to MySQL, it captures the changes and propagates them to MongoDB, Redis, and Cassandra databases.
- **Verification**: The script verifies the data propagation by reading data from MongoDB, Redis, and Cassandra.

To start the data operations, simply run the script without any arguments.
```bash
python container.py
```

### Time Loop
The script utilizes a time loop (`timeloop()`) to perform data operations at regular intervals. This ensures continuous data synchronization among different databases.

## Note
- Ensure Docker is properly configured and running before executing the script.
- This script is intended for educational purposes and should be used responsibly.
