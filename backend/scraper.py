import requests
from bs4 import BeautifulSoup
from typing import Dict

def scrape_wikipedia_article(url: str) -> Dict[str, str]:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title_element = soup.find('h1', {'id': 'firstHeading'})
        title = title_element.get_text() if title_element else "Unknown Article"
        
        content_div = soup.find('div', {'id': 'mw-content-text'})
        
        if not content_div:
            raise ValueError("Could not find article content")
        
        paragraphs = content_div.find_all('p')
        
        content_parts = []
        for p in paragraphs:
            text = p.get_text().strip()
            if text and len(text) > 50:
                content_parts.append(text)
        
        content = "\n\n".join(content_parts[:15])
        
        if len(content) < 200:
            raise ValueError("Article content is too short")
        
        return {
            "title": title,
            "content": content
        }
    
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch Wikipedia article: {str(e)}")
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Failed to parse Wikipedia article: {str(e)}")
