from setuptools import setup, find_packages

setup(
    name="gravitycore",
    version="16.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="Mechanical solar conversion simulation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Unkown-pixel/GravityCore-v16.1-Mechanical-Solar-Conversion",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Researchers",
        "License :: CC0 1.0 Universal",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
)
