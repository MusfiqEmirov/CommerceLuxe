from django import forms# formsu aliriq
from myapp.models import Product

# class ProductCreateForm(forms.Form):
#     product_name = forms.CharField(label="mehsul adi", min_length=3, max_length=20,error_messages={
#         "min_length": "minimum 3 herf olmaldiir",
#         "max_length": "maxxsimumn 20 herf olmaldiir",
#     },widget=forms.TextInput(attrs={'class':'form-control'}))

#     price = forms.FloatField(label="mehsulun qiymeti", widget=forms.TextInput(attrs={'class':'form-control'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),label="reyleriniz")
#     slug = forms.SlugField(label="slug elavene et", widget=forms.TextInput(attrs={'class':'form-control'}))


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","price","description","slug", "image"]
        error_messages = {

            "name": {

                "required": "bu sahe dolmaldir ",
                "max_length":"maxs 100 xarakter olmalidir"
                
            }
        }
        labels = {
            "name":"mehsulun adi",
            "price":"mehsulun qoymeti",
            "description":"mehsul haqqinda rey",
            "slug":"slug elave et"
        },
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"})
        }




class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        error_messages = {

            "name": {

                "required": "bu sahe dolmaldir blinnnnnn",
                "max_length":"maxs 100 xarakter olmalidir"
                
            }
        }
        labels = {
            "name":"mehsulun adi",
            "price":"mehsulun qoymeti",
            "description":"mehsul haqqinda rey",
            "slug":"slug elave et"
        },
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"})
        }


class UploadForm(forms.Form):
    image = forms.FileField()