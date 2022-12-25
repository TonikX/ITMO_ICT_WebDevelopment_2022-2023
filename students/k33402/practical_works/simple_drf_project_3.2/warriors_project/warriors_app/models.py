from django.db import models

# Create your models here.
class Warrior(models.Model):
    
   race_types = (
       ('s', 'student'),
       ('d', 'developer'),
       ('t', 'teamlead'),
   )
   race = models.CharField(max_length=1, choices=race_types, verbose_name='Раса')
   name = models.CharField(max_length=120, verbose_name='Имя')
   level = models.IntegerField(verbose_name='Уровень', default=0)
   skill = models.ManyToManyField('Skill', verbose_name='Умения', through='SkillOfWarrior',
                                  related_name='warrior_skils')
   profession = models.ForeignKey('Profession', on_delete=models.CASCADE, verbose_name='Профессия',
                                  blank=True, null=True)

   def __str__(self):
       return self.name

class Profession(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
       return self.title


class Skill(models.Model):
 
   title = models.CharField(max_length=120, verbose_name='Наименование')

   def __str__(self):
       return self.title


class SkillOfWarrior(models.Model):
  
   skill = models.ForeignKey('Skill', verbose_name='Умение', on_delete=models.CASCADE)
   warrior = models.ForeignKey('Warrior', verbose_name='Воин', on_delete=models.CASCADE)
   level = models.IntegerField(verbose_name='Уровень освоения умения')

   def __str__(self):
        return f'{self.warrior.name} has {self.skill.title}'