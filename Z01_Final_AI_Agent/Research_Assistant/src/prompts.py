class ResearchPrompts():
    """Collection of prompts for analyzing research"""

    # Tool extraction prompts
    REPORT_CREATION_SYSTEM = """You are a top researcher. Extract valuable information from articles pertaining to the topic.
                            Focus on factual information that could be used to write an academic report."""

    @staticmethod
    def report_creation_user(topic: str, content: str) -> str:
        return f"""Topic: {topic}
                Website Content: {content}

                Write 5 detailed paragraphs of relevant information for "{topic}".

                Rules:
                - Only include factual
                
                After, create me numbered citations for the information that you use. 
                
                Then go back through the paragraphs and put a number after the information used from the sources corresponding to their citation number.

                Next to each citation provide a Credibility and Relevancy Score from 0-100:

                Example:

                <citation> Credibility: <score> | Relevancy: <score>
                """
    
    INPUT_VALIDATION_SYSTEM = """ You are a meticulous reviewer of words and phrases. """

    @staticmethod
    def input_validation_user(topic: str) -> str:
        return f""" Topic: {topic}
                Determine whether the topic is inappropriate or contains harmful requests.

                Only respond with True if it does or False if it doesnt

                """