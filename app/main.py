from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
import forker

# For purpose of this assignment, let's define required values as constants
REPO_TO_FORK = "doublewhy/healthjoy-github-forker"
GITHUB_TOKEN = "<github-access-token>"

app = FastAPI()

env = Environment(loader=FileSystemLoader("../front/templates/"))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    template = env.get_template("index.html")
    return HTMLResponse(content=template.render())


@app.post("/")
async def fork_github_repo(request: Request):
    try:
        # If Github's OAuth will be implemented, replace constant with a
        # provided token
        token = GITHUB_TOKEN

        # Fork the repository using the provided GitHub access token
        forker.fork_repo(REPO_TO_FORK, token)

        # Render the success template with a message indicating that the fork was successful
        template = env.get_template("success.html")
        return HTMLResponse(content=template.render())

    except Exception as e:
        # Catch any exceptions that occur and render the error template with an error message
        template = env.get_template("error.html")
        content = template.render(error=str(e))
        return HTMLResponse(content=content, status_code=500)
