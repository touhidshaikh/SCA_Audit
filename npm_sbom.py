import json

def generate_sbom(file_path):
    # Load the package.json file
    with open(file_path) as json_file:
        data = json.load(json_file)

    # Initialize an empty list to store the SBOM
    sbom = []

    # Iterate through the dependencies and devDependencies
    for dep_type in ['dependencies', 'devDependencies']:
        if dep_type in data:
            for name, version in data[dep_type].items():
                # Retrieve the license information for the dependency
                try:
                    license_info = subprocess.run(["npm", "view", name, "license"], capture_output=True, text=True)
                    license = license_info.stdout.strip()
                except:
                    license = "Unknown"

                # check for latest version available
                try:
                    latest_version = subprocess.run(["npm", "view", name, "version"], capture_output=True, text=True)
                    latest_version = latest_version.stdout.strip()
                except:
                    latest_version = "Unknown"
                # Append the dependency information to the SBOM
                sbom.append({'name': name, 'version': version, 'latest_version':latest_version, 'dependency_type': dep_type, 'license': license})

    # Return the generated SBOM
    return sbom
