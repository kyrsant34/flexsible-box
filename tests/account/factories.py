from factory import DjangoModelFactory, Sequence, PostGenerationMethodCall, SubFactory

from apps.account.models import Department, User


class DepartmentFactory(DjangoModelFactory):
    title = Sequence('Department {}'.format)
    parent = None

    class Meta:
        model = Department


class UserFactory(DjangoModelFactory):

    email = 'user@example.com'
    password = PostGenerationMethodCall('set_password', 'password')
    department = SubFactory(DepartmentFactory)
    is_active = True

    class Meta:
        model = User
