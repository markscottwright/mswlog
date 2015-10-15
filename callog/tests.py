from django.test import TestCase
from django.contrib.auth.models import User
from callog.models import WeighIn
from callog.forms import WeighInForm
from django.utils import timezone


class WeighInModelTest(TestCase):

    def test_weigh_in(self):
        u = User.objects.create_user(username="mark", password="password")
        weigh_in = WeighIn()
        weigh_in.date = timezone.now()
        weigh_in.pounds = 195
        weigh_in.user = u
        weigh_in.save()

        weigh_ins = WeighIn.objects.all()
        self.assertEqual(weigh_ins.count(), 1)


class WeighInViewTest(TestCase):

    def setUp(self):
        super().setUp()
        User.objects.create_user(username="mark", password="password")
        self.client.login(username="mark", password="password")

    def test_weigh_in_uses_correct_template(self):
        response = self.client.get("/callog/weighins")
        self.assertTemplateUsed(response, 'weighins.html')

    def test_weigh_in_uses_correct_form(self):
        response = self.client.get("/callog/weighins")
        self.assertIsInstance(response.context['form'], WeighInForm)


class WeighInFormTest(TestCase):

    def test_good_weigh_in(self):
        form = WeighInForm(data={'date': '2000-01-01', 'pounds': '150'})
        self.assertTrue(form.is_valid())

    def test_cant_save_empty_date(self):
        form = WeighInForm(data={'date': '', 'pounds': '150'})
        self.assertFalse(form.is_valid())

    def test_cant_have_zero_weight(self):
        form = WeighInForm(data={'date': '2015-10-10', 'pounds': '0'})
        self.assertFalse(form.is_valid())

    def test_cant_have_zero_weight(self):
        form = WeighInForm(data={'date': '2015-10-10', 'pounds': '-1'})
        self.assertFalse(form.is_valid())
