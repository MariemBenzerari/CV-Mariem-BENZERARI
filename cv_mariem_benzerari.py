# Candidature en code : Mariem Benzerari - Stage Full Stack (Java/JavaScript) chez SAP Labs

class Candidate:
    def __init__(self, name, location, email, phone, linkedin, stage_title, education, experiences, skills, languages, achievements, interests, motivation):
        self.name = name
        self.location = location
        self.email = email
        self.phone = phone
        self.linkedin = linkedin
        self.stage_title = stage_title
        self.education = education
        self.experiences = experiences
        self.skills = skills
        self.languages = languages
        self.achievements = achievements
        self.interests = interests
        self.motivation = motivation

    # Introduction : Qui suis-je ?
    def introduce(self):
        intro = (f"Bonjour Erik Marcadé,\n\n"
                 f"Je m'appelle {self.name}. Actuellement Hotel Account Executive chez HRS Group à Paris, "
                 f"je suis à la recherche d'un stage de {self.stage_title} pour élargir mes compétences techniques dans le développement Full Stack (Java/JavaScript). "
                 f"J’ai plus de 7 ans d’expérience dans la gestion de relations B2B et l’optimisation de programmes de voyage dans des sociétés diversifiées. "
                 f"Mon expertise en gestion de projet et en adoption de solutions SaaS, combinée à ma passion pour les technologies, fait de moi une candidate motivée "
                 f"pour rejoindre une entreprise innovante comme SAP Labs.")
        return intro

    # Motivation spécifique pour SAP Labs
    def show_motivation(self):
        return (f"Je suis particulièrement attirée par SAP Labs car cette entreprise est reconnue pour son leadership en innovation "
                f"et ses initiatives dans la transformation digitale. Je souhaite contribuer à des projets qui ont un impact à grande échelle, "
                f"tout en continuant à développer mes compétences en Java/JavaScript et en développement Full Stack dans un environnement agile et stimulant.")

    # Informations de contact
    def contact_info(self):
        return f"Localisation : {self.location}\nEmail : {self.email}\nTéléphone : {self.phone}\nLinkedIn : {self.linkedin}"

    # Expériences professionnelles
    def show_experiences(self):
        exp_details = "\n".join([f"- {exp['role']} chez {exp['company']} ({exp['dates']})\n  {exp['summary']}" for exp in self.experiences])
        return f"Expériences professionnelles :\n{exp_details}"

    # Compétences clés
    def show_skills(self):
        skills_list = "\n".join(self.skills)
        return f"Compétences techniques et professionnelles :\n{skills_list}"

    # Langues parlées
    def show_languages(self):
        return f"Langues maîtrisées : {', '.join(self.languages)}."

    # Réalisations clés
    def show_achievements(self):
        achievements_list = "\n".join(self.achievements)
        return f"Réalisations clés :\n{achievements_list}"

    # Formation académique
    def show_education(self):
        edu_details = "\n".join([f"- {edu['degree']} : {edu['institution']} ({edu['dates']})" for edu in self.education])
        return f"Formation académique :\n{edu_details}"

    # Centres d'intérêt
    def show_interests(self):
        interests_list = "\n".join(self.interests)
        return f"Centres d'intérêts :\n{interests_list}"

# Création de la candidature de Mariem Benzerari avec éléments enrichis
mariem = Candidate(
    name="Mariem Benzerari",
    location="Nice, France",
    email="mariem.benzerari@live.fr",
    phone="+33621446252",
    linkedin="LinkedIn: Cliquez ici Mariem Benzerari",
    stage_title="Développeuse Full Stack (Java/JavaScript)",
    education=[
        {"degree": "BTS Assistante Manager", "institution": "CCI Hautes Alpes", "dates": "2016-2017"},
        {"degree": "Baccalauréat Économique et Social", "institution": "Lycée Honoré d'Estiennes d'Orves", "dates": "2006-2007"}
    ],
    experiences=[
        {"role": "Hotel Account Executive", "company": "HRS Group", "dates": "Août 2018 - Présent", 
         "summary": "Pilotage d'un portefeuille de suppliers clés, analyse de KPI, optimisation des revenus et adoption de solutions SaaS pour améliorer la visibilité des hôtels sur la plateforme HRS."},
        {"role": "Hotel Account Manager", "company": "HRS Group", "dates": "Décembre 2016 - Juillet 2018", 
         "summary": "Gestion des partenariats, analyse de performance, upselling stratégique et lancement de nouveaux produits SaaS 'Connect'."},
        {"role": "Assistant Manager", "company": "ACCOR", "dates": "Avril 2015 - Mars 2016", 
         "summary": "Gestion des opérations hôtelières, formation des équipes, et mise en place de solutions innovantes pour l'optimisation des coûts."}
    ],
    skills=[
        "Gestion de projet",
        "Analyse de données (KPI, RFP, positionnement concurrentiel)",
        "Développement commercial (Upselling stratégique, négociation)",
        "Solutions SaaS (Procure2Stay, Connect)",
        "Gestion des partenariats (Connectivité via GDS, Booking, EAN)",
        "Résolution de problèmes",
        "Leadership et management",
        "Apprentissage actuel : JavaScript, Java, développement Full Stack"
    ],
    languages=["Français", "Anglais"],
    achievements=[
        "Top vendeuse Market place EMEA 2020",
        "100% des chaînes gérées au label Green Stay",
        "Réduction des coûts de voyage de 7% grâce à des programmes optimisés",
        "Lancement réussi de produits SaaS 'Connect'",
        "Amélioration de la conformité des programmes de voyage"
    ],
    interests=[
        "Technologies digitales",
        "Voyages responsables",
        "Transformation digitale",
        "Innovation dans le secteur du voyage"
    ],
    motivation="SAP Labs représente pour moi une opportunité unique d'apprendre dans un environnement où l'innovation est au cœur des projets."
)

# Présentation
print(mariem.introduce())

# Motivation pour SAP Labs
print(mariem.show_motivation())

# Informations de contact
print(mariem.contact_info())

# Expériences professionnelles
print(mariem.show_experiences())

# Compétences clés
print(mariem.show_skills())

# Langues
print(mariem.show_languages())

# Réalisations clés
print(mariem.show_achievements())

# Formation académique
print(mariem.show_education())

# Centres d'intérêt
print(mariem.show_interests())

# Conclusion
print("\nMerci pour votre attention, j'espère avoir l'opportunité de discuter avec vous au sujet de ce stage et des possibilités chez SAP Labs !")
