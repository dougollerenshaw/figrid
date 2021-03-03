from setuptools import setup
'''
figrid provides a set of convenience functions to make it easier to 
place axes on a grid using matplotlib
'''
setup(name='figrid',
    version='0.1.0',
    description='Formats multipanel figures',
    url='https://github.com/dougollerenshaw/figrid',
    author='Doug Ollerenshaw',
    author_email="dougo@alleninstitute.org",
    license='MIT',
    install_requires=[
        "matplotlib",
        "numpy",
        "seaborn"
    ],
)