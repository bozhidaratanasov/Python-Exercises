from project.player import Player


class Guild:
    list_of_players = []

    def __init__(self, name):
        self.name = name

    def assign_player(self, player: Player):
        if player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        elif not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.list_of_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for player in self.list_of_players:
            if player.name == player_name:
                self.list_of_players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = ""
        for player in self.list_of_players:
            players_info += player.player_info()

        return f"Guild: {self.name} \n" \
               f"{players_info}"
