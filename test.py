import subprocess, json, os, pathlib

print("current_dir: " + os.getcwd())

clone_dir = "F:\Desktop\py\clone_dir"
clone_url = "https://git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/"

print("mkdir実行")
pathlib.Path(clone_dir).mkdir(parents=True, exist_ok=True)
os.chdir(clone_dir)

repositories_result = subprocess.run(['aws', 'codecommit', 'list-repositories'], stdout = subprocess.PIPE, encoding='UTF-8', shell=True)
print(repositories_result.returncode)
print(repositories_result.stdout)
json_load = json.loads(repositories_result.stdout)
repositories = json_load.get("repositories")

for repository in repositories:
    repository_name = repository.get("repositoryName")
    print("repository_name: " + repository_name)
    if os.path.exists(repository_name):
        os.chdir(clone_dir + "/" + repository_name)
        result = subprocess.run(['git', 'pull'], stdout = subprocess.PIPE, encoding='UTF-8', shell=True)
        os.chdir(clone_dir)
    else:
        result = subprocess.run(['git', 'clone', clone_url + repository_name], stdout = subprocess.PIPE, encoding='UTF-8', shell=True)

