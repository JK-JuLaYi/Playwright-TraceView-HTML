
from setuptools import setup, find_packages

setup(
    name="playwright-trace-server",
    version="0.1.0",
    author="Your Name",
    author_email="jayakrishna107@gmail.com",
    description="Interactive local HTML report and server for Playwright trace results.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JK-JuLaYi/Playwright-TraceView-HTML",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "playwright-trace-server=trace_server.generator:main",
        ],
    },
    python_requires=">=3.11",
    license="MIT",
)
