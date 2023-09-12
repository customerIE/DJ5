from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label='��������', max_length=100)
    description = forms.CharField(label='��������', widget=forms.Textarea)
    price = forms.DecimalField(label='����', max_digits=10, decimal_places=2)
    amount = forms.IntegerField(label='����������')
    image = forms.ImageField(label='�����������', required=False)


class ImageForm(forms.Form):
    image=forms.ImageField()