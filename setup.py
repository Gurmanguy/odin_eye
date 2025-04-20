from setuptools import setup, find_packages

setup(
    name="odin_eye",
    version="0.1.0",
    description="Odin_Eye: Collect live process & network data into Google Sheets",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Guy Gurman",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "gspread",
        "google-auth"
    ],
    entry_points={
        "console_scripts": [
            "odin_eye = odin_eye.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
