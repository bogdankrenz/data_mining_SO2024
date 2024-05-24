from setuptools import find_packages, setup

setup(
    name="my_data_science_project",
    version="0.1.0",
    description="A data science project for analysis and modeling",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-username/your-repository-name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "jupyter",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
