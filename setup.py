from setuptools import setup, find_packages

setup(
    name="bojji",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "openai",
    ],
    entry_points={
        'console_scripts': [
            'bojji=src.generate_documentation:main',
        ],
    },
)
