import os
import requests
import openai

# Set up the OpenAI API
openai.api_key = "your_openai_api_key"

# Set your GitHub access token
github_token = "your_github_token"

# Set your GitHub repository information
owner = "your_github_username"
repo = "your_repository_name"

# Function to generate documentation using GPT-4
def generate_documentation(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to get file content from GitHub
def get_file_content(file_url):
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(file_url, headers=headers)
    return response.text

# Get repository files
headers = {"Authorization": f"token {github_token}"}
repo_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1"
response = requests.get(repo_url, headers=headers)
files = response.json()["tree"]

# Iterate over files and generate documentation
for file in files:
    if file["type"] == "blob" and (file["path"].endswith(".py") or file["path"].endswith(".rs")):
        print(f"Generating documentation for {file['path']}...")
        file_content = get_file_content(file["url"])
        file_type = file['path'].split('.')[-1].upper()
        prompt = f"Document the following {file_type} code in AsciiDoc format:\n{file_content}\n"
        doc = generate_documentation(prompt)
        print(doc)
        print("\n" + "=" * 80 + "\n")
