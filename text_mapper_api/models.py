import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user manager for the CustomUser model.
    """

    def create_user(self, email, name, password=None):
        """
        Create and save a regular user with the given email, name, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a superuser with the given email, name, and password.
        """
        user = self.create_user(
            email=email,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    """
    Custom user model extending AbstractBaseUser.
    """

    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email",
                              max_length=255, unique=True)
    name = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        """
        Check if the user has a specific permission.
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Check if the user has permissions to access the app `app_label`.
        """
        return True


class Paragraph(models.Model):
    """
    Model representing a paragraph of text.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()

    objects = models.Manager()


class Word(models.Model):
    """
    Model representing a word in a paragraph.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(max_length=255)
    paragraph = models.ForeignKey(
        Paragraph, related_name='words', on_delete=models.CASCADE)

    objects = models.Manager()
