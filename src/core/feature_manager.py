from utils.logger import log_success, log_info

class FeatureManager:
    def __init__(self):
        self.features = {
            "health": False,
            "stamina": False,
            "ore": False,
            "lockpick": False,
            "dawn": False,
            "speed": False,
            "damage": False,
        }
        self.ore_count = 0
    
    def toggle(self, name):
        if name in self.features:
            self.features[name] = not self.features[name]
            status = "ON" if self.features[name] else "OFF"
            log_success(f"{name.upper()} {status}")
    
    def trigger(self, name):
        if name == "ore":
            self.ore_count += 100
            log_info(f"Added 100 Ore (total: {self.ore_count})")
        elif name == "dawn":
            log_info("Time set to 06:00")
        else:
            log_info(f"Triggered: {name}")
