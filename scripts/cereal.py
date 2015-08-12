#!/usr/bin/env python
import csv, os, sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Manufacturer, Cereal, NutritionFacts, DisplayShelf

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cereal.csv")

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    
    cereal, created = Cereal.objects.get_or_create(name=row['Cereal Name'])

    manufacturer, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])

    try:
        manufacturer.save()
    except Exception, e:
        print e
        print "ERROR :::: Failed to save Manufacturer instance"

    cereal.cereal_type = row['Type']
    #cereal.display_shelf = row['Display Shelf']
    cereal.ss_weight = row['Serving Size Weight']
    cereal.cps = row['Cups per Serving']
    cereal.manufacturer = manufacturer

    shelf, created = DisplayShelf.objects.get_or_create(number=row['Display Shelf'])

    
    try:
        shelf.save()
        print "saved."
    except Exception, e:
        print e
        print 'ERROR :::: Failed to save DisplayShelf instance "%s"' % shelf.number
        print "created: %s" % created

    cereal.display_shelf = shelf

    try:
        cereal.save()
    except Exception, e:
        print e
        print "ERROR :::: Failed to save Cereal instance %s" % row['Cereal Name']

    nutrition = NutritionFacts()
    nutrition.calories = row['Calories']
    nutrition.protein = row['Protein (g)']
    nutrition.fat = row['Fat']
    nutrition.fiber = row['Dietary Fiber']
    nutrition.carbs = row['Carbs']
    nutrition.sugar = row['Sugars']
    nutrition.sodium = row['Sodium']
    nutrition.potassium = row['Potassium']
    nutrition.vitamins_minerals = row['Vitamins and Minerals']
    nutrition.cereal = cereal

    try:
        nutrition.save()
    except Exception, e:
        print e
        print 'ERROR :::: Failed to save Nutrition instance  with "%s" calories' % nutrition.calories


    print 'Cereal "%s" was manufactured by "%s" and has %s calories.' % (cereal.name, manufacturer.name, nutrition.calories)
    print "------------------------------------------------------"

