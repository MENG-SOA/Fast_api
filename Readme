Part A: Introduction to FastAPI

1. Understanding FastAPI:
   - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.
   - It is built on top of Starlette for the web handling and Pydantic for data validation and serialization.
   - FastAPI provides high-performance, easy-to-use, and easy-to-deploy solutions for building APIs.

2. Setting Up the Development Environment:
   - Install Python on your machine if you haven't already (version 3.7 or higher is recommended).
   - Create a new virtual environment for your FastAPI project.
   - Activate the virtual environment and install FastAPI and its dependencies.

3. Creating a FastAPI Application:
   - Create a new Python file named "main.py" to hold your FastAPI application.
   - Import the necessary modules and libraries, such as FastAPI and Pydantic.
   - Create an instance of the FastAPI class to represent your application.

4. Defining API Endpoints:
   - FastAPI uses decorators to define API endpoints.
   - Use the `@app.get`, `@app.post`, `@app.put`, `@app.delete`, etc., decorators to define the HTTP methods and routes for your API endpoints.
   - Specify the route, request method, and any necessary path parameters or query parameters.

5. Handling Request Data:
   - FastAPI integrates with Pydantic to handle request data validation and serialization.
   - Create Pydantic models to represent the request and response data structures.
   - Use these models as function parameters or return types in your API endpoints.

6. Adding Business Logic:
   - Implement the necessary business logic inside your API endpoint functions.
   - This can include interacting with databases, calling external APIs, or performing any other required operations.

7. Handling Responses:
   - FastAPI handles response serialization automatically based on the Pydantic models you use.
   - Return the desired response data as a Pydantic model instance from your API endpoint functions.
   - FastAPI will automatically convert the response data to the appropriate format (JSON, XML, etc.) and set the correct HTTP headers.

Part B: Example Application - Bookstore API

For the purpose of this course, we will build a simple Bookstore API using FastAPI. The API will allow us to perform basic CRUD operations on books.

1. Define the Book Model:
   - Create a Pydantic model named "Book" with attributes such as title, author, publication year, and ISBN.

2. Create the Database:
   - Set up a database (e.g., SQLite, MySQL, or PostgreSQL) to store book data.
   - Connect to the database and create a table or collection to store books.

3. Implement the CRUD Operations:
   - Create: Define an API endpoint to add a new book to the database.
   - Read: Define an API endpoint to retrieve a specific book by its ID or retrieve all books.
   - Update: Define an API endpoint to update the information of an existing book.
   - Delete: Define an API endpoint to delete a book from the database.

4. Test the API:
   - Use tools like cURL, Postman, or HTTPie to test the API endpoints and ensure they return the expected responses.
 - Send requests to create, retrieve, update, and delete books, and verify the results.
 Solution 

Part B: Example Application - Bookstore API

Let's dive into the implementation of the Bookstore API using FastAPI. Follow the step-by-step instructions to create the CRUD operations for managing books.

Step 1: Define the Book Model
In your "main.py" file, import the necessary modules and libraries:
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
```
Define the Book model using Pydantic:
```python
class Book(BaseModel):
    title: str
    author: str
    publication_year: int
    isbn: str
```

Step 2: Create the Database
For simplicity, we will use an in-memory list to store the book data.
```python
books = []
```

Step 3: Implement the CRUD Operations
a. Create - Adding a new book:
Define an API endpoint using the `@app.post` decorator:
```python
@app.post("/books/")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully"}
```

b. Read - Retrieving books:
i. Retrieve all books:
Define an API endpoint using the `@app.get` decorator:
```python
@app.get("/books/")
def get_books():
    return books
```
ii. Retrieve a specific book by its ID:
Define an API endpoint using the `@app.get` decorator and specify the book ID as a path parameter:
```python
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"message": "Book not found"}
```

c. Update - Updating book information:
Define an API endpoint using the `@app.put` decorator and specify the book ID as a path parameter:
```python
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for book in books:
        if book.id == book_id:
            book.title = updated_book.title
            book.author = updated_book.author
            book.publication_year = updated_book.publication_year
            book.isbn = updated_book.isbn
            return {"message": "Book updated successfully"}
    return {"message": "Book not found"}
```

d. Delete - Deleting a book:
Define an API endpoint using the `@app.delete` decorator and specify the book ID as a path parameter:
```python
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}
```

Step 4: Test the API
You can now test the API using tools like cURL, Postman, or HTTPie. Here are a few examples:

- To add a new book:
```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"title":"Book Title", "author":"Author Name", "publication_year": 2022, "isbn": "1234567890"}' http://localhost:8000/books/
```

- To retrieve all books:
```bash
$ curl http://localhost:8000/books/
```

- To retrieve a specific book by its ID:
```bash
$ curl http://localhost:8000/books/1
```

- To update a book:
```bash
$ curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Title", "author":"Updated Author", "publication_year": 2022, "isbn": "1234567890"}' http://localhost:8000/books/1
```

- To delete a book:
```bash
$ curl -X DELETE http://localhost:8000/books/1
```
Let's enhance the Bookstore API by adding a custom HTML form for easy book. Follow the steps below to integrate the form into the FastAPI application.

Step 1: Create an "index.html" file
In the same directory as your "main.py" file, create a new file named "index.html". This file will contain the HTML form for book submission.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Bookstore API</title>
</head>
<body>
    <h1>Add a Book</h1>
    <form action="/books/" method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br><br>
        <label for="author">Author:</label>
        <input type="text" id="author" name="author" required><br><br>
        <label for="publication_year">Publication Year:</label>
        <input type="number" id="publication_year" name="publication_year" required><br><br>
        <label for="isbn">ISBN:</label>
        <input type="text" id="isbn" name="isbn" required><br><br>
        <input type="submit" value="Add Book">
    </form>
</body>
</html>
```

Step 2: Serve the HTML file
Modify your FastAPI application to serve the "index.html" file when accessing the root URL ("/").

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load HTML templates
templates = Jinja2Templates(directory="templates")

# Define the root route to serve the index.html file
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
```

Step 3: Add CSS styling (optional)
If desired, create a "styles.css" file in a new "static" directory within the project directory. Add custom CSS styles to this file to enhance the appearance of the HTML form.

Step 4: Test the form
Start the FastAPI server and navigate to http://localhost:8000 in your web browser. You should see the "Add a Book" form. Fill in the book details and click the "Add Book" button. The form submission will trigger a POST request to the "/books/" endpoint, adding the book to the database.


To demonstrate interoperability between a FastAPI application and a JAX-WS WSDL web service, we will create a FastAPI application that consumes the JAX-WS web service. 

Step 1: Install Required Libraries
Ensure you have the required libraries installed by running the following commands:

```
pip install zeep
pip install fastapi
pip install uvicorn
```

Step 2: Create a FastAPI Application
Create a new Python file, e.g., `app.py`, and import the necessary modules:

```python
from fastapi import FastAPI
from zeep import Client

app = FastAPI()

# Create a Zeep client to consume the WSDL web service
client = Client('http://example.com/your-wsdl-url')
```

Step 3: Define FastAPI Routes
Define the FastAPI routes that will interact with the JAX-WS web service. Here's an example of a route that consumes a method from the web service:

```python
@app.get("/example-route")
def example_route():
    # Call a method from the JAX-WS web service
    result = client.service.example_method()

    # Process the result
    # ...

    return {"message": "Response from JAX-WS web service: " + result}
```

Step 4: Run the FastAPI Application
To run the FastAPI application, use the following command:

```
uvicorn app:app --reload
```

This will start the FastAPI application on a local server.

Now, you can access the FastAPI routes, such as `http://localhost:8000/example-route`, which will call the JAX-WS web service method and return the response.

Remember to replace `http://example.com/your-wsdl-url` with the actual URL of your JAX-WS WSDL web service.

By following these steps, you can create a FastAPI application that interoperates with a JAX-WS WSDL web service. 
Certainly! Let's create an example application for a Bank app using FastAPI that demonstrates interoperability with a JAX-WS WSDL web service. This application will allow users to perform basic banking operations such as checking account balance, making deposits, and withdrawing funds by consuming methods from the JAX-WS web service.

Step 1: Set up the FastAPI Application
Create a new Python file, e.g., `bank_app.py`, and import the necessary modules:

```python
from fastapi import FastAPI
from zeep import Client

app = FastAPI()

# Create a Zeep client to consume the WSDL web service
client = Client('http://example.com/your-wsdl-url')
```

Step 2: Define the Account Model
Create a data model for the account that includes attributes like account number, account holder name, and current balance. Add the following code below the imports:

```python
from pydantic import BaseModel

class Account(BaseModel):
    account_number: str
    account_holder: str
    balance: float
```

Step 3: Create the Account Endpoint
Define an API endpoint to retrieve the account details by calling a method from the JAX-WS web service. Add the following code below the account model:

```python
@app.get("/account/{account_number}")
def get_account(account_number: str):
    # Call the method from the JAX-WS web service to retrieve account details
    result = client.service.get_account_details(account_number)

    # Process the result
    # Extract relevant information from the response and create an Account object
    account = Account(
        account_number=result['account_number'],
        account_holder=result['account_holder'],
        balance=result['balance']
    )

    return account
```

Step 4: Create Deposit and Withdrawal Endpoints
Define API endpoints for making deposits and withdrawals by calling respective methods from the JAX-WS web service. Add the following code below the get_account endpoint:

```python
@app.post("/account/{account_number}/deposit")
def deposit(account_number: str, amount: float):
    # Call the method from the JAX-WS web service to make a deposit
    result = client.service.make_deposit(account_number, amount)

    # Process the result
    # ...

    return {"message": "Deposit successful"}


@app.post("/account/{account_number}/withdraw")
def withdraw(account_number: str, amount: float):
    # Call the method from the JAX-WS web service to make a withdrawal
    result = client.service.make_withdrawal(account_number, amount)

    # Process the result
    # ...

    return {"message": "Withdrawal successful"}
```

Step 5: Run the FastAPI Application
To run the FastAPI application, use the following command:

```
uvicorn bank_app:app --reload
```

This will start the Bank app on a local server.

Now, you can access the following routes:

- `http://localhost:8000/account/{account_number}`: Retrieve account details by providing the account number. This will call the corresponding method from the JAX-WS web service.
- `http://localhost:8000/account/{account_number}/deposit`: Make a deposit by providing the account number and the amount. This will call the respective method from the JAX-WS web service.
- `http://localhost:8000/account/{account_number}/withdraw`: Withdraw funds by providing the account number and the amount. This will call the respective method from the JAX-WS web service.

Remember to replace `http://example.com/your-wsdl-url` with the actual URL of your JAX-WS WSDL web service.

By following these steps, you have created a Bank app using FastAPI that interoperates with a JAX-WS WSDL web service. Users can retrieve account details, make deposits, and withdraw funds by consuming methods from the JAX-WS web service through the provided API endpoints. 
Integration ORM for data Access

To integrate ORM (Object-Relational Mapping) for MySQL operations in a Java application, we can use a popular ORM framework like Hibernate. Hibernate simplifies database operations by mapping Java objects to relational database tables.

Here's a step-by-step guide to integrating ORM MySQL operations using Hibernate in a Java application:

Step 1: Set up the Project Dependencies
Add the necessary dependencies to your project's build file (e.g., pom.xml if using Maven) to include Hibernate and the MySQL connector. Here's an example:

```xml
<dependencies>
    <!-- Hibernate ORM -->
    <dependency>
        <groupId>org.hibernate</groupId>
        <artifactId>hibernate-core</artifactId>
        <version>5.5.7.Final</version>
    </dependency>

    <!-- MySQL Connector -->
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>8.0.27</version>
    </dependency>
</dependencies>
```

Step 2: Configure Hibernate
Create a Hibernate configuration file (e.g., `hibernate.cfg.xml`) and provide the necessary configurations for connecting to your MySQL database. Here's an example:

```xml
<hibernate-configuration>
    <session-factory>
        <!-- Database connection properties -->
        <property name="hibernate.connection.driver_class">com.mysql.cj.jdbc.Driver</property>
        <property name="hibernate.connection.url">jdbc:mysql://localhost:3306/your-database</property>
        <property name="hibernate.connection.username">your-username</property>
        <property name="hibernate.connection.password">your-password</property>

        <!-- Mapping configuration -->
        <!-- Add your entity classes here -->

        <!-- Other Hibernate properties -->
        <property name="hibernate.dialect">org.hibernate.dialect.MySQL8Dialect</property>
        <property name="hibernate.hbm2ddl.auto">update</property>
    </session-factory>
</hibernate-configuration>
```

Step 3: Create Entity Classes
Create Java classes representing the entities (database tables) that you want to map. Annotate the classes and their attributes with Hibernate annotations to define the mapping. Here's an example:

```java
import javax.persistence.*;

@Entity
@Table(name = "customers")
public class Customer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    // ... getters and setters
}
```

Step 4: Perform Database Operations
Now you can use Hibernate to perform database operations in your Java application. Here's an example of saving a new customer to the database:

```java
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class Main {
    public static void main(String[] args) {
        // Create a SessionFactory (should be done once per application)
        SessionFactory sessionFactory = new Configuration()
                .configure("hibernate.cfg.xml")
                .buildSessionFactory();

        // Create a Session
        Session session = sessionFactory.getCurrentSession();

        try {
            // Start a transaction
            session.beginTransaction();

            // Create a new customer
            Customer customer = new Customer();
            customer.setName("John Doe");

            // Save the customer to the database
            session.save(customer);

            // Commit the transaction
            session.getTransaction().commit();

            System.out.println("Customer saved successfully!");
        } finally {
            // Close the session and the SessionFactory
            session.close();
            sessionFactory.close();
        }
    }
}
```

By following these steps, you have integrated ORM MySQL operations using Hibernate in your Java application. You can perform various database operations like saving, updating, retrieving, and deleting entities using the power of Hibernate's ORM capabilities.
To integrate Hibernate and the MySQL JDBC driver in a Java project, you'll need to follow these steps:

Step 1: Download Hibernate and MySQL Connector/J
First, download the Hibernate ORM framework and the MySQL Connector/J JDBC driver.

- Hibernate: Visit the official Hibernate website (https://hibernate.org/orm/releases/) and download the latest stable version of Hibernate ORM.
- MySQL Connector/J: Go to the MySQL website (https://dev.mysql.com/downloads/connector/j/) and download the latest version of the MySQL Connector/J JDBC driver.

Step 2: Set Up Project Structure
Create a new Java project in your preferred Integrated Development Environment (IDE). Once the project is set up, create a folder called "lib" (or any name you prefer) in your project's root directory. Copy the downloaded Hibernate and MySQL Connector/J JAR files into this "lib" folder.

Step 3: Add JAR Files to Project Classpath
Add the Hibernate and MySQL Connector/J JAR files to your project's classpath. The specific steps to do this depend on the IDE you're using. Here are general instructions for some popular IDEs:

- Eclipse: Right-click on your project, select "Build Path" > "Configure Build Path." In the "Libraries" tab, click "Add JARs" and navigate to the "lib" folder to select the Hibernate and MySQL Connector/J JAR files.
- IntelliJ IDEA: Right-click on your project, select "Open Module Settings." In the "Libraries" section, click the "+" button and choose "Java." Locate and select the Hibernate and MySQL Connector/J JAR files from the "lib" folder.

Step 4: Configure Hibernate
Create a Hibernate configuration file (e.g., `hibernate.cfg.xml`) in your project's source directory. Provide the necessary configurations for connecting to your MySQL database. Here's an example configuration:

```xml
<hibernate-configuration>
    <session-factory>
        <!-- Database connection properties -->
        <property name="hibernate.connection.driver_class">com.mysql.cj.jdbc.Driver</property>
        <property name="hibernate.connection.url">jdbc:mysql://localhost:3306/your-database</property>
        <property name="hibernate.connection.username">your-username</property>
        <property name="hibernate.connection.password">your-password</property>

        <!-- Mapping configuration -->
        <!-- Add your entity classes here -->

        <!-- Other Hibernate properties -->
        <property name="hibernate.dialect">org.hibernate.dialect.MySQL8Dialect</property>
        <property name="hibernate.hbm2ddl.auto">update</property>
    </session-factory>
</hibernate-configuration>
```

Ensure that the `driver_class` property value matches the MySQL Connector/J driver class.

Step 5: Start Using Hibernate
With the Hibernate configuration set up, you can start using Hibernate in your Java project. Create entity classes, annotate them with Hibernate annotations, and write code to perform database operations.

Remember to import the necessary Hibernate packages in your Java classes, such as `org.hibernate.SessionFactory`, `org.hibernate.Session`, and `org.hibernate.cfg.Configuration`.

That's it! You have integrated Hibernate and the MySQL JDBC driver in your Java project. You can now leverage Hibernate's ORM capabilities to interact with your MySQL database. 
