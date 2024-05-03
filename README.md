# parse.py

This Python script is used to extract specific information about investors from a given URL. The URL is expected to point to an HTML page that contains investor information.

## Dependencies

This script depends on the following Python libraries:

- `langchain_core`
- `scrape` (a custom module)

## How it Works

The script defines a function `extract_company_info(url: str)`. This function takes a URL as input, fetches the HTML content of the page at that URL, and extracts information about investors.

The information extracted includes:

1. Name of the investor
2. LinkedIn URL of the investor
3. Position of the investor
4. Bio of the investor

The function uses the `Ollama` model from the `langchain_core` library to perform the extraction. The model is given a prompt that specifies what information to extract. The prompt is defined using a `PromptTemplate` from the `langchain_core` library.

The HTML content of the page is fetched using the `extract_html_from_url(url: str)` function from the `scrape` module. This function is not defined in `parse.py`, so it must be imported from elsewhere.

## Usage

To use the `extract_company_info(url: str)` function, import it in your Python script and call it with the URL of the page you want to extract information from. For example:

```python
from parse import extract_company_info

url = "http://example.com"  # Replace with your actual URL
extract_company_info(url)
```
