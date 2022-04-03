root := justfile_directory()

install:
    #!/bin/bash
    python3 -m venv {{root}}/.pyenv
    source {{root}}/.pyenv/bin/activate
    python -m pip install -r {{root}}/requirements.txt

start:
    #!/bin/bash
    source {{root}}/.pyenv/bin/activate
    python main.py