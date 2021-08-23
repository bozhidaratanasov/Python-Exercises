class Player:
    skills = {}
    guild = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skills {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_mana = ""
        for key, value in self.skills.items():
            skills_mana += "===" + key + " - " + str(value) + "\n"
        return f"Name: {self.name} \n" \
               f"Guild: {self.guild} \n" \
               f"HP: {self.hp} \n" \
               f"MP: {self.mp} \n" \
               f"{skills_mana}"
