### Project structure

```
Project Root
│
├── static
│   ├── skyrim.bmp
│   └── steg-image.bmp
│
├── .gitignore
├── app.py
├── encode.py
├── decode.py
└── requirements.txt
```

`Note:` The static folder will contain the image to be encoded as well as the output image generated

### Local Setup

1. First clone the repository

```bash
git clone https://github.com/AkshayBenny/lsb-python.git
```

2. Change directory into the project

3. Setup a virtual environment

```bash
python -m venv venv
```

And run the following command to activate the virtual environment

```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the app

```bash
python app.py
```
