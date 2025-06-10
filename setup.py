"""Setup configuration for BeMind AI SDK."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bemind-ai",
    version="0.1.0",
    author="BeMind Technology Co., Ltd.",
    author_email="dev@bemindlab.com",
    description="A Python SDK for integrating AI capabilities into BeMind applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bemindlab/bmt-bemind-ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "pydantic>=2.0.0",
        "httpx>=0.24.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.0",
            "pytest-cov>=4.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.3.0",
            "build>=0.10.0",
            "twine>=4.0.0",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/bemindlab/bmt-bemind-ai/issues",
        "Source": "https://github.com/bemindlab/bmt-bemind-ai",
    },
)