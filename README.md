# Expense Tracker Project Using OOP </h1>
## Project Description
The goal of this project is to use object-oriented progreamming (OOP) concept in python to implement Expense and ExpenseDatabase classes to model and manage financial expenses.

This simple Python project allows users to manage and track individual financial expenses. It consists of two main classes: `Expense` for representing a single expense and `ExpenseDB` for managing a collection of expenses.

### Expense Class

The `Expense` class represents a single expense and is defined by the following attributes:

- **id:** A unique identifier generated as a UUID string.
- **title:** A string representing the title or description of the expense.
- **amount:** A float representing the monetary value of the expense.
- **created_at:** A timestamp indicating when the expense was created in Coordinated Universal Time (UTC).
- **updated_at:** A timestamp indicating the last time the expense was updated in UTC.

In addition, the `Expense` class provides the following methods:

- **__init__:** Initializes the attributes of the expense.
- **update:** Allows updating the title and/or amount, automatically updating the `updated_at` timestamp.
- **to_dict:** Returns a dictionary representation of the expense.

### ExpenseDB Class

The `ExpenseDB` class manages a collection of `Expense` objects and serves as a centralized repository for expense-related operations. Its key features include:

- **__init__:** Initializes the expenses list.
- **add_expense:** Adds an expense to the database.
- **remove_expense:** Removes an expense from the database based on its ID.
- **get_expense_by_id:** Retrieves an expense from the database based on its ID.
- **get_expenses_by_title:** Retrieves a list of expenses from the database based on their titles.
- **to_dict:** Returns a list of dictionaries representing all expenses in the database.

### Project use cases

1. **Expense Tracking:** Users can create, update, and delete individual expenses, allowing for detailed tracking of financial transactions.
  
2. **Data Organization:** The `ExpenseDatabase` class provides a structured way to organize and manage a collection of expenses, facilitating easy retrieval and modification.

3. **User Interaction:** While the provided code is primarily focused on the backend logic, this project could be extended to include a user interface (UI) for a more user-friendly experience.

4. **Customization:** Users can customize the project based on their specific financial tracking needs, and additional features such as data persistence, reporting, or integration with external tools can be implemented.

This project provides a foundation for building a more comprehensive expense tracking system and can be adapted and extended according to specific requirements.

## How this project was cloned.
To clone this project from my remote repository on Github to my local repository, I followed these steps:

1. **Copied Repository URL:**
   - Clicked on the "Code" button, and copied the repository URL `https://github.com/JussieT/Alt_sch_fall_semester_project.git`.

2. **Opened windows powershell:**
   - Opened the windows powershell on my local machine.

3. **Navigated to the Directory Where I Cloned the Repository:**
   - Used the `pwd` command to find out the current directory I was working on, `ls -l` command to list the files and directories on that directory and  `cd` command to navigate to the directory where I stored the local copy of the repository.

4. **Cloned the Repository:**
   - Used the `git clone` command followed by the personal access token i generated and then @ the repository URL.
     ```powershell
     git clone https://(personal access token)@github.com/JussieT/Alt_sch_fall_semester_project.git
     ```
5. **Verified the Cloning Process:**
   - After I executed the `git clone` command, I saw an output indicating that it was successfully cloned.

## How to run this project
The codes below demonstrates the basic functionality of this project which includes but not limited to creating expenses, updating them, managing them in a database, and performing operations like retrieval and removal based on ID or title.

1. **Create an Expense:**
   ```python
   expense = Expense(title="Chicken", amount=10000.0)
   ```

2. **Print Expense Details:**
   ```python
   print(expense.to_dict())
   ```
   The `to_dict` method of the `Expense` class is used to print a dictionary representation of the expense. This includes details such as the expense ID, title, amount, created_at timestamp, and updated_at timestamp.

3. **Update the Expense:**
   ```python
   expense.update(title="Christmas Chicken", amount=15000.0)
   ```

4. **Print Updated Expense Details:**
   ```python
   print(expense.to_dict())
   ```

5. **Create an Expense Database:**
   ```python
   database = ExpenseDB()
   ```

6. **Add Expenses to the Database:**
   ```python
   database.add_expense(expense1)
   database.add_expense(expense2)
   ```

7. **Get Expense by ID:**
   ```python
   found_expense = database.get_expense_by_id(expense1.id)
   if found_expense:
       print(found_expense.to_dict())
   else:
       print("Expense not found.")
   ```

8. **Get Expenses by Title:**
   ```python
   expenses_by_title = database.get_expenses_by_title("Utilities")
   for expense in expenses_by_title:
       print(expense.to_dict())
   ```
   
   ```python
   database.remove_expense(expense1.id)
   ```

10. **Print Remaining Expenses in the Database:**
    ```python
    print(database.to_dict())
    ```
    The `to_dict` method of the `ExpenseDatabase` class is used to print a list of dictionaries representing the remaining expenses in the database.

The above python script can be run by navigating to the script's directory on powershell and using the command `python3` before the script's name. or by running it using an ide for example, visual studio code or jupyter notebook.
