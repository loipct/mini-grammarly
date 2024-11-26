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
