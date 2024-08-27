from fastapi import FastAPI
import git
import os
import logging

param_repo_dir = "{}/repo/param".format(os.getcwd())
script_repo_dir = "{}/repo/script".format(os.getcwd())
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

app=FastAPI()
GIT_ACCESS_TOKEN = "glpat-tMWUq1262VFyRhBV4wMQ"
param_repo_url = "https://oauth2:{}@gitlab.com/automate-solutions-tasks/heppai.tasks.prototype.git".format(
            GIT_ACCESS_TOKEN
        )
script_repo_url = "https://oauth2:{}@gitlab.com/automate-solutions-tasks/heppai.scripts.prototype.git".format(
            GIT_ACCESS_TOKEN
        )

def clone_repository():
    if not os.path.exists(script_repo_dir):
        logging.info("Cloning script repository...")
        repo = git.Repo.clone_from(script_repo_url, script_repo_dir)
    else:
        logging.info("Repository already exists. Skipping clone.")
        repo = git.Repo(script_repo_dir)
        logging.info("Pulling repository")
        repo.remote(name="origin").pull()
        repo = git.Repo(script_repo_dir)

    if not os.path.exists(param_repo_dir):
        logging.info("Cloning param repository...")
        repo = git.Repo.clone_from(param_repo_url, param_repo_dir)
    else:
        logging.info("Repository already exists. Skipping clone.")
        repo = git.Repo(param_repo_dir)
        logging.info("Pulling repository")
        repo.remote(name="origin").pull()
        repo = git.Repo(param_repo_dir)

@app.get('/task/execution')
def task_execute(task_id:str):
    clone_repository()
    return {'task_id':task_id}

if __name__=='__main__':
    clone_repository()