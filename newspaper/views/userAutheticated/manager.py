# -*- endcoding=utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from newspaper.models import News, Section, SubSection
from newspaper.utils import getNewsFromSection
def manager(request, id_section = None, id_subsection = None):
	if not request.user.has_perm('newspaper.access_manager'):
		return HttpResponseRedirect("/newspaper/")

	news = News.objects.all()
	sections = Section.objects.all()
	subsections = Section.objects.all()

	if id_section == None and id_subsection == None:
		news = News.objects.all()
	elif id_section != None and id_subsection == None:
		try:
			section = Section.objects.get(id = id_section)
			news = getNewsFromSection(section)
			open_sections = True
		except:
			news = []
	elif id_subsection != None:
		try:
			news = News.objects.filter(subsection = id_subsection)
			open_sections = True
			open_subsections = True
		except:
			news = []

	return render(request, 'newspaper/userAuthenticated/manager.html', locals())