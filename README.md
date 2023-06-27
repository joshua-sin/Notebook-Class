# Notebook-Class
A Python Class that acts like a notebook

Notebooks are books with lined pages to record notes. Your job is to create a class Notebook() which has optional parameters of pages (an integer of the number of pages, default is 1), lines (an integer of the number of lines on each page, default is 5) and content (a dictionary of the content of the notebook. The keys are the page numbers and each object in the value (a list) is what is on each line. The default keys are the page numbers and the default values are empty strings ‘’, one per line on every page.

Functions:
•	__str__()
- Returns the number of pages in the notebook, number of lines per page, and the content of each page in the form of a dictionary

•	changelines(newlines)
- Removes lines on each page if newlines is less than the current number of lines on each page, adds lines on each page if newlines is more than the current number of lines on each page. Retains the orginal values on the pages. Returns True if the operation is successful

- Returns false if newlines <= 0 or newlines is not an integer

•	add_page(num_pages = 1)
- Adds num_pages more pages to the notebook. Returns True if the operation is successful

- Returns False if num_pages is <= 0 or num_pages is not an integer.

•	write(page_number,page_line,content)
- Replaces the line on the page with content. Returns the new line.

- Returns False if content is not a string, page_number is invalid or page_line is out of range. 

•	add(page_number,page_line,content)
- Adds on to the lines on the page with content. Returns the new line.

- Returns False if content is not a string, page_number is invalid or page_line is out of range. 

•	clear(page_number,first_line = 1, last_line = 1)
- Sets the content of the lines within the range to an empty string (‘’). Returns True if the operation is successful.

- Returns False if page_number is invalid, first_line is out of range or last_line is out of range.

•	read_line(page_number,line)
- Returns the content of that line

- Returns False if page_number is invalid or line is out of range

•	read_lines(page_number,first_line = 1,last_line = 1)
- Returns the content of all the lines in the range as a list

- Returns False if page_number is invalid, first_line is out of range or last_line is out of range.
