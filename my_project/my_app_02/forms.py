from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CustomerForm(forms.Form):
    customer_name = forms.CharField(min_length=1, max_length=128,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'form-control placeholder',
                                            'placeholder': 'Имя пользователя'}),
                                    label='')
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control placeholder',
               'placeholder': 'user@example.ru'}), label='')
    phone_number = PhoneNumberField(widget=forms.TextInput(
        attrs={'class': 'form-control placeholder',
               'placeholder': '+79161234567', 'type': 'tel'}), label='')
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control placeholder',
               'placeholder': 'Адрес'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control placeholder', 'placeholder': 'Пароль'}),
        label='')
