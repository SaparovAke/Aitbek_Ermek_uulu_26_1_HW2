from django import forms

class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    product_name = forms.CharField(max_length=255, min_length=3)
    price = forms.IntegerField(required=False)
    description = forms.CharField(widget=forms.Textarea())

class CommentCreateForm(forms.Form):
    text = forms.CharField(max_length=255, min_length=1)