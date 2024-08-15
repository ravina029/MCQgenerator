MCQ_Generator

This module contains the code for developing MCQ generator application for the topics specified by the user.

Organization of the code:
1. Created the virtual environment.
2. Install all the required liberaies in requirements.txt file.
3. Add environment variables file .env in .gitignore file.
4. Experiment folder contains the rough code skech for the application.
5. mcqgenerator folder in the src directory contains all the required code of the application. This is also generated as a package.
6. utils file contains the frequently used function in the Mcqgenerator file.
7. response.json file contains layout for ouput MCQ file.
8. setup.py contains the code for defining the metadata for this application package.
9. app.py contains the code for streamlit application layout for generating  MCQs for user entered specific topic.

steps:
1. clone the repository in your local using ```https://github.com/ravina029/MCQgenerator.git```.
2. create virtual environment ```conda create -p venv pyhton==3.10```.
3. create your openai_api key and store in the .env file.
4. make sure to include .env inside .gitingonre file.
4. run ```pip install -r requirements.txt```
5. run app.py in the terminal ```streamlit run app.py```
6. follow all the instructions shown on the application interface to create the MCQs.