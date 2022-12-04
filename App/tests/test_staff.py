import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import Staff
from App.controllers import (
    create_staff,
    get_staff,
    get_all_staff_json,
    get_all_notifs_json,
    get_staff_by_recommendation,
    get_staff_by_name,
    get_staff_feed_json,
    change_status,
    create_recommendation,
    submit_recommendation,
)


from wsgi import app
LOGGER = logging.getLogger(__name__)


class UserUnitTests(unittest.TestCase):

    def test_create_staff(self):
        staff = Staff(username= "sponge",password= "pass123",name = "spongebob",id= "816000001",faculty= "FST",department= "DCIT")
        assert staff.name == "spongebob"
'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


class StudentsIntegrationTests(unittest.TestCase):
    
    #checks if a staff user was created
    def test_create_staff(self):
        staff = create_staff(name= "Betty",username= "boop",password= "pass123",id= "816000000",faculty= "FST",department= "DCIT")
        assert staff.name == "Betty"

    #checks if data from the staff table in json was retrieved
    def test_get_all_staff_json(self):
        staff_json = get_all_staff_json()
        self.assertListEqual([{"name"=="Betty", "username"=="boop", "password"=="pass123", "id"=="816000000", "faculty"=="FST", "department"=="DCIT"}], staff_json)

    # #checks to see if a staff was be found by ID
    # def test_search_all_staff(self):
    #     #id = "816000000"
    #     staff = get_staff("816000000")
    #     assert staff.name == "Betty"