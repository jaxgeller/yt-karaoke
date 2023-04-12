from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="yt_karaoke",
    author="Jackson Geller",
    version="1.0",
    description="Generate karaoke video from youtube",
    license="MIT",
    packages=find_packages(),
    py_modules=["yt_karaoke"],
    python_requires=">=3.8",
    install_requires=required,
    entry_points={
        "console_scripts": ["yt_karaoke=yt_karaoke.cli:main"],
    },
    include_package_data=True,
)
