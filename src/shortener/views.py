from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import KirrUrl
# Create your views here.
class HomeView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			'form':the_form,
		}
		return render(request, 'shortener/home.html', context)

	def post(self, request, shortcode=None, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			'form':form,
		}
		template = 'shortener/home.html'
		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = KirrUrl.objects.get_or_create(url=new_url)
			context = {
			'object':obj,
			'created': created,
			}
			if created:
				template = 'shortener/success.html'
			else:
				template = 'shortener/already-exist.html '
		return render(request, template, context)

class URLRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		qs = KirrUrl.objects.filter(shortcode__iexact=shortcode)
		if qs.count() != 1 and not qs.exist():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		#obj = get_object_or_404(KirrUrl, shortcode=shortcode)
		#ClickEvent.objects.create_event(obj)

		return HttpResponseRedirect(obj.url)