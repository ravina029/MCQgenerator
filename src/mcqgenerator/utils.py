import os
import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("error reading the pdf file"+str(e))
    
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("Unsupported file format is pdf and txt format is supported")




def get_table_data(Quiz):
    try:
        quiz=json.loads(Quiz)

        quiz_data=[]

        for key, val in quiz.items():
            mcq=val['mcq']
            options= " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in val['options'].items()
                ]
            )
            correct=val['correct']
            quiz_data.append({"MCQ":mcq, "Choices":options,"Correct":correct})
        return quiz_data

    except Exception as e:
            raise Exception("error in creating the tablular file"+str(e))
        
