name = 'kwangil ahn'
age = 46 #it's a lie
my_height_cm = 178 # inches
cm_to_inch = 1.0/2.54
my_height_inch = my_height_cm * cm_to_inch
my_weight_kg = 75
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % my_height_cm
print "He's %d pounds heavy." % my_weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (
    age, my_height_cm, my_weight_kg, age + my_height_cm + my_weight_kg)
