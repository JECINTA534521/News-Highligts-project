# News Highlights Project

## Description
An application that allows users to get news articles form multiple news sources online.

#### Link to deployed site


## Table of content
1. [Description](#description)
2. [Setup and installations](#setup-and-installations)
3. [Deployment](#deployment)
4. [Contributing](#contributing)
5. [Bugs](#bugs)
6. [Licensing](#license)


## Setup and installations

#### Prerequisites
1. Python 3.6
2. Pip
3. virtualenv


## Technologies Used
* Python 3.6.5
* Flask Framework
* HTML/CSS
* JavaScript

#### Clone the Repo and checkout into the project folder.
```bash
git clone https://github.com/JECINTA534521/News-Highligts-project && cd News-highlights
```

#### Setting up environment variables
Create a file to start the application. `touch start.sh` 
Inside the start file  input the environment variables and start command below.
```
export NEWS_API_KEY=<Get an API KEY from newsapi.com >


python3.6 manage.py server

```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv env
```

```bash
source env/bin/activate
```

#### Install dependencies
While in the activated virtual environment, install dependencies needed to run the application.
```bash
(env)$ pip install -r requirements.txt
```

#### Run the app
While in the activated virtual environment export environment variables and run the app with the commands below.

```bash
(env)$ export NEWS_API_KEY=<Your api key>
(env)$ export SECRET_KEY=<Your secret key>
(env)$ ./start.sh
```
## Deployment
This is the live link to the project:  https://news-highlights-project.herokuapp.com/
## Contributing
Feel free to contribute to this repository to make pull requests.

## Bugs
No known bugs if a bug is found feel free to contact me at: jecintawanjirug@gmail.com

## [LICENSE](LICENSE)

Copyright (c) [2019] [JECINTA WANJIRU]

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


