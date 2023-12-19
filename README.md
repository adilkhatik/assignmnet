# assignmnet
Yoga Class Admission Form
This project implements a simple admission form for Yoga Classes. The form allows participants to enroll in monthly classes, adhering to specific requirements such as age limits, monthly fees, and batch choices. The backend is built using Django, providing a REST API for handling enrollments, payment simulation, and data storage.

Requirements
Age Limit: Participants must be within the age range of 18 to 65 to enroll.
Monthly Payment: Participants pay fees every month, and they can enroll any day, covering the entire month. The monthly fee is 500 INR.
Batch Choices: There are four batches available each day (6-7AM, 7-8AM, 8-9AM, and 5-6PM). Participants can choose any batch in a month and can switch batches in different months.
Implementation
Backend (Django)
Models:

YogaParticipant: Represents a participant with fields for name, age, selected batch, and enrollment timestamp.
Views:

enroll_participant: Handles POST requests for participant enrollment. Validates age, simulates payment using a mock function, and saves participant data to the database.
Serializers:

YogaParticipantSerializer: Converts YogaParticipant model instances to JSON and vice versa.
URLs:

/enroll/: Endpoint for enrolling participants.
Frontend (HTML/JavaScript)
Enrollment Form:

HTML form with fields for name, age, and batch selection.
JavaScript function (submitForm) to handle form submission using fetch API.
Enrollment Process:

On form submission, JavaScript sends a POST request to the Django backend (/enroll/).
Backend performs basic validation, simulates payment, and stores participant data.
Frontend receives response and displays a success or error message.
Setup Instructions
Backend Setup:

Install Python and Django.
Create a virtual environment.
Install required packages using pip install -r requirements.txt.
Apply database migrations: python manage.py migrate.
Run the Django development server: python manage.py runserver.
Frontend Setup:

Open index.html in a web browser.
Enter participant details and click the "Enroll" button.
Additional Notes:

Ensure CORS is configured correctly, especially if frontend and backend are on different domains.
Check the browser console and Django server logs for debugging.
Directory Structure
admissions/: Django app containing models, views, serializers, and URLs.
yoga_admission/: Django project settings.
index.html: HTML file for the enrollment form.
Technologies Used
Backend: Django, Django REST Framework.
Frontend: HTML, JavaScript.
Database: SQLite (default Django database).
Future Enhancements
Implement real payment processing logic.
Enhance frontend with better user experience and error handling.
Add user authentication for secure enrollment tracking.
