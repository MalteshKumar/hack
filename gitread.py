import os
import tempfile
from git import Repo
from pathlib import Path

def clone_github_repo(repo_url):
    """
    Clones a GitHub repository to a temporary directory.

    Args:
        repo_url (str): The URL of the GitHub repository.

    Returns:
        str: The path to the cloned repository, or None if cloning failed.
    """
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            print(f"Cloning repository from {repo_url} to {temp_dir}")
            Repo.clone_from(repo_url, temp_dir)
            print("Repository cloned successfully.")
            return temp_dir
    except Exception as e:
        print(f"Error cloning repository: {e}")
        return None

if __name__ == "__main__":
    github_url = input("Enter the GitHub URL of the repository: ")
    cloned_path = clone_github_repo(github_url)
    if cloned_path:
        print(f"Repository cloned to {cloned_path}")
    else:
        print("Failed to clone the repository.")