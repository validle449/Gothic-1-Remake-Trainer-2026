from utils.logger import log_info

class ConsoleRenderer:
    def __init__(self):
        self.menu_visible = False
    
    def toggle_menu(self):
        self.menu_visible = not self.menu_visible
        if self.menu_visible:
            self.show_menu()
        else:
            log_info("Menu hidden")
    
    def show_menu(self):
        print("""
╔══════════════════════════════════════╗
║   ⚔️ GOTHIC 1 REMAKE TRAINER v1.0   ║
║   🔥 F2 - Infinite Health            ║
║   🔥 F3 - Infinite Stamina           ║
║   🔥 F4 - Add Ore (+100)             ║
║   🔥 F5 - Indestructible Lockpicks   ║
║   🔥 F6 - Set Time to Dawn           ║
║   🔥 F7 - Super Speed                ║
║   🔥 F8 - One-Hit Kill               ║
║   🔥 F9 - Exit                       ║
╚══════════════════════════════════════╝
        """)
