#!/usr/bin/python

#File Name: SCA_Audit.py
#Author: Touhid Shaikh
#Description: SBOM, Audit

import csv
import argparse
import os
from git import Repo
import urllib.parse
import subprocess
import phpmetrics_module
import local_php_security_checker_module

# Create the parser
parser = argparse.ArgumentParser(description='Clone private repositories')

# Add the arguments
parser.add_argument('csv_file', help='The CSV file containing the repository information')
parser.add_argument('local_dir', help='The local directory to clone the repositories into')
parser.add_argument('-u', '--username', help='GitLab username')
parser.add_argument('-p', '--password', help='GitLab password')

# Parse the arguments
args = parser.parse_args()

# Open the CSV file
with open(args.csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Create a new CSV file to store information about the repositories
    with open("composer_status.csv", "w", newline="") as composer_status:
        composer_status_writer = csv.writer(composer_status)
        composer_status_writer.writerow(["Repo Name", "Composer Found", "Folder Name"])

        for row in reader:
            # Extract the repository name and URL from the CSV file
            repo_name = row['Name']
            repo_url = row['URL']
            repo_url_added = f"https://"+args.username+":"+urllib.parse.quote(args.password)+"@"+repo_url
            # Create the local directory using the repository name
            repo_folder = os.path.join(args.local_dir, repo_name)
            if not os.path.exists(repo_folder):
                os.makedirs(repo_folder)

            # Clone the repository using the git python module and
            try:
                print("Clonning: "+repo_name+" From: "+repo_url)
                repo = Repo.clone_from(repo_url_added, repo_folder,env={"GIT_HTTP_USERNAME": args.username, "GIT_HTTP_PASSWORD": args.password})
            except:
                os.system("rm -rf "+repo_folder)
            
            # Create the local directory using the repository name for result output
            result_folder = "./results/"+str(repo_name)
            if not os.path.exists(result_folder):
                os.makedirs(result_folder)
            
            # Check if the composer.json file exists in the repository folder
            if os.path.isfile(os.path.join(repo_folder, 'composer.json')):
                print("Scanning Reportitories using PHPMatrics for "+ repo_folder)
                phpmetrics_module.generate_report(repo_folder, result_folder)

                print("Running PHP Local Security Check on "+ repo_folder)
                local_php_security_checker_module.generate_report(repo_folder, result_folder)
                composer_status_writer.writerow([repo_name, "True", repo_folder])
                
            else:
                print(f"composer.json file not found in {repo_folder}. Skipping PHPMetrics and local-php-security-checker report generation.")
                composer_status_writer.writerow([repo_name, "False", repo_folder])
