from django.contrib import admin

from .league import LeagueAdmin
from .player import PlayerAdmin
from .ranking import RankingAdmin
from .tournament import TournamentAdmin
from front.models import (
    League,
    Player,
    Ranking,
    Tournament,
)

admin.site.register(League, LeagueAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(Tournament, TournamentAdmin)
