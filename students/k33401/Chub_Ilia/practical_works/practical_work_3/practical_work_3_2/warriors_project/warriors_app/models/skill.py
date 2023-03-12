from django.db.models import Model, CharField


class Skill(Model):
    title = CharField(max_length=120)

    def __str__(self):
        return self.title
