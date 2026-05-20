from converter import load_config, run

def main():
    config_path = 'config.json'
    input_path, output_path = load_config(config_path)
    run(input_path, output_path)

if __name__ == '__main__':
    main()
