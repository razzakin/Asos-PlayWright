from playwright.sync_api import Page, expect
from HomePage import HomePage
from SearchPage import SearchPage

def test_search_bar_exists(page: Page):
    home_page = HomePage(page)
    home_page.navigate()

    expect(home_page.search_bar).to_be_visible()

def test_search_directs_correctly (page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.search("shirt")

    expect(page).to_have_url("https://www.asos.com/search/?q=shirt")

def test_search_has_results (page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.search("shirt")

    search_page = SearchPage(page)
    expect(search_page.results_count).to_be_visible()

#def test_men_button_directs_correctly

#def test_item_page_directs_to_home_page: