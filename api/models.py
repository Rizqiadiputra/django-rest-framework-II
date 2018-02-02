from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

"""
We're going to make a couple of changes to our Student model class. First, let's add a couple of fields. One of those fields will be used to represent the user who created the code student. The other field will be used to store the highlighted HTML representation of the code.
"""

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Student(models.Model):
    owner = models.ForeignKey('auth.User', related_name='students', on_delete=models.CASCADE)
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    #method save
    def save(self, *args, **kwargs):
        """
         Use the `pygments` library to create a highlighted HTML
    representation of the code student.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Student, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)


"""
diatas
Tutorial 4: Authentication & Permissions
Currently our API doesn't have any restrictions on who can edit or delete code students. We'd like to have some more advanced behavior in order to make sure that:

Code students are always associated with a creator.
Only authenticated users may create students.
Only the creator of a student may update or delete it.
Unauthenticated requests should have full read-only access.
"""


"""tutorial 1 - 3"""
# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
#
# class Student(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
#
#     class Meta:
#         ordering = ('created',)