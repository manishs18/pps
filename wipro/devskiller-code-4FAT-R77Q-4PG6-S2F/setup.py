from setuptools import find_packages, setup

packages = [
    "pytest>=5",
    "pytest-timeout",
]

setup(
    name="currency-exchange-library",
    version="1.1.0",
    author="Devskiller",
    author_email="support@devskiller.com",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
    install_requires=packages + ["wheel>=0.38.4", "setuptools>=51"],
    setup_requires=["pytest-runner"],
    tests_require=packages,
)
