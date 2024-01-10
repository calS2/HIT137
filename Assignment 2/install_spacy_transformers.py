import subprocess

def install_packages():
    packages = ['spacy', 'transformers']

    for package in packages:
        try:
            subprocess.check_call(['pip', 'install', package])
            print(f'Successfully installed {package}')
        except subprocess.CalledProcessError as e:
            print(f'Failed to install {package}. Error: {e}')

install_packages()