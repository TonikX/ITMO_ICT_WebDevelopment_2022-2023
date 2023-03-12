from django.db.models import Model, CharField, IntegerField, ManyToManyField, CASCADE, ForeignKey


class Warrior(Model):
    race_types = (
        ('s', 'student'),
        ('d', 'developer'),
        ('t', 'teamlead')
    )
    race = CharField(max_length=1, choices=race_types)
    name = CharField(max_length=120)
    level = IntegerField(default=0)
    skill = ManyToManyField('Skill', through='SkillOfWarrior', related_name='warrior_skills')
    profession = ForeignKey('Profession', on_delete=CASCADE, blank=True, null=True)
