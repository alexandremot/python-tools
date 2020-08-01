
import os
import win32com.client as win32


directory = os.getcwd()
dir_files = os.listdir()
word_file = 'test.docx'
path = os.path.join(directory, word_file)

# frame proprieties (9:16 ascpet ratio)
frame_width = 202.5
frame_height = 360

# table proprieties
cell_row = 1
cell_column = 1
total_column = 1
total_row = 1


word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = True
doc = word.Documents.Open(path)

def insert_new_page():

    global range
    global table

    # pointer to the document start
    range = doc.Range()
   
    # collapse the range so we point at the end
    range.Collapse(win32.constants.wdCollapseEnd)
   
    # insert a hard page break
    range.InsertBreak(win32.constants.wdPageBreak)

    range.ParagraphFormat.Alignment = win32.constants.wdAlignParagraphCenter

    table = doc.Tables.Add(range, total_row, total_column)
    table.Borders.Enable = False


# loop through all the files and folders for adding pictures
for each in dir_files:

    index = dir_files.index(each)

    if os.path.isfile(each):

        if each[-3::1].upper() == 'PNG':

            insert_new_page()    

            # formatting the style of each
            cell_range = table.Cell(cell_row, cell_column).Range
            cell_range.ParagraphFormat.LineSpacingRule = win32.constants.wdLineSpaceSingle
            cell_range.ParagraphFormat.SpaceBefore = 0
            cell_range.ParagraphFormat.SpaceAfter = 3
            
            # this is where we are going to insert the images
            path = os.path.join(directory, each)
            current_pic = cell_range.InlineShapes.AddPicture(path)
            
			# changing the size of each image to fit the table cell
            current_pic.Height = frame_height
            current_pic.Width = frame_width

            # putting a name underneath each image which can be
            table.Cell(cell_row, cell_column).Range.InsertAfter("\n evidência " + str(index))