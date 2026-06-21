import configparser
import os

def load_config(filename="config.ini"):
    config = configparser.ConfigParser()
    if os.path.exists(filename):
        config.read(filename)
    else:
        config["Settings"] = {
            "health_key": "f2",
            "stamina_key": "f3",
            "ore_key": "f4",
            "lockpick_key": "f5",
            "dawn_key": "f6",
            "speed_key": "f7",
            "damage_key": "f8",
            "exit_key": "f9"
        }
        with open(filename, "w") as f:
            config.write(f)
    return config["Settings"]
