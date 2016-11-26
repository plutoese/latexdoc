# coding = UTF-8

from libs.class_latexfromtemplate import LatexFromTemplate
from libs.class_article import Article


# Template
TEMPLATE = 'E:/github/latexdoc/latexdoc/template/academicjournal/{}/{}'
TEX_FILE = 'pluto_doc.tex'
PDF_FILE = 'pluto_doc.pdf'

# template path setup
template_path = 'f1000'
template_file = 'main_copy.tex'

doc_template = TEMPLATE.format(template_path,template_file)
doc_tex = TEMPLATE.format(template_path,TEX_FILE)
doc_pdf = TEMPLATE.format(template_path,PDF_FILE)

'''
# to generate tex and pdf from the template
docu = LatexFromTemplate(tex_template=doc_template)
docu.document.generate_tex(doc_tex)
docu.document.generate_pdf(doc_pdf)'''

replace_word = {'articleTitle':'计量经济学',
                'arcticleabstract':'经济研究的论文集'}

doc = Article(doc_template,replace_word)
'''
doc.document.append("SomeThing")
doc.document.add_section("我的第三级章节",3)
doc.document.add_section("我的第二级章节",2)
doc.document.add_section("我的第三级章节2",3)
doc.document.add_list(['我的列表','你的列表'],type=2)
doc.document.add_table([['变量', '第一产业占GDP的比重_(全市)', '第一产业占GDP的比重_$市辖区','我错了'],[1,2,3,4],[5,6,7,8]])
doc.document.add_pretty_table(data=[['name','gender','age'],['Tom','Male',24],['Marry','Female',19]])'''
doc.document.generate_tex(doc_tex)
doc.document.generate_pdf(doc_pdf)