from setuptools import setup, find_packages

setup(
    name="dyncfg",  # Replace with your package's name
    version="0.1.0",   # Start with an initial version number
    author="Lukas G. Olson",
    author_email="olson@student.ubc.ca",
    description="A short description of your package.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",  # Replace with your repository URL
    packages=find_packages(),  # Automatically discover all packages and subpackages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust if using a different licence
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the Python versions your package supports
)
