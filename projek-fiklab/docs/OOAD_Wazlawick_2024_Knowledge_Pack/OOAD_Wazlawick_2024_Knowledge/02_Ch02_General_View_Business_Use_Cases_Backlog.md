<!-- Knowledge file: Chapter 2 — General view of the system -->
> **About this file.** Chapter 2 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** General view of the system: early effort estimation, acceptance criteria, project/goal/product structure, product backlog, business use cases, business actors and workers, automation opportunities (SISMOB example).  
> **Use this file when:** defining system scope at the start, writing a product backlog or acceptance criteria, drawing a business use case diagram, or deciding what to automate.  
> **Sections:** 2.1 Introduction to general view of the system (p. 5); 2.2 Early effort estimation (p. 8); 2.3 Acceptance criteria (p. 8); 2.4 Completing the general view of the system (p. 9); 2.5 Product backlog (p. 16); 2.6 Business use cases (p. 18); 2.7 Discussion (p. 25)  
> **Contains:** 9 figures transcribed as text, 0 code listings.

# Chapter 2: General view of the system

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 5*

Key topics in this chapter

- General view of the system

- Early effort estimation

- Product backlog

- Business use case diagram

## 2.1 Introduction to general view of the system

*Chapter 2 · p. 5*

The activities related to the definition of the scope of a project should usually take a relatively small fraction of the time of the whole project, although variations may exist depending on the kind of the project: projects with simple and well-defined requirements (e.g., a vaccination app) may demand no more than a couple of days of business modeling while complex and large projects (e.g., a hospital management system) may demand weeks or months. At the time of scope definition, all information about the organization can be explored by interviewing users, clients, and domain specialists, as well as by the examination of documents, reports, existing systems (desk research), and related bibliography.

For most projects, the first question the team should answer is the following: What is the vision of the organization for the project? In other words, what does the organization want with the project? Why is it being proposed, and why is the organization going to spend money with it? What are the pains of the users in their daily journey? What bothers them? At that moment, another question, often forgotten, may be raised: Buying or developing? Sometimes, the product the client wants is available for purchase.

These questions must be answered in a relatively short time, because, at this time, the client and the development team usually do not have an idea of the real extension of the project and it is, from the point of view of both, an investment on the future and, therefore, a risk.

The general view of the system or executive summary is a free format document, where the team may report the relevant items they discovered about the system after the initial interviews with the stakeholders.

This book does not intend to propose rules for writing that document. But it is suggested that it should not be too long. A few pages of text and some diagrams may be sufficient to describe in a summarized way the scope of most systems. More than that could mean that too much detail was included in the summary. 

7

The scope declaration in the general view should present the products that must be developed, what must be included, and eventually, what could be included but would not. This information may be obtained initially by interviewing the stakeholders and may be refined later with the use of the tools presented in this book.

If possible, the main deliverables of the project should be also defined in the general view as well as the time frame when the client is going to receive some kind of delivery from the development team. Normally, this list of deliverables consists of implemented versions of the software, but the list can also include other items, such as design, manuals, media, training, and documentation.

## 2.2 Early effort estimation

*Chapter 2 · p. 8*

It can be difficult to establish deadlines for deliveries before doing the requirements analysis of the system, because estimation effort techniques such as function points (Albrecht and Gaffney, 1983), use case points (Karner, 1993), or COCOMO II (Boehm, 2000) can generally be applied after a good deal of the requirements is known. Thus the information about deadlines at this early stage can be more a guess than a formal strong commitment for development.

At the Bridge Laboratory, a technique that is obtaining success in early development cost estimation is a variation of the technique known as “expert opinion.” A senior systems specialist known as CXO (Chief Experience Officer) conducts the first contacts with the client to understand the project’s goals and products. This is outlined in a report with three levels, as shown in the UML Object Diagram in Fig. 2–1.

Then, each product, usually an epic, is presented and discussed by an experienced agile team. More than one team may be consulted for the same product if necessary. The team will try to understand the extension, complexity, and risks of each product and produce an effort estimation for each one. This divide-and-conquer technique helps in obtaining a more precise estimation than trying to estimate the whole project at once. In soccer, one probably would miss the goal if trying to kick the ball from the center of the field (neither Pelé could do it). However, with small kicks, one can approach the goal more precisely and convert.

## 2.3 Acceptance criteria

*Chapter 2 · p. 8*

The general view document may also contain some acceptance criteria for the product, that is, quantifiable items that will be used to decide whether the project was a success or not. The product acceptance criteria should at least include metrics for deadlines, budget, and quality.

If subjective criteria such as “customer satisfied,” “system easy to use,” or “state-of-the-art technology” are used, they should be quantified, that is, it should be defined how to measure “customer satisfaction,” “ease of use,” “state of the art,” and so on. Examples of quantifiable acceptance criteria are “the system must support up to 50,000 simultaneous accesses without degrading performance,” “the system must eliminate the need to use paper for performing processes x and y,” “the system must allow any user to send pictures taken from their own smartphone,” and “the system must allow the management of 20,000 works of construction simultaneously.”

**Figure 2–1: Object diagram with the initial three-level structure of a project.** *(p. 9)*

> **Diagram content (transcribed from the figure image):** Composition tree: Project (root) composed of goal 1, goal 2 … goal n; each goal composed of products (product 1.1 … 1.m, product 2.1 … 2.j, product n.1 … n.k). Shows the three-level structure project → goals → products used to organize the general view of the system.

## 2.4 Completing the general view of the system

*Chapter 2 · p. 9*

More information may be added to the general view document if needed (e.g., main risks, technologies to be used). The general view of the system is the base agreement document for the client and the developer. It will be taken as a basis for planning the rest of the project.

It is important to mention that when the general view is being built, the requirements analysis has not yet been completed, and therefore, the information mentioned in the general view consists of early commitments. It is expected that the requirements analysis will detail the scope in depth, but not augment its extension. For example, in requirements analysis, the process of managing construction works may be detailed with propositions, authorizations, assessments, and so on (considering that “managing construction works” is mentioned in the scope declaration), but if the payment roll of the building company was not mentioned in the scope declaration, then the inclusion of that item in the project would require a renegotiation of the scope declaration.

Pressman (2008) proposes some techniques to communicate with stakeholders to discover business goals, for example:

- Traditional focus groups, where a trained analyst meets with a group of end users or people representing their roles.

- Electronic focus groups, where the meetings are conducted using electronic media.

- Iterative surveys, where a few surveys are conducted among end users, presenting them some questions and asking for clarification.

- Exploratory surveys, where exploratory research is conducted among end users that use a similar existing product.

- Scenario building, where a group of end users is led to produce a description of some scenarios for using the system.

The last option seems to be very popular among agile practitioners, where scenarios are sometimes identified as user stories.

Chart 2–1 presents a general view with a preliminary scope declaration for a real project developed by the Bridge Laboratory in 2017^1 . This example will be used often to illustrate some of the modeling techniques within this book.

The contents of this chart are the initial agreement between the development organization and its client. Using it as a basis, a deeper study may be conducted with business use cases and other diagrams, so that the information contained in it is refined, as shown further in this chapter. The document is divided into 10 parts:

- A short summary, as this is the third phase of the project, and many modules were already developed for the other two versions and are known by the client.

- A short presentation of the developing organization.

- The public intended to be using this system.

- The justification for this project and the investment.

- The objective of the project.

- The methodology (agile development) to be used in this project.

- The success indicators used to assess whether the project has achieved its goals.

- A concern about the sustainability of the project.

- The work plan, built in accordance to Fig. 2–1.

- The schedule, considering possible parallelism that can be obtained by using four agile teams for Web (Teams A, B, C, and D), two agile teams for mobile (Teams iOS and Android), one Quality Assurance team, one team specialized in producing media, and three specialized teams at the end of the project.

- A preliminary risk list.

- The lead time of the project.

> *Footnote 1:* This 18-month project was the third phase of a project named SISMOB—Sistema de Monitoramento de Obras (Construction Works Monitoring System) that was developed having the Brazilian Ministry of Health as client and federal, state, and municipal managers, professionals of control organizations, and society in general as users.

CHART 2–1 Example of a general view of the system with its scope declaration.

CHART 2–1 (Continued).

CHART 2–1 (Continued).

CHART 2–1 (Continued).

CHART 2–1 (Continued).

CHART 2–1 (Continued).

After agreeing to this summary with the client, the team may start deepening the knowledge about the client/user needs. In the Bridge case, this document was used to build a contract with the client in order to start the development.

## 2.5 Product backlog

*Chapter 2 · p. 16*

Product backlog is one of the most cherished tools in agile development. It may have different configurations, though. For example, in Kanban (Anderson, 2010), its columns or cells have limits in the number of tasks than can be contained; this happens to avoid many tasks being initiated but not concluded, which could happen because Kanban does not use the concept of sprint as in Scrum and other methods, but continuous development without timeboxes. In Scrum, only a limited number of tasks are selected and must be concluded within the sprint. This avoids the problem of having many unfinished tasks in the backlog.

**Figure 2–2: A product backlog with epics.** *(p. 17)*

> **Diagram content (transcribed from the figure image):** Kanban-style product backlog board with columns Pool, Being analyzed, Being developed, Being revised, Done. Pool cards: 2 Consolidated information module for state and municipal profiles; 7 Citizen App for Android; 8 Citizen App for iOS; 9 Proposal reactivation module; 10 Address change module by the federal manager; 11 Size Change Module; 12 Module for Revocation of Opinions; 13 Technical Research Report; 14 Framework Vaadin Version 8; 15 Tutorial videos about system usage; 16 Documentation of functional requirements and business rules; 17 Software source code; 18 Database modeling. Being analyzed: 1 Consolidated information module for the federal profile (Team A); 3 File generation module with records for payments (Team B); 4 Adaptation and correction of functionalities in the system (QA); 5 Module with the evaluation form in the SISMOB Android App (Android Team); 6 Module with the evaluation form of works in the APP SISMOB iOS (iOS Team). Other columns empty.

Scrum divides the Kanban board into two boards: the product backlog and the sprint backlog. The sprint backlog is used to manage one single sprint (usually 2 weeks of work), while the product backlog is used to manage the whole project (usually several months). This chapter concentrates on the product backlog.

The product backlog may have a different number of columns depending on the team’s needs. One possible and useful configuration is to have the following columns.

- Pool of epics (initialized with all 18 products in the example shown in Chart 2–1).

- Epics being analyzed (epics from the first column are moved here when the team starts studying them—the team may use a schedule, as in the SISMOB example, or deciding on priorities along the project with the client).

- Epics being developed (in this case, the epics may be broken in shorter activities using the 100% rule, that is, the sum of the products of the shorter activities corresponds to 100% of the product of the epic).

- Epics being revised (all work is revised!—after developing the products of the epic, they will be revised as well, preferably by people more experienced).

- Epics done (after revision and acceptance of the products, the epic is considered done).

The 18 products shown in Chart 2–1 may be considered as the epics that will populate the product backlog for the SISMOB project. Fig. 2–2 shows how the product backlog for SISMOB would look a few days after the project started. Notice that different teams are working on different epics, and some epics that will be started later are still in the first column.

Notice also that not every epic in this project consists of the implementation of new features for the system. For example, Product 15 is about producing videos, not software. Product 14 is about upgrading the framework used in the software, and although it is about developing and revising software, it does not imply in the implementation of new features. Those kinds of activities will not be addressed in this book. Instead, we will continue to explore the epics that mean features development or modification.

## 2.6 Business use cases

*Chapter 2 · p. 18*

Jacobson (1994) presents in detail techniques for business modeling with business use cases. In general, in business models, there are entities (people or organizations) external to the target organization, called business actors, and internal entities, called business workers. Business use cases are the processes performed by those actors and workers that allow them to reach some of the company business goals.

The business use case model considers the entire target organization as a system, and the actors may be people, companies, government, or other organizations that create and maintain relationships with the target organization (Kroll and Kruchten, 2003).

The first thing the team must think about when doing business modeling is that what is being modeled is not a software system. An organization is being modeled. Business information is sought from higher-level management people and specialists because they know and sometimes create the organization’s goals.

Most agile teams may prefer to use epic user stories instead of business use cases. In this book, we consider that user stories are written by users while use cases are usually the same stories but refined by analysts. Thus the team may first hear the client and users and identify the important stories and then work on them to refine, obtain more details, correct imperfections, and improve optimization. After that, the user story may be considered as a use case.

The quantity of business use cases that will be identified may be small relatively to the size of the project. A business process is a long-range process that is performed by the organization; think, for example, of one of the main objectives of the SISMOB system that is to manage the development of construction works. Some relatively simpler processes may compose the stages of that larger process, for example, “registering a proposal,” “publish a proposal,” “assess a proposal,” and “deliver money”. The larger process consists of a business use case while the smaller component processes are system use cases, which will be introduced later.

Although UML officially does not have a standard symbol to differentiate business use cases from system use cases, it is usual to represent business use cases with the stereotype «business», or by cutting the use case ellipse with an edge as shown in Fig. 2–3.

In this example, “Manage work” is a business use case because it involves a relationship between the organization (the Ministry of Health) and external entities (such as municipal proponents, external reviewers, citizens), producing a perceptible and consistent result: one construction work is managed from its proposal to its conclusion. This use case possibly will be performed by the external users with the collaboration of some workers inside the organization.

**Figure 2–3: Business use case.** *(p. 19)*

> **Diagram content (transcribed from the figure image):** Two notations for a business use case: an ellipse stereotyped «business» labelled "Manage Work", and the same ellipse with a diagonal slash cut across its edge (alternative business-use-case symbol).

Use case names must be chosen carefully, because at this stage they will summarize critical information about the system, and wrong choices may prevent the team and stakeholders from sharing comprehension about the real intention of business actors and workers. Blain^2 presents some best practices collected from many sources:

- Good use case names reflect user goals. Names such as “Access system” or “Open main window” must be avoided because they reflect technology and not a business goal. Also, names without verbs such as “Invoice” must be avoided because it is not clear what is going to happen to the invoice. Better names might be “Generate invoice,” “Cancel invoice,” “Pay invoice,” etc.

- Good use case names are as short as possible. Although some people may propose that a use case name should not have more than two or three words (or any other number), it is unfeasible to define such a limit because there is a risk of losing clarity on the business goal if the name is too short. As Blain points out, which word could be removed from the name “Collect late payment” without obscuring its meaning? However, that name is better than “Collect late payment from customers that are past due.”

- Good use case names use meaningful verbs. Use case names not only should have strong verbs, but they must be meaningful. A meaningless verb is one that does not make clear what the use case accomplishes; for example, what does a use case such as “Process order” accomplish? What result does it produce? A name such as “Separate ordered items for dispatch” would be more meaningful in that case.

- Good use case names use active voice. As in general writing, active voice is preferable to passive voice. “Pay for order” is better than “Order is paid.”

- Good use case names use present tense. The present tense indicates what the user is trying to do. Past and future tense may sound confusing and unnecessary.

- Good use case names do not identify the actor. As use cases are linked to actors, actors must not be part of their names. Thus a use case name must not identify the actor as in “Manager creates sales report.” Just name the use case as “Create sales report” and link it to a manager and other actors if necessary.

- Good use case names are consistent. The same naming rules and naming conventions should be applied along a project or group of projects. Avoid, for example, naming one use case “Generate sales report” and another “Produce reservations report.” Choose one verb for that meaning and use it consistently.

2 http://tynerblain.com/blog/2007/01/22/how-to-write-good-use-case-names/

**Figure 2–4: Some business use cases found in the example.** *(p. 20)*

> **Diagram content (transcribed from the figure image):** Business use cases found in the SISMOB example (all drawn with the business slash): Monitor work; Report evaluation; Generate file with payment information; Display state and municipal consolidated information; Reactivate canceled proposal; Change address of work; Revoke opinion; Display federal consolidated information.

Additionally, Probasco (2001) proposes that the list of use case names should resemble a to-do list. Thus instead of writing “Cash withdrawal,” “Funds transfer,” and “ATM service,” it would be better to write “Withdraw cash,” “Transfer funds,” and “Service the ATM,” respectively.

Probasco also insists that the meaning of a use case name must be precise. For example, is “Auction” a good use case name? Is it a verb or a noun? If you consider that it is a noun and that a verb must be added, is “Execute auction” a good name? The verb “Execute” would probably be a programmer’s choice, but it probably has no meaning for an auctioneer (Is the auction going to be shot to death?). In this case, an idea would be to hear the user or a domain specialist in order to discover a better name. On the other hand, even if “auction” is indeed a verb, it is not sufficiently clear. Is it the auction of a single item? Is it the auction of a complete set of items? Is it simply an auction participant placing a bid? In that case, names such as “Auction items,” “Auction single item,” or “Place bid” would be clearer.

Fig. 2–4 presents some business use cases that were detected among the 18 products of the SISMOB Phase 3 project. Considering the more general use case of this project that is to manage works from proposal to conclusion, we can observe that some of those use cases are in fact extensions or used by the main use case. The arrows with stereotypes «extend» and «use» may be used to represent extensions and uses, respectively. The difference between them is the following:

- An extension is a use case that can be performed while the main use case is performed, but not mandatorily. The arrow flows from the extension to the main use case.

- A use case includes another if it is a mandatory part of the former. The arrow flows from the main use case to the included use case.

Fig. 2–5 presents the structure of extensions and inclusions of the business use cases for the SISMOB project. As use cases “Display state and municipal consolidated information” and “Display federal consolidated information” are not necessarily performed during the management of a single work, they are not related to “Manage work” by those criteria.

**Figure 2–5: Examples of the use of «extend» and «include».** *(p. 21)*

> **Diagram content (transcribed from the figure image):** Business use case diagram with relationships: Manage work is the central business use case. «include» from Manage work to Report evaluation and to Generate file with payment information. «extend» toward Manage work from Monitor work, Reactivate canceled proposal, Change address of work and Revoke opinion. Display state and municipal consolidated information and Display federal consolidated information stand alone.

On the other side, “Report evaluation,” and “Generate file with payment information” are mandatory parts of the use case “Manage work.” Finally, “Monitor works” (by a citizen), “Reactivate cancelled proposal,” “Change address of work,” and “Revoke opinion” are use cases considered as optional regarding the management of a single work, that is, they can happen or not.

### 2.6.1 Business actors and business workers — 2.6 Business use cases

During business modeling, there are two kinds of actors that must be addressed:

- Business actors: People, organizations, or even systems that perform some activities belonging to the process, but which are not part of the target organization. That is, they are not under the organization’s control. Business actors could be, for instance, customers, publishers, external reviewers, partner companies, or even other automatic systems that the target organization could interact with.

- Business workers:^3 People, organizations, or even systems that perform some activities belonging to the process and that are part of the target organization. They could be the organization’s employees, its departments, or even existing software systems belonging to the organization. Graphically, they are distinguished from business actors by the use of the stereotype «worker».

Examples are shown in Fig. 2–6.

> *Footnote 3:* If we are modeling an organization as a whole, usually business workers do not appear, as they are internal to the company’s system. But if connections between different subsystems of the company are shown, then business workers must appear.

**Figure 2–6: Business actor and business worker.** *(p. 22)*

> **Diagram content (transcribed from the figure image):** Two business-actor symbols (stick figures with the business slash): "Independent Reviewer" (business actor, external) and «worker» "Clerk" (business worker, internal to the organization).

**Figure 2–7: Business actors and business use cases.** *(p. 22)*

> **Diagram content (transcribed from the figure image):** Complete business use case diagram of SISMOB with actors: Citizen — Monitor work; Reviewer — Report evaluation; «worker» Financial clerk — Generate file with payment information; State/Municipality user — Display state and municipal consolidated information; Federal manager — Reactivate canceled proposal, Change address of work, Revoke opinion; Federal user — Display federal consolidated information. Monitor work, Reactivate canceled proposal, Change address of work and Revoke opinion «extend» Manage work; Manage work «use»s Report evaluation and Generate file with payment information.

This differentiation is important because business actors usually cannot be automated, that is, they will not be replaced by computational systems. However, business workers’ roles can possibly be replaced by automatic systems (English, 2007).

Business actors and business workers are linked to the business use cases they participate in by connecting lines without arrows,^4 as shown in Fig. 2–7.

### 2.6.2 Automation opportunities — 2.6 Business use cases

SISMOB is a system that is operated by several actors through the Internet. Before its existence, works funded by the Ministry were managed by using paper and spreadsheets. Considering this situation, the original system had business workers that were basically real people. Some of these workers’ roles were automated. For example, the role of the clerk that sends email to stakeholders after the identification of delays or irregularities was replaced by an automatic messaging system. However, the role of the analysts that assess the works and decide if it is going well or not was not automated. Maybe only artificial intelligence may fill this role in the future.

> *Footnote 4:* Some approaches suggest the use of arrows to indicate whether the actor only receives or sends information to the system. But that practice, besides not being supported by UML 2, brings practically no useful information at this point of the business analysis, because now it is only important to know which use cases really exist, and which actors are involved with them. The details on the interaction will be given later with the activity diagrams that will describe how a business use case is performed.

Not every business worker role will usually be replaced. It depends on the scope of the project and the technology available. A nurse role to measure a patient’s temperature could be replaced by an automatic device, for example.

An advantage in making the business use case diagram, then, is to help in visualizing and making decisions on automation. With the diagram, it is possible to visualize what must stay inside and outside the automation scope, depending on the project’s goals.

Normally, during an automation process within an organization, it is useful to replace at least the workers’ roles that correspond to mere proxies, that is, the ones that simply perform actions in the place of an external actor. In the case of SISMOB, for example, the clerk that only receives an email, prints it, and stores it in the appropriate physical file could be replaced by a system that allows the reviewers to type their own texts on the system.

The association of the business use cases with the organization’s major business goals helps to identify the scope of the system, that is, the activities that will be effectively automated in the project that is being initiated.

The system boundary can be used to identify the set of business use cases and business workers that will be automated, as shown in Fig. 2–8.

**Figure 2–8: System boundary.** *(p. 23)*

> **Diagram content (transcribed from the figure image):** Automation opportunities: a System Boundary box containing Business use case 1, Business use case 2, the «worker» Clerk and Business use case 3. Technician (actor outside) — Business use case 1; «worker» Assessor — Business use case 2; Clerk — Business use case 3 — Reviewer (actor outside). Outside the boundary (not automated): External organization — Business use case 5; Reviewer — Business use case 4.

**Figure 2–9: Using system boundaries to represent a project with many phases.** *(p. 24)*

> **Diagram content (transcribed from the figure image):** Nested release/phase boundaries over use cases numbered 1–13: Phase 1 contains use cases 1, 2, 3; Phase 2a contains Phase 1 plus 4 and 5; Phase 2b contains 6, 7, 8, 9; Phase 3 contains Phase 2a, Phase 2b and use cases 10, 11, 12, 13 (incremental scope growth of the system).

The business use case diagram shows that the automation project will include use cases 1, 2, and 3 and the role of “Clerk.” It also shows that use cases 4 and 5 are not meant to be automated at least for the moment.

Regarding the actors, it can be said that only actors outside the system boundary that own at least one connection to a use case that is inside the boundary are meant to continue to be system actors in the next steps of analysis. This is the case with “Technician,” “Assessor,” and “Reviewer.” The last one will continue to perform business use case 4 as it is done today and will have business use case 3 routines implemented in the new system. As for actor “Clerk,” its role will be automated, and no such actor will exist when the new version of the system is implemented. Finally, actor “External organization” is not associated to any use case that is inside the system boundary, meaning, that this actor will continue to perform business use case 5 the same way as before the implementation of the new system.

If the project, on the other hand, consists of some subprojects or stages, in which different parts of the it would be automated, that could also be indicated by the use of different system boundaries in the diagram: one for each subproject or stage. Fig. 2–9, for example, shows a project that starts with phase 1, by the implementation of use cases 1, 2, and 3. Then, it has two parallel developments: phases 2a and 2b, which will develop use cases 4 and 5 (Phase 2a) and 6, 7, 8, and 9 (Phase 2b). Finally, Phase 3 can be executed by the implementation of use cases 10, 11, 12, and 13.

The next step that leads to the requirements analysis is the detailed study of the business use cases that will be automated. The level of precision and detail depends on the objectives of the project, as already discussed early in this chapter.

## 2.7 Discussion

*Chapter 2 · p. 25*

It is important to remember that the goal of business modeling is usually to find a general view of the business and not a detailed specification of its processes. Thus in most cases, the team’s goal is to concentrate on discovering information about the business and not on formally specifying how the business works as if it was a machine.

Business modeling is not just about building diagrams, however. The purpose of diagrams is to help understand the context and the initial general requirements of a project and a system. Business modeling is one of the key activities that help a team to identify and prepare for project risks. Other risk mitigation activities may also be performed, such as proof-of-concept, workshops, prototyping, and early tests. Any strategy that helps in understanding the big picture and identifying the major risks and complexities of a project is valid.

## Questions (Chapter 2)

1. Why effort estimation is less precise at the beginning of a project?

2. What is the public for a general view of a system; who would be interested in reading it?

3. Why are acceptance criteria important in a software project?

4. Why the business use case diagram may be useful for a general view of the system?

5. How to represent in a business use case diagram a project with many phases?

6. What is the difference between a business worker and a business actor?

This page intentionally left blank

3

