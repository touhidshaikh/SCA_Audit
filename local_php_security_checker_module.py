import subprocess
import os

def generate_report(folder, output_folder):
    """
    Generate a report using local-php-security-checker on the specified folder and save it in the same folder with the name local-php-security-checker-result.txt
    :param folder: The name of the folder/repo to generate the report on.
    """
    # Check if the output_folder  exists
    if not os.path.exists(output_folder):
        raise ValueError(f"The specified folder: {output_folder} does not exist.")
    report_file = os.path.join(output_folder,'local-php-security-checker-result.txt')
    # generate the report
    try:
        #./results/Project-api/local-php-security-checker-result.txt
        os.system("./bin/local-php-security-checker -no-dev --path="+folder+">"+report_file)
        print(f"Successfully generated report for {folder} in {output_folder}")
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Failed to generate report for {folder}. Error: {e.stderr}")
