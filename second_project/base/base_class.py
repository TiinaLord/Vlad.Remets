import datetime


class Base():
    def __init__(self, driver_g):
        self.driver = driver_g

    #Method get
    def get_current_url(self):
        get_url = self.driver_g.current_url
        print("Current url: " + get_url)

    #Method screenshot
    def screenshot(self):
        current_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")  # Выводим текущую дату
        name_screen = "sceenshot" + current_time + ".png"  # К названию файла добавляем формат и время
        self.driver_g.save_screenshot('C:\\Users\\Влад\\PycharmProjects\\second_project\\screen\\' + name_screen)

    # Method assert url

    def assert_url(self, result):
        get_url = self.driver_g.current_url
        assert get_url == result
        print("URL is correct")