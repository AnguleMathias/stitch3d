# "Redis-like" key-value store

A program that runs accepting shell commands

## Considerations

#### What data structures would be more adequate?

- Dictionaries

#### What is the Big O complexity of each operation?

- GET <key> :

- SET <key> <value> :

- UNSET <key> :

- NUMEQUALTO <value> :

- END :

## Getting Started

- Clone the project into your local repository using this command:

  `git clone https://github.com/AnguleMathias/stitch3d.git`

- Change directory to the cloned folder using the following command for Windows, Linux and MacOS

  `cd stitch3d`

- Run the app(for Windows, Linux and MacOS)

  `python3 run.py`

## Running the tests

- If you do not have a virtual environment installed run the following command, else follow the next steps.

  `pip install virtualenv`

- Create a virtual environment(for Windows, Linux and MacOS)

  `virtualenv venv`

- Activate the virtual environment(Windows only)

  `source venv/Scripts/activate`
  and for Linux and MacOS
  `source venv/bin/activate`

- Install pytest while the virtual environment is active

  `pip install pytest`

- Run the tests.

  `pytest`

:wink:
