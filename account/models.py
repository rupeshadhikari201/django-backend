from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom Model Manager
class UserManager(BaseUserManager):
    def create_user(self, firstname, lastname, email,password=None, cnfpassword=None):
        """
        Creates and saves a User with the given firstname, lastname, email, password
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            firstname = firstname,
            lastname = lastname,
            email=self.normalize_email(email), 
            password = password,
        
            
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, firstname, lastname, email,password=None, ):
        """
        Creates and saves a superuser with the given firstname, lastname, email,password=None, cnfpassword=None
        """
        user = self.create_user(
            firstname = firstname,
            lastname = lastname,
            email = email, 
            password = password,
       
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom Model
class User(AbstractBaseUser):
    
    ROLES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    ]
    
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    
    password = models.CharField(max_length=255)
    # = models.CharField(max_length=10, choicesS, default='client')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Add a foreign key relationship to Project model
    # projects = models.ManyToManyField('Project', related_name='users', blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"    #takes email to login user
    REQUIRED_FIELDS = ["firstname", "lastname", "password"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

# # Model for Project
# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     users = models.ManyToManyField(User, related_name='projects', blank=True)
    
# # Model for Skills
# class Skill(models.Model):
#     name = models.CharField(max_length=255, unique=True)