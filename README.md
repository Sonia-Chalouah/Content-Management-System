CMS Project
Description
This project is a simple Content Management System (CMS) designed to manage words and phrases. It allows users to view, search, edit, and update words or phrases along with their corresponding translations and example sentences.
Features
- **Paginated Word List**: View words/phrases in a paginated list.
- **Search Functionality**: Search words/phrases by keyword.
- **Edit Functionality**: Edit or update words/phrases with a new translation or example sentence.
- **Responsive Design**: Optimized interface for both desktop and mobile devices.
Tech Stack
- **Frontend**: HTML, CSS, Bootstrap 4, JavaScript
- **Backend**: Django 5.x (Python)
- **Database**: SQLite (can be replaced with other databases like MySQL)
- **Authentication**: Built-in Django authentication
Setup
Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- pip (Python package installer)
- Git (for cloning the repository)
Steps to Run the Project Locally
1. **Clone the Repository**:
   ```bash
   git clone <repo_url>
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd cms_project
   ```

3. **Install Dependencies**:
   It's recommended to use a virtual environment (optional but recommended). Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   Apply the database migrations to set up the necessary tables:
   ```bash
   python manage.py migrate
   ```

5. **Load Initial Data (if applicable)**:
   If there are any initial data fixtures or sample data to load, use the following command:
   ```bash
   python manage.py loaddata <data_file_name>.json
   ```

6. **Start the Development Server**:
   Run the Django development server to start the application:
   ```bash
   python manage.py runserver
   ```

7. **Access the App**:
   Open your web browser and navigate to:
   ```plaintext
   http://127.0.0.1:8000/
   ```
Usage
- On the adminpage, you will see a list of words and phrases.
- You can search for specific words or phrases by entering a keyword in the search bar.
- To edit a word or phrase, click on the 'Edit' button beside the word.
- The sidebar provides navigation to the Word List .
Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes.
4. Commit your changes:
   ```bash
   git commit -am 'Add feature'
   ```
5. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
6. Create a new Pull Request.

Demo Link:[https://drive.google.com/file/d/1BdeY6Yy52pZtCGCAH-x7bfBgBNyteFS2/view]
