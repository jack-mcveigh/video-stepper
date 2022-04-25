from setuptools import setup, find_packages


setup(
    name='video-stepper',
    version='0.1.0',
    description=('CLI tool for displaying frame by '
                 'frame loops of your favorite videos'),
    author='Jack McVeigh',
    author_email='jmcveigh55@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['video-stepper=video_stepper.main:main'],
    }
)
