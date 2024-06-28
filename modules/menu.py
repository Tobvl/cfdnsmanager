

class Menu():

    def __init__(self, settings=None):
        self.settings = settings
        
    def show_settings(self, settings):
        print("\n\n    Settings:")
        for key, value in settings.items():
            print(f"    {key}: {value}")

    def show_mainmenu(self, options):
        if self.settings:
            self.show_settings(self.settings)
        print("\n")
        for i, option in enumerate(options):
            print(f"    {i+1}. {option}")
        print("    0. Exit")
        
        choice = input(
            """
    Select an option:
    >>>  """)
        
        return choice
    
    @classmethod
    def edit_settings(self, settings):
        print("\n    Edit Settings      [INTRO TO CANCEL]:")
        for key, value in settings.items():
            new_value = input(f"    {key} [{value}]: ")
            if new_value == "":
                new_value = value
                continue
            settings[key] = new_value
        return settings