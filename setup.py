from setuptools import setup, find_packages

setup(
    name="pdf_to_audio",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "PyPDF2==3.0.1",
        "pyttsx3==2.90"
    ]
)
