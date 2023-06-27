class Notebook(object):
    def __init__(self,pages = 1,lines = 5,content= {}):
        self.pages = pages
        self.lines = lines
        self.content = content
        if self.content == {}:
            for i in range(pages):
                self.content[i+1] = []
                for j in range(lines):
                    self.content[i+1].append('')
        
    def changelines(self,newlines):
        if type(newlines) == int and newlines >= 1:
            self.lines = newlines
            for i in range(self.pages):
                if self.content[i+1] != []:
                    if len(self.content[i+1]) > newlines:
                        self.content[i+1] = self.content[i+1][:newlines+1]
                    elif len(self.content[i+1]) < newlines:
                        for k in range(newlines - len(self.content[i+1])):
                            self.content[i+1].append('')
                else:
                    self.content[i+1] = []
                    for j in range(newlines):
                        self.content[i+1][0].append('')
            return True
        else:
            return False
        
    
    def add_page(self,num_pages = 1):
        if type(num_pages) == int and num_pages >= 1:
            for m in range(num_pages):
                self.pages += 1
                self.content[self.pages] = []
                for j in range(self.lines):
                        self.content[i+1][0].append('')
            return True
        else:
            return False
                
    def write(self,page_number,page_line,content):
        if type(content) == str:
            if page_number in self.content.keys():
                if page_line <= len(self.content[page_number]):
                    self.content[page_number][page_line-1] = content
                    return self.content[page_number][page_line-1]
        return False

    def add(self,page_number,page_line,content):
        if type(content) == str:
            if page_number in self.content.keys():
                if page_line <= len(self.content[page_number]):
                    self.content[page_number][page_line-1] += content
                    return self.content[page_number][page_line-1]

        return False

    def clear(self,page_number,first_line = 1, last_line = 1):
        if page_number in self.content.keys():
            if first_line >= 1 and last_line <= self.lines:
                for m in range(len(self.content[page_number])):
                    if m + 1 >= first_line and m + 1 <= last_line:
                        self.content[page_number][m] = ''
                return True
        return False

    def read_line(self,page_number,line):
        if page_number in self.content.keys():
            if line >= 1 and line <= self.lines:
                return self.content[page_number][line-1]
        return False
        
    def read_lines(self,page_number,first_line = 1, last_line = 1):
        if page_number in self.content.keys():
            if first_line >= 1 and last_line <= self.lines:
                lines = []
                for key,value in self.content.items():
                    if key == page_number:
                        for j in range(len(value)):
                            if j >= first_line-1 and j <= last_line-1:
                                lines.append(value[j])
                return lines
        return False

    def __str__(self):
        return 'Number of pages: ' + str(self.pages) + ', Number of lines per page: '+ str(self.lines) + ', Contents: (' + (str(self.content)[1:-1]) + ')'
