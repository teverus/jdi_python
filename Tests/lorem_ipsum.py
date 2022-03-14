def test_first_test(driver):
    _.login_page._open()
    _.login_page.username_input._send_keys("Admin")
    _.login_page.password_input._send_keys("admin123")
    _.login_page.login_button._click()
    _.dashboard_page.logo._is_visible()
