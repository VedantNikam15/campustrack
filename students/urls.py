from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    # Skills
    path('skills/new/', views.SkillCreateView.as_view(), name='skill_create'),
    path('skills/<int:pk>/edit/', views.SkillUpdateView.as_view(), name='skill_update'),
    path('skills/<int:pk>/delete/', views.SkillDeleteView.as_view(), name='skill_delete'),

    # Achievements
    path('achievements/new/', views.AchievementCreateView.as_view(), name='achievement_create'),
    path('achievements/<int:pk>/edit/', views.AchievementUpdateView.as_view(), name='achievement_update'),
    path('achievements/<int:pk>/delete/', views.AchievementDeleteView.as_view(), name='achievement_delete'),

    # Certificates
    path('certificates/new/', views.CertificateCreateView.as_view(), name='certificate_create'),
    path('certificates/<int:pk>/edit/', views.CertificateUpdateView.as_view(), name='certificate_update'),
    path('certificates/<int:pk>/delete/', views.CertificateDeleteView.as_view(), name='certificate_delete'),

    # Profile
    path('profile/edit/', views.profile_update, name='profile_update'),
]
