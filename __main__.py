from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class Twitter_sender:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir="User Data"')
        self.driver = webdriver.Chrome(options=options)

    def twitter(self):
        self.driver.get("https://www.twitter.com/")
        sleep(4)
        
        print("Finding Search...")
        b1 = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
        print("Search, ok.")
        b1.click()

        sleep(2)
        print('Find inputer')
        inputer = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        print("Send keys to inputer.")
        inputer.send_keys('muito calor')

        sleep(2)
        print("Clicking on inputer")
        click_inp = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[2]/div/div')
        click_inp.click()

        sleep(2)
        print("Enter in latest session")
        latest = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a')
        latest.click()

        sleep(2)
        print("Finding results")
        rs = self.driver.find_elements(By.TAG_NAME, 'article')
        for result in rs:
            print(result.text)
            #clicking in likw button
            try:
                like = self.driver.find_element(By.CSS_SELECTOR, 'div [data-testid="like"]')
                try:
                    like.click()
                    print("Liked!")

                    scrolled = """let scroll = window.scrollY;
                    let nScroll = scroll + 10
                    window.scrollTo(0, nScroll)
                    
                    """

                    self.driver.execute_script(scrolled)

                except:
                    print("Error while try t click in like button")
            except Exception as e:
                print(e)

        input()

tw = Twitter_sender()
tw.twitter()
