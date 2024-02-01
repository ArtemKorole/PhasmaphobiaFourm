from django.db import models
from django.urls import reverse


class Ghost_category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name

# class HardCategoryGostsManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(category=1)

class Ghost(models.Model):
    class Status(models.IntegerChoices):
        HARD = 1, 'Сложные'
        MIDDLE = 2, 'Средние'
        EASY = 3, 'Легкие'

    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    number = models.IntegerField()
    category = models.ForeignKey(Ghost_category, choices=Status.choices, on_delete=models.PROTECT, default=Status.EASY, related_name='ghosts')
    img_url = models.TextField(blank=True, null=True)
    description = models.TextField(max_length=500)
    tags = models.ManyToManyField('TagGhost', blank=True, related_name='tags')

    # Hard_Ghosts = HardCategoryGostsManager()
    # objects = models.Manager()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('slug_ghost', kwargs={'ghost_slug': self.slug})

class TagGhost(models.Model):
    tag = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)

    def get_absolute_url(self):
        return  reverse('tag', kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.tag

class Map(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.TextField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Tier(models.Model):
    tier_number = models.IntegerField()
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.tier_number

class Tool(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.TextField()
    tier = models.ForeignKey(Tier,on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Ghost_event(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.TextField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Evidence(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.TextField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Cursed_items(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.TextField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
