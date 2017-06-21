from django.core.management.base import BaseCommand
from shortener.models import KirrUrl


class Command(BaseCommand):
	"""docstring for Command"""
	help = 'Refreshes all KirrUrl shortcodes'

	def add_arguments(self, parser):
		parser.add_argument('items', type=int)

	def handle(self, *args, **options):
		return KirrUrl.objects.refresh_shortcode(items=options['items'])
