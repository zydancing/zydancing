from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="jianmu-core",
    version="1.0.0",
    description="建木离散拓扑自洽校准引擎，全域建木锚点校准底层库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Zhang You",
    author_email="youzhang2026@outlook.com",
    url="https://github.com/yourname/jianmu-core",
    project_urls={
        "Bug Tracker": "https://github.com/yourname/jianmu-core/issues",
        "Source Code": "https://github.com/yourname/jianmu-core",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
