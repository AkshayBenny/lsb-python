## Running locally without Docker

1. Initialize a new virtual environment

```bash
python -m venv venv
```

2. Activate the virtual environment

```bash
source venv/bin/activate
```

3. Install the requirements

```bash
pip3 install -r requirements.txt
# OR
pip install -r requirements.txt

```

4. Now run the following command to setup a local dev server

```bash
python embed.py
```

## Running locally with Docker

1. Install docker https://docs.docker.com/desktop/

2. Install Python

3. CD into the root directory and run to build the docker image

```bash
docker build -t python-lsb .
```

4. Now run the docker image by running the following command

```bash
docker run -d -p 5000:5000 python-lsb
```
