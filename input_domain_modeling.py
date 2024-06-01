import argparse

class Characteristic:
    def __init__(self, name, values):
        self.name = name
        self.values = values

class AbstractBlock:
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics

def acoc_mode(blocks):
    from itertools import product
    results = []
    for block in blocks:
        combinations = product(*[c.values for c in block.characteristics])
        results.extend(combinations)
    return results

def mbcc_mode(blocks):
    return [[c.values[0] for c in block.characteristics] for block in blocks]

def ecc_mode(blocks):
    results = []
    for block in blocks:
        for c in block.characteristics:
            for value in c.values:
                results.append([value])
    return results

def bcc_mode(blocks):
    return [[c.values[0] for c in block.characteristics] for block in blocks]

def parse_arguments():
    parser = argparse.ArgumentParser(description='Input Domain Modeling')
    parser.add_argument('--characteristics', nargs='+', required=True, help='Characteristics in the format name:value1,value2,...')
    parser.add_argument('--abstract_blocks', nargs='+', required=True, help='Abstract blocks in the format name:char1,char2,...')
    parser.add_argument('--mode', choices=['ACoc', 'MBCC', 'ECC', 'BCC'], required=True, help='Working mode')
    return parser.parse_args()

def main():
    args = parse_arguments()
    characteristics = {}
    
    for char in args.characteristics:
        name, values = char.split(':')
        characteristics[name] = Characteristic(name, values.split(','))

    abstract_blocks = []
    for block in args.abstract_blocks:
        name, chars = block.split(':')
        block_chars = [characteristics[c] for c in chars.split(',')]
        abstract_blocks.append(AbstractBlock(name, block_chars))

    if args.mode == 'ACoc':
        results = acoc_mode(abstract_blocks)
    elif args.mode == 'MBCC':
        results = mbcc_mode(abstract_blocks)
    elif args.mode == 'ECC':
        results = ecc_mode(abstract_blocks)
    elif args.mode == 'BCC':
        results = bcc_mode(abstract_blocks)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
