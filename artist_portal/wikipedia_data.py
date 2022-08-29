import json
import re
import wikipediaapi
import openai

class WikiGPT:

    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key
        self.wiki_wiki = wikipediaapi.Wikipedia('en')

    def artist_to_json(self, artist_key, verbose = False, model = 'curie'):

        if model == 'davinci':

            model_name = 'text-davinci-002'

            prefix = """The following is a Wikipedia Summary text of an Artist:

            ```
            """

            suffix = """
            ```

            Translate this summary text into JSON. Use the following format:
            ```
            {
                "name" : <Str Name of Person>
                "Gender" : <Str Pronouns>
                "birth_year" : <Str Year Born (YYYY)>
                "death_year" : <Str Year Died (YYYY)>
                "Style" :  <Str Name of Artist Style>
                "Movement" :  <Str Name of Associated Art Movement>
                "Location" : <Str Name of Country of Location>
                "Nationality" : <Str Name of Country of Origin>
                "Occupation" : <Str Name of Occupation>
                "Art School": <Str Name of Art School>
            }
            ```

            Answer:
            ```
            """

        elif model == 'curie':

            model_name = "text-curie-001"

            prefix = """
            The following is a Wikipedia Summary text of an Artist:

            ```
            Hugo Alvar Henrik Aalto (pronounced [ˈhuːɡo ˈɑlʋɑr ˈhenrik ˈɑːlto]; 3 February 1898 – 11 May 1976) was a Finnish architect and designer. His work includes architecture, furniture, textiles and glassware, as well as sculptures and paintings. Aalto's early career ran in parallel with the rapid economic growth and industrialization of Finland during the first half of the 20th century. Many of his clients were industrialists, among them the Ahlström-Gullichsen family. The span of his career, from the 1920s to the 1970s, is reflected in the styles of his work, ranging from Nordic Classicism of the early work, to a rational International Style Modernism during the 1930s to a more organic modernist style from the 1940s onwards.
            Typical for his entire career is a concern for design as a Gesamtkunstwerk, a total work of art, in which he would design the building, and give special treatment to the interior surfaces, furniture, lamps and glassware. The Alvar Aalto Museum, designed by Aalto himself, is located in what is regarded as his home city Jyväskylä.

            Biography
            Life
            Hugo Alvar Henrik Aalto was born in Kuortane, Finland. His father, Johan Henrik Aalto, was a Finnish-speaking land-surveyor and his mother, Selma Matilda "Selly" (née Hackstedt) was a Swedish-speaking postmistress. When Aalto was 5 years old, the family moved to Alajärvi, and from there to Jyväskylä in Central Finland.He studied at the Jyväskylä Lyceum school, where he completed his basic education in 1916, and t

            ```
            Translate this summary text into JSON. Represent a missing piece of information with " "
            the JSON should have these keys: "Name", "Gender", "BirthYear", "DeathYear", "ArtStyle", "ArtMovement","Location","Nationality","Occupation","ArtSchool"

            Answer:
                ```
            {
                    "Name": "Hugo Alvar Henrik Aalto",
                    "Gender": "He",
                    "BirthYear": "1898",
                    "DeathYear": "1976",
                    "ArtStyle": "Scandinavian Modern",
                    "ArtMovement": "Nordic Classicism",
                    "Location": "Finland",
                    "Nationality": "Finland",
                    "Occupation": "Architect and Designer",
                    "ArtSchool": "Jyväskylä Lyceum"
            }
                ```

            The following is a Wikipedia Summary text of an Artist:
            ```
            """

            suffix = """
            ```
            Translate this summary text into JSON. Represent a missing piece of information with " "
            the JSON should have these keys: "Name", "Gender", "BirthYear", "DeathYear", "ArtStyle", "ArtMovement","Location","Nationality","Occupation","ArtSchool"

            Answer:
            ```
            """
        else:
            print('please enter a valid openai model name. see: https://beta.openai.com/docs/models/models')

        wiki_page = self.wiki_wiki.page(artist_key)

        unspecified_page = ('may refer to' in wiki_page.text[:400].split(':')[0])

        if wiki_page.exists() and not unspecified_page:

            artist_summary = wiki_page.text[:2000]

            full_prompt = f"{prefix}{artist_summary}{suffix}"

            response = openai.Completion.create(
                engine = model_name,
                prompt = full_prompt,
                temperature = 0,
                max_tokens = 400,
                top_p = 1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0
            )

            model_output = response['choices'][0]['text']

            # clean output by removing all non-data characters & any multi blankspaces
            clean_output = model_output.replace('```', '').replace('\n', '').replace("{", "").replace("}", "").strip()
            clean_output = re.sub(' {2,}', '', clean_output)

            # check for pesky last comma
            if clean_output[-1] == ',':
                clean_output = clean_output[:-1]

            # add curly brackets back on
            if clean_output[0] != '{':
                clean_output = '{' + clean_output
            if clean_output[-1] != '}':
                clean_output = clean_output + '}'

            results_dict = json.loads(clean_output)

            results_dict['ArtistKey'] = artist_key
            results_dict['WikipediaUrl'] = wiki_page.fullurl

            return results_dict

        else:
            if verbose:
                print('Wikipedia page not found.')
            return {}
