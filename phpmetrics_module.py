import subprocess
import os

def generate_report(folder, output_folder):
    """
    Generate a report using PHPMetrics on the specified folder and save it in the output folder.
    :param folder: The name of the folder/repo to generate the report on.
    :param output_folder: The name of the folder to save the report in.
    """
    # Check if the folder and output_folder exists
    if not os.path.exists(folder):
        raise ValueError(f"The specified folder: {folder} does not exist.")
    if not os.path.exists(output_folder):
        raise ValueError(f"The specified output folder: {output_folder} does not exist.")

    # generate the report
    try:
        subprocess.run(["./bin/phpmetrics", folder, "--report-html=" + output_folder], check=True)
        print(f"Successfully generated report for {folder} in {output_folder}")
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Failed to generate report for {folder}. Error: {e.stderr}")

