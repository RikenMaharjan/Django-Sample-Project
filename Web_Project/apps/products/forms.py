from django.forms import forms, ModelForm

from apps.products.models import Product


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control abcdef'
            })
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'
        #     visible.field.widget.attrs['style'] = 'form-control'
