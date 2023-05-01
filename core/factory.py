import selenium.webdriver as webdriver


class Factory:
    def __init__(self):
        pass

    @staticmethod
    def get_config(config):
        if config['type'] == 'local':
            if config['browser'] == 'Firefox':
                opts = webdriver.FirefoxOptions()
                opts.add_argument("--width=1920")
                opts.add_argument("--height=1080")
                browser = webdriver.Firefox(options=opts)
            elif config['browser'] == 'Chrome':
                opts = webdriver.ChromeOptions()
                opts.add_argument('--window-size=1920,1080')
                browser = webdriver.Chrome(options=opts)
            else:
                raise Exception(
                    f'Browser "{config["browser"]}" is not supported in local mode')

        # Initialize the remote WebDriver instance
        elif config['type'] == 'remote':
            if config['browser'] == 'Headless Firefox':
                opts = webdriver.FirefoxOptions()
            elif config['browser'] == 'Headless Chrome':
                opts = webdriver.ChromeOptions()
            else:
                raise Exception(
                    f'Browser "{config["browser"]}" is not supported in remote mode')

            opts.add_argument('--no-sandbox')
            opts.add_argument('--headless')
            opts.add_argument('--disable-gpu')
            browser = webdriver.Remote(
                command_executor=config['url_remote'],
                options=opts
            )

        return browser


def factory(config):
    if config['type'] == 'local':
        if config['browser'] == 'Firefox':
            opts = webdriver.FirefoxOptions()
            opts.add_argument("--width=1920")
            opts.add_argument("--height=1080")
            browser = webdriver.Firefox(options=opts)
        elif config['browser'] == 'Chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('--window-size=1920,1080')
            browser = webdriver.Chrome(options=opts)
        else:
            raise Exception(
                f'Browser "{config["browser"]}" is not supported in local mode')

    # Initialize the remote WebDriver instance
    elif config['type'] == 'remote':

        if config['browser'] == 'Headless Firefox':
            opts = webdriver.FirefoxOptions()
        elif config['browser'] == 'Headless Chrome':
            opts = webdriver.ChromeOptions()
        else:
            raise Exception(
                f'Browser "{config["browser"]}" is not supported in remote mode')

        opts.add_argument('--no-sandbox')
        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')
        browser = webdriver.Remote(
            command_executor=config['url_remote'],
            options=opts
        )

        return browser
