class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_bar = page.get_by_test_id("search-input")

    def navigate(self):
        self.page.goto("https://www.asos.com/")

    def search(self, item):
        self.search_bar.fill(item)
        self.search_bar.press("Enter")