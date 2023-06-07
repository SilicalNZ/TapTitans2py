import setuptools


requirements = []
with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()


setuptools.setup(
    name="TapTitans2py",
    version="0.0.1",
    license="Anyone may use this, but the origin (this project) must be credited",
    url="https://gihtub.com/SilicalNZ/TapTitans2py",
    description="A Pythonic wrapper for the Tap Titans 2 API",
    long_description="A Pythonic wrapper for the Tap Titans 2 API",
    author="SilicalNZ@gmail.com",
    install_requires=requirements,
    packages=["TapTitans2py.abcs", "TapTitans2py.handlers", "TapTitans2py.models", "TapTitans2py.providers", "TapTitans2py.utils"],
)
