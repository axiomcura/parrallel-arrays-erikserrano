from setuptools import find_packages, setup

setup(
    name="plot_viz",
    author="Erik Serrano",
    description="Gene reads CLI Tool",
    version="0.1",
    python_requires=">3.10",
    packages=find_packages(),
    scripts=["plot_gtex.py"],
)
