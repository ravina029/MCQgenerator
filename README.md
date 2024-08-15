MCQ_Generator

This module contains the code for developing MCQ generator application for the topics specified by the users.

Organization of the code:
1. Created the virtual environment.
2. Install all the required liberaies in requirements.txt file.
3. Add the environment variables in .gitignore file.
4. The experiment folder contains the rough code skech of the application.
5. mcqgenerator folder in the src directory contains all the required code of the application. This is also generated as a package.
6. utils file contains the frequently used function in the Mcqgenerator file.
7. response.json file contains the layout for the generated MCQ file.
8. setup.py contains the code for defining the version for this package.
9. app.py contains the code for the user interface for generating the MCQs for a pecific topic.

steps:
1. clone the repository in your local.
2. create virtual environment ```conda create -p venv pyhton==3.10```.
3. create your openai_api key and store in the .env file.
4. make sure to include .env in the .gitingonre file.
4. run ```pip install -r requirements.txt```
5. run app.py in the terminal ```streamlit run app.py```
6. follow all the instructions shown on the application interface to create the MCQs.