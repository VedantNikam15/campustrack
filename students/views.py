from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Skill, Achievement, Certificate, StudentProfile
from .forms import SkillForm, AchievementForm, CertificateForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    skills = user.skills.all().order_by('-added_at')
    achievements = user.achievements.all().order_by('-date')
    certificates = user.certificates.all().order_by('-issue_date')
    profile, _ = StudentProfile.objects.get_or_create(user=user)
    context = {'skills': skills, 'achievements': achievements, 'certificates': certificates, 'profile': profile}
    return render(request, 'students/dashboard.html', context)

# Skill CRUD
class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'students/skill_form.html'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Skill added.")
        return super().form_valid(form)

class SkillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'students/skill_form.html'
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user == self.get_object().user

class SkillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Skill
    template_name = 'students/confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user == self.get_object().user

# Achievement CRUD
class AchievementCreateView(LoginRequiredMixin, CreateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'students/achievement_form.html'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Achievement added.")
        return super().form_valid(form)

class AchievementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'students/achievement_form.html'
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user == self.get_object().user

class AchievementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Achievement
    template_name = 'students/confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user == self.get_object().user

# Certificate CRUD
class CertificateCreateView(LoginRequiredMixin, CreateView):
    model = Certificate
    form_class = CertificateForm
    template_name = 'students/certificate_form.html'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Certificate added.")
        return super().form_valid(form)

class CertificateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Certificate
    form_class = CertificateForm
    template_name = 'students/certificate_form.html'
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user == self.get_object().user

class CertificateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Certificate
    template_name = 'students/confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    def test_func(self):
        return self.request.user == self.get_object().user

# Profile edit
@login_required
def profile_update(request):
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'students/profile_form.html', {'form': form})
