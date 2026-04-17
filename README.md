<div align="center">

# 🌍 GoGlobe

### *Find your perfect country to call home.*

**A full-stack travel platform that helps users discover the most suitable country to relocate to — based on personal preferences, life goals, and real-world data.**

---

![Angular](https://img.shields.io/badge/Frontend-Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)
![Django](https://img.shields.io/badge/Backend-Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/API-DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

![Status](https://img.shields.io/badge/status-in%20development-yellow?style=flat-square)
![License](https://img.shields.io/badge/license-Educational-blue?style=flat-square)
![Made with love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red?style=flat-square)

</div>

---

## ✈️ About the Project

**GoGlobe** is a modern web platform for people who dream of living abroad but don't know where to start. Whether you're a student, a professional, or just someone chasing a better life — GoGlobe helps you explore countries, compare relocation options, and make the decision with confidence.

Built as a full-stack application with **Angular** on the client side and **Django + DRF** on the server side.

---

## 🎯 Who Is It For?

> *"Choosing a country shouldn't feel like guessing."*

- 🎓 **Students** looking for the best country to study in
- 💼 **Professionals** seeking better career opportunities abroad
- 🧳 **Future migrants** exploring long-term relocation
- ✨ **Travelers** who want structured, data-driven guidance

---

## 🚀 Main Features

| Category | Features |
|----------|----------|
| 🔍 **Discovery** | Smart country search based on preferences |
| ⚖️ **Comparison** | Side-by-side country comparison |
| 📋 **Information** | Visa, migration, and legal details |
| 💰 **Finance** | Cost of living overview |
| 🎓 **Opportunities** | Jobs, education, and career paths |
| 🌤 **Lifestyle** | Climate, language, and cultural insights |
| 🔐 **Auth** | Secure user registration with JWT |
| ⭐ **Personalization** | Tailored recommendations for each user |

---

## 🖥️ Front-End Architecture *(Angular)*

The Angular client is designed around clarity, modularity, and clean API communication.

**Key implementations:**
- 🧩 Services and interfaces for API interaction
- 🖱️ At least **4 click events** triggering API requests
- 📝 At least **4 form controls** using `[(ngModel)]`
- 🎨 Custom CSS styling for every component
- 🧭 Routing module with **3+ named routes**
- 🔁 `@for` loops and `@if` conditional rendering
- 🔐 JWT authentication with HTTP interceptor
- 🚪 Login / Logout flow
- 🌐 Angular `HttpClient` service layer
- ⚠️ Graceful API error handling

---

## ⚙️ Back-End Architecture *(Django + DRF)*

A clean, scalable REST API built with best practices in mind.

**Key implementations:**
- 🗂 **4+ models** with relational integrity
- 🔗 **2+ ForeignKey** relationships
- 🧵 **2 serializers** using `serializers.Serializer`
- 🧶 **2 serializers** using `serializers.ModelSerializer`
- 🛠 **2 Function-Based Views** (FBV)
- 🏗 **2 Class-Based Views** (CBV) via `APIView`
- 📡 REST endpoints fully integrated with the front-end

---

## 🧱 Planned Data Models

```
User  ──┬──▶  FavoriteCountry  ──▶  Country
        │                             │
        └──▶  Review                  ├──▶  Category
                                      ├──▶  VisaInfo
                                      └──▶  RelocationOption
```

- **User** — profile and authentication
- **Country** — core country data
- **Category** — country groupings (e.g. Europe, Asia, etc.)
- **RelocationOption** — study, work, family, investment
- **VisaInfo** — visa types and requirements
- **Review** — user feedback on countries
- **FavoriteCountry** — saved destinations per user

---

## 🛠 Tech Stack

<table>
<tr>
<td valign="top" width="33%">

### 🎨 Front-End
- Angular
- TypeScript
- HTML5
- CSS3

</td>
<td valign="top" width="33%">

### ⚙️ Back-End
- Django
- Django REST Framework
- Python

</td>
<td valign="top" width="33%">

### 🧰 Tools
- Git & GitHub
- Postman
- VS Code

</td>
</tr>
</table>

---

## 👥 Team

| Name | Role |
|------|------|
| **Atimbekova Yenlik** | Full-stack Developer |
| **Symbat Mukhamedkarim** | Full-stack Developer |
| **Inkar Bakhytkali** | Full-stack Developer |

---

## 📍 Project Status

> 🚧 **In active development**

- [x] Repository initialized
- [x] README documented
- [x] Angular project template created
- [ ] Django backend scaffolding
- [ ] Authentication flow
- [ ] Core features (search, compare, details)
- [ ] Final integration & testing

---

## 🎓 Purpose

This project is built for **educational purposes** as part of a university full-stack development course — combining theoretical knowledge with real-world engineering practices.

---

<div align="center">

### 🌐 *"The world is big. Let's find your place in it."*


</div>

# CountryfitFrontend

This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 19.2.20.

## Development server

To start a local development server, run:

```bash
ng serve
```

Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Karma](https://karma-runner.github.io) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
