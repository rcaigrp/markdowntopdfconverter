from markdown_to_pdf import converter

if __name__ == '__main__':
    config = converter.read_config()
    converter.convert(config['input'], config['output'])
