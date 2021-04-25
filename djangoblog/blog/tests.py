from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import POst

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = POst.objects.create(
            tittle='A good tittle',
            body='Nice body content',
            author=self.user,
        )
    def test_string_representation(self):
        post = POst(tittle='A sample tittle')
        self.assertEqual(str(post), post.tittle)

    def test_get_absolute_url(self):  # new
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.tittle}', 'A good tittle')

        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')

        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good tittle')
        self.assertTemplateUsed(response, 'detail.html')

    def test_post_create_view(self):  # new
        response = self.client.post(reverse('post_new'), {
            'tittle': 'New tittle',
            'body': 'New text',
            'author': self.user.id,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(POst.objects.last().tittle, 'New tittle')
        self.assertEqual(POst.objects.last().body, 'New text')

    def test_post_update_view(self):  # new
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated tittle',
            'body': 'Updated text',
        })

        self.assertEqual(response.status_code, 200)

    def test_post_delete_view(self):  # new
        response = self.client.post(
            reverse('post_delete', args='1'))

        self.assertEqual(response.status_code, 302)

