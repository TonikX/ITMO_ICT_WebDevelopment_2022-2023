from django.db.models import Model, IntegerField, CASCADE, ForeignKey


class SkillOfWarrior(Model):
    skill = ForeignKey('Skill', on_delete=CASCADE)
    warrior = ForeignKey('Warrior', on_delete=CASCADE)
    level = IntegerField()
