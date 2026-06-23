from markdown_to_pdf.main import main

if __name__ == "__main__":
    config_path = "config.json"
    if not os.path.exists(config_path):
        print("Error: config.json not found.")
        exit(1)
    with open(config_path, 'r') as f:
        config = json.load(f)
    main(config)