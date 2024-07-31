from django.test import TestCase, Client
from .models import CustomUser
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import User

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        user = User.objects.create_user(username='johnnytest', password='testpassword')
        CustomUser.objects.create(user=user, name='johnny test', bio='No bio.')
        
    # test to see if the user's name is initialized as expected
    def test_user_name(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # test to see if the default image is used if no other pic uploaded
    def test_users_pic(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.pic, 'no_picture.jpg')

    # test to see if the length of the name field is a maximum of 120 characters 
    def test_user_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 120, 'name has over 120 characters')

    # test to see if the length of the username field is a maximum of 120 characters 
    def test_user_username_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user.user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150, 'username has over 120 characters')

    # test to see if the user's bio is initialized as expected
    def test_user_bio(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

class UserAuthTest(TestCase):
    def setUpTestData():
        Client()
        user = User.objects.create_user(username='testuser', password='testpassword')
        CustomUser.objects.create(
            user = user,
            name='testcustomuser',
            bio='No bio'
        )

    def test_profile_redirect_without_auth(self):
        response = self.client.get(reverse('users:profile'))
        self.assertRedirects(response, f'/login/?next={reverse("users:profile")}')
    
    def test_profile_redirect_with_auth(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users:profile'))
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_profile.html')