import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='matrix-display',
    version='1.0.0',
    author='6871',
    author_email='55576043+6871@users.noreply.github.com',
    description='Print rows on a matrix display, scrolling long rows',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/6871/matrix-display',
    package_dir={'': 'src'},
    packages=['matrix_display', 'matrix_display.displays'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7.5',
)
