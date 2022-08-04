import sys
import unittest

from . import session
from .. import test
from .. import lib
from .. import paths
from ..configuration import IrodsConfig

admins = [('otherrods', 'rods')]
users  = [('alice', 'apass')]

class Test_Project_Template_Cpp_Microservice(session.make_sessions_mixin(admins, users), unittest.TestCase):

    def setUp(self):
        super(Test_Project_Template_Cpp_Microservice, self).setUp()
        self.admin = self.admin_sessions[0]
        self.user = self.user_sessions[0]

    def tearDown(self):
        super(Test_Project_Template_Cpp_Microservice, self).tearDown()

    def test_your_first_fix(self):
        pass
