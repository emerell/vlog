from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
from vlog import forms


class TransliterationTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )

    def test_transliteration(self):
        im_io = BytesIO()
        im = Image.new(mode='RGB', size=(200, 200))
        im.save(im_io, 'JPEG')

        cat_form = forms.CategoryForm(
            {
                'title': 'спорт',
                'author': self.user.pk,
                'image': InMemoryUploadedFile(
                    im_io, None, 'random.jpg', 'image/jpeg', len(im_io.getvalue()), None
                )
            }
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'sport')

        cat_form = forms.CategoryForm(
            {'title': 'тест'}, instance=cat
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'test')

        cat_form = forms.CategoryForm(
            {'title': 'Breaking News! Новости.'}, instance=cat
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'breaking-news-novosti')