# SLR, LR, and LALR Parser Table Generator

## What is the purpose of this project?
This project aims to develop the backend for an application that will generate tables for SLR, LR, and LALR parsers.

## Why was this project initiated?
While studying compiler theory at UTFPR, I realized that I encountered some challenges when generating parsing tables. I believe that by implementing a tool capable of automatically generating these tables, following the same steps I would take manually, I will gain a deeper understanding of the underlying algorithms. Additionally, it will provide me with a means of validating the solutions to exercises for which answer keys are unavailable.

## What are the routes of this API?
- /table/<parser_type>
    - parser_type can be slr, lr, or lalr
    - The post request must include a list of language productions, with each symbol separated by a space. For example:
        ```
        {
            "productions": [
                "E' -> E",
                "E -> E + n",
                "E -> n"
            ]
        }
        ```
- /execute

## Important commands:
- To initialize the project:
    1. Clone the repository: ```git clone https://github.com/NailsonChagas/LR-Parser-Table-Generator.git```
    2. Navigate to the repository: ```cd LR-Parser-Table-Generator```
    3. Create a virtual environment: ```python3 -m venv venv```
    4. Activate the virtual environment: ```source ./venv/bin/activate```
    5. Install dependencies: ```pip install -r requirements.txt```
- To update requirements: ```pip freeze > requirements.txt```