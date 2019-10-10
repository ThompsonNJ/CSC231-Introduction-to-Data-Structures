from Stacklinked import Stack
import time

stack = Stack()


# filename: a string containing a filename. Appropriate for use in an open() call.
def process_tags(filename):
    balanced = True
    with open(filename) as file:
        for line in file.readlines():
            opening_left = None
            closing_left = None

            for i in range(len(line)):
                if line[i] == '<' and line[i+1] != '/':
                    if line[i + 2] == ' ':
                        stack.push(line[i:i+3])
                        opening_left = None

                    else:
                        opening_left = i

                elif line[i] == '<' and line[i+1] == '/':
                    closing_left = i

                elif line[i] == '>':
                    if opening_left is None and closing_left is not None:
                        closing_right = i
                        close_tag = line[closing_left: closing_right + 1]
                        try:
                            if stack.is_empty():
                                raise ValueError
                            else:
                                opening_tag_check = stack.pop()
                                
                        except ValueError:
                                print("Cannot pop when stack is empty")
                        try:
                            if close_tag[2: -1] != opening_tag_check[1: -1]:                                
                                balanced = False
                                raise ValueError

                        except ValueError:
                            print("Closing tags do not match! ({} != {})".format(close_tag[2: -1],
                                                                                 opening_tag_check[1: -1]))

                        closing_left = None

                    elif opening_left is not None and closing_left is None:
                        opening_right = i
                        open_tag = line[opening_left: opening_right+1]
                        stack.push(open_tag)
                        opening_left = None

        if not stack.is_empty():
            balanced = False

        return balanced
    
def format_time(t):
    if t > 1:
        return '{:.1f}s'.format(t)
    if t * 1000 > 1:
        return '{:.1f}ms'.format(t * 1000)
    if t * 1000000 > 1:
        return '{:.1f}{:}s'.format(t * 1000000, u'\u03BC')
    return '<1{:}s'.format(u'\u03BC')
    
start = time.time()

if __name__ == '__main__':
    if process_tags('EC1.html'):
        print('All tags are matched!', format_time(time.time()-start))
    else:
        print('The HTML tags do not match!', format_time(time.time()-start))
