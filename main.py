from pars import *
def main():
    driver = set_driver()
    html = get_page(driver)
    news = parses(html)
    set_text(news)
    return

if __name__ == '__main__':
    main()
