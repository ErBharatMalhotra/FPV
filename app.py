import streamlit as st
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
import requests
# Define a function to fetch the page content
def get_page_content(url):
    response = requests.get(url)
    return response.content
# Define a function to handle the page reloads
def reload_page(url, n):
    # Set up the webdriver in headless mode
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    

        # Loop through the reloads
    for i in range(n):
        try:
            # Get the page content
            content = get_page_content(url)

            # Load the page content in the browser
            driver.get("data:text/html;charset=utf-8," + content.decode())

            # Wait for the page to fully load
            time.sleep(0.2)  # Change the number of seconds as needed

            # Print the title of the page
            st.write(f"Reload {i+1}: Page Title - {driver.title}")
        except Exception as e:
            st.write(f"An error occurred while reloading page {i+1}: {e}")
            break

    # Close the browser
    driver.quit()

# Set the title of the Streamlit app
st.title("GitHub Profile Views")

# Add a text input for the URL
url = st.text_input("Enter the URL to be reloaded")

# Add a number input for the number of reloads
n = st.number_input("Enter the number of reloads", min_value=1, step=1)

# Add a submit button to start the reloads
if st.button("Reload"):
    if not url:
        st.warning("Please enter a valid URL.")
    else:
        try:
            reload_page(url, n)
        except Exception as e:
            st.error(f"An error occurred while processing the page reloads: {e}")
