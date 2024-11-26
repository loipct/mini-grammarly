from app.ai.inference.predict import predict_essay_score

def grade_essay(essay_text, task_type):
    return predict_essay_score(essay_text, task_type)
  
  
if __name__ == "__main__":
    essay_text = """Information about the thousands of visits from overseas to three different European natural places during 1987 and 2007 is provided in the given line chart.
    Overall, it can be seen that the number of visitors increased significantly in the three places compared to the initial year. Although, visits to Europeans lakes demostrated more changes over the 20 years than its counterparts.
    In more detail, the most steady growth was experienced by the visits to Europeans mountains. For example, from 1987 the number of visitors grew from 20,000 to almost the double 20 years later. Similarly, visits to the coast also rose after a slight fall in 1992, reaching almost twice as much since 1987, with 75,000.
    Those visiting Europeans lakes subtantially increased over the years from 10 thousand to a peak of 75 thousand in 2002. Despite falling for about 25 thousand in 2007, the visitis to this place remained higher compared to 1987, with 50,000 at the end of the period."""  # Replace with your essay text
    task_type = [1, 0]  # Example: [Task_Type_0, Task_Type_1], adjust based on your encoding
    print(predict_essay_score(essay_text, task_type))