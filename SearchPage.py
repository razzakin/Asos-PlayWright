class SearchPage:
    def __init__(self, page):
        self.page = page
        self.results_count = page.locator('p:has-text("styles found")')