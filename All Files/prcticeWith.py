# with open('Example.txt', 'r') as reading_file:
#     with open('new.txt', 'w') as writing_file:
#         reading_writing = writing_file.writelines(reading_file)
data = []
with open('Progress.txt', 'r') as reading_file:
    while True:
        content = reading_file.readline()
        # print(content)
        if not content:
            break
        marks1 = (f'Marks of {content.split(",")[0]} in Maths is {content.split(",")[1]} ') 
        marks2 = (f'Marks of {content.split(",")[0]} in Physics is {content.split(",")[2]} ')
        marks3 = (f'Marks of {content.split(",")[0]} in Chemistry is {content.split(",")[3]} ')
        marks4 = (f'Marks of {content.split(",")[0]} in English is {content.split(",")[4]} ')
        marks = [marks1,"\n",marks2,"\n",marks3,"\n",marks4,"\n"]
        data.extend(marks)
        
Final_result = ["\n\n---------------------Result---------------------"]
with open('Progress.txt', 'r') as reading_file:
    while True:
        content = reading_file.readline()
        # print(content)
        if not content:
            break
        studentName = f'{content.split(",")[0]}' 
        marks1 = f'{content.split(",")[1]}' 
        marks2 = f'{content.split(",")[2]}' 
        marks3 = f'{content.split(",")[3]}' 
        marks4 = f'{content.split(",")[4]}' 
        marks = [studentName,marks1,marks2,marks3,marks4]
        def result(marks1,marks2,marks3,marks4):
            percentage = (((int(marks1) + int(marks2) + int(marks3) + int(marks4))/400)*100)
            return f'{int(percentage)}'
        
        passing_number =  result(marks1,marks2,marks3,marks4)
        printing = f'Percentage of {marks[0]} is {passing_number}%'
        Final_result.extend(["\n",printing])
        
with open('Result.txt', 'w' ) as writing:
    contentWriting = writing.writelines(data)
    contentWriting2 = writing.writelines(Final_result)