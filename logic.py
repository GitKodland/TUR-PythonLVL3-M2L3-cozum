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
   Question("Kimse onları görmediğinde kediler ne yapar?", 1, "Uyumak", "Mizah yapmak"),
   Question("Kediler sevgilerini nasıl ifade ederler?", 0, "Yüksek sesli mırlama", "Harika pozlar", "Havlama"),
   Question("Kediler hangi kitapları okumaktan hoşlanır?", 3, "Kişisel gelişim kitapları", "Zaman yönetimi: günde 18 saat nasıl uyunur", "Sahibinizden 5 dakika önce uyumanın 101 yolu”, ”İnsan yönetimi için bir rehber")
]
