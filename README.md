# Birthdays Tracker

This is simple Flask web application that allows users to track and store birthdays.This application stores birthdays entries in a SQLite database and display them on the homepage.Users can add new birthdays through a form, and the application will provide feedback using flash messages.

## Features

- Add a new birthdays (name, month, day).
- Validate user inputs to ensure the correct day and month values.
- Display all stored birthdays on the homepage.
- Use the flash messages to provide feedback to users for successful operations.
- Prevent browser catching to ensure users recieve the most up-to-date version of the website.


## Installation

1. **Clone the repository:**

```
bash
git clone https://github.com/eddie-96/birthdays.git
cd birthdays
```

2. **Setup virtual environment**

```pip install -r requirements.txt```

3. **Structure database**

```
CREATE TABLE birthdays (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
month INTEGER NOT NULL,
day INTEGER NOT NULL
);
```

4. **Run the application**

``` flask run ```

## Usage

- Open your browser  and navigate to http://127.0.0.1:5000/ through the search bar.
- Add a new birthday through the form on the homepage.
- The application will display all stored birthdays and notify you when a new birthdays is added.