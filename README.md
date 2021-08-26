# news-recommender-system

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">news-recommender-system</h3>

  <p align="center">
    News recommender system web app with news from G1 and Google News.
    <br />
    <br />
    <a href="https://news-system-recommender.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>

  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project 
<br />
<p align="center">
  <img src="https://i.imgur.com/ZQFaHk9.gif" width="700" height="400" />
</p><br />  

News content-based recommender system web app made with Machine Learning and Natural Language Processing techniques.</br>
The news are obtained from a MySQL Database fed with a web-scraping project, avaliable in this [repository](https://github.com/andre-albuquerque/web-scraping).

### Built With


* [Python](https://www.python.org/)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [Streamlit](https://streamlit.io/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Beyond the MySQL Database with the web-scraped news, </br>
Install these following modules utilizing pip install

* pip
  ```sh
  pandas==1.1.3
  gensim==4.0.1 
  scikit-learn==0.24.2
  fuzzywuzzy==0.18.0
  mysql-connector-python==8.0.25
  streamlit==0.85.1
  nltk==3.6.2
  python-dotenv==0.19.0
  bokeh==2.3.3
  ```

The following files are requisites from the Heroku plataform for deploy the web app
```sh
  requirements.txt
  runtime.txt
  setup.sh
  Procfile
  nltk.txt
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/andre-albuquerque/news-recommender-system.git
   ```
3. In the project's directory, create a .env and a secrets.toml file with the database connection information

   ```sh
   DB_HOST = 'mydbhost'
   DB_USERNAME = 'mydbusername'
   DB_PASSWORD = 'mydbpassword'
   DB_DATABASE =  'mydbname'
   DB_PORT = 'mydbport'
   ```
    The file structure must be
    
    ```bash
    recommender-system
    |---.dotenv
    |___.streamlit
    |   |---secrets.toml
    |
    ```




<!-- USAGE EXAMPLES -->
## Usage

To initialize the web app, open your terminal in the directory's project and run the following command

   ```sh
   streamlit run news_streamlit.py
   ```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/andre-albuquerque/news-recommender-system/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

André de Albuquerque - [Linkedin](https://www.linkedin.com/in/andr%C3%A9-albuquerque-/) - andrealbuquerqueleo@gmail.com

Project Link: [https://github.com/andre-albuquerque/news-recommender-system](https://github.com/andre-albuquerque/news-recommender-system)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://i.imgur.com/ZQFaHk9.gif 
