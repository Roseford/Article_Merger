from fastapi import Request, APIRouter, status, HTTPException
from ..schemas import Links, Topic, Docs
from ..prompt import summarize_docs1, summarize_docs2, merge_content # Import merge_content from prompt.py
from ..config import settings
from ..beautifulSoup import scrape_data_from_url  # Import the scrape_data_from_url function

router = APIRouter(tags=["routes"], prefix="/merge_articles")

@router.post("/link/", status_code=status.HTTP_201_CREATED,)
async def merge_link(request: Request, links: Links, topic: Topic):
    # Extract the URLs from the Links schema
    url1_list, url2_list = links.link1, links.link2

    # Initialize empty lists to store scraped content from multiple links
    doc1_list = []
    doc1_list_str = str(doc1_list)

    doc2_list = []
    doc2_list_str = str(doc2_list)

    # Scrape content from the provided URLs in link1_list and link2_list
    for url in url1_list:
        doc1 = scrape_data_from_url(url)
        if doc1:
            doc1_list.append(doc1)

    for url in url2_list:
        doc2 = scrape_data_from_url(url)
        if doc2:
            doc2_list.append(doc2)

    if not doc1_list or not doc2_list:
       raise HTTPException(status_code=400, detail="Failed to scrape content from one or both URLs")


    content_1 = summarize_docs1(doc1_list_str)
    content_1_str = str(content_1)

    content_2 = summarize_docs2(doc2_list_str)
    content_2_str = str(content_2)

    # Use OpenAI to merge the content based on the topic
    merged_content = merge_content(topic.topic, content_1_str, content_2_str)

    if not merged_content:
       raise HTTPException(status_code=400, detail="Could not merge documents")
    
    return {"merged_content": merged_content}


@router.post("/texts/", status_code=status.HTTP_201_CREATED,)
async def merge_texts(request: Request, topic: Topic, docs: Docs):
    # Extract the topic and the two different text strings
    doc1 = docs.doc1
    doc2 = docs.doc2

    doc1_summary = summarize_docs1(doc1)

    doc2_summary = summarize_docs2(doc2)

    # Use OpenAI to merge the content based on the topic
    merged_content = merge_content(topic.topic, doc1_summary, doc2_summary)

    if not merged_content:
       raise HTTPException(status_code=400, detail="Could not merge documents")

    return {"merged_content": merged_content}

