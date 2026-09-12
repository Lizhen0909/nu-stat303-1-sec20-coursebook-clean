"""Build a Canvas Classic QTI 1.2 import from the instructor quiz draft.

Uses Canvas's question_type metadata, including file_upload_question.
Reference: instructure/canvas-lms, lib/cc/qti/{qti_items,qti_generator}.rb.
"""
from pathlib import Path
from html import escape
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED

BASE = Path(__file__).resolve().parent
SOURCE = (BASE / 'chapter02-quiz.md').read_text()
TITLE = 'Chapter 2 Quiz: Your Python Environment and Project Files'
IDENT = 'stat303_chapter02_quiz_v1'
LINK = 'https://lizhen0909.github.io/nu-stat303-1-sec20-coursebook-clean/python_venv.html#practice-activity-find-your-python-and-your-data'
QTI = 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2'
CP = 'http://www.imsglobal.org/xsd/imscp_v1p1'
CANVAS = 'http://canvas.instructure.com/xsd/cccv1p0'

def child(parent, tag, text=None, **attrs):
    e = ET.SubElement(parent, tag, attrs)
    if text is not None:
        e.text = str(text)
    return e

def html(text):
    text = escape(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return '<p>' + text + '</p>'

def field(parent, name, value):
    f = child(parent, 'qtimetadatafield')
    child(f, 'fieldlabel', name)
    child(f, 'fieldentry', value)

def material(parent, markup):
    child(child(parent, 'material'), 'mattext', markup, texttype='text/html')

def xml(root):
    ET.indent(root, space='  ')
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)

root = ET.Element('questestinterop', xmlns=QTI)
assessment = child(root, 'assessment', ident=IDENT, title=TITLE)
section = child(assessment, 'section', ident='root_section')
blocks = re.findall(r'### Question (\d+) — (.*?) \(1 point\)\n\n(.*?)(?=\n### Question|\n## Question 5)', SOURCE, re.S)
assert len(blocks) == 4
correct = []
for number, title, block in blocks:
    item = child(section, 'item', ident=f'{IDENT}_q{number}', title=f'Question {number}: {title}')
    meta = child(child(item, 'itemmetadata'), 'qtimetadata')
    field(meta, 'question_type', 'multiple_choice_question')
    field(meta, 'points_possible', '1')
    options = re.findall(r'^\*\*([A-D])\.\*\* (.+)$', block, re.M)
    assert len(options) == 4
    field(meta, 'original_answer_ids', ','.join(letter for letter, _ in options))
    presentation = child(item, 'presentation')
    material(presentation, html(block.split('**A.**')[0].strip()))
    choices = child(child(presentation, 'response_lid', ident='response1', rcardinality='Single'), 'render_choice')
    answers = []
    for letter, text in options:
        if '**(Correct answer)**' in text:
            answers.append(letter)
        text = text.replace(' **(Correct answer)**', '')
        material(child(choices, 'response_label', ident=letter), html(text))
    assert len(answers) == 1
    correct.append(answers[0])
    processing = child(item, 'resprocessing')
    child(child(processing, 'outcomes'), 'decvar', varname='SCORE', vartype='Decimal', minvalue='0', maxvalue='100')
    condition = child(processing, 'respcondition', **{'continue': 'No'})
    child(child(condition, 'conditionvar'), 'varequal', answers[0], respident='response1')
    child(condition, 'setvar', '100', action='Set', varname='SCORE')
assert correct == ['D', 'A', 'B', 'D']

item = child(section, 'item', ident=f'{IDENT}_q5', title='Question 5: Upload Your Activity 2 HTML Report')
meta = child(child(item, 'itemmetadata'), 'qtimetadata')
field(meta, 'question_type', 'file_upload_question')
field(meta, 'points_possible', '16')
field(meta, 'original_answer_ids', '')
material(child(item, 'presentation'), f'<p>Submit one file: <code>activity02.html</code>.</p><p>Upload the HTML prepared by following the <a href="{LINK}">Chapter 2 Practice Activity instructions</a>. Grading follows the criteria listed there.</p>')
# Canvas exports file-upload questions with metadata, presentation, and outcomes;
# no text-response control and no automatic scoring condition.
child(child(child(item, 'resprocessing'), 'outcomes'), 'decvar', varname='SCORE', vartype='Decimal', minvalue='0', maxvalue='100')

metadata = ET.Element('quiz', identifier=IDENT, xmlns=CANVAS)
for key, value in {
    'title': TITLE,
    'description': f'<p>Complete <a href="{LINK}">Chapter 2’s Practice Activity</a> before answering the quiz. That chapter section contains the complete activity and HTML preparation instructions.</p><p>You may consult Chapter 2, your notebook, and your terminal. Choose one best answer for each MCQ, then upload your HTML report. Total: 20 points (four MCQs at 1 point each; upload at 16 points).</p>',
    'shuffle_answers': 'false',
    'quiz_type': 'assignment',
    'points_possible': '20',
    'show_correct_answers': 'false',
    'available': 'false',
}.items():
    child(metadata, key, value)

manifest = ET.Element('manifest', identifier=f'{IDENT}_package', xmlns=CP)
child(manifest, 'organizations')
resources = child(manifest, 'resources')
resource = child(resources, 'resource', identifier=IDENT, type='imsqti_xmlv1p2')
child(resource, 'file', href=f'{IDENT}/assessment.xml')
child(resource, 'dependency', identifierref=f'{IDENT}_metadata')
resource = child(resources, 'resource', identifier=f'{IDENT}_metadata', type='associatedcontent/imscc_xmlv1p1/learning-application-resource', href=f'{IDENT}/assessment_meta.xml')
child(resource, 'file', href=f'{IDENT}/assessment_meta.xml')

out = BASE / 'chapter02-canvas-quiz.zip'
with ZipFile(out, 'w', ZIP_DEFLATED) as z:
    z.writestr('imsmanifest.xml', xml(manifest))
    z.writestr(f'{IDENT}/assessment.xml', xml(root))
    z.writestr(f'{IDENT}/assessment_meta.xml', xml(metadata))

# Validate package references, question types, points, answer IDs and visible text.
with ZipFile(out) as z:
    assert z.testzip() is None
    ns = {'q': QTI, 'c': CP}
    m = ET.fromstring(z.read('imsmanifest.xml'))
    for f in m.findall('.//c:file', ns):
        assert f.attrib['href'] in z.namelist()
    a = ET.fromstring(z.read(f'{IDENT}/assessment.xml'))
    items = a.findall('.//q:item', ns)
    assert len(items) == 5
    total = 0
    for i, it in enumerate(items):
        fields = {f.find('q:fieldlabel', ns).text: f.find('q:fieldentry', ns).text for f in it.findall('.//q:qtimetadatafield', ns)}
        total += int(fields['points_possible'])
        if i < 4:
            assert fields['question_type'] == 'multiple_choice_question'
            assert len(it.findall('.//q:response_label', ns)) == 4
            assert it.find('.//q:varequal', ns).text == correct[i]
        else:
            assert fields['question_type'] == 'file_upload_question'
            assert it.find('.//q:respcondition', ns) is None
    assert total == 20
    for mat in a.findall('.//q:mattext', ns):
        assert 'Correct answer' not in (mat.text or '')
print(f'Created {out.name}: 4 MCQs + 1 file upload, 20 points; structural checks passed.')
