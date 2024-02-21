import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="haagentus",
    version="0.0.1",
    author="Layla-focalors",
    author_email="sjhhjs2004@kakao.com",
    description="An statiscian package for python & very easy version",
    install_requires=['math','numpy','scipy', 'statistics', 'pandas', 'matplotlib', 'stemgraphic'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/layla-focalors/r2python",
    project_urls={
        "Bug Tracker": "https://github.com/layla-focalors/r2python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)