from django.shortcuts import render
from history.models import History

def history(request):
	history = History.objects.all().order_by('date')
	return render(request, 'history.html', {'history': history})