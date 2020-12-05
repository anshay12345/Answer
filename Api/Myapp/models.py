from django.db import models
from django.contrib.auth.models import (PermissionsMixin,
                                        BaseUserManager,
                                        AbstractBaseUser)


# Create your models here.

class UserManager(BaseUserManager):
    # HELPS DJANGO WITH OUR CUSTOM USER MODEL
    use_in_migrations = True

    def _createuser_(self, email, username, password=None):
        # CREATING AND SAVING A NEW USER WITH THE GIVEN EMAIL AND PASS WORD

        if username is None:
            raise ValueError('User should have a username')
        if not email:
            raise ValueError('User should have an email')

        user = self.model(username=username, email=self.normalize_email(email))
        # CREATING USER
        user.set_password(password)
        # SETTING PASSWORD
        user.save()
        # SAVING THE USER
        return user

    def create_superuser(self, email, name, password):  # CREATING AND SAVING THE SUPERUSER
                                                        # WITH THE GIVEN DETAILS


        user = self.create_user(email, name, password)

        user.is_superuser = True  # SUPERUSER STATUS
        user.is_staff = True

        user.save(using=self._db)

        return user
