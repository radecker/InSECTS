import yaml

with open("/home/jhu-ep/InSECTS-Vehicle-Testbed/config.yaml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)


class ConfigLoader():
    def __init__(self) -> None:
        pass

    def __parse_params(self):
        pass

    def read_file(self):
        pass

    def get_config(self):
        pass