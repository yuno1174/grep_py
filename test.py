# coding= utf-8
import subprocess, json, os, pathlib, glob, codecs, chardet

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

search_word = "cpu"

for repository in repositories:
    repository_name = repository.get("repositoryName")
    print("repository_name: " + repository_name)
    if os.path.exists(repository_name):
        os.chdir(clone_dir + "/" + repository_name)
        result = subprocess.run(['git', 'pull'], stdout = subprocess.PIPE, encoding='UTF-8', shell=True)
        os.chdir(clone_dir)
    else:
        result = subprocess.run(['git', 'clone', clone_url + repository_name], stdout = subprocess.PIPE, encoding='UTF-8', shell=True)

    object_list = glob.glob("**", recursive=True)

    for object in object_list:
        if os.path.isfile(object):
            with codecs.open(object, 'rb', 'utf-8', 'ignore') as f:
                lines = f.readlines()
                for line in lines:
                    if search_word in line:
                        print(line)
                        
                    
