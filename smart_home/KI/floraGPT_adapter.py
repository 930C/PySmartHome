from smart_home.KI.floraGPT import ermittlePflegehinweis
from smart_home.commands.plant_care_command import PlantCareCommand
from smart_home.interfaces.command_interface import CommandInterface


class PlantCareAdapter:
    def getPlantCareInstructions(self, einPflanzenbild: str) -> PlantCareCommand:
        care_instruction = ermittlePflegehinweis(einPflanzenbild)
        error_code = self.get_error_code(care_instruction)
        self.command = PlantCareCommand(error_code)
        return self.command

    def get_error_code(self, care_instruction: str) -> str:
        # Trennen des Strings anhand des Doppelpunkts '::'
        parts = care_instruction.split('::')

        # Extrahieren des Codes (der erste Teil nach dem Trennzeichen ist der Code)
        error_code = parts[0].split(" ")[1].strip()

        return error_code