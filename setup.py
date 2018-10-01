from setuptools import setup

files = ["model/*"]

package_list = ['scikit-learn']

setup(
    name='sentence_segment',
    version='0.1.0',
    author="Henghui Zhu",
    url='None',
    author_email="henghuiz@bu.edu",
    packages=['simple_sentence_segment', ],
    package_data={'simple_sentence_segment': files},
    license='None',
    description="A sentence segmentation tools based on ML.",
    install_requires=package_list,
)
