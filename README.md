# SCA_Audit | Software Composition Analyse Auditor

This script is used to clone multiple private Git repositories from a CSV file. It takes in three inputs: a CSV file containing the repository names and URLs, a local directory to clone the repositories into, and a GitLab username and password. The script reads the CSV file and for each repository listed, it creates a directory with the repository's name, and clones the repository into that directory. The script uses the GitLab username and password to authenticate when cloning the repositories.


**Technical Description**

This script uses the argparse library to parse command-line arguments, the os library to create directories, and the git library (specifically the Repo class) to clone Git repositories. The script takes in three arguments: a CSV file containing the repository information, a local directory to clone the repositories into, and an optional GitLab username and password. The script reads the CSV file using the csv library, and for each row in the file, it extracts the repository name and URL. It then creates a local directory with the same name as the repository and clones the repository into that directory. The repository URL is modified by adding the username and password to it. The script also uses env variable to pass the credentials while cloning the repository.

The script uses two options `-u` or `--username` and `-p` or `--password` which can be used to provide GitLab username and password.

It will clone the repositories and save them in a folder with the name provided in the CSV file.

Below is example of CSV.
| Name | URL |
| -------- | -------------- |
| Example-Demo| github.com/example/api-repo|

### Run
For script execution, use the following command.
```
python script.py -u touhid -p password repositories.csv /path/to/local/directory
```

### Installation
