from setuptools import setup, find_packages

setup(
    name='pulsar_excel',
    version='0.0.7',
    license='MIT',
    author="Gyeongmin Kim",
    author_email='kgm1306@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=['PulsarExcel'],
    url='https://github.com/Gyeongmin-lucid/pulsar-pip',
    keywords='pulsar',
    install_requires=[
      'pandas',
    ],
)