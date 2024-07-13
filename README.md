# GlitchSpy

GlitchSpy is an innovative application designed to track and expose software products from various organizations that have defects and bugs. It also provides a web-based API service to facilitate easy reporting and tracking of these issues.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## About

### Inspiration

The inspiration for GlitchSpy stemmed from a personal frustration with encountering unresolved bugs and defects in software products. There is a growing demand for transparency in how software companies handle bugs, and users want to be informed about known issues and their resolution status. GlitchSpy aims to provide a platform where users and developers can report and track bugs, harnessing the power of community collaboration to improve software quality.

## Features

- **Report Bug**: Users can report bugs in various software products, specifying details such as title, description, category, severity, product, version, and attachments.
- **View Bug Reports**: Users can view a list of all reported bugs, along with detailed information for each bug.
- **Upvote Bugs**: Users can upvote bug reports to indicate which issues are most pressing.
- **Comment on Bugs**: Users can add comments to bug reports to provide additional information or discuss the issue.
- **User/Organization Registration**: Organizations can register themselves, and individual users can also create accounts.

## Technologies

### Libraries, Languages, Platforms, Frameworks
- **Python**: Programming language for backend development.
- **Flask**: Web framework for building the API and web application.
- **SQLAlchemy**: ORM for database interactions.
- **HTML/CSS/JavaScript**: Frontend technologies.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/omollpeter/GlitchSpy.git
   cd GlitchSpy
   ```

2. **Set Up a Virtual Environment**:
    ```bash
    python3 -m venv venv
    ```

    Activate the virtual environment:

    - **On Windows**:
    ```bash
    venv\Scripts\activate
    ```

    - **On macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**
    Ensure that all the necessary environment variables are set for database interaction. See 'models/engine/db_storage.py'.

    Start the development server:
    ```bash
    python3 -m frontend.gspy
    ```
    The application should now be running at http://127.0.0.1:5050.


## Usage 
Visit [website](https://www.omollpeter.tech)

### Reporting a Bug

1. **Navigate to the "Report Bug" section.**
   - Access the "Report Bug" page from the main navigation menu.

2. **Fill in the details:**
   - **Title**: Provide a concise title for the bug report.
   - **Description**: Enter a detailed description of the bug.
   - **Category**: Select the appropriate category for the bug.
   - **Severity**: Choose the severity level of the bug (e.g., Low, Medium, High).
   - **Product**: Specify the product or software where the bug was found.
   - **Version**: Indicate the version of the product affected by the bug.
   - **Attachments**: Add any relevant files, such as screenshots or videos, that help illustrate the bug.

3. **Submit the bug report.**
   - Click the "Submit" button to send your bug report to the system.

### Viewing Bug Reports

1. **Go to the "View Bug Reports" section.**
   - Navigate to the "View Bug Reports" page from the main menu.

2. **Browse the list of reported bugs.**
   - Scroll through the list to see all reported bugs.

3. **Click on a bug to view detailed information.**
   - Select a bug report from the list to see more detailed information, including descriptions, comments, and attachments.

### Upvoting and Commenting

1. **Select a bug report.**
   - Open the detailed view of the bug report you are interested in.

2. **Click the "Upvote" button to indicate priority.**
   - Click the "Upvote" button to increase the priority of the bug report.

3. **Add comments to discuss the bug or provide additional information.**
   - Use the comment section to add your thoughts or additional details about the bug.

### GlitchSpy API
See documentation at [api](https://www.omollpeter.tech/gspy/api)


## License
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.