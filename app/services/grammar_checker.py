import language_tool_python
from app.models.schemas import CorrectionDetail, CorrectionResponse

tool = language_tool_python.LanguageTool('en-US')

def check_and_correct_text(input_text: str) -> list[CorrectionResponse]:
    sentences = input_text.split('.')  # Tách đoạn văn thành các câu
    result = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        matches = tool.check(sentence)
        if matches:
            corrected_sentence = language_tool_python.utils.correct(sentence, matches)
            corrections = [
                CorrectionDetail(
                    error_text=match.context,
                    message=match.message,
                    suggestions=match.replacements,
                    offset=match.offset,
                    length=match.errorLength
                )
                for match in matches
            ]
            result.append(CorrectionResponse(
                original=sentence,
                corrected=corrected_sentence,
                corrections=corrections
            ))
    return result


if __name__ == "__main__":
    essay_text = """Information about the thousands of visits from overseas to three different European natural places during 1987 and 2007 is provided in the given line chart.
    Overall, it can be seen that the number of visitors increased significantly in the three places compared to the initial year. Although, visits to Europeans lakes demostrated more changes over the 20 years than its counterparts.
    In more detail, the most steady growth was experienced by the visits to Europeans mountains. For example, from 1987 the number of visitors grew from 20,000 to almost the double 20 years later. Similarly, visits to the coast also rose after a slight fall in 1992, reaching almost twice as much since 1987, with 75,000.
    Those visiting Europeans lakes subtantially increased over the years from 10 thousand to a peak of 75 thousand in 2002. Despite falling for about 25 thousand in 2007, the visitis to this place remained higher compared to 1987, with 50,000 at the end of the period."""  # Replace with your essay text
    print(check_and_correct_text(essay_text))