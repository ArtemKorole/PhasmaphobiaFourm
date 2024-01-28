from django.db import models

class Ghost_category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Ghost(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    number = models.IntegerField()
    category = models.ForeignKey(Ghost_category,on_delete=models.PROTECT)
    img_url = models.TextField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

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
