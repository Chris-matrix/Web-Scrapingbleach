import pandas as pd
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import matplotlib.pyplot as plt
import seaborn as sns

# Define the URL
url = "https://bleach.fandom.com/wiki/Category:Characters"

# Request the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize the list to store character data
characters = []

# Find all character links
for link in soup.find_all('a', href=True):
    if '/wiki/' in link['href'] and not link['href'].startswith('/wiki/Category:'):
        character_url = urljoin("https://bleach.fandom.com", link['href'])

        # Request the character page
        response = requests.get(character_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the infobox
        infobox = soup.find('aside', class_='portable-infobox')

        if infobox:
            # Extract the character name
            name_element = infobox.find("h2")
            name = name_element.text if name_element else "N/A"

            # Extract height
            height_element = infobox.find("div", attrs={"data-source": "height"})
            height = height_element.find("div", class_="pi-data-value pi-font").text if height_element else "N/A"

            # Extract weight
            weight_element = infobox.find("div", attrs={"data-source": "weight"})
            weight = weight_element.find("div", class_="pi-data-value pi-font").text if weight_element else "N/A"

            characters.append({
                'Name': name,
                'Height': height,
                'Weight': weight
            })

# Create a DataFrame
df = pd.DataFrame(characters)

# Clean and convert Height and Weight columns
df['Height'] = df['Height'].str.replace(' cm', '').astype(pd.to_numeric, errors='coerce')
df['Weight'] = df['Weight'].str.replace(' kg', '').astype(pd.to_numeric, errors='coerce')

# Filter the data
filtered_by_height = df[df['Height'] > 170]
filtered_by_weight = df[df['Weight'] < 70]
filtered_by_name = df[df['Name'].str.contains('Ichigo', case=False, na=False)]

# Print the results
print("Filtered by Height:")
print(filtered_by_height)

print("Filtered by Weight:")
print(filtered_by_weight)

print("Filtered by Name:")
print(filtered_by_name)

# Visualize the data
plt.figure(figsize=(12, 6))

# Plot Height vs Weight
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='Height', y='Weight', hue='Name', palette='viridis', legend=False)
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

# Plot distribution of Heights
plt.subplot(1, 2, 2)
sns.histplot(df['Height'].dropna(), bins=20, kde=True)
plt.title('Height Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
