from django.http import HttpResponseRedirect
from django.shortcuts import render
from seedspaceapp.facade.person_facade import PersonFacade
from seedspaceapp.forms.add import AddForm

__author__ = 'ife'


def add_person(request):

    if request.method == 'POST':

        add_form = AddForm(request.POST)

        if add_form.is_valid():
            full_name = add_form.cleaned_data['full_name']
            email_address = add_form.cleaned_data['email_address']

            save_result = PersonFacade.create_person(full_name=full_name, email_address=email_address)

            if save_result:
                return HttpResponseRedirect('/')
            return render(request, 'add.html', {'form': add_form})
    else:
        add_form = AddForm()

    return render(request, 'add.html', {'form': add_form})