# helper.py
from firecrawl import FirecrawlApp, JsonConfig
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv
import json

# Load API key once
load_dotenv()
api_key = os.getenv("API_KEY")
app = FirecrawlApp(api_key)

class CategoryCollection(BaseModel):
    surgery_name: str
    overview: str
    causes: Optional[List[str]] = []
    symptoms: Optional[List[str]] = []
    non_surgical_treatments: Optional[List[str]] = []
    surgical_procedures: Optional[List[str]] = []
    procedure_description: Optional[str] = None
    risks_and_complications: Optional[List[str]] = []
    recovery_time: Optional[str] = None
    rehabilitation: Optional[str] = None
    success_rate: Optional[str] = None
    when_to_consider_surgery: Optional[str] = None
    results: Optional[str] = None
    cost_estimation: Optional[str] = None


def get_treatment_links(URL):
    try:
        json_config = JsonConfig(schema=CategoryCollection)

        llm_extraction_result = app.scrape_url(
            URL,
            formats=["json"],
            json_options=json_config,
            only_main_content=False,
            timeout=120000,
        )

        result = llm_extraction_result.json
        treatment_links_grouped = CategoryCollection(**result)

        # Save per page to prevent overwrite
        
        with open(f"treatment_links.json",'+a', encoding='utf-8') as f:
            json.dump(treatment_links_grouped.model_dump(), f, indent=4)
            
            if not treatment_links_grouped:
                print("Data not scrapped for" , treatment_links_grouped.surgery_name)

        return treatment_links_grouped

    except Exception as e:
        print(f"[ERROR] Failed to scrape {URL}: {e}")
        return None
