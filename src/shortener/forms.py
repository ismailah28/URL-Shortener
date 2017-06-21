from django import forms

from .validators import validate_url


class SubmitUrlForm(forms.Form):
	url = forms.CharField(
		label='',
		validators=[validate_url,],
		widget=forms.TextInput(
			attrs={
				'placeholder':'Enter Long URL',
				'class': 'form-control'
				}
			)
		)

	'''def clean(self):
					cleaned_data = super(SubmitUrlForm, self).clean()
					url = cleaned_data.get('url')
					return url'''