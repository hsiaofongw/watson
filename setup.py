import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="watson", 
    version="0.0.1",
    author="Wayne",
    author_email="i@beyondstars.xyz",
    description="tool helping website administration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hsiaofongw/watson",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)