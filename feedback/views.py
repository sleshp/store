from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from requests import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from feedback.forms import FeedbackForm
from feedback.models import Feedback, ReferenceMaterial
from feedback.serializers import FeedbackSerializer, ReferenceMaterialSerializer


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('index')
    else:
        form = FeedbackForm()

    context = {
        'title': 'Feedback Form',
        'form': form,
    }
    return render(request, 'feedback/feedback.html', context)


"""
class FeedbackView(View):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('index')

"""
class FeedbackModelViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    pagination_class = None


class ReferenceMaterialList(generics.ListAPIView):
    queryset = ReferenceMaterial.objects.all()
    serializer_class = ReferenceMaterialSerializer
    pagination_class = None