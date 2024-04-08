
from django.shortcuts import render


""" This function loads the summary page"""
def summary(request):
    return render(request, 'Summary.html')