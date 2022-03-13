def test_first_test(_):
    _.login_page.open()
    _.login_page.username_input.send_keys("Admin")
    _.login_page.password_input.send_keys("admin123")
    _.login_page.login_button.click()
    _.dashboard_page.logo.is_visible()
