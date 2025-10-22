
from django.db import models
from ckeditor.fields import RichTextField

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile/')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, help_text="Upload your CV/Resume (PDF preferred)")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Education(models.Model):

    GRADE_TYPE_CHOICES = [
        ('cgpa', 'CGPA'),
        ('gpa', 'GPA'),
    ]

    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    grade = models.FloatField(help_text="Enter your GPA or CGPA value (e.g., 3.8)")
    grade_type = models.CharField(
        max_length=10,
        choices=GRADE_TYPE_CHOICES,  
        default='cgpa',
        help_text="Select whether this is a CGPA or GPA"
    )
    study_period = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.degree} at {self.institution}"

    @property
    def grade_label(self):
        
        return dict(self.GRADE_TYPE_CHOICES)[self.grade_type].upper()
    
class Experience(models.Model):
    position = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    period = models.CharField(max_length=100)
    responsibilities = models.TextField()

class Skill(models.Model):
    SKILL_CATEGORIES = [
    ('Language', 'Programming Languages'),
    ('Frameworks', 'Frameworks & Libraries'),
    ('Front-End', 'Front-End'),
    ('Tools', 'Tools & Platforms'),
    ('Databases', 'Databases'),
    ('Cloud', 'Cloud & DevOps'),
    ('Concepts', 'Concepts & Methodologies'),
    ('Soft Skills', 'Soft Skills'),
    ('Hardware & Networking', 'Hardware & Networking'),
    ('Other', 'Other'),
]
    category = models.CharField(
        max_length=30,
        choices=SKILL_CATEGORIES,
        default='Language'
    )
    name = models.CharField(max_length=100, help_text="e.g., Python, React, Docker")

    def __str__(self):
        return f"{self.get_category_display()} – {self.name}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    features = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_link = models.URLField()
    live_link = models.URLField(blank=True)

class ProblemSolving(models.Model):
    site_name = models.CharField(max_length=100)
    problems_solved = models.IntegerField()
    rating = models.CharField(max_length=50, blank=True)
    link = models.URLField()

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    event = models.CharField(max_length=200)
    rank = models.CharField(max_length=100)
    year = models.IntegerField()
    organization = models.CharField(max_length=200)

class Leadership(models.Model):
    role = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    duration = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=200, blank=True)
    credential_link = models.URLField(blank=True)

class Publication(models.Model):
    title = models.CharField(max_length=300)
    authors = models.TextField()
    conference = models.CharField(max_length=300, blank=True)
    year = models.IntegerField()
    status = models.CharField(max_length=100)  # Published, Accepted, etc.
    publisher = models.CharField(max_length=200, blank=True, help_text="Optional: e.g., IEEE, Springer, ACM")
    doi_link = models.URLField(blank=True, help_text="Optional: Full DOI URL (e.g., https://doi.org/10.xxxx/xxxxx)")
    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to='blogs/')
    content = RichTextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recommendation(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Gallery"