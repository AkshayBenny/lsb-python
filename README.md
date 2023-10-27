## Steganography using Least Bit Algorithm

The Steganography Application is a Python-based project designed to explore the art of hiding information within images. Steganography is the practice of concealing secret data within seemingly innocuous files, making it a valuable technique for secure communication and data protection. In this application, users can encode text messages into images and later decode these messages back, ensuring confidentiality and privacy in digital communication.

The following project includes the following features:

1. Users can input text messages, and the application encodes this text within a chosen image using steganographic techniques. The encoded image appears unchanged to the naked eye but contains hidden information.

2. The application provides a mechanism to extract and decode the hidden messages from previously encoded images. This ensures the recipients can retrieve and read the concealed information.

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

### Requirements

1. Git

2. Python version 3 or higher

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

-   On MacOs and Linux

```bash
source venv/bin/activate
```

-   On Windows

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the app

```bash
python app.py
```
