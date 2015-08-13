from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __unicode__(self):
		return self.name

class Cereal(models.Model):

	# cereal identification attributes
	name = models.CharField(max_length=30, unique=True)
	cereal_type = models.CharField(max_length=1, null=True)
	manufacturer = models.ForeignKey("main.Manufacturer", null=True)
	image = models.ImageField(upload_to="cereal", null=True)
	info = models.TextField()

	# other
	display_shelf = models.ForeignKey("main.DisplayShelf", null=True)
	ss_weight = models.FloatField(null=True)
	cps = models.FloatField(null=True)

	def __unicode__(self):
		return self.name

class NutritionFacts(models.Model):

	calories = models.IntegerField(null=True)

	protein = models.IntegerField(null=True)				# grams
	fat = models.IntegerField(null=True)					# grams
	fiber = models.FloatField(null=True)					# grams
	carbs = models.FloatField(null=True)					# grams
	sugar = models.IntegerField(null=True)					# grams

	sodium = models.IntegerField(null=True)					# milligrams
	potassium = models.IntegerField(null=True)				# milligrams
	vitamins_minerals = models.IntegerField(null=True)		# milligrams
	cereal = models.OneToOneField("main.Cereal")

	def __unicode__(self):
		return str(self.calories)

	def list(self):
		values = []
		values.append('has "%s" calories' % self.calories)
		values.append('protein: %sg' % self.protein)
		values.append('carbs: %sg' % self.carbs)
		values.append('fat: %sg' % self.fat)
		values.append('fiber: %s' % self.fiber)
		values.append('sugar: %s' % self.sugar)
		values.append('sodium: %s' % self.sodium)
		values.append('potassium: %s' % self.potassium)
		values.append('vitamins and minerals: %s' % self.vitamins_minerals)

		return values

class DisplayShelf(models.Model):
	number = models.IntegerField(unique=True)

	def __unicode__(self):
		return str(self.number)
