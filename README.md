## UniLink

UniLink is a web application designed to simplify the university application process for students in Ghana. It offers a centralized online platform where students can search for universities and apply to multiple schools directly from the application, saving time and effort.

### Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Development Workflow](#development-workflow)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

### About the Project

UniLink addresses the traditional, time-consuming process of physically visiting schools to purchase application forms and stand in long queues. With UniLink, students can easily search for universities and apply online, while schools can manage applications more efficiently. The platform integrates seamlessly with the backend to handle application data securely and efficiently, providing an all-in-one solution for higher education applications in Ghana.

### Features

- **University Search:** Allows students to search for universities using keywords or filters to find relevant options.
- **Application Submission:** Enables students to submit applications directly through the platform.
- **Secure Data Handling:** Integrates with backend services to securely manage application data.
- **User-Friendly Interactions:** Ensures a smooth and intuitive user experience with robust error handling and data validation.
- **Responsive Design:** The frontend is designed to be fully responsive and mobile-friendly.
- **Automated Testing and CI/CD:** Utilizes automated testing and continuous integration/continuous deployment (CI/CD) pipelines for reliable, high-quality deployments.

### Technologies Used

- **Languages:** JavaScript, Python
- **Frameworks & Libraries:** Flask (Python), React (JavaScript), Tailwind CSS
- **Database:** PostgreSQL
- **Tools:** GitHub (version control), Jenkins (CI/CD)

### Installation

To get a local copy up and running, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/unilink.git
   cd unilink
   ```

2. **Backend Setup:**

   - Navigate to the `backend` directory.
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Set up the PostgreSQL database and run migrations:
     ```bash
     flask db upgrade
     ```

3. **Frontend Setup:**

   - Navigate to the `frontend` directory.
   - Install Node.js dependencies:
     ```bash
     npm install
     ```

4. **Environment Variables:**

   - Create a `.env` file in the `backend` directory and configure your environment variables (e.g., database URL, secret keys).

5. **Start the Application:**

   - Start the backend server:
     ```bash
     flask run
     ```
   - Start the frontend server:
     ```bash
     npm start
     ```

6. **Access the Application:**
   - Open your web browser and navigate to `http://localhost:3000` to access the frontend.

### Usage

1. **Search for Universities:**
   - Use the search bar to enter keywords or select filters to find universities.

2. **Apply to a University:**
   - Click on a university from the search results to view more details.
   - Fill out the application form and submit it directly from the platform.

3. **User Account Management:**
   - Sign up or log in to manage your applications and view the status of submitted applications.

### API Documentation

The backend API is built with Flask and follows RESTful principles. Below is an overview of the key endpoints:

- **GET /api/universities:** Retrieve a list of universities based on search criteria.
- **POST /api/applications:** Submit a new application.
- **GET /api/applications/{id}:** Retrieve details of a specific application.
- **PUT /api/applications/{id}:** Update an existing application.
- **DELETE /api/applications/{id}:** Delete an application.

Refer to the [API documentation](docs/API.md) for more detailed information on request parameters and response formats.

### Development Workflow

1. **GitHub Flow:**
   - Create a new branch for each feature or bugfix (`feature/feature-name` or `bugfix/issue-description`).
   - Commit your changes to the new branch.
   - Open a pull request (PR) for code review.
   - After approval, merge the PR into the `main` branch.

2. **Continuous Integration/Continuous Deployment (CI/CD):**
   - Jenkins will automatically build and deploy the latest version to the staging environment when changes are merged into the `main` branch.
   - After successful testing in staging, deployment to the production environment will be triggered.

### Testing

- **Unit Tests:** Located in the `tests` directory for both frontend and backend.
  - Run backend tests:
    ```bash
    pytest
    ```
  - Run frontend tests:
    ```bash
    npm test
    ```
- **Integration Tests:** Ensure API endpoints and frontend components work together seamlessly.
- **End-to-End Tests:** Use Cypress to simulate real user interactions.
  - Run end-to-end tests:
    ```bash
    npx cypress open
    ```

### Deployment

- **Staging Environment:** Deployed automatically via Jenkins after changes are merged into the `main` branch.
- **Production Environment:** After successful testing in staging, the production environment is updated with the latest stable release.

### Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on the code of conduct, and the process for submitting pull requests.

### License

Distributed under the MIT License. See `LICENSE` for more information.

### Contact

**Maxwell Duedu**  
Backend Developer, Database Administrator, Frontend Developer, QA Tester  
Email: duedumaxwell63@gmail.com