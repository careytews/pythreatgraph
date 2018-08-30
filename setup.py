import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="threatgraph",
    version="0.1",
    author="Trust Networks",
    author_email="support@trustnetworks.com",
    description="Python Threat Graph API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trustnetworks/pythreatgraph",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests', 'gaffer'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
