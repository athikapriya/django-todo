# third party imports
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

# local imports
from .models import Todo


# create task form
class TaskFrom(ModelForm):

    class Meta:
        model = Todo
        fields = ["title", "priority", "deadline", "description"]

        widgets = {

            "title" : forms.TextInput(attrs={
                "class" : "form-control custom-input",
                "placeholder" : "Enter a task title"
            }),

            "priority" : forms.Select(attrs={
                "class" : "form-control custom-input"
            }),

            "deadline" : forms.DateInput(attrs={
                "class" : "form-control custom-input",
                "type" : "date"
            }),

            "description" : forms.Textarea(attrs={
                "class" : "form-control custom-input textarea-scroll",
                "rows" : 3,
                "placeholder" : "Add a comment..."
            }) ,

        }
        
    
    def clean_description(self):
        description = self.cleaned_data.get("description")

        if description:
            words = description.split()
            if len(words) > 300:
                raise ValidationError("Description cannot exceed 300 words.")

        return description