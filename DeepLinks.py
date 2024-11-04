import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Web scraping project to collect specific URLs from a public procurement website using Selenium and BeautifulSoup

# 1. SET UP THE WEB DRIVER
# Initialize a Chrome web driver to interact with the browser
# You can use other drivers like Firefox or Edge by replacing "webdriver.Chrome()" with another appropriate driver
# URL of the public procurement website to be accessed

# Load the driver
# URL to navigate to
# Start timer for performance tracking
driver = webdriver.Chrome()
url = "https://contrataciondelestado.es/wps/portal/licitaciones"
driver.get(url)
start_time = time.time()

# 2. ACCESS THE SEARCH FORM
# Find the button to access the form by its ID and click it
button = driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:linkFormularioBusqueda')
button.click()

# Implicitly wait for elements to load
# This allows JavaScript on the page to load all necessary elements
driver.implicitly_wait(20)
current_url = driver.current_url

# 3. FILL IN THE SEARCH FORM
# 3.1. Select "Obras" from the dropdown menu
select_element = Select(driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:combo1MAQ'))
select_element.select_by_value('3')

# 3.2. Enter a code "41000000" in the CPV code field
# If you want to obtain all the deeplins, comment this lines
input_element = driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:cpvMultiple:codigoCpv')
input_element.send_keys('41000000')

# 3.3. Click the "Añadir" button to add the CPV code to the form
add_button = driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:cpvMultiplebuttonAnyadirMultiple')
add_button.click()

# Click the search button to start the search based on filled criteria
button = driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:button1')
button.click()
driver.implicitly_wait(25)

# 4. EXTRACT URLs FROM THE SEARCH RESULTS
# 4.1. Create a list to store extracted URLs
all_deeplink_urls = []
i = 1

# Loop through each page of the search results to collect all URLs
while True:
    # Start timer for each loop iteration
    loop_start_time = time.time()
    try:
        # Wait until at least one row of search results is available on the page
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr[@class='rowClass1']"))
        )
        print('Page: ', i)
        i += 1

        # Parse the page source using BeautifulSoup to find the table containing search results
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        table = soup.find('table', {'id': 'myTablaBusquedaCustom'})
        deeplink_urls = []

        # Extract the URLs from the table rows that contain links with "deeplink"
        for row in table.select('tbody tr'):
            deeplink_link = row.find('a', href=lambda x: x and 'deeplink' in x)
            if deeplink_link:
                deeplink_url = deeplink_link['href']
                deeplink_urls.append(deeplink_url)

        # Append the extracted URLs to the list of all URLs
        all_deeplink_urls.extend(deeplink_urls)

        # Check if there is a "Next" button and click it to proceed to the next page
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:footerSiguiente'))
            )
            next_button.click()
        except TimeoutException:
            # If the "Next" button is not found, we have reached the last page
            print("No more pages or 'Next' button not found.")
            break

    except NoSuchElementException:
        # If no search results are found, break the loop
        break

    # End timer for each loop iteration
    loop_end_time = time.time()
    loop_elapsed_time = loop_end_time - loop_start_time
    print(f"Time taken for this iteration: {loop_elapsed_time:.2f} seconds")

# Close the driver after all data is collected
driver.quit()

# 4.2. Write all collected URLs to a text file
with open('all_deeplink_urls.txt', 'w') as file:
    for url in all_deeplink_urls:
        file.write(url + '\n')

print("All URLs have been saved to all_deeplink_urls.txt")

# 4.3 End timer and print total elapsed time for the script
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total time taken: {elapsed_time:.2f} seconds")
