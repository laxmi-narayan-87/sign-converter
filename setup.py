import setuptools

setuptools.setup(
    name='Text to sign converter SPH-25',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)