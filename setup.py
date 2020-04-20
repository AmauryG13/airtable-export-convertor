import os, setuptools

with open('README.md', mode='r') as f:
    long_description = f.read()

def get_metadata():
    """Get version and version_info from markdown/__meta__.py file."""
    module_path = os.path.join(os.path.dirname('__file__'), 'src/airtor', '__meta__.py')

    import importlib.util
    spec = importlib.util.spec_from_file_location('__meta__', module_path)
    meta = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(meta)
    return meta.__version__, meta.__author__, meta.__prog__

__version__, __author__, __prog__ = get_metadata()

setuptools.setup(
    name=__prog__,
    version=__version__,
    url='https://github.com/amauryg13/airtable-export-convertor.git',
    author=__author__,
    author_email='amauryguillermin@gmail.com',
    description='Script pour retirer les sauts de lignes dans un fichier CSV',
    long_description=long_description,
    long_description_content_type='text/markdown',
    scripts=['bin/airtable-convertor'],
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
