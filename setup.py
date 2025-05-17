from setuptools import setup, find_packages

setup(
    name="e-commerce-bot",
    version="0.0.1",
    author="Vishal Poshtiwala",
    author_email="vnposhti@gmail.com",
    description="An e-commerce bot for a company",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "langchain",
        "langchain-astradb",
    ],
)