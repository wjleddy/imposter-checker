from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BaseHandleForm
from .models import BaseHandle, SimilarHandles
from django.views import generic
from .get_sim_handles import create_similar_handles

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
            # Create similar_handles instance with the above handle instance
            sim_handles_batch = create_similar_handles(handle_instance)
            SimilarHandles.objects.bulk_create(sim_handles_batch)
            # Redirect to similar handles page (Redirect on response?)
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
    """Lists each base handle once"""
    model = BaseHandle
    paginate_by = 10
    queryset = BaseHandle.objects.order_by('handle', '-date_pulled').distinct('handle')
    
class SimilarListView(generic.ListView):
    """View shows similar handles for a given base handle and date."""
    model = SimilarHandles
    paginate_by = 30
    
    def get_queryset(self):
        qs = super(SimilarListView, self).get_queryset()
        return qs.filter(base_handle_date__exact=self.kwargs['handle'])
    
