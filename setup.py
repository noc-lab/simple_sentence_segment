from setuptools import setup

files = ["model/*"]

package_list = ['scikit-learn', 'six']

setup(
    name='simple_sentence_segment',
    version='0.1.1',
    author="Henghui Zhu",
    url='None',
    author_email="henghuiz@bu.edu",
    packages=['simple_sentence_segment', ],
    package_data={'simple_sentence_segment': files},
    license='None',
    description="A simple sentence segmentation tool based on decision tree.",
    install_requires=package_list,
)
