from setuptools import setup, find_packages

setup(
    name="plot_viz",
    author="Erik Serrano",
    description="Gene reads CLI Tool",
    version="0.1",
    python_requires=">3.10",
    packages=find_packages(),
    install_requires=["matplotlib"],
    scripts=["plot_gtex.py"],
)