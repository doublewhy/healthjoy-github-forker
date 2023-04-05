from github import Github, GithubException


def fork_repo(repo, token):
    try:
        # Check if the repo name and token are not empty
        if not token:
            raise ValueError("GitHub access token cannot be empty")

        if not repo:
            raise ValueError("Repo name cannot be empty")

        account = Github(token)
        user = account.get_user()
        repo_to_fork = account.get_repo(repo)

        # Check if the repository is already forked by the user
        for repo in user.get_repos():
            if repo_to_fork.name == repo.name:
                raise ValueError("Repository has already been forked")

        # Fork the repository
        forked_repo = user.create_fork(repo_to_fork)

        return forked_repo

    except GithubException as e:
        raise ValueError("Unable to fork repository: " + str(e))
