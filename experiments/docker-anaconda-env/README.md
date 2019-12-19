# Data Visualization with Python and JavaScript

## Jupyter Notebook Using Custom Docker Image for Anaconda running Python 3.7
This environment is being used to illustrate concepts that will be used in the full data visualization project. To provide an interactive environment that requires litte setup, I have created a Jupyter Notebook that can run inside of a docker container, using docker compose to provide related resources such as databases and to handle setup and teardown. 

## Usage
I have provided a few convenience scripts for using the docker compose environment. 
- Make sure that Docker is installed on your machine.
    - [Install Docker](https://www.docker.com/products/container-runtime)
- Clone the git repository
    - `git clone https://github.com/Jonathan-Llovet/dataviz-with-py-and-js.git`
- Start: `dataviz-with-py-and-js/experiments/anaconda-env/anaconda-up.sh`
    - This runs `docker-compose up --build` and generates log files.
        - Note: This may take longer the first time, since docker will pull several images from DockerHub. Subsequent executions will be much faster.
    - A token is needed to log into the Jupyter Notebook for the first time in a session. The startup script will direct you to the log that contains a link with the token.
        - The link should look like this: `http://127.0.0.1:3000/?token=8cd21f8b028c3d517e3f3c11697479bb6faaccadb9050cae`
- Stop: `dataviz-with-py-and-js/experiments/anaconda-env/anaconda-down.sh`
    - This runs `docker-compose down`, which tears down the private network that was created during startup and stops the containers


