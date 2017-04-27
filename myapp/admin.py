from django.contrib import admin

from .models import Game, Player, Team, PlatformGame, Platform, PlayerTeam, Match, TeamMatch

admin.site.register(Player)

admin.site.register(Game)

admin.site.register(Team)

admin.site.register(PlatformGame)

admin.site.register(Platform)

admin.site.register(PlayerTeam)

admin.site.register(Match)

admin.site.register(TeamMatch)
