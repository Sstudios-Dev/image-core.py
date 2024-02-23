import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name= 'image-core.py',
    version= '1.0.0',
    license= 'MIT',
    long_description=long_description,
    author= 'SstudiosDev',
    author_email= 'sstudiosdev@gmail.com',
    url= 'https://github.com/Sstudios-Dev/image-core.py',
    projec_urls={
        "Bug Tracker": "https://github.com/Sstudios-Dev/image-core.py/issues"
    },
    classifiers=[
        "programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requiere=">=3.6"
)
