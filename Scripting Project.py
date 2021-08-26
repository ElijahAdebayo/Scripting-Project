import docx

doc = docx.Document(r"C:\Users\ElijahAdebayo\OneDrive - NetImpact Strategies, Inc\Documents\Tara Scripting\AIMMS_PPON_2021_05_21.docx")
single_para = doc.paragraphs[4]
print(single_para.text)