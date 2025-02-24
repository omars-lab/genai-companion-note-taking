from langchain.prompts import PromptTemplate
# from langchain_core.output_parsers.json import SimpleJsonOutputParser
from IPython.display import display
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from operator import itemgetter


def idea_generation_chain(llm, usecase):
    # Prompts
    gn_pt = PromptTemplate(
        input_variables=['usecase'],
        template = """
        I want to build a llm agent that serves as {usecase}. 
        Suggest a good, catchy name for this app that creatively includes the term AI in the name but still makes sense.
        Also ensure the name for the application gives off buddy vibes.
        Keep the repsonse concise and pick top 3.
        """
    )

    gk_pt = PromptTemplate(
        input_variables=['usecase', 'names'],
        template = """
        Given I want to develop a genAI companion with one of these names: {names} for this use case: {usecase}, determine what search keywords are worth sponsoring in google search for each of the names. 
        Pick the most profitable 5 for each name.
        Format them as a JSON object where each key is the name and the value is the list is the keywords to sponsor for the name.
        """
    )
    # Chaining
    name_gen_chain = gn_pt | llm | StrOutputParser()
    keyword_gen_chain = gk_pt | llm | JsonOutputParser()
    overall_chain = {"names": name_gen_chain, "usecase": itemgetter("usecase")} | keyword_gen_chain
    return overall_chain.invoke({'usecase': usecase})