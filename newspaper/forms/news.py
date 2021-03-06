#-*- encoding=utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from django.forms.widgets import HiddenInput
from newspaper.models import News
import hashlib


class NewsForm(ModelForm):
	class Meta:
		model= News
		fields = '__all__'

class PartialNewsForm(ModelForm):
	class Meta:
		model= News
		fields = ['title', 'subtitle', 'description','subsection', 'image', 'video', 'author']	
		widgets = {
			'title': TextInput(attrs={'required': 'required'}),
			'subtitle': Textarea(attrs={'required': 'required'}),
			'description': Textarea(attrs={'required': 'required'}),
			'subsection': Select(attrs={'required': 'required'}),
			'author': HiddenInput(),
		}
	def __init__(self, *args, **kwargs):
		super(PartialNewsForm, self).__init__(*args, **kwargs)
		self.fields['description'].widget.attrs['class'] = 'ckeditor'
		self.fields['subtitle'].widget.attrs['class'] = 'ckeditor'
		

	def setAuthor(self, author):
		data = self.data.copy()
		data['author'] = author
		self.data = data

	def my_clean_image(self):
		image = self.cleaned_data["image"]
		try:
			if image:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "".join((hash, ".", image.name.split(".")[-1]))
				return image
		except:
			pass
		return image

	def my_clean_video(self):
		video = self.cleaned_data["video"]
		try:
			if video:
				hash = hashlib.md5(video.read()).hexdigest()
				video.name = "".join((hash, ".", video.name.split(".")[-1]))
		except:
			pass
		return video
