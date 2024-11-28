# sound-synth

## Setup

1. Create virtual environment: `python -m venv .venv`
2. Activate the virtual environment: `source .venv/bin/activate`
3. Install packages: `pip install -r requirements.txt`
4. Run: `python app/main.py`

## OpenAi

To use ChatGPT LLM integration you need to provide an API.
This project use `dotenv`, the library will extract the environment variables declared
in the `.env` file and add the to the running context's environment variable.

The .gitignore file in the project excludes this file, thereby keeping you API key safe from
accidental commits.

1. Create a `.env` file in the root directory
2. Add your API key: `OPEN_API_KEY="your_key_goes_here"`

## Links

PyPi
https://pypi.org/project/synthesizer/


