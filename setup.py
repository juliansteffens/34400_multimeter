from setuptools import setup, find_packages

setup(
    name='34400_multimeter',  # Name deines Pakets
    version='0.1.0',            # Versionsnummer
    packages=find_packages(),   # Alle Pakete finden (in diesem Fall multimeter_control)
    install_requires=[          # Abhängigkeiten
        'pyvisa', 
        'visa',             # Die Bibliothek, die du für die Kommunikation mit dem Multimeter verwendest
    ],
    description='Python API for controlling Agilent 34400 series measurement devices',  # Kurze Beschreibung des Pakets
    long_description=open('README.md').read(),  # Längere Beschreibung aus der README-Datei
    long_description_content_type='text/markdown',  # Format der README-Datei
    author='Julian Steffens, Robin Binger',
    author_email='deine.email@example.com',
    url='https://github.com/dein_username/34400_multimeter',  # GitHub-Repository-Link
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python-Version, die unterstützt wird
)
