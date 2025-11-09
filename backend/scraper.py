import requests
from bs4 import BeautifulSoup
from typing import Dict

def scrape_wikipedia_article(url: str) -> Dict[str, str]:
    """
    Scrape Wikipedia article and extract clean content.
    
    Args:
        url: Wikipedia article URL
        
    Returns:
        Dict with 'title' and 'content' keys
        
    Raises:
        ValueError: If article cannot be scraped or content is too short
    """
    try:
        # Set user agent to avoid blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Fetch the Wikipedia page
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title_element = soup.find('h1', {'id': 'firstHeading'})
        title = title_element.get_text().strip() if title_element else "Unknown Article"
        
        # Find main content area
        content_div = soup.find('div', {'id': 'mw-content-text'})
        
        if not content_div:
            raise ValueError("Could not find article content")
        
        # Remove unwanted elements
        # Remove reference links (sup tags)
        for sup in content_div.find_all('sup'):
            sup.decompose()
        
        # Remove tables
        for table in content_div.find_all('table'):
            table.decompose()
        
        # Remove infoboxes
        for infobox in content_div.find_all('table', {'class': 'infobox'}):
            infobox.decompose()
        
        # Remove navigation boxes
        for navbox in content_div.find_all('div', {'class': 'navbox'}):
            navbox.decompose()
        
        # Remove image captions and thumbnails
        for thumb in content_div.find_all('div', {'class': 'thumb'}):
            thumb.decompose()
        
        # Extract paragraphs from the content
        paragraphs = content_div.find_all('p')
        
        # Clean and collect paragraph text
        content_parts = []
        for p in paragraphs:
            text = p.get_text().strip()
            # Only include substantial paragraphs (more than 50 characters)
            if text and len(text) > 50:
                # Remove citation brackets like [1], [2], etc.
                import re
                text = re.sub(r'\[\d+\]', '', text)
                content_parts.append(text)
        
        # Limit to first 15 paragraphs to keep content manageable
        content = "\n\n".join(content_parts[:15])
        
        # Validate content length
        if len(content) < 200:
            raise ValueError("Article content is too short or could not be extracted properly")
        
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
