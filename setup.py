from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="crImageProcessing",
    version="0.0.1",
    author="tysson_cr",
    author_email="tyssoncr@gmail.com",
    description="Image Processing Package using scikit-image",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tyssondocarmo/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)