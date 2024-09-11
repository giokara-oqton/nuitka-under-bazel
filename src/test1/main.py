import yaml

def main():
    config_file_path = 'src/test1/config.yml'
    with open(config_file_path) as f:
        print(yaml.safe_load(f))

if __name__ == '__main__':
    main()
