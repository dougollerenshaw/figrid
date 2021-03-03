from setuptools import setup

setup(name='figrid',
    version='0.0.1',
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