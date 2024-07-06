from setuptools import setup, find_packages

setup(
    name='data-quality-utility-kit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Tu Nombre',
    author_email='tuemail@example.com',
    description='A utility kit for data quality analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tu_usuario/data-quality-utility-kit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

