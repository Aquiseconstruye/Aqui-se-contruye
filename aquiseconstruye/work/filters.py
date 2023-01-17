from work.models import Work
import django_filters
 
class ObrasFilter(django_filters.FilterSet):
    class Meta:
        model = Work
        fields = ['traffic_light', ]