from aloe import world, step, before, after
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'http://myinsecureapp.com'


@step
def compare_tokens(self):
    '''session tokens should be different'''
    try:
        assert world.session_tokens[0] != world.session_tokens[1]
    except IndexError:
        print "Not enough session tokens to compare."


@step
def user_login(self, user, password):
    '''user (\w+) with password (\w+) is logged in'''
    world.browser.get(URL)
    #find username field and type the given username
    username_field = world.browser.find_element_by_name('Email')
    username_field.send_keys(user)
    #same for password
    pass_field = world.browser.find_element_by_name('Password')
    pass_field.send_keys(password)
    #submit form
    world.browser.find_element_by_id('submit-btn').click()
    #wait for landing page to load
    try:
        WebDriverWait(world.browser, 30).until(EC.title_contains("Landing Page"))
    except:
        print "Unable to login"

    self.then('the value of the session token is saved')


@step
def user_login_2(self, user, password):
    ''' user (\w+) logs in with password (\w+)'''
    self.behave_as("Given user {} with password {} is logged in".format(user, password))


@step
def user_logout(self):
    '''user logs out'''
    world.browser.execute_script("return LogMeout();")


@step
def new_browser_instance(self):
    '''a new browser instance'''
    world.browser = webdriver.Firefox()


@step
def visit_homepage(self):
    '''the homepage'''
    world.browser.get(URL)


@step
def is_cookie_httponly(self):
    '''session token should be flagged as httpOnly'''
    for cookie in world.browser.get_cookies():
        if cookie['name'] == 'PHPSESSID':
            print cookie
            assert cookie['httpOnly']


@step
def is_cookie_secure(self):
    '''session token should be flagged as Secure'''
    for cookie in world.browser.get_cookies():
        if cookie['name'] == 'PHPSESSID':
            print cookie
            assert cookie['secure']


@step
def store_session_token(self):
    '''the value of the session token is saved'''
    for cookie in world.browser.get_cookies():
        if cookie['name'] == 'PHPSESSID':
            world.session_tokens.append(cookie['value'])


@before.all
def init():
    world.session_tokens = []

# closing the browser is slower but provides more deterministic results
@after.each_example
def teardown_browser(scenario, outline, steps):
    world.session_tokens = []
    world.browser.delete_all_cookies()
    world.browser.quit()
