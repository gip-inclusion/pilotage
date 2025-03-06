import re
from collections import defaultdict
from itertools import chain

from bs4 import BeautifulSoup


def remove_static_hash(content):
    return re.sub(r"\.[\da-f]{12}\.(svg|png|jpg)\b", r".\1", content)


def parse_response_to_soup(response, selector=None, no_html_body=False, replace_in_attr=None):
    soup = BeautifulSoup(response.content, "html5lib", from_encoding=response.charset or "utf-8")
    if no_html_body:
        # If the provided HTML does not contain <html><body> tags
        # html5lib will always add them around the response:
        # ignore them
        soup = soup.body
    if selector is not None:
        [soup] = soup.select(selector)
    title = soup.title
    if title:
        title.string = re.sub(r"\s+", " ", title.string)
    for csrf_token_input in soup.find_all("input", attrs={"name": "csrfmiddlewaretoken"}):
        csrf_token_input["value"] = "NORMALIZED_CSRF_TOKEN"
    if "nonce" in soup.attrs:
        soup["nonce"] = "NORMALIZED_CSP_NONCE"
    for csp_nonce_script in soup.find_all("script", {"nonce": True}):
        csp_nonce_script["nonce"] = "NORMALIZED_CSP_NONCE"
    for img in chain(
        soup.find_all("img", attrs={"src": True}), soup.find_all("input", attrs={"type": "image", "src": True})
    ):
        img["src"] = remove_static_hash(img["src"])
    for img in soup.find_all("source", attrs={"srcset": True}):
        img["srcset"] = remove_static_hash(img["srcset"])
    if replace_in_attr:
        replace_in_attr = list(replace_in_attr)
        # Get the list of the attrs (deduplicated) we should search for replacement
        attr_replacements = defaultdict(list)
        for attr, from_str, to_str in replace_in_attr:
            attr_replacements[attr].append((from_str, to_str))
        for attr, replacements in attr_replacements.items():
            nodes = (
                # Search and replace in descendant nodes
                *soup.find_all(attrs={attr: True}),
                # Also replace attributes in the top node
                *([soup] if attr in soup.attrs else []),
            )
            for node in nodes:
                for from_str, to_str in replacements:
                    node.attrs.update({attr: node.attrs[attr].replace(from_str, to_str)})
    return soup
