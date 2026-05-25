import json

from langchain_core.prompts import ChatPromptTemplate

from src.model.llm import get_model

llm = get_model()

def analyze_code(diff):

    prompt = ChatPromptTemplate.from_template("""
    You are an expert AI code reviewer.

    Analyze the following code diff.

    Detect:

    1. Security vulnerabilities
    2. Performance issues
    3. Bugs
    4. Code smells

    Code Diff:
    {diff}

    Return ONLY valid JSON.

    Format:

    {{
      "security": [
        {{
          "issue": "",
          "severity": "LOW/MEDIUM/HIGH",
          "line": 1,
          "explanation": "",
          "suggestion": ""
        }}
      ],

      "performance": [],

      "bugs": [],

      "code_smells": []
    }}

    If no issue found use empty array.

    Return ONLY JSON.
    """)

    chain = prompt | llm

    response = chain.invoke({
        "diff": diff
    })

    content = response.content.strip()

    # Remove markdown if model returns ```json
    content = content.replace("```json", "")
    content = content.replace("```", "")

    try:

        return json.loads(content)

    except Exception as e:

        print("\nJSON Parsing Error\n")
        print(e)

        print("\nRaw Response:\n")
        print(content)

        return {
            "security": [],
            "performance": [],
            "bugs": [],
            "code_smells": []
        }