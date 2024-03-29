import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read().replace(":heavy_check_mark:", "✔️").replace(":x:", "❌")

with open("requirements.txt", "r") as r:
    dependencies = [line.strip() for line in r.readlines() if line.strip() and not line.strip().startswith("#")]

setuptools.setup(
    name="AoE2ScenarioParser",
    version="VERSION_HERE",
    author="Kerwin Sneijders",
    author_email="ksneijders@hotmail.com",
    description="This is a project for editing parts of an 'aoe2scenario' file from Age of Empires 2 Definitive Edition",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KSneijders/AoE2ScenarioParser",
    packages=setuptools.find_namespace_packages(),

    # According to the docs glob patterns are allowed.
    # But when using: "versions/**/*.json", it does not work.
    package_data={
        'AoE2ScenarioParser': [
            'datasets/sources/*.json',
            'versions/*/*/*.json'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=dependencies
)
