# Bojji

This script generates documentation for Cairo files in a GitHub repository using GPT-4 and outputs it in AsciiDoc format.

## Installation

1. Clone the repository.
2. Change into the repository directory: `cd bojji`.
3. Install the dependencies: `pip install -r requirements.txt`. You may want to use a virtual environment. See [this guide](https://docs.python.org/3/tutorial/venv.html) for more information.

## Usage

Before running the script, make sure to set the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `GITHUB_TOKEN`: Your GitHub personal access token
- `GITHUB_OWNER`: The GitHub username of the repository owner
- `GITHUB_REPO`: The name of the GitHub repository

Run the script using the following command:

```python
python src/generate_documentation.py
```



