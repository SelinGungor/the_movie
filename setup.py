from setuptools import setup, find_packages

VERSION = {}

with open("src/the_movie/__init__.py") as fp:
    exec(fp.read(), VERSION)

setup(
    name="the_movie",
    author="Selin Gungor",
    description="""Example spark project which works with a sample movie data.""",
    version=VERSION.get("__version__", None),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
	    "setuptools",
	    "click",
	    "numpy",
	    "pyspark",
	    "pandas",
	    "scikit-learn",
	    "pyhocon",
	    "google-cloud-storage"
    ],
    entry_points={"console_scripts": ["the_movie=the_movie.__main__:main"]},

)
