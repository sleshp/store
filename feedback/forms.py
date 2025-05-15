from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите текст отзыва'}))
    RATING_CHOICES = [
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Neutral'),
        (4, 'Good'),
        (5, 'Very Good'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, initial=5, widget=forms.Select())
    class Meta:
        model = Feedback
        fields = ('text', 'rating')