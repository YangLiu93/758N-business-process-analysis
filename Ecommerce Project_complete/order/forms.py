from django import forms

from .models import Product, return_order


class return_orderForm(forms.ModelForm):
    class Meta:
        model = return_order
        fields = ('ProductId', 'ReturnReason', 'ReturnOptions', 'ProductQuality')

    def __init__(self, user, *args, **kwargs):
        super(return_orderForm, self).__init__(*args, **kwargs)
        self.fields['ProductId'].queryset = Product.objects.filter(ProBuyer=user)

