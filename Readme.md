# MLFullStack Mini Project
This repo were built for study, research, and implementation of end to end data science project. This project includes work in the fields of software engineering, data science, and AI/ML Engineer that is done fully using python.

## installation
Installation for this projcet only using this command
`pip install -r requirements.txt`

## Run Program
### Backend
Run this command in separate terminal 
`uvicorn src.BE:app --reload`

### Frontend
Run this command in separate terminal 
`streamlit run src/FE/iris_frontend.py`

### MLserver (Optional)
1. run mlfow server using this command `mlflow server --host 127.0.0.1 --port 8080`
2. run training file program `python research/train.py`
3. you can access the result of training like model and hyperparameter by accessing `localhost:8080`

# Next Step
After we have polished the basics of our mini project, we will add things that are worked on by devops such as dockerizing, CI/CD, unit testing and also change the frontend structure to replace streamlit with a frontend framework according to our skills and knowledge.