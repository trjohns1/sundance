from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.views import View
from django.urls import reverse
from django.urls import reverse_lazy

from .forms import PointsetCreateForm
from .forms import PointsetDeleteForm
from .forms import PointsetUpdateForm
from .forms import PointCreateForm
from .forms import PointDeleteForm
from .forms import PointUpdateForm
from .models import Point
from .models import Pointset

# ------------------------------ Utility Classes ------------------------------

class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'pinpoint/home.html', context)

# class SignupView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

class ErrorView(View):
    def get(self, request):
        return render(request, "pinpoint/error.html")

# ------------------------------ PointSet Classes ------------------------------

class PointsetListView(LoginRequiredMixin, View):
    def get(self, request):
        pointsets = Pointset.objects.filter(created_by=request.user.username)
        context = {
            'pointsets': pointsets
        }
        return render(request, 'pinpoint/pointset_list.html', context)

class PointsetCreateView(LoginRequiredMixin, View):
    def get(self, request):
        # Create a blank instance of a form
        form=PointsetCreateForm()
        return render(request, 'pinpoint/pointset_create.html', {'form': form})

    def post(self, request):
        # Create an instance of a form and populate with data from the request
        form=PointsetCreateForm(request.POST)
        # If the form is valid begin processing it
        if form.is_valid():
            # Process data in form.cleaned_data
            newPointset = Pointset(name=form.cleaned_data['name'], creation_date=timezone.now(), created_by=request.user.username)
            newPointset.save()
            # Redirect to a new URL
            return HttpResponseRedirect(reverse('pointset_list'))
        return render(request, 'pinpoint/pointset_create.html', {'form': form})

class PointsetUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        # If id parameter not present in URL then error
        id=request.GET.get('id', '')
        if id == '':
            return HttpResponseRedirect(reverse('error'))
        # Lookup the requested pointset from the database
        try:
            pointset = Pointset.objects.get(pk=id)
        except Pointset.DoesNotExist:
            return HttpResponseRedirect(reverse('error'))
        # Create a form instance with data from the database
        data = {
            'id': pointset.id,
            'name': pointset.name
        }
        form=PointsetUpdateForm(data)
        return render(request, 'pinpoint/pointset_update.html', {'form': form})

    def post(self, request):
        # Create an instance of a form and populate with data from the request
        form=PointsetUpdateForm(request.POST)
        # If the form is valid begin processing it
        if form.is_valid():
            # Process data in form.cleaned_data
            id =  form.cleaned_data['id']
            name = form.cleaned_data['name']
            try:
                # Update database object
                Pointset.objects.filter(id=id).update(name=name)
            except Pointset.DoesNotExist:
                return HttpResponseRedirect(reverse('error'))
            # Redirect to a new URL
            return HttpResponseRedirect(reverse('pointset_list'))  
        return render(request, 'pinpoint/pointset_update.html', {'form': form})

class PointsetDeleteView(LoginRequiredMixin, View):
    def get(self, request):
        # If id parameter not present in URL then error
        id=request.GET.get('id', '')
        if id == '':
            return HttpResponseRedirect(reverse('error'))
        # Lookup the requested pointset from the database
        try:
            pointset = Pointset.objects.get(pk=id)
        except Pointset.DoesNotExist:
            return HttpResponseRedirect(reverse('error'))
        # Create a form instance with data from the database
        data = {
            'id': pointset.id,
            'name': pointset.name
        }
        form=PointsetDeleteForm(data)
        name = pointset.name
        return render(request, 'pinpoint/pointset_delete.html', {'form': form, 'name': name})

    def post(self, request):
        # Create an instance of a form and populate with data from the request
        form=PointsetDeleteForm(request.POST)
        # If the form is valid begin processing it
        if form.is_valid():
            # Process data in form.cleaned_data
            id =  form.cleaned_data['id']
            try:
                # Delete database object
                Pointset.objects.filter(id=id).delete()
            except Pointset.DoesNotExist:
                return HttpResponseRedirect(reverse('error'))
            # Redirect to a new URL
            return HttpResponseRedirect(reverse('pointset_list'))
        return render(request, 'pinpoint/pointset_delete.html', {'form': form})


# ------------------------------ Point Classes ------------------------------

class PointListView(LoginRequiredMixin, View):
    def get(self, request):
        points = Point.objects.filter(pointset=request.GET['id'])
        pointset_name = Pointset.objects.get(pk=request.GET['id'])
        context = {
            'points': points,
            'pointset': request.GET['id'],
            'pointset_name': pointset_name
        }
        return render(request, 'pinpoint/point_list.html', context)

class PointCreateView(LoginRequiredMixin, View):
    def get(self, request):
        # Create a blank instance of a form
        form=PointCreateForm(initial= { 'pointset': request.GET['id'] })
        return render(request, 'pinpoint/point_create.html', {'form': form})

    def post(self, request):
        # Make sure the target point set exists in the database
        try:
            the_pointset = Pointset.objects.get(pk=request.POST['pointset'])
        except Pointset.DoesNotExist:
            return HttpResponseRedirect(reverse('error'))
        # Create an instance of a form and populate with data from the request
        form=PointCreateForm(request.POST)
        # If the form is valid begin processing it
        if form.is_valid():
            # Process data in form.cleaned_data
            newPoint = Point(name=form.cleaned_data['name'], creation_date=timezone.now(), created_by=request.user.username, pointset=the_pointset)
            newPoint.save()
            # Redirect to a new URL
            return HttpResponseRedirect(reverse('point_list') + '?id=' + request.POST['pointset'])
        return render(request, 'pinpoint/point_create.html', {'form': form} )

class PointUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        # If id parameter not present in URL then error
        id=request.GET.get('id', '')
        if id == '':
            return HttpResponseRedirect(reverse('error'))
        # Lookup the requested point from the database
        try:
            point = Point.objects.get(pk=id)
        except Point.DoesNotExist:
            return HttpResponseRedirect(reverse('error'))
        # Create a form instance with data from the database
        data = {
            'id': point.id,
            'name': point.name,
            'pointset': point.pointset.id
        }
        form=PointUpdateForm(data)
        return render(request, 'pinpoint/point_update.html', {'form': form})

    def post(self, request):
        # Create an instance of a form and populate with data from the request
        form=PointUpdateForm(request.POST)
        # If the form is valid begin processing it
        if form.is_valid():
            # Process data in form.cleaned_data
            id =  form.cleaned_data['id']
            name = form.cleaned_data['name']
            try:
                # Update database object
                Point.objects.filter(id=id).update(name=name)
            except Pointset.DoesNotExist:
                return HttpResponseRedirect(reverse('error'))
            # Redirect to a new URL
            return HttpResponseRedirect(reverse('point_list') + '?id=' + request.POST['pointset']) 
        return render(request, 'pinpoint/point_update.html', {'form': form})

class PointDeleteView(LoginRequiredMixin, View):
    def get(self, request):
        # If id parameter not present in URL then error
        id=request.GET.get('id', '')
        if id == '':
            return HttpResponseRedirect(reverse('error'))
        # Lookup the requested point from the database
        try:
            point = Point.objects.get(pk=id)
        except Point.DoesNotExist:
            return HttpResponseRedirect(reverse('error'))
        # Create a form instance with data from the database
        data = {
            'id': point.id,
            'name': point.name,
            'pointset': point.pointset.id
        }
        form=PointDeleteForm(data)
        name = point.name
        return render(request, 'pinpoint/point_delete.html', {'form': form, 'name': name})

    def post(self, request):
        # Create an instance of a form and populate with data from the request
        form=PointDeleteForm(request.POST)
        # If the form is valid begin processing it
        if form.is_valid():
            # Process data in form.cleaned_data
            id =  form.cleaned_data['id']
            try:
                # Delete database object
                Point.objects.filter(id=id).delete()
            except Point.DoesNotExist:
                return HttpResponseRedirect(reverse('error'))
            # Redirect to a new URL
            return HttpResponseRedirect(reverse('point_list') + '?id=' + request.POST['pointset']) 
        return render(request, 'pinpoint/point_delete.html', {'form': form})



# ------------------------------ CODE SNIPPETS ------------------------------
# Return JSON data
# return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})

