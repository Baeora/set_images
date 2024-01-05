
# Set Images

## Greeting
Hello! Thank you for being interested, if you are new to coding - a lot of this will seem a bit overwhelming but remember you can always reach out to me via Discord @Beora.

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

## Overview
This is a simple repo which aims to tackle the automation of updating images in a spreadsheet so that they include the most recent champions/items/runes

## Usage
To use this you will need to obtain a `Google Oauth2` key, afterwards you will need to import [Images](https://docs.google.com/spreadsheets/d/1HT0XfLMEZwwFYI9DorpNt31rWUchTfRnJcN8m_6mGz4/edit?usp=sharing) to a new sheet, and add your `Oauth2 Service Email` as an editor

Then you may use the code provided to run `set_images()` with your url as a parameter and it should update the images in that sheet.

For ease of use you can use `sheet_dct` in `dictionaries.py` to store your sheet urls so they are easier to keep track of

## Installation

### Preparation
Before installing, complete the following tasks:

- (For beginners) Make sure [Python](https://www.python.org/downloads/) and [PIP](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) are added to [PATH](https://realpython.com/add-python-to-path/).

	- During your Python install, you can specify that you'd like to do this by choosing Custom Installation, highly recommend!

	- You'll also need an IDE to code in, I use [VSCode](https://code.visualstudio.com/download).

- Obtain Google [Oauth2](https://console.cloud.google.com/projectselector2/apis/credentials?supportedpurview=project) credentials (JSON format).

	- Might need to google how to do this if you're new to it.

### Install
Once you have finished the above tasks, navigate to the directory you'd like to work in and do the following:

- Clone this repository

	```git clone https://github.com/Baeora/set_images.git```

- Inside said repository, use Pip to install dependencies

	```pip install -r requirements.txt```

- Create a 'JSON' folder in the main `set_images` directory, put your Oauth2 JSON file here.

- Inside `scripts`, navigate to `core.py` and replace the following line:
`service_file  =  os.path.join(os.path.dirname(Path.cwd()), 'JSONs\\<Your Oauth2 filename>.json')`
  
That **should** be everything. If you run into errors or spot anything that I missed, please reach out!

## License
MIT License

Copyright (c) 2023 Beora

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.