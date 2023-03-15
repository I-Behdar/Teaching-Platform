from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(
            self: "CustomUserManager",
            username: str | None,
            email: str | None,
            password: str | None,
            **extra_fields
    ):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
            self: "CustomUserManager",
            username: str | None = None,
            email: str | None = None,
            password: str | None = None,
            **extra_fields
    ):
        """
        make the 'username' field nulable
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self.create(username, email, password, **extra_fields)

    def create_superuser(self: "CustomUserManager", email: str, password: str | None, **extra_fields):
        return super().create_superuser(email, email, password, **extra_fields)
