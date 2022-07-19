"""This script reads the config file and generates a new config.proto file
"""

import ConfigLoader


def header():
    pass

if __name__=="__main__":
    config_fp = "/home/jhu-ep/InSECTS-Vehicle-Testbed/main_service/config.yaml"
    cl = ConfigLoader.ConfigLoader(config_path=config_fp)
    data = cl.read_config()

    for key, value in data.items():
        pass