import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="antiblock-scrapy-selenium",
    version="0.0.1",
    author="Elves M. Rodrigues",
    author_email="elvesmateusrodrigues@gmail.com",
    description="Mecanismos antibloqueios para Scrapy-Selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elvesrodrigues/antiblock-scrapy-selenium",
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
        'antiblock-selenium',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.0',
)
