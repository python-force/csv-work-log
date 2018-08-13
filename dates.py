import datetime

"""
def validate(date_text):
    try:
        
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
"""

text = datetime.datetime.strptime("1981/12/25", '%Y/%m/%d')

print(text)