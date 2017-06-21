import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
	new_code =  code_generator(size=size)
	#print('\ninstance: '+str(instance))
	#print('\ninstance class: '+str(instance.__class__))
	#print('\ninstance name: '+str(instance.__class__.__name__))
	klass= instance.__class__
	qs_exists = klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		create_shortcode(size=size)
	return new_code