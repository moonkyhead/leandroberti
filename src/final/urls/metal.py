from django.urls import path
from final import views

metal_patterns = [
    path('numetal/', views.numetal, name='numetal'),
    path('trashmetal/', views.trashmetal, name='trashmetal'),
    path('deathmetal/', views.deathmetal, name='deathmetal'),
]


numetal_patterns = [
    path('numetal/korn/', views.korn, name='korn'),
    path('numetal/disturbed/', views.disturbed, name='disturbed'),
    path('numetal/deftones/', views.deftones, name='deftones'),
]


trashmetal_patterns = [
    path('trashmetal/metallica/', views.metallica, name='metallica'),
    path('trashmetal/megadeth/', views.megadeth, name='megadeth'),
    path('trashmetal/testament/', views.testament, name='testament'),
]


deathmetal_patterns = [
    path('deathmetal/archenemy/', views.archenemy, name='archenemy'),
    path('deathmetal/children/', views.children, name='children'),
    path('deathmetal/cannibal/', views.cannibal, name='cannibal'),
]

urlpatterns = metal_patterns + numetal_patterns + trashmetal_patterns + deathmetal_patterns
