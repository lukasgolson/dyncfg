from setuptools import setup, find_packages

setup(
    name="dyncfg",
    version="0.1.0",
    author="Lukas G. Olson",
    author_email="olson@student.ubc.ca",
    description="A dynamic, easy-to-use .ini configuration system built for humans.",
    long_description=open("readme.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lukasgolson/dyncfg",
    packages=find_packages(),  # Automatically discover all packages and subpackages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
