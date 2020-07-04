import setuptools

with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name             = 'flacToItunes',
    author           = 'O. Kliemann',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    scripts          = ['flacToItunes'],
    python_requires  = '>=3.0',
    install_requires = ['mutagen>=1.44.0, <2']
)
