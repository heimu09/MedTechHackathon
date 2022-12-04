from django.contrib import admin
from src import models

admin.site.register([models.Mother, models.Post])