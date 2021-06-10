from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

 def test_create_user_with_valid_email(self):
  email = 'niyo@gmail.com'
  password = 'Test123'

  user = get_user_model().objects.create_user(
   email = email,
   password = password
  )
  self.assertEqual(user.email, email)
  self.assertTrue(user.check_password(password))

 def test_new_user_email_normarized(self):
  """ testing user email is lower"""
  email = 'niyo@GMAIL.com'
  user = get_user_model().objects.create_user(email, 'Test123')
  self.assertEqual(user.email, email.lower())

 def test_new_user_invalid_email(self):
  """ checking if user email is provided """
  with self.assertRaises(ValueError):
   get_user_model().objects.create_user(None, 'Test123')

 def test_new_superuser(self):
  """ chaking if user is super user """
  user = get_user_model().objects.create_superuser(
   'niyo@gmail.com',
   'Test123'
  )
  self.assertTrue(user.is_superuser)
  self.assertTrue(user.is_staff)