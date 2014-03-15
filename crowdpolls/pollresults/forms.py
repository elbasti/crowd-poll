from django.forms import ModelForm
from pollresults.models import Lead
# We put all of our forms here

class LeadForm(ModelForm):
    class Meta:
        model = Lead
