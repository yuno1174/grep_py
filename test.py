import subprocess
import json

result = subprocess.run(['aws', 'codecommit', 'list-repositories'], stdout = subprocess.PIPE, encoding='UTF-8', shell=True)
print(result.returncode)
print(result.stdout)

json_load = json.loads(result.stdout)
repositories = json_load.get("repositories")
for repository in repositories:
    print("repository_name: " + repository.get("repositoryName"))