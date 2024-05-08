from setuptools import setup, find_packages

setup(
    name='vis_analysis_torch',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "os",
        "opencv-python",
        "torch"
    ],
    author='Curtis Chen',
    author_email='chenyang001001@gmail.com',
    description='a package for visualization analysis of pytorch models',
    license='MIT',
    keywords='visualization analysis pytorch',
    url=''
)