import setuptools


with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()


setuptools.setup(
    name="TapTitans2py",
    version="1.5.1",
    license="MIT",
    url="https://gihtub.com/SilicalNZ/TapTitans2py",
    description="A Pythonic wrapper for the Tap Titans 2 API",
    long_description="A Pythonic wrapper for the Tap Titans 2 API",
    author="SilicalNZ@gmail.com",
    install_requires=requirements,
    python_requires=">=3.10",
    packages=["tap_titans.abcs", "tap_titans.handlers", "tap_titans.models", "tap_titans.providers", "tap_titans.utils"],
)
