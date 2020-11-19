import json

class ApplicationConfiguration(object):

    def __init__(self):
        self.settings = {}
        
        try:
            with open("settings.json") as settings:
                self.settings = json.load(settings)
        except:
            pass

        self.version          = {
                                    "major": 1,
                                    "minor": 0
                                }

        self.application_name  = "Python Point Observer (PyPo) : " + str(self.version["major"]) + "." + str(self.version["minor"])
        self.organization_name = "DanAurea"
        self.style             = "styles/default.qss"
        self.debug             = False

    def load(self):
        """
        Configure application to set different behaviors or styles that user can save between 
        reboot of running application. 
        """
        if "version" in self.settings:
            self.version          = self.settings["version"]
        
        if "application_name" in self.settings:
            self.application_name = self.settings["application_name"] + " : " + str(self.version["major"]) + "." + str(self.version["minor"])

        if "organization_name" in self.settings:
            self.organization_name = self.settings["organization_name"]

        if "style" in self.settings:
            with open("styles/" + self.settings["style"] + ".qss") as style:
                self.style = style.read()

        if "debug" in self.settings:
            self.debug = self.settings["debug"]

    def __str__(self):
        """
        Returns a string representing settings defined in json settings with dictionary form.
        """
        return str("{\n" + "\n".join("{!r}: {!r},".format(k, v) for k, v in self.settings.items()) + "\n}")

if __name__ == "__main__":
    configuration = Configuration()
    configuration.load()
    
    print(configuration)