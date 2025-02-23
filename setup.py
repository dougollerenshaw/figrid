from setuptools import setup
'''
figrid provides a set of convenience functions to make it easier to 
place axes on a grid using matplotlib
'''
setup(name='figrid',
    version='0.1.6',
    packages=['figrid'],
    include_package_data = True,
    description='Formats multipanel figures',
    url='https://github.com/dougollerenshaw/figrid',
    author='Doug Ollerenshaw',
    author_email="d.ollerenshaw@gmail.com",
    license='MIT',
    install_requires=[
        "matplotlib",
        "numpy",
        "seaborn"
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)