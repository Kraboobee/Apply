'''
This program takes user input to generate a custom cover letter for a given job posting
'''

# This paragraph contains placeholders for the position, company name, and the site where the job was posted
intro_template      = "Good day, \n\nMy name is Kaamraan and I am a software developer with 3 years of experience in Python and Java.  I would like to apply for the position of {position} at {company}, as advertised on {site}. \n\n"

# This is the main body of the cover letter
body                = "I am a graduate of HyperionDev's 3-month Software Engineering Bootcamp, during which I received praise from mentors for my elegant solutions and excellent documentation. I also have experience with the Django web framework, React, and technologies such as Linux and Github.\n\nCurrently I am focusing on learning more about IOT Development and Edge Computing.\n\n"

# This includes the conclusion and salutation
conclusion  =        "I look forward to hearing from you.\n\nKind regards,\nKaamraan Raboobee"

def apply():
    
    '''
    This is the function which runs on input of "python apply()" in terminal
    '''
    
    # Relevant variables taken through user input
    this_position  = input("Position: ")
    this_company   = input("Company: ")
    this_site      = input("Site: ")
    
    # Formats variables into final intro
    intro = intro_template.format(position  = this_position, 
                          company   = this_company,
                          site      = this_site)
    
    # File will be saved as company_name.txt
    file_name = "{fname}.txt".format(fname = this_company)
    
    # Creates file with this name
    file = open(file_name, "w+")
    
    # Writes all paragraphs to file
    L = [intro, body, conclusion]
    file.writelines(L) 
    
    # Closes file
    file.close()
    
    # Notifies user that file has been saved
    print("\nFile Saved")
    
# Runs the function    
apply() 