# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-jduke",
    version="1.0",
    author="Jonathan Duke",
    author_email="jonduke90@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jonDuke/lambdata-jduke",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)