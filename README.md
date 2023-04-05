# healthjoy-github-forker
 Take Home assignment for HealthJoy

# README

## Introduction

This repository contains a FastAPI application that allows to fork it's own
Github repo to a user's account using a provided access token. The application uses Jinja2 templates to display HTML pages.

## Installation

__It is highly recommended to create a virtual environment for Python to isolate your project's dependencies and prevent conflicts with other projects. You can easily create a virtual environment using tools such as `venv` or `conda`, activate it, and install the necessary dependencies.__

To install the required dependencies, run:

`pip install -r requirements.txt`

## Usage

To start the application, run:

`uvicorn main:app --reload`

Then, navigate to `http://localhost:8000` in your web browser.

To fork a repository, enter the repository name and your GitHub access token in the form on the main page and click the "Fork" button. The application will fork the repository and display a success message if the operation was successful, or an error message if it was not.

## Configuration

The following constants in the `main.py` file can be modified to change the behavior of the application:

- `REPO_TO_FORK`: The name of the repository to fork. Change this to fork a different repository.
- `GITHUB_TOKEN`: Your GitHub access token. Change this to use a different
  token.

If you do not have a GitHub access token, you can generate one by following [these instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

## Testing

To run the unit tests, run:

`pytest tests.py`

To separately test the `forker.py` module, run:

`python -m unittest forker_test.py`


## Comments
- This application was developed with a focus on simplicity and working within a
  constrained time frame.
- In the provided code, the GitHub token and repository to fork are hardcoded as
  constants. In real-world scenarios,
  these values should be passed as environment variables or obtained from a
  secure configuration management system. Hardcoding sensitive information in
  the code should be avoided.

## TO-DO
- **UI**. Improve the user interface to provide a better user experience and
  make it more visually appealing.
- **GitHub's OAuth** Implement GitHub's OAuth to authenticate users and secure
  the application.






