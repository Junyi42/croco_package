from setuptools import setup, find_packages

print('Found packages:', find_packages())
setup(
    description='CROCO as a package',
    name='croco',
    version='0.0',    
    packages=find_packages(),
    install_requires=[
        # 'torch==2.0.1',
        # 'torchvision==0.15.2',
        'matplotlib',
        'notebook',
        'ipykernel', 
        'ipywidgets',
        'widgetsnbextension'
    ],
    extras_require={
        'all': [
        ],
    },
)

