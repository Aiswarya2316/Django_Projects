from django.urls import path
from . import views
urlpatterns = [
path('fun1',views.fun1),
path('fun2',views.fun2),
path('fun3/<int:a>/<b>',views.fun3),
path('fun4/<int:a>/<int:c>',views.fun4),
path('salary/<int:year>/<int:sal>',views.salary),
path('bill/<int:unit>',views.bill),
path('number/<int:num>',views.number),
path('city/<city>',views.city),
path('cost/<int:costprice>',views.cost),
path('num/<int:nmbr>',views.num),
path('html',views.html),
path('htmll',views.htmll),
path('student',views.student),
path('above',views.above),
path('below',views.below),
path('pet',views.pet),
path('form',views.form),
path('edit/<std>',views.edit),
path('delete/<name>',views.delete),
path('add',views.add),
path('display',views.display),
path('edits/<int:id>',views.edits),
path('deletes/<int:id>',views.deletes),
path('normal_forms',views.normal_forms),
path('model_form',views.model_form_dis),
path('parent',views.parent),
path('child',views.child),



]