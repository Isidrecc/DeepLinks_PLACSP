import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# 1. SET UP THE WEB DRIVER
driver = webdriver.Chrome()  # You can use other drivers like Firefox or Edge
url = "https://contrataciondelestado.es/wps/portal/licitaciones"
driver.get(url)
start_time = time.time()

# 2. ACCES TO THE NEW WEBSITE
# Find the button by its ID (you can also use other locators like class name, XPath, etc.)
button = driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:linkFormularioBusqueda')
# Click the button
button.click()
# Wait for a few seconds to allow any potential JavaScript actions to take place
driver.implicitly_wait(20)
# Get the current URL after the button click
current_url = driver.current_url

# 3. FILL THE DYNAMIC TABLE
# 3,1. Fill the dropdown menu with the option "Obras"
select_element = Select(driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:combo1MAQ'))
select_element.select_by_value('3')
# 3,2. Fill the text input field with the code "41000000"
input_element = driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:cpvMultiple:codigoCpv')
input_element.send_keys('41000000')
# 3,3. Click the "Añadir" button
add_button = driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:cpvMultiplebuttonAnyadirMultiple')
add_button.click()
# Find the button by its ID (you can also use other locators like class name, XPath, etc.)
button = driver.find_element(By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:button1')
# Click the button
button.click()
# Wait for a few seconds to allow any potential JavaScript actions to take place
driver.implicitly_wait(25)

# 4. EXTRACT URLs
# 4.1. Create a list to store all the extracted URLs
all_deeplink_urls = []
i = 1
while True:
    # Start timer for each loop iteration
    loop_start_time = time.time()
    try:
        # Use WebDriverWait to wait until the specific <tr> element is present
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr[@class='rowClass1']"))
        )
        print('Pagina: ', i)
        i += 1
        # Existing code to extract URLs from the current page
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        table = soup.find('table', {'id': 'myTablaBusquedaCustom'})
        deeplink_urls = []

        for row in table.select('tbody tr'):
            deeplink_link = row.find('a', href=lambda x: x and 'deeplink' in x)
            if deeplink_link:
                deeplink_url = deeplink_link['href']
                deeplink_urls.append(deeplink_url)

        # Append the extracted URLs to the list
        all_deeplink_urls.extend(deeplink_urls)

        # Check if there is a "Siguiente" (Next) button and click it
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'viewns_Z7_AVEQAI930OBRD02JPMTPG21004_:form1:footerSiguiente'))
            )
            next_button.click()
        except TimeoutException:
            print("No more pages or 'Next' button not found.")
            break

    except NoSuchElementException:
        # If there is no "Siguiente" button, extit the driver and break out of the loop
        break

    # End timer for each loop iteration and print elapsed time
    loop_end_time = time.time()
    loop_elapsed_time = loop_end_time - loop_start_time
    print(f"Time taken for this iteration: {loop_elapsed_time:.2f} seconds")

driver.quit()

# 4.2. Write all the URLs to a text file
with open('all_deeplink_urls.txt', 'w') as file:
    for url in all_deeplink_urls:
        file.write(url + '\n')

print("All URLs have been saved to all_deeplink_urls.txt")

# 4.3 End timer and print elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total time taken: {elapsed_time:.2f} seconds")