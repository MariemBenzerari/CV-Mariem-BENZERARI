const cvData = {
  personalInfo: {
    name: "Mariem Benzerari",
    location: "Nice, France",
    email: "mariem.benzerari@live.fr",
    phone: "+33621446252",
    linkedIn: "https://linkedin.com/in/mariem-benzerari"
  },
  experiences: [
    {
      role: "Hotel Account Executive | HRS Group",
      dates: "Août 2018 - Présent",
      location: "Paris, France",
      description: [
        "Pilotage et gestion d’un portefeuille de fournisseurs clés (top hôtels indépendants et chaînes régionales).",
        "Assurer l'optimisation de leurs revenus et leur visibilité sur la plateforme HRS.",
        "Préparation et présentation régulières de revues commerciales fondées sur des analyses de KPI (couverture, positionnement, prix, disponibilité, RFP, produits HRS).",
        "Proposition de solutions personnalisées basées sur le framework HRS 5S pour répondre aux besoins des clients et accroître la part de marché des fournisseurs."
      ]
    },
    {
      role: "Hotel Account Manager | HRS Group",
      dates: "Décembre 2016 - Juillet 2018",
      location: "Paris, France",
      description: [
        "Responsable des relations hôtelières pour des chaînes d'hôtels indépendants et régionales.",
        "Gestion des partenariats de la contractualisation à la mise en ligne sur la plateforme HRS.",
        "Réalisation des mappings avec les channel managers et connectivité via GDS, Booking, EAN."
      ]
    },
    {
      role: "Assistant Manager | ACCOR",
      dates: "Avril 2015 - Mars 2016",
      location: "Serre Chevalier, France",
      description: [
        "Gestion des opérations hôtelières et formation d’équipes.",
        "Pilotage de projets transversaux liés à la gestion de l’établissement.",
        "Optimisation des coûts et analyse des KPI."
      ]
    }
  ],
  education: [
    {
      degree: "BTS Assistante Manager",
      school: "CCI Hautes Alpes",
      year: "2016-2017"
    },
    {
      degree: "Baccalauréat Économique et Social",
      school: "Lycée Honoré d'Estiennes d'Orves",
      year: "2006-2007"
    }
  ],
  skills: [
    "Gestion de projets",
    "Analyse de données",
    "Business Development",
    "Technologies Digitales",
    "Voyages Responsables"
  ],
  languages: [
    "Français",
    "Anglais"
  ],
  interests: [
    "Technologies Digitales",
    "Voyages responsables"
  ]
};

function displayCV(cv) {
  const cvContent = document.getElementById("cv-content");

  let content = `<h2>Informations personnelles</h2>
    <p><strong>Nom :</strong> ${cv.personalInfo.name}</p>
    <p><strong>Localisation :</strong> ${cv.personalInfo.location}</p>
    <p><strong>Email :</strong> <a href="mailto:${cv.personalInfo.email}">${cv.personalInfo.email}</a></p>
    <p><strong>Téléphone :</strong> <a href="tel:${cv.personalInfo.phone}">${cv.personalInfo.phone}</a></p>
    <p><strong>LinkedIn :</strong> <a href="${cv.personalInfo.linkedIn}" target="_blank">Profil LinkedIn</a></p>`;

  content += `<h2>Expériences professionnelles</h2>`;
  cv.experiences.forEach((exp) => {
    content += `<div class="section">
      <p><strong>Rôle :</strong> ${exp.role}</p>
      <p><strong>Dates :</strong> ${exp.dates}</p>
      <p><strong>Lieu :</strong> ${exp.location}</p>
      <ul>`;
    exp.description.forEach((task) => {
      content += `<li>${task}</li>`;
    });
    content += `</ul></div>`;
  });

  content += `<h2>Éducation</h2>`;
  cv.education.forEach((edu) => {
    content += `<div class="section">
      <p><strong>${edu.degree}</strong></p>
      <p>${edu.school}, ${edu.year}</p>
    </div>`;
  });

  content += `<h2>Compétences</h2><ul>`;
  cv.skills.forEach((skill) => {
    content += `<li>${skill}</li>`;
  });
  content += `</ul>`;

  content += `<h2>Langues</h2><ul>`;
  cv.languages.forEach((language) => {
    content += `<li>${language}</li>`;
  });
  content += `</ul>`;

  content += `<h2>Centres d’intérêt</h2><ul>`;
  cv.interests.forEach((interest) => {
    content += `<li>${interest}</li>`;
  });
  content += `</ul>`;

  cvContent.innerHTML = content;
}

displayCV(cvData);
