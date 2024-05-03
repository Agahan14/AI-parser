from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

from scrape import extract_html_from_url


def extract_company_info(url: str):
    summary_template = """ given the investors information {information} of a company on investor page in html format, I want you to extract information about the investors. You are not allowed to make any assumptions while extracting the information. Every link you provide should be from the information given. There should be no assumptions for Links/URLS. You should not return code to do it.:
        You should extract the following text infromation from the html:
        1. Name of the investor.
        2. Linkedin URL of the investor.
        3. Position of the invetor.
        4. Bio of the investor.
    """

    # Initialize the Ollama model
    llm_model = Ollama(
        model="llama2",
        verbose=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )

    prompt = PromptTemplate(
        template=summary_template,
        input_variables=["information"],
    )

    output_parser = StrOutputParser()

    llm_chain = prompt | llm_model | output_parser

    company_profile_data = extract_html_from_url(url)

    user_data = llm_chain.invoke(
        input={"information": company_profile_data},
    )


extract_company_info("https://www.intelcapital.com/team/jennifer-ard/")
