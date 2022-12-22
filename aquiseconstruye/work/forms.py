from django import forms
from django import forms
from django.core.exceptions import ValidationError
from bootstrap_forms.forms import Base64ModelForm
from .models import Work, Survey, Newsletter 


class WorkModelForm(Base64ModelForm):



    class Meta:
        model = Work
        base64_images = ['image', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10', 'image11', 'image12', 'image13', 'image14', 'image15', 'image16', 'image17', 'image18', 'image19', 'image20']
        fields = ['name', 
                'latitude', 
                'longitude', 
                'address',
                'image', 
                'image1', 
                'image2', 
                'image3', 
                'image4', 
                'image5', 
                'image6', 
                'image7', 
                'image8', 
                'image9', 
                'image10', 
                'image11', 
                'image12', 
                'image13', 
                'image14', 
                'image15', 
                'image16', 
                'image17', 
                'image18', 
                'image19', 
                'image20',
                'price',
                'traffic_light',
                'official',
                'dependence',
                'constructor',
                'constructor1',
                'constructor2',
                'constructor3',
                'constructor4',
                'contracts',
                ]