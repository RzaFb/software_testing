import unittest
import subprocess
import sys
from input_domain_modeling import Characteristic, AbstractBlock, acoc_mode, mbcc_mode, ecc_mode, bcc_mode, parse_arguments, main

class TestInputDomainModeling(unittest.TestCase):

    def setUp(self):
        self.char_size = Characteristic('size', ['S', 'M', 'L'])
        self.char_color = Characteristic('color', ['Red', 'Green', 'Blue'])
        self.block_shirt = AbstractBlock('shirt', [self.char_size, self.char_color])
        self.block_car = AbstractBlock('car', [Characteristic('speed', ['low', 'medium', 'high']),
                                               Characteristic('gear', ['1', '2', '3'])])
        self.block_experiment = AbstractBlock('experiment', [Characteristic('temperature', ['hot', 'cold']),
                                                             Characteristic('duration', ['short', 'long'])])

    def test_acoc_mode(self):
        result = acoc_mode([self.block_shirt])
        expected = [('S', 'Red'), ('S', 'Green'), ('S', 'Blue'),
                    ('M', 'Red'), ('M', 'Green'), ('M', 'Blue'),
                    ('L', 'Red'), ('L', 'Green'), ('L', 'Blue')]
        self.assertEqual(result, expected)

    def test_mbcc_mode(self):
        result = mbcc_mode([self.block_shirt])
        expected = [['S', 'Red']]
        self.assertEqual(result, expected)

    def test_ecc_mode(self):
        result = ecc_mode([self.block_shirt])
        expected = [['S'], ['M'], ['L'], ['Red'], ['Green'], ['Blue']]
        self.assertEqual(result, expected)

    def test_bcc_mode(self):
        result = bcc_mode([self.block_shirt])
        expected = [['S', 'Red']]
        self.assertEqual(result, expected)

    def test_acoc_mode_car(self):
        result = acoc_mode([self.block_car])
        expected = [('low', '1'), ('low', '2'), ('low', '3'),
                    ('medium', '1'), ('medium', '2'), ('medium', '3'),
                    ('high', '1'), ('high', '2'), ('high', '3')]
        self.assertEqual(result, expected)

    def test_mbcc_mode_car(self):
        result = mbcc_mode([self.block_car])
        expected = [['low', '1']]
        self.assertEqual(result, expected)

    def test_ecc_mode_car(self):
        result = ecc_mode([self.block_car])
        expected = [['low'], ['medium'], ['high'], ['1'], ['2'], ['3']]
        self.assertEqual(result, expected)

    def test_bcc_mode_car(self):
        result = bcc_mode([self.block_car])
        expected = [['low', '1']]
        self.assertEqual(result, expected)

    def test_acoc_mode_experiment(self):
        result = acoc_mode([self.block_experiment])
        expected = [('hot', 'short'), ('hot', 'long'), ('cold', 'short'), ('cold', 'long')]
        self.assertEqual(result, expected)

    def test_mbcc_mode_experiment(self):
        result = mbcc_mode([self.block_experiment])
        expected = [['hot', 'short']]
        self.assertEqual(result, expected)

    def test_ecc_mode_experiment(self):
        result = ecc_mode([self.block_experiment])
        expected = [['hot'], ['cold'], ['short'], ['long']]
        self.assertEqual(result, expected)

    def test_bcc_mode_experiment(self):
        result = bcc_mode([self.block_experiment])
        expected = [['hot', 'short']]
        self.assertEqual(result, expected)

    def test_parse_arguments(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue',
                    '--abstract_blocks', 'shirt:size,color', '--mode', 'ACoc']
        args = parse_arguments()
        self.assertEqual(args.characteristics, ['size:S,M,L', 'color:Red,Green,Blue'])
        self.assertEqual(args.abstract_blocks, ['shirt:size,color'])
        self.assertEqual(args.mode, 'ACoc')

    def test_main_acoc(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue',
                    '--abstract_blocks', 'shirt:size,color', '--mode', 'ACoc']
        result = subprocess.run([sys.executable, 'input_domain_modeling.py', 
                                 '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue', 
                                 '--abstract_blocks', 'shirt:size,color', '--mode', 'ACoc'], 
                                capture_output=True, text=True)
        expected = "('S', 'Red')\n('S', 'Green')\n('S', 'Blue')\n('M', 'Red')\n('M', 'Green')\n('M', 'Blue')\n('L', 'Red')\n('L', 'Green')\n('L', 'Blue')\n"
        self.assertEqual(result.stdout, expected)

    def test_main_mbcc(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue',
                    '--abstract_blocks', 'shirt:size,color', '--mode', 'MBCC']
        result = subprocess.run([sys.executable, 'input_domain_modeling.py', 
                                 '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue', 
                                 '--abstract_blocks', 'shirt:size,color', '--mode', 'MBCC'], 
                                capture_output=True, text=True)
        expected = "['S', 'Red']\n"
        self.assertEqual(result.stdout, expected)

    def test_main_ecc(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue',
                    '--abstract_blocks', 'shirt:size,color', '--mode', 'ECC']
        result = subprocess.run([sys.executable, 'input_domain_modeling.py', 
                                 '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue', 
                                 '--abstract_blocks', 'shirt:size,color', '--mode', 'ECC'], 
                                capture_output=True, text=True)
        expected = "['S']\n['M']\n['L']\n['Red']\n['Green']\n['Blue']\n"
        self.assertEqual(result.stdout, expected)

    def test_main_bcc(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue',
                    '--abstract_blocks', 'shirt:size,color', '--mode', 'BCC']
        result = subprocess.run([sys.executable, 'input_domain_modeling.py', 
                                 '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue', 
                                 '--abstract_blocks', 'shirt:size,color', '--mode', 'BCC'], 
                                capture_output=True, text=True)
        expected = "['S', 'Red']\n"
        self.assertEqual(result.stdout, expected)

    def test_invalid_mode(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue',
                    '--abstract_blocks', 'shirt:size,color', '--mode', 'INVALID']
        with self.assertRaises(SystemExit):
            parse_arguments()

    def test_invalid_characteristics_format(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'invalidformat',
                    '--abstract_blocks', 'shirt:size,color', '--mode', 'ACoc']
        with self.assertRaises(ValueError):
            main()

    def test_invalid_abstract_blocks_format(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue',
                    '--abstract_blocks', 'invalidformat', '--mode', 'ACoc']
        with self.assertRaises(ValueError):
            main()

    def test_main_function_integration(self):
        sys.argv = ['input_domain_modeling.py',
                    '--characteristics', 'size:S,M,L', 'color:Red,Green,Blue',
                    '--abstract_blocks', 'shirt:size,color', '--mode', 'ACoc']
        main()

if __name__ == '__main__':
    unittest.main()
