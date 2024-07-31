from django import forms

CHART__CHOICES = (
   ('#1', 'Bar chart'),
   ('#2', 'Pie chart'),
   ('#3', 'Line Chart'),
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=100)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)