import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="RobotFrameworkLANotifications",
    version="1.0.0",
    description="Send notifications to Slack or Mattermost using Robot Framework. Forked from tlolkema/RobotNotifications. Originally created by tlolkema. Modified by Lucas Greyhounds.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasgreyhounds/RobotFrameworkLANotifications",
    author="Lucas Greyhounds",
    author_email="lucasgreyhounds@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["RobotFrameworkLANotifications"],
    include_package_data=True,
    install_requires=["requests"],
)