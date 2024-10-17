from django.test import TestCase

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)
        # creem usuari amb permisos normals
        user = User.objects.create_user("mpareja", "mario.pareja@coetic.cat", "123456")
        user.is_superuser = False
        user.is_staff = False
        user.save()
