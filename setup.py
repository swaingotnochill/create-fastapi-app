from setuptools import setup, find_packages

setup(
    name="create-fastapi-app",
    version="0.1.0",
    packages=find_packages(include=["cfa", "cfa.*"]),
    install_requires=[
        "click",
        "jinja2",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "create-fastapi-app = cfa.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "cfa": ["templates/*", "templates/**/*"],
    },
    package_dir={"cfa": "cfa"}
)
