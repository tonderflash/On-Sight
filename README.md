# Django Project in Docker with Postgres

This project is designed as a guide for those learning to work with Django, Docker, and Postgres. It incorporates best practices in development, unit testing, and is configured with GitHub Actions and Flake 8 to ensure code quality and continuous integration.

## Features

- **Django**: A high-level web framework written in Python.
- **Docker**: A platform for developing, shipping, and running applications in containers.
- **Postgres**: A relational database management system.
- **GitHub Actions**: Workflow automation for CI/CD.
- **Flake 8**: A Python linting tool to enhance code quality.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic knowledge in Django, Docker, and Postgres.

## Configuration Instructions

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <directory_name>
   ```

3. Build the proyect:

   ```bash
   docker-compose build
   ```

4. Start the project:

   ```bash
   docker-compose up
   ```

   Or, if you prefer to run the Django server directly:e:

   ```bash
   docker-compose run --rm app sh -c "python manage.py runserver"
   ```
   Run the following command to initiate the superuser creation process:

  ```bash
    docker-compose run --rm app sh -c "python manage.py createsuperuser"
  ```

## How to Run Commands

To run any command related to the project::

```bash
docker-compose run --rm app sh -c "<comando>"
```

For example, to run migrations:

```bash
docker-compose run --rm app sh -c "python manage.py migrate"
```

## Contribution and Support

If you have suggestions, corrections, or improvements, feel free to submit a pull request or create an issue on GitHub. If you have questions about the project or encounter any issues, you can reach out to me directly.

## License

This project is distributed under the MIT License. You are free to use, modify, and distribute the code, but please provide proper attribution.

---

I hope this project serves as a guide and reference in your learning and development. Good Luck!
