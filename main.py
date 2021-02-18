#!/usr/bin/python3
import os
from datetime import date
from github import Github, GithubObject


def main():
    """ The main method executed. """

    # Input variables
    github_token = os.environ.get('GITHUB_TOKEN')
    github_repository = os.environ.get('GITHUB_REPOSITORY')
    input_milestone_title = os.environ.get('INPUT_TITLE')
    input_milestone_state = os.environ.get('INPUT_STATE', 'open')
    input_milestone_description = os.environ.get('INPUT_DESCRIPTION', '')
    input_milestone_due_on = os.environ.get('INPUT_DUE_ON', '')

    # Post-process date-time.
    milestone_title = input_milestone_title
    milestone_state = input_milestone_state
    milestone_description = GithubObject.NotSet
    if input_milestone_description != '':
        milestone_description = input_milestone_description
    milestone_due_on = GithubObject.NotSet
    if input_milestone_due_on != '':
        milestone_due_on = date.fromisoformat(input_milestone_due_on)

    # Get repository.
    github = Github(github_token)
    github_repo = github.get_repo(github_repository)

    # Check if already exists.
    existing_github_milestone = None
    for github_milestone in github_repo.get_milestones(state='all'):
        if github_milestone.title.lower() == milestone_title.lower():
            existing_github_milestone = github_milestone
            break

    # Manage state.
    if milestone_state in ('open', 'closed'):
        if not existing_github_milestone:
            existing_github_milestone = github_repo.create_milestone(
                title=milestone_title, state=milestone_state, description=milestone_description, due_on=milestone_due_on)
        else:
            existing_github_milestone.edit(
                title=milestone_title, state=milestone_state, description=milestone_description, due_on=milestone_due_on)

        # Return milestone number.
        print(f"::set-output name=number::{existing_github_milestone.number}")

    elif milestone_state == 'deleted':
        # Delete if repo exists.
        if existing_github_milestone is not None:
            existing_github_milestone.delete()

        # Return 0 as number.
        print("::set-output name=number::0")


if __name__ == "__main__":
    main()
