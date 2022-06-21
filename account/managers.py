from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('email field is required')

        if not username:
            raise ValueError('username field is required')

        if password is None:
            raise ValueError('password field is required')

        email=self.normalize_email(email)
        user_obj = self.model(
            email=email,
            username=username,
            **extra_fields
        )

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, username, password=password, **extra_fields)
    
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, username, password=password, **extra_fields)
