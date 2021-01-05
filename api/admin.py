from django.contrib import admin
from api.models import (Game,
                        Player,
                        Session,
                        GameOwnership,
                        PlayerSessionLink
                        )

# Register your models here.

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Session)
admin.site.register(GameOwnership)
admin.site.register(PlayerSessionLink)
