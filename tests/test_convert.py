from unittest import TestCase
from os import path as os_path

from pandas import read_csv
from genes2doe.convert import extract_genes


class Test_Converter(TestCase):

    folder = os_path.join(
        os_path.dirname(
            os_path.realpath(__file__)
        ),
        'data'
    )
    input = os_path.join(
        folder,
        'input',
        'lycopene.xml'
    )
    output = os_path.join(
        folder,
        'output',
        'lycopene.csv'
    )

    def test_extract_genes(self):
        genes = extract_genes(sbml_file=self.input)
        self.assertDictEqual(
            genes.to_dict(),
            read_csv(self.output).to_dict()
        )
