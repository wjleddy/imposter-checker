from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from datetime import date
from .forms import BaseHandleForm
from .models import BaseHandle, SimilarHandles
from django.views import generic

def index(request):
    """View function for home page"""
    num_base_handles = BaseHandle.objects.count()
    num_similar_handles = SimilarHandles.objects.distinct().count()
    form = BaseHandleForm()
    # Get info for our form
#    handle_instance = get_object_or_404(BaseHandle)
#    # For a POST request return the list of similar handles
    if request.method=='POST':
        # Create a form instance and populate it with data from the request
        form = BaseHandleForm(request.POST)
        # Check validity
        if form.is_valid():
            handle_instance = form.save(commit=False)
            handle_instance.save()
            # Redirect to similar handles page
            return redirect('similar-handles', handle=handle_instance.handle)
    # Create blank form for non-POST methods
    else:
        form = BaseHandleForm()
    
    
    context = {
            'num_base_handles': num_base_handles,
            'num_similar_handles' : num_similar_handles,
            'form': form,
            }
    return render(request, 'index.html', context=context)

class BaseListView(generic.ListView):
    model = BaseHandle
    paginate_by = 10
    
class SimilarListView(generic.ListView):
    model = SimilarHandles
    #queryset = SimilarHandles.objects.latest('date_pulled')
    paginate_by = 50

#def get_handle(request, handle):
#    handle_instance = get_object_or_404(BaseHandle, handle=handle, date_pulled=date.today())
#    # For a POST request return the list of similar handles
#    if request.method=='POST':
#        # Create a form instance and populate it with data from the request
#        form = BaseHandleForm(request.POST)
#        # Check validity
#        if form.is_valid():
#            handle_instance.handle = form.cleaned_data['handle']
#            handle_instance.save()
#            # Redirect to waiting page
#            return HttpResponseRedirect(reverse('/'))
#    # Create blank form for non-POST methods
#    else:
#        form = BaseHandleForm()
#    
#    context = {
#            'form': form,
#            'handle_instance': handle_instance,
#            }
#    
#    return render(request, 'base_handle.html', context)
    
