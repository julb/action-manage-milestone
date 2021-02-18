import os
from datetime import date
from github import Github, GithubObject


def main():
    """ The main method executed. """

    # Input variables
    github_token = os.environ.get('GITHUB_TOKEN')
    github_repository = os.environ.get('GITHUB_REPOSITORY')
    milestone_title = os.environ.get('INPUT_TITLE')
    milestone_state = os.environ.get('INPUT_STATE', GithubObject.NotSet)
    milestone_description = os.environ.get(
        'INPUT_DESCRIPTION', GithubObject.NotSet)
    milestone_due_on = os.environ.get('INPUT_DUE_ON', GithubObject.NotSet)

    # Post-process date-time.
    milestone_due_on_datetime = GithubObject.NotSet
    if milestone_due_on is not GithubObject.NotSet:
        milestone_due_on_datetime = date.fromisoformat(milestone_due_on)

    # Get repository.
    github = Github(github_token)
    github_repo = github.get_repo(github_repository)

    # Check if already exists.
    existing_github_milestone = None
    for github_milestone in github_repo.get_milestones(state='all'):
        if github_milestone.title.lower() == milestone_title.lower():
            existing_github_milestone = github_milestone
            break

    if not existing_github_milestone:
        existing_github_milestone = github_repo.create_milestone(
            title=milestone_title, state=milestone_state, description=milestone_description, due_on=milestone_due_on_datetime)
    else:
        existing_github_milestone.edit(
            title=milestone_title, state=milestone_state, description=milestone_description, due_on=milestone_due_on_datetime)

    # Return number.
    print(f"::set-output name=number::{existing_github_milestone.number}")


if __name__ == "__main__":
    main()
