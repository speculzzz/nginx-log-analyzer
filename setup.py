from sys import exit, version_info

from setuptools import find_packages, setup

if version_info[:3] < (3, 7, 0):
    print("Requires Python 3.7 or higher to run.")
    exit(1)

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

setup(
    name="nginx-log-analyzer",
    version="0.1.0",
    description="A service for analyzing Nginx logs and generating statistical reports",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/speculzzz/nginx-log-analyzer",
    author="speculzzz",
    author_email="speculzzz@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="OTUS homework 1",
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pydantic>=1.8.0",
    ],
    extras_require={
        "dev": [
            "black>=21.0",
            "flake8>=3.9.0",
            "pytest>=6.0.0",
            "isort>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nginx-log-analyzer=nginx_log_analyzer.main:run_server",
        ],
    },
)
