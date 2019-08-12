from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    # def create_user(self, email, password=None, **extra_fields):
    #     """Creates and saves a new User"""
    #     if not email:
    #         raise ValueError('유저는 이메일을 필요로 합니다.')
    #     user = self.model(email=self.normalize_email(email), **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #
    #     return user
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # def create_superuser(self, email, password):
    #     """슈퍼유저 생성 및 저장"""
    #     user = self.create_user(email, password)
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.save(using=self._db)
    #
    #     return user
    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
