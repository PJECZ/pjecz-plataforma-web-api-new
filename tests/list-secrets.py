"""
Google Secret Manager

Listar todos los secretos de un proyecto
"""
import os

from dotenv import load_dotenv
from google.cloud import secretmanager

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID", "justicia-digital-gob-mx")


def list_secrets(project_id: str = PROJECT_ID) -> list:
    """List all secrets in the given project"""

    # Create the Secret Manager client
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the parent project
    parent = f"projects/{project_id}"

    # Return a list with all secrets
    return [secret for secret in client.list_secrets(request={"parent": parent})]


def main():
    """Test Google Secret Manager"""

    # If not in google cloud, exit
    if PROJECT_ID == "":
        print("No project id")
        return

    # Print all secrets ids
    for secret in list_secrets():
        print(secret.name)


if __name__ == "__main__":
    main()
