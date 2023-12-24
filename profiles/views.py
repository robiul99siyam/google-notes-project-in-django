from django.shortcuts import render, redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic import TemplateView
from django.contrib import messages
def profile(request):
    data = models.WriteModel.objects.filter(user=request.user)

    if request.method == "POST":
        form = forms.WriteForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("profile")

    else:
        form = forms.WriteForm()

    return render(request, "profile.html", {"form": form, "data": data})


def reminder(request):
    remin = models.WriteModel.objects.all()
    return render(request,'reminder.html',{'remin':remin})


class data_update(UpdateView):
    model = models.WriteModel
    form_class = forms.WriteForm
    template_name = 'profile.html'
    pk_url_kwarg = 'id'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request,'Edit Successfully ')
        return super().form_valid(form)
    

def temp(request):
    tmp = models.WriteModel.objects.all()
    return render(request,'update.html',{'tmp':tmp})

class deleteNow(DeleteView):
    model = models.WriteModel
    form_class = forms.WriteForm
    pk_url_kwarg = 'id'
    def get_success_url(self):
        return reverse_lazy('profile')
    template_name = 'profile.html'

def deleteNow(request , id):
    post = models.WriteModel.objects.get(pk=id)
    messages.success(request,'Your Data Delete Now ')
    post.delete()
    return redirect('reminder')