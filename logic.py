from discord import ui, ButtonStyle


class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        buttons = []
        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'correct_{i}'))
            else:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'wrong_{i}'))
        return buttons


quiz_questions = [
   Question("What do cats do when nobody sees them?", 1, "Sleep", "Write memes"),
   Question("How do cats express their love?", 0, "Loud purring", "Lovaely photos", "Barking"),
   Question("What books do cats like to read?", 3, "Self-help books", "Time management: how to sleep 18 hours a day", "101 ways to go to sleep 5 minutes earlier than your owner", "A guide to human management")
]
