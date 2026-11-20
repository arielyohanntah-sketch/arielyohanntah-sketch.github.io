import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage

pdf_path = os.path.abspath('assets/CV_Ariel_Tah.pdf')
photo_path = os.path.abspath('assets/images/profile.png')

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    leftMargin=36,
    rightMargin=36,
    topMargin=32,
    bottomMargin=32
)

styles = getSampleStyleSheet()

PRIMARY = colors.HexColor('#0f172a')   # Bleu nuit profond
SECONDARY = colors.HexColor('#0d9488') # Teal / Turquoise élégant
TEXT_MAIN = colors.HexColor('#1e293b') # Texte principal
TEXT_MUTED = colors.HexColor('#475569')# Texte secondaire

meta_style = ParagraphStyle(
    'MetaStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12.2,
    textColor=TEXT_MUTED
)

section_title_style = ParagraphStyle(
    'SectionTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10.5,
    leading=13.5,
    textColor=PRIMARY
)

body_style = ParagraphStyle(
    'BodyStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.8,
    textColor=TEXT_MAIN
)

item_header_style = ParagraphStyle(
    'ItemHeader',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=12,
    textColor=PRIMARY
)

elements = []

# En-tête : Photo + Infos
img_cell = ''
if os.path.exists(photo_path):
    img_cell = RLImage(photo_path, width=72, height=88)

info_lines = [
    '<b><font size="16" color="#0f172a">GUELASSÉ ARIEL YOHANN MONDÉSIR TAH</font></b>',
    '<font size="10" color="#0d9488"><b>Étudiant en Génie Logiciel — Développeur Mobile, Logiciel & Web</b></font>',
    '<font size="8.2" color="#475569"><b>Institut Ivoirien de Technologie (IIT)</b> | Localisation : Abidjan / Grand-Bassam, CI</font>',
    '<font size="8.2" color="#475569">Email : <a href="mailto:taharielyohann@gmail.com"><u>taharielyohann@gmail.com</u></a> | LinkedIn : <a href="https://www.linkedin.com/in/guelassé-ariel-yohann-mondésir-tah-b823193b1"><u>linkedin.com/in/ariel-tah</u></a></font>',
    '<font size="8.2" color="#475569">GitHub : <a href="https://github.com/arielyohanntah-sketch"><u>github.com/arielyohanntah-sketch</u></a> | Portfolio : <a href="https://arielyohanntah-sketch.github.io"><u>arielyohanntah-sketch.github.io</u></a></font>'
]

info_paragraph = Paragraph('<br/>'.join(info_lines), meta_style)

header_table = Table([[img_cell, info_paragraph]], colWidths=[80, 440])
header_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
elements.append(header_table)
elements.append(Spacer(1, 8))

def add_section_header(title):
    t = Table([[Paragraph(f'<b><font color="#0d9488">//</font> {title.upper()}</b>', section_title_style)]], colWidths=[520])
    t.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 1.2, SECONDARY),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    return t

# 1. PROFIL
elements.append(add_section_header('Profil Personnel'))
profile_txt = Paragraph(
    'Étudiant rigoureux et curieux en 2ème année de Licence en Génie Logiciel à l\'<b>Institut Ivoirien de Technologie (IIT)</b>. '
    'Passionné par le développement d\'applications et la résolution méthodique de problèmes, je combine la programmation '
    'mobile (Flutter), les applications de bureau interconnectées aux bases relationnelles (C#, SQL Server, MySQL), '
    'le traitement de données en Python et l\'intégration quotidienne des technologies d\'Intelligence Artificielle. '
    'Doté d\'un excellent relationnel et d\'un fort esprit d\'équipe, je recherche activement une opportunité de stage pratique / projets innovants.',
    body_style
)
elements.append(profile_txt)
elements.append(Spacer(1, 6))

# 2. FORMATION
elements.append(add_section_header('Formation Académique'))
form_txt = Paragraph(
    '<b>Licence en Génie Logiciel (2ème année - L2)</b> — <i>Institut Ivoirien de Technologie (IIT), Grand-Bassam</i><br/>'
    '<font color="#475569">Formation approfondie : Algorithmique, Programmation (C, Python, C#), Technologies Web & Mobile, Modélisation relationnelle (SQL Server, MySQL), Architecture Réseau & Systèmes.</font><br/>'
    '<b>Baccalauréat Scientifique</b> — <i>Enseignement Secondaire</i> [Obtenu]',
    body_style
)
elements.append(form_txt)
elements.append(Spacer(1, 6))

# 3. PROJETS & RÉALISATIONS
elements.append(add_section_header('Projets & Réalisations Pratiques'))
projs = [
    ('Application Mobile « prof-ci »', 'Flutter, Dart, Firebase, Mobile UI/UX',
     'Conception et développement d\'une solution mobile fluide facilitant la mise en relation entre apprenants et enseignants. Intégration de Firebase (Realtime Database & Authentification), structuration du cycle de vie et travail collaboratif.'),
    ('Applications Desktop & Systèmes de Données', 'C#, Windows Forms, SQL Server, MySQL, SSMS',
     'Développement d\'interfaces de bureau interconnectées à des bases relationnelles. Modélisation de schémas, implémentation des opérations transactionnelles (CRUD via ADO.NET) et sécurisation des requêtes contre les injections SQL.'),
    ('Scraping & Automatisation E-Commerce', 'Python, Web Scraping, Parsing DOM, Automatisation',
     'Extraction automatisée de catalogues de données e-commerce sur Amazon. Gestion des requêtes réseau, parsing des balises du DOM et structuration de données brutes en formats exploitables.'),
    ('Analyse Comparative de Marché', 'Python, Data Analytics, Traitement Algorithmique',
     'Scripts d\'exploration et de traitement de données économiques. Calculs de métriques comparatives et conversion de flux bruts en indicateurs clairs facilitant la prise de décision.'),
    ('Système de Gestion de Bibliothèque', 'Python, POO, Conception Modulaire, Persistance',
     'Modélisation logicielle d\'un établissement documentaire appliquant les principes de la POO : catalogue d\'ouvrages, gestion des emprunteurs, suivi des retours et architecture modulaire.')
]

for p_title, p_tags, p_desc in projs:
    elements.append(Paragraph(f'<b>• {p_title}</b> — <font color="#0d9488"><i>{p_tags}</i></font>', item_header_style))
    elements.append(Paragraph(p_desc, body_style))
    elements.append(Spacer(1, 2.5))
elements.append(Spacer(1, 4))

# 4. COMPÉTENCES TECHNIQUES
elements.append(add_section_header('Compétences & Environnements'))
skills_data = [
    [Paragraph('<b>Développement & Mobile :</b>', item_header_style), Paragraph('Flutter, Dart, Python, C# / .NET, Langage C, HTML5, CSS3, Bootstrap, Windows Forms', body_style)],
    [Paragraph('<b>Bases de Données :</b>', item_header_style), Paragraph('Microsoft SQL Server (SSMS), MySQL, SQLite, Firebase (Firestore, Realtime DB)', body_style)],
    [Paragraph('<b>Outils & Environnements :</b>', item_header_style), Paragraph('Git, GitHub, VS Code, Visual Studio Community, PyCharm, Android Studio, Code::Blocks', body_style)],
    [Paragraph('<b>IA & Systèmes Réseaux :</b>', item_header_style), Paragraph('Usage quotidien des outils IA (assistance au code, productivité), Notions réseaux client-serveur, Sens UI/UX', body_style)]
]
skills_table = Table(skills_data, colWidths=[140, 380])
skills_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ('TOPPADDING', (0,0), (-1,-1), 1.5),
]))
elements.append(skills_table)
elements.append(Spacer(1, 6))

# 5. ATOUTS & LANGUES
elements.append(add_section_header('Atouts Personnels & Langues'))
atouts_txt = Paragraph(
    '<b>Savoir-être :</b> Rigueur scientifique, fort esprit d\'équipe, sens du travail bien fait, persévérant, poli, ponctuel et curieux d\'apprendre.<br/>'
    '<b>Langues :</b> Français (Langue maternelle / Courant) | Anglais (Niveau intermédiaire — documentation technique et échanges professionnels).',
    body_style
)
elements.append(atouts_txt)

doc.build(elements)
print('PDF created successfully at:', pdf_path)
