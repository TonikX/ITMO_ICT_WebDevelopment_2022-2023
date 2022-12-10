from django.db import models


class Warrior(models.Model):
    """
    Warrior description
    """
    race_types = (
        ('s', 'student'),
        ('d', 'developer'),
        ('t', 'team-lead'),
    )
    race = models.CharField(max_length=1, choices=race_types, verbose_name='Race')
    name = models.CharField(max_length=120, verbose_name='Name')
    level = models.IntegerField(verbose_name='Level', default=0)
    skill = models.ManyToManyField('Skill', verbose_name='Skill', through='SkillOfWarrior',
                                   related_name='warrior_skils')
    job = models.ForeignKey('Job', on_delete=models.CASCADE, verbose_name='Job',
                            blank=True, null=True)


class Job(models.Model):
    """
    Job description
    """
    title = models.CharField(max_length=120, verbose_name='Title')
    description = models.TextField(verbose_name='Description')


class Skill(models.Model):
    """
    Skill description
    """
    title = models.CharField(max_length=120, verbose_name='Title')

    def __str__(self):
        return self.title


class SkillOfWarrior(models.Model):
    """
    Warrior's skills description
    """
    skill = models.ForeignKey('Skill', verbose_name='Skill', on_delete=models.CASCADE)
    warrior = models.ForeignKey('Warrior', verbose_name='Warrior', on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name='Level')
