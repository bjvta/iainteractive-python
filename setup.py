from setuptools import find_packages, setup

REQUIREMENTS = []


setup(
    name="django-template",
    author="Brandon",
    author_email="brandon.valle@bjvsoft.net",
    version="1.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
)
