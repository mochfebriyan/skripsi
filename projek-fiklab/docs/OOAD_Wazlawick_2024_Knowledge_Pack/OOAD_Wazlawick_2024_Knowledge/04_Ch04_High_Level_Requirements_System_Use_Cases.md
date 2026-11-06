<!-- Knowledge file: Chapter 4 — High-level requirements -->
> **About this file.** Chapter 4 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** High-level requirements: system actors, system use cases and criteria for a good use case (single session, interactive, consistent result, essential, brief, system boundary), deriving use cases from business use cases, BPMN and state diagrams; requirement types (evident/hidden functional, non-functional, supplementary, ISO/IEC 25010), preliminary conceptual model, CRUDL pattern.  
> **Use this file when:** turning business processes into system use cases / functional requirements, classifying requirements, or finding missing use cases with CRUDL.  
> **Sections:** 4.1 Introduction to high-level requirements (p. 39); 4.2 System actors (p. 42); 4.3 System use cases (p. 43); 4.4 How to find system use cases in the business use case model? (p. 48); 4.5 How to find system use cases in BPMN diagrams? (p. 50); 4.6 How to find system use cases in machine state diagrams? (p. 51); 4.7 Requirements (p. 51); 4.8 Preliminary conceptual model (p. 59); 4.9 Discussion (p. 64)  
> **Contains:** 5 figures transcribed as text, 0 code listings.

# Chapter 4: High-level requirements

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 39*

Key topics in this chapter

- System Actors

- System Use Cases

- How to Find System Use Cases in the Business Diagrams

- Types of Requirements

- Preliminary Conceptual Model

## 4.1 Introduction to high-level requirements

*Chapter 4 · p. 39*

Once the business has been reasonably understood and modeled, the requirements analysis may be deepened. Although there are several approaches to represent requirements, this book presents a technique based on system use cases.

The system use case is an individual process that may be derived from the business diagrams. A high-level (or brief) system use case represents the more abstract functional requirements of a system. The annotations on those use cases represent the nonfunctional requirements or business rules, that is, the constraints related to those functions. The supplementary requirements are nonfunctional requirements that apply to the system as a whole— not only to an individual system use case. Table 4–1 explains the differences among the three types of requirements and their associations to use cases.

System use cases are useful for many activities related to systems development, such as:

- Definition and validation of the system architecture: In general, classes, associations, and attributes that form part of the system architecture are obtained from the detailed use case^1 texts.

- Creation of test cases: Use cases can be seen as a basis for system and acceptance tests, where the functionality is tested from the point of view of the user. In agile development, it is useful to have a test analyst working with a use case analyst for developing testing units while use cases are being defined.

- Planning sprints: For each use case, it may be assigned a priority, and an effort estimation to develop it, so that the team can decide on which use cases to develop at each sprint.

- Basis for user documentation: Use cases are descriptions of the system’s normal operation flows, as well as alternate flows that represent how to deal with eventual exceptional conditions. These descriptions are an excellent basis for starting the user manual because all possible functionalities are described there in a structured and complete way.

1 From now on, system use cases will be referred as use cases for simplicity, except when they are compared to business use cases. 

41

**Table 4–1: Classification of requirements.**

|Type|Explanation|
|---|---|
|Functional requirements|Things that the system should do—may be represented by system use cases|
|Nonfunctional|Constraints about how a functional requirement may work—may be represented by|
|requirements|annotations to a system use case|
|Supplementary|Constraints about the whole system, not necessarily a single requirement or use case—|
|requirements|usually represented in an appropriate table or list|

Each use case represents a coherent set of functional system requirements. Usually, more than one function is related to a single use case, especially if it is a complex one. Some functions, on the other hand, may be associated to more than one use case. In some situations, it may also happen that a function corresponds to a single use case and vice versa. This usually occurs with very simple use cases such as reports and entity management.

As use cases are requirements, then the activities of requirements elicitation and analysis correspond to the discovery and study of use cases and their properties.

## 4.2 System actors

*Chapter 4 · p. 42*

A system actor represents an entity of the real world that interacts with the system through a use case. Actors may be roles performed by people such as customers, publishers, sellers, and operators. Actors can also be external systems, that is, systems that are outside the scope of the project being developed.

Human actors or external systems interact with the target system by sending and receiving information through an interface. In the case of human actors, the information is usually exchanged through data entry devices such as keyboards, mice, or other special devices. Those actors receive information from the system through interfaces such as screens, printers, or other special devices.

Communication with actors that are external systems usually happens through a computer network. In this case, the communication interface consists of the network and its protocols.

The idea of external systems as actors must not be confused with internal ones that are components of the system under development. For instance, a database management system, used to implement data persistence for the system under development, is not an actor but a component of the inner architecture of the system. The following rules may help to appropriately identify external systems that could be actors:

- System actors are complete information systems, and not only libraries of classes or procedures. These systems store their own data, which can be exchanged with the system being developed. That data may change independently from the system being implemented.

- System actors are out of the scope of development, that is, the team will not necessarily have access to the internal design of these systems or the ability to change them. The team must communicate with a system actor using the system actor’s own interfaces, and they usually cannot be modified by the team.

Some approaches consider that there are two kinds of actors: primary and secondary. Primary actors are the ones whose goal the use case is trying to satisfy, while secondary actors are actors that just provide some help to the process under study. Examples of secondary actors are a clerk (secondary actor) that confirms that the client (primary actor) has paid in cash. In this book, we do not follow that distinction: we distinguish use case actors into human or system actors only.

A recurrent question is that if actors correspond to security profiles. This is not necessarily the case. The goal behind the identification and modeling of actors is more related to the process of finding and organizing requirements than to the process of granting access to the system. A good software design will treat access permission in a dynamic way, allowing user profiles to be created, and permissions to be associated to the different profiles of individual users. As that aspect of the system is not domain-dependent, it is not adequate to model it within the domain. In other words, use case actors may not be necessarily considered as security profiles. Those profiles will be created dynamically with the use of a generic domain-independent mechanism. Although, the use cases may be a hint in order to define such profiles.

## 4.3 System use cases

*Chapter 4 · p. 43*

System use cases differ from business use cases in some respects. For example, business actors may spend days or even weeks performing a business use case, while system use cases are often performed in a short period of time, usually seconds or minutes, with one or a few actors interacting with a system and obtaining a consistent and complete result for at least one of their goals. System use cases must also usually be performed without interruptions while business use cases are not restricted in that respect.

Another fundamental difference between a business use case and a system use case is that the business use case is usually performed by many human actors, while a system use case is normally performed by a few (sometimes just one) human actors. The fact is that if a system use case is going to be performed by more than one human actor, then they should be interacting at the same time with the system, and that is not a common situation. Usually, each human actor accesses the system at a time of her convenience, accessing necessary data and performing the necessary actions. For example, a municipal manager registers and sends a proposal on Monday, but the federal manager will read it only on Wednesday. Thus those two activities may belong to the same business use case but not to the same system use case.

As said above, sometimes more than one human actor should be available online for a system use case. For example, at a supermarket when a customer is buying goods, a supervisor may be summoned to perform actions that the cashier is not allowed to do (e.g., cancel a sale). The point is that the supervisor must be available online and the other actors must wait for her to show up before proceeding.

On the other hand, external computational systems may be considered online actors, because they are available continuously. For example, it can be assumed that a credit card operator is available online 24/7. When a customer decides to make a payment with her credit card, the system actor “Credit card operator” should be available.

A high-level system use case is represented only by a name inside an ellipse. It is usually associated to one or more actors as seen in Fig. 4–1. Notice that the stereotype for business use cases and business actors is no longer used.

In the diagram in Fig. 4–1, the ellipses represent system use cases. By default, an actor is a role performed by a human. Other kinds of actors may be represented using stereotypes, as shown in Fig. 4–1, where the stereotype «system» indicates that “Publication system” is an external system, not a human.

The use case diagram is a very popular UML diagram, but it is also frequently misunderstood. It is usual to see these diagrams with dozens of use cases and some of their fragments attached. A fragment is an incomplete activity, that is, an activity that does not produce an actor’s business goal. For example, “Register a proposal” may be considered as a use case because it produces a record that can be evaluated by a third part. One of its first steps could be “Open registering page.” Although this is something that must be done if the user is going to fill in this page, just opening the page does not produce a business goal. Consider, for example, that if the user turns the system off just after opening the page, no result will be available for using when the system is again turned on.

The presence of fragments in the use case diagram and the use of the include and extend relationships between use cases (which sometimes reveal part of their internal structure)

**Figure 4–1: System use cases and system actors.** *(p. 44)*

> **Diagram content (transcribed from the figure image):** System use case diagram, boundary "SISMOB 3.0": Municipal manager — Register proposal, Send proposal; Federal manager — Produce assessment; «system» Publication system (external system actor) — Publish funds allocation.

should be made with some concerns. Not every possible piece of a use case must be represented in this diagram, as there is a better structure (yet to be shown in this book) to show use case details. Sometimes, a use case really includes another complete use case, for example, “Register new user” that may be part of many other use cases that demand a registered user.

Thus there is a need for strong criteria to decide which use cases should be maintained in the diagram to avoid, on the one hand, many excessively detailed processes, and on the other hand, too few processes that could lack important features of the system.

The rule is to consider as a use case only those processes that can be performed not only as part of a bigger process (this affirmation is only valid for system use cases, not business ones). Partial processes that must necessarily be performed during other processes should not be represented in the system use case diagram, except if they are a part that is shared by two or more use cases.

However, even following this guide, the number of use cases in a real-world system may still be too high, so that dealing with them may become difficult. To reduce the number without losing information and precision, a second rule may be used. It consists of grouping use cases that are somewhat related, especially if that may be done more than once, like a pattern. For example, there could be four use cases such as “Create user,” “Retrieve user,” “Update user,” “Delete user,” and “List users,” or just one use case called “Manage user” that includes the five single processes. This is a pattern, because it may be repeated for other concepts: “Manage reviewer” may be used instead of Create, Retrieve, Update, Delete reviewer. This pattern is known as CRUDL, which is an acronym for Create, Retrieve, Update, Delete, and List.

Other example is a screen where a user may update some data about herself such as date of birth, document number, name, and address. After updating one information (such as “document”), she could decide to save the register and resume updating other fields later. Thinking like this, we could decide that there are use cases named “Update date of birth,” “Update document number,” “Update name,” “Update address,” etc., that can be performed one after the other in any order. However, this is too verbose and not useful for understanding the user activities. It is preferable that the use case represented is “Update user” that allows the user to update one or more fields and save the record. Later we will see also that there are fields that can never be updated in normal conditions (date of birth, for example).

The next subsections present other criteria for achieving the best use case granularity.

### 4.3.1 Single session — 4.3 System use cases

A good system use case must be performed in a single session.^2 This means that it should begin and finish without long interruptions. For example, the registration of a project is made during a single session of the system, involving the identification of the municipal manager, type of construction work, justification, cost, etc.

> *Footnote 2:* That idea follows Larman’s (2004) definition of an EBP (Elementary Business Process) use case. The EBP definition comes from the business process engineering field: “a task performed by one person in one place at one time, in response to a business event, which adds measurable business value and leaves the data in a consistent state.”

This process may terminate in two ways: even it is finished and submitted, or it is saved to be continued later. In the second case, the business value obtained is a project partially registered in the system. For now, consider that a use case such as “Register proposal” (Fig. 4–2 left) is better than having one use case for each field composing the proposal as in Fig. 4–2 (right).

On the other hand, a proposal is not automatically evaluated when it is registered: the federal manager is responsible for verifying, from time to time, which proposals have been registered; and only after that she decides on which one to assess.

If the municipal manager is lucky, the assessment can start just a few seconds after it is registered; on the other side, it can take weeks.

This fact indicates that the use case “Produce assessment” is not part of the use case “Register proposal” or “Send proposal”; it should be considered as a different system use case.

### 4.3.2 Interactive — 4.3 System use cases

A use case must also be interactive, meaning that an actor must exist to interact with the system. The internal processes of the system are not use cases no matter how complex they are. On the other side, a simple query on some information may be a (very simple) use case if there is an actor that starts it.

A system actor, such as a clock, for example, may also start a use case by sending some information to the system.

**Figure 4–2: Avoid representing fragments in the diagram.** *(p. 46)*

> **Diagram content (transcribed from the figure image):** Good vs bad use case decomposition. BETTER: a single use case "Register proposal". AVOID (note: "AVOID including fragments that are not complete use cases or shared fragments"): Register proposal «include» four «fragment» use cases — Identify municipal manager, Register type of construction, Register justification, Register cost.

### 4.3.3 Consistent result — 4.3 System use cases

A use case must produce a consistent result, be it a complete entry or transformation on a piece of information, or simply a query where relevant information is passed to a user. A use case cannot leave the information at an inconsistent state at its end. For instance, the registering of an project cannot be concluded without the identification of the municipal manager that is responsible for it, or else the information about the proposal would be incomplete regarding the business rules. If the author of the proposal is not known and the proposal is registered, who would be able to gain access to proceed with it? Usually, allowing data registration only for logged users may cope with this issue.

To decide if a use case has a consistent result, one could think like this: only a complete process is a system use case, in the sense that a user could go to the computer, turn it on, perform the process, and at its end, turn off the computer, because some business goal was obtained (some relevant information was received or updated by the user).

This excludes from the use case definition fragments such as “Login,” because it is not an isolated process that produces palpable change in data or user information. Considering that the computer could be turned off immediately after that operation, no business goal would have been produced. “Login” usually is part of so many use cases that it is omitted from diagrams in order to not pollute them.

### 4.3.4 Essential and concrete — 4.3 System use cases

Regarding abstraction level, at least two styles for writing use cases may be identified:

- Essential use cases, which do not mention interface technology.

- Concrete (or real) use cases, which are specifically written for a given interface technology.

During requirements elicitation and analysis, system use cases are considered requirements, not design. It is a mistake to include among these use case actions that are purely related to an interface technology, such as Open main window, Print report, or Login. People prepared to handle that facet of design will decide on those actions later, after the real user needs are better understood.

Ambler (2000) points out that essential models are more flexible, leaving more options open and more readily accommodating changes in technology. He also says that essential models are more robust than concrete representations because they are more likely to remain valid in the face of changing implementation technology.

A team that uses the UX technique may try to test different approaches to the same interface. They could initiate with an essential use case and then produce one or more possible interfaces for the user. The different designs may be evaluated, and the best may be chosen for finally producing real (concrete) use cases that indicate which buttons or menus may be activated by the user.

Thus essential use cases can be chosen as the best option during requirements elicitation before a study on the best interfaces has not yet been made. After decisions about technology are taken, real use cases may be produced, usually by just adding notes to the essential use case. This is detailed later in the book.

### 4.3.5 Brief — 4.3 System use cases

During analysis, use cases usually are brief, meaning that they are described just by their name or, in some cases, by one or two sentences. However, this is not the only way a use case may be described. Later they will be extended and contain more details. Cockburn (2001) identifies three types of use cases regarding the level of detail:

- Brief: A one-paragraph synopsis of the use case.

- Casual: Written in simple, paragraph, prose style. It is likely to be less rigorous in its description than a fully dressed use case.

- Fully Dressed or Detailed: Expanded to include a main flow and alternate flows, as well as other sections such as postconditions, preconditions, stakeholders, and technological variations.

In this book, we expect that use cases considered during the initial phases will be brief. This means that usually their name is sufficient to explain their meaning. However, additional explanation is allowed for the sake of requirements comprehension. Also, if some key use cases must be expanded to identify risks regarding their inherent complexity, this is also acceptable. Usually, fully dressed or detailed use cases will be useful only when requirements must be understood in their most complete details.

### 4.3.6 System boundary — 4.3 System use cases

One of the decisions a team must make when designing system use cases is where to place the system boundary. Graphically, the boundary is only a rectangle that is placed on the diagram. Inside it are the use cases and outside are the actors. In business use case diagrams, the system boundary represents the limits of the organization (company, department, etc.). But now, at the system level, it represents the limits of a computational system.

A decision was made earlier on which workers to include in the automation border. One example is the clerk that helps the reviewers entering their reviews. If this assignment is to be performed directly by the reviewer using an information system, then the worker clerk role disappears, and the reviewer is connected directly to the use case (Fig. 4–3).

## 4.4 How to find system use cases in the business use case model?

*Chapter 4 · p. 48*

To discover system use cases and actors, the team may examine the business use case diagram with the defined automation boundary (scope of automation).

**Figure 4–3: From business to system use cases diagram.** *(p. 49)*

> **Diagram content (transcribed from the figure image):** Business view vs system view of the same use case. Business view: business actor Reviewer and «worker» Clerk both linked to business use case Register proposal. System view: only the actor who operates the system appears — Reviewer — Register proposal (the worker becomes the system user / disappears depending on automation).

**Figure 4–4: Login must not be considered a complete use case.** *(p. 49)*

> **Diagram content (transcribed from the figure image):** System use cases derived from business use cases (System Boundary): Technician — "Use case(s) derived from Business use case 1"; Assessor — "Use case(s) derived from Business use case 2"; Reviewer — "Use case(s) derived from Business use case 3" (continuation of the automation-opportunity example in Fig 2–8).

First, the actors that are really interested in the process to be automated should be identified. These are the business actors that interact with the business use cases inside the automation scope, and the business workers that interact with such use cases but that are not themselves inside the automation scope. Let’s go back to Chapter 2 and look at Fig. 2–8. Applying the above rules to the actors and use cases in that figure, the following system actors could be identified (Fig. 4–4):

- “Technician” and “Reviewer”: because they are business actors that interact with use cases that will be automated.

- “Assessor”: because it is a business worker that will not be automated and that interacts with a use case that will be (business use case 2).

On the other hand, the following will not be considered system actors:

- “Clerk”: because it is a business worker whose activities will be fully automated.

- “External organization”: because it is a business worker that does not interact with any use case inside the automation scope.

After transforming the business use case model into a system model, only system users will remain and only system use cases inside the system boundary will remain. In many cases, a business use case can be derived into a single system use case, but the most interesting business use cases are those that will be derived into more than one system use case.

Despite some business workers being not present in the system use case diagram because their tasks will be automated or reassigned, they are still an important source of information during the initial steps of analysis, when knowing how they work and what problems they face may be useful for designing the new system. Another source of requirements is the business actors that will become system actors.

However, business actors and workers would not always be available for requirements elicitation, and in that case, the team should try to find other domain specialists. For example, it may not be possible to interview the user of a system for a business that does not yet exist. Thus someone that knows about the new business will be a key person for obtaining the right requirements.

If some business actors are not available but the knowledge about their business is already published, then it would be possible to examine existing documentation instead of interviewing them.

## 4.5 How to find system use cases in BPMN diagrams?

*Chapter 4 · p. 50*

BPMN is a good source for system use cases. One could think that each task in a BPMN diagram could correspond to a system use case. However, this is not true all the time. If two or more tasks in a path must be executed without, say, a long interruption, then they are to be considered as parts of the same use case. For example, in Fig. 3–5 in the previous chapter, the municipal manager may perform the task “Register proposal,” but as soon as the registration is concluded, it is not mandatory to perform “Send proposal.” She may wait hours or even days before sending the proposal. This situation characterizes “Register proposal” and “Send proposal” as two separate use cases.

On the other hand, as soon as the FNS has performed the task “Allocate funds,” it may (or even must) perform “Publish funds allocation” immediately. There is no need to wait to make this publication and even postponing the publication could create concurrency problems, for example, with other projects trying to allocate the same funds. This situation indicates that the tasks “Allocate funds” and “Publish funds allocation” both belong to the same system use case, meaning that there is no situation where you can allocate funds and not immediately publish it.

## 4.6 How to find system use cases in machine state diagrams?

*Chapter 4 · p. 51*

A machine state diagram is also particularly helpful in terms of finding system use cases. Each event that changes the state of a business object may be done by someone or some system. Usually, that someone or some system is an actor performing a system use case.

Let’s consider, as an example, the initial machine state diagram for a work in the SISMOB system (Fig. 3–11). Notice that the nodes in this case are not tasks such as in BPMN diagrams, but states in which the object may exist (e.g., “Under preparation,” “Canceled”). If a task is executed in this diagram, it occurs in the flows between the nodes. For example, when a proposal is finished and sent to evaluation, the event “propose” indicates that the proposal goes from state “Under preparation” to “Under assessment.” Therefore the system use case that occurs here is “Propose Project.” It would be preferable to use “Propose project” instead of simply “Propose” because other things may be proposed in the context of this diagram, for example, and ongoing project and a concluded project. Thus from the diagram in Fig. 3–11, the following system use cases could be identified:

- Register project: from the start node to “Under preparation.”

- Propose project: from “Under preparation” to “Under assessment.”

- Approve project: from “Under assessment” to “Approved.”

- Request changes in project: from “Under assessment” to “Under preparation.”

- Approve: from “Under assessment” to “Approved.”

Here, we do not consider that approval or cancelation of a project must be made just after the assessment of the project. The federal manager could produce an assessment, record it, and only take her decision later. This is symmetrical with the situation between “Under assessment” and “Under preparation” because the municipal manager is not forced to modify the project as soon as she receives the changes request.

## 4.7 Requirements

*Chapter 4 · p. 51*

As seen up to this point, requirements are represented in use cases: business use cases are the more abstract, and organization-related requirements and system use cases are more user oriented. The team can and must use every available source to identify requirements (specialists, users, documents, interfaces, literature, etc.), and for each source, a set of functions that the system must perform may be identified.

Requirements elicitation, in this case, is the activity that involves studying business models and interacting with clients, users, and other stakeholders in order to discover which are their needs. For now, we have identified the existence of system use cases, that are, per se, a set of user stories. Let’s first discuss their nature and properties, and later we could manage to start detailing them and producing the user journey that corresponds to the possible paths of the detailed use case.

Remember always that a requirement does not establish how the constraint will be implemented, it just demands a solution to a problem. The design and implementation of the system must meet the requirement in one way or another, or otherwise, the analyst should negotiate with the client for some requirement flexibility.

### 4.7.1 Requirements challenges — 4.7 Requirements

So, why to describe and draw so many diagrams at this point of the analysis? Why do not start programming yet? Well, before starting to build the more concrete and more expensive parts of the software, a good common understanding about requirements is necessary, because refactoring code is expensive (although sometimes necessary). This is true even in the agile culture. The challenges regarding requirements are, at least, the following (Pressman, 2010):

- How to discover requirements.

- How to communicate requirements to the other phases and teams of the project.

- How to recall requirements during development to verify if they have all been implemented.

- How to manage requirements change.

It would be useless to develop a nice use case diagram and later not be able to know if the requirements incorporated there were included in the design. The existence of automatic mechanisms to conduct this verification is crucial. Therefore it is important to maintain traceability relations between use cases and other parts of the design. The following chapters show how those relations among design artifacts are obtained.

It is necessary to keep in mind that requirements necessarily change during the development of a project. In the case of SISMOB Phase 3, more than 30% of the products were changed after the project started. Thus the change must be managed, not avoided. However, this is not only an inspirational coach quote: you must be prepared to that. In special, keep the user close and check with her about any doubts you have about requirements.

The changing nature of requirements incentives the software industry to avoid the requirements-driven analysis (Alford, 1991), because it would be inadequately timeconsuming for most systems. Using requirements as a base to support system architecture is like building a house over moving sand; when requirements change, the structure suffers. However, we can use a much more stable basis for the system architecture, which is the set of classes and components that encapsulate information and behavior, the so-called “objectoriented” development.

These classes implement functionalities that combined allow the implementation of the requirements. If requirements change, the combinations change, but not the basic structure. This kind of architecture follows the open-close principle (Meyer, 1988), in the sense that the system components are always closed for modification (they work), but open for extension (they may accommodate new functionalities).

It is important to trace the origin of each requirement (e.g., a business actor, a business worker, the client itself, or even a domain specialist), because it is necessary to validate requirements with those sources, verifying if they are well written, complete, and sound.

Sometimes it may also occur that different people or departments present different specifications for the same requirement. In that case, it is necessary to produce an agreement among them, or identify who has the highest authority to determine the acceptable form for the requirement.

### 4.7.2 Evident and hidden functional requirements — 4.7 Requirements

Functional requirements can be optionally identified as evident or hidden (Gause and Weinberg, 1989):

- Evident functional requirements are functions that are performed with the user’s knowledge. These requirements usually correspond to information exchange between the user and the system, such as queries and data entry, which flows through the system interface.

- Hidden functional requirements are functions performed by the system without explicit knowledge of the user. Usually, these functions are math operations and data updating performed by the system without explicit user knowledge, but because of other functions performed by the user.

Hidden requirements are performed internally by the system. Thus although they do not appear explicitly as use cases, they must be adequately associated to them to be recalled at the time of design and implementation. Thus they could also be added as annotations to a use case.

An example of an evident requirement is the task “Allocate funds” in Fig. 3–5 because, the employee at the FNS must know that she is approving those funds. However, the task “Publish funds allocation” is performed automatically by the system. Although the user may know that this is going to happen, she must not take any action to initiate it. Thus “Publish funds allocation” can be considered here as a hidden requirement and part of the “Allocate funds” use case.

### 4.7.3 Nonfunctional and supplementary requirements — 4.7 Requirements

Nonfunctional requirements are not tasks neither use cases, but constraints that may be linked to specific use cases of a system (e.g., “a description of a project must not exceed 4000 words.”), and therefore, they can be treated as annotations on those use cases.

Sometimes, however, nonfunctional requirements may be generic, that is, not necessarily attached to a function (e.g., “the application must work on a smartphone with 32GB”), and in that case, they will appear in the supplementary specifications document, not attached to any use case.

Constraints that are specifically related to a use case are called nonfunctional requirements, and generic constraints are called supplementary requirements.

### 4.7.4 Logical and technological nonfunctional requirements — 4.7 Requirements

There are two kinds of nonfunctional requirements:

- Logical: Business rules attached to a use case. For example, the date in the project registration must be the same date or before the project was submitted.

- Technological: Constraints and qualities related to the technology used to perform the function, such as the user interface, the kind of communication protocol, security constraints, and fault tolerance. The second type is mostly related to the software qualities, such as security, usability, and configurability. Please refer to ISO 25010 for a complete set of possible software qualities.

### 4.7.5 Permanent and transient nonfunctional requirements — 4.7 Requirements

One of the most fundamental features of a requirement is whether a given nonfunctional or supplementary requirement is permanent or transient.

Nonfunctional and supplementary requirements can be considered permanent (they are not expected to change) or transient (they are expected to change) depending on a decision made by the team and the client. Permanence or transience is not an intrinsic feature of a requirement: the requirement may change or not independently of our will, but we can decide if we are going to be prepared for the change or not. The criteria to consider a requirement as permanent or transient depends on the cost of the change if we are prepared, the cost of the change if we are not prepared, and the cost of the preparation itself.

It is like deciding on buying insurance. If your car is expensive and you drive poorly, maybe you should buy insurance to avoid losing a large quantity of money if an accident happens. Otherwise, maybe it is not wise to pay insurance for a car that has little value and is kept on the garage most of the time (you better count on luck).

However, an accident may happen whether or not you buy an insurance. In the first scenario, you spend more before the accident and save money after it, and in the second scenario, you save money before the accident but spend more after. The first scenario is the one with transient requirements because you bet something (an accident) may produce high cost in the future. The second scenario is the one with permanent requirement because you bet that even if a cost happens in the future, it would be too low to compensate the investment in insurance.

If a software team invests in flexible design, so that most requirements are transient, less effort will be spent during maintenance to accommodate changes. However, the cost of that flexible design during development may become prohibitive for some projects. It will always be a good idea to ponder which constraints should really be treated as transient requirements.

For example, a supplementary requirement could establish that the SISMOB system must deal with a single currency: the Mira. If that requirement is considered permanent, then the system will be designed for a single currency (“Mira” could even be a primitive data type used to define variables and attributes). However, if the requirement is considered transient, then even if there is no other currency being used today, the whole system must be prepared to accommodate future currency, or even more than one currency at a time.

The consequences of deciding that a requirement is permanent are the following:

- It is cheaper and quicker to develop the system.

- It is more expensive and difficult to change the system if, by any chance, the requirements change in the future.

On the other hand, deciding that the requirement is transient has the following consequences:

- It is more expensive and complex to develop the system (it should accommodate functionalities for changing the currency, for example).

- It is easier and quicker to maintain the system (if the currency changes, the system is already prepared to accommodate that with a simple reconfiguration).

Thus it is not the nature of the nonfunctional requirement that will decide whether it is permanent or transient. It is the client, with the help of the team, that must make the decision. The ideal situation would be to list the requirements of greater importance (those that are really expected to change soon with a bigger impact on the system) and consider them transient, while leaving the others as permanent.

### 4.7.6 Mandatory and desired requirements — 4.7 Requirements

Requirements (especially nonfunctional ones) may also be considered mandatory or desired,^3 that is, those that must be obtained by any means and those that could be obtained if no bigger issue hinders the development process.

In the case of functional requirements, that classification indicates development priorities. If there is flexibility in the contract such that only the most important use cases are implemented if there is no time to implement them all, then the team must know which ones are mandatory for they have bigger priority.

However, if the team can make a good estimate of the effort needed to develop the system, and if they have a good history of accurate estimation, there will be less motivation for such distinction regarding functional requirements, because all requirements are expected to be implemented in time.

On the other hand, nonfunctional and supplementary requirements are much more unpredictable than functional ones regarding effort estimation. Thus in some cases, it may be necessary to consider those requirements with some flexibility.

In this case, some restrictions are defined such that they must be obtained by any means and others may be considered simply desirable, and some time is allocated to pursue them.

3 Another option is to use the MoSCoW scale: Must, Should, Could, and Would.

For example (real Bridge case), in the case of the vaccination app, a mandatory requisite is that a patient must be identified by the number of her document. One could suggest also that a camera on a smartphone could be used to read the document number avoiding the need to type it and the possible errors that come with this kind of entry. As the team had no experience with text extraction from image, they decided to consider this feature as desired, not mandatory. After developing the more important features and study about text extraction, they decided with the client that the effort to develop and perfect this feature would not compensate the cost and time necessary to do it and also the urgency to have the system available during the pandemics.

### 4.7.7 Supplementary requirements — 4.7 Requirements

Supplementary requirements are all types of constraints and qualities related to the system as a whole and not only to individual functions. For example, a supplementary requirement may establish that the system must be compatible with a given legacy database, or be implemented with a given programming language, or even follow a given look and feel.

Care must be taken when supplementary requirements are defined. A requirement such as “the system must be easy to use” is not sufficiently clear. It would be better to say something like “novice users must be able to complete tasks without errors in their first attempt.” That gives a more precise idea of what must be designed to accomplish the requirement.

Nonfunctional and supplementary requirements may also be identified with different groups such as interface, implementation, performance, and fault tolerance. The goal of making such distinctions is to allow for better organization.

Although most teams would choose to use the FURPS 1 classification system (Grady, 1992) for organizing supplementary requirements, the newest source to decide on supplementary requirements classification is ISO/IEC 25010,^4 as shown in Table 4–2.

Although this list is extensive, the team must keep in mind that it is only a classification to improve the ability to identify which requirements are important. There is no need to seek nonexistent requirements only to fill a box, for example, establishing complicated packaging requirements for a client that does not care about the way the software will be packaged.

It is also advisable not to lose time discussing if a given requirement belongs to this or that type. More important than deciding on its type is to know that it exists: long discussions on requirements classification do not add significant knowledge to the project.

Not every feature must have a requirement generation question. Thus usually there are not requirements in all categories. The questions that generate requirements mentioned in Table 4–2 are a good basis for finding eventual needs in meetings with the client. But it is not mandatory to have an answer to all those questions.

4 http://www.iso.org/iso/catalogue_detail?csnumber 5 35733 (Continued)

**Table 4–2: Supplementary requirements classification based in the norm ISO/IEC 25010:2011 and requirement generating questions.**

|25010 Feature|25010 Sub feature|Requirements generating questions|
|---|---|---|
|Functional suitability|Functional completeness|Must all necessary functions be implemented? May some of them be left outside the system scope? May some functions be implemented by a further project?|
||Functional appropriateness|In which degree the user activities must be made easier by the system?|
||Functional correctness (accuracy)|Are there accuracy specifications, that is, a desirable precision for data? Are there limits for tolerating imprecision?|
|Reliability|Maturity Availability|Must special care be taken to avoid the system to present defects during use? Must critical parts be defined by formal specification? What is the intensity and type of tests that must be performed to assure the system is free from bugs? Which is the degree of availability required for the system? How many simultaneous accesses must be supported? How many hours by day? How many days by year?|
||Fault tolerance|How should the system react in the case of anomalies externally provoked, such as communication interruption?|
||Recoverability|Must the system recover automatically in the case of a disaster? Lost data and aborted processes can be recovered under which circumstances?|
|Usability|Appropriateness recognizability|In which way should the software present itself to a potential user so that she may recognize its applicability? How should the software be packaged?|
||Learnability|How are the concepts inherent to the software being presented to the user so that she can become competent on its use?|
||Operability|In which degree must the product be easy to use and control? What kind of help must the system provide? What forms of documentation and manuals should be available? How are they going to be produced? What kind of information should they present?|
||User error protection|What kind of protection against user error is necessary?|
||User interface esthetics|Which design patterns will be used for the interface to provide visual pleasure and satisfactory interaction?|
||Accessibility|In which degree must the product be designed to attend people with special needs?|
|Performance|Time behavior|Which time restrictions exist related to the software processes and functions?|
|efficiency|Resource utilization|Are there data storage space restrictions? Energy limitations? Communication network limitations?|
||Capacity|Regarding processing capacity, which are the nominal values expected and which are the critical values? For example, the software may be designed to support up to 2000 simultaneous accesses but assured to keep working when up to 10,000 simultaneous accesses happen.|
|Security|Confidentiality Integrity| In which degree must the information and functions of the system be available only to those authorized to access them? In which degree data and functions must be protected against unauthorized modification by people and systems?|
||Nonrepudiation Accountability|In which degree must the system guarantee that the records kept by it are effectively true so that their authors cannot deny them? In which degree user actions are recorded by the system? Which information is kept?|
||Authenticity|In which degree it must be guaranteed that a logged user is really who she is supposed to be?|

**Table 4–2: (Continued)**

|25010 Feature|25010 Sub feature|Requirements generating questions|
|---|---|---|
|Compatibility|Coexistence|With which products must the software potentially coexist? Which tools and programming languages must be used? Is it necessary to run the system with legacy systems?|
||Interoperability|Which other products must communicate with the system? To which systems must it send data? From which systems must it receive data?|
|Maintainability|Modularity|What kind of architecture will be used? Layers? Partitions? Components? Web services?|
||Reusability|Will the system be produced from parts of other systems? Must the system de designed so that its parts could be reused in future projects?|
||Analyzability|Will special techniques or tools be used to ease debugging the code?|
||Modifiability|Will special techniques or tools be used to guarantee that changes introduced in the system will not produce new defects?|
||Testability|Will special techniques and tools be used to ease regression tests? Automated test tools will be used? TDD (Test-Driven Development) will be used? How are test assets produced during development going to be kept?|
|Portability|Adaptability|In which degree must the software adapt itself to other contexts besides the ones it was originally designed? Must it be recompiled or just reconfigured? What can be configured in the system? Examples of configurable items are printers, currency, company policies, interface fonts and colors, language, etc. Transient requirements would probably be related to configurable items.|
||Installability|What installation resources will be provided? Should installation be automatic? Is data migration automatic?|
||Replaceability|What resources must the system provide when it replaces other systems with the same goals? What resources must the system provide when it is going to be replaced by other system with the same goals? Should it generate data and configuration in formats widely understood such as XML?|
|Effectiveness|Effectiveness|Which business goals on the real use environment must the system help to obtain? In which degree must the system be responsible for obtaining those goals in a complete and correct way?|
|Efficiency|Efficiency|What kind of return of investment (ROI) must the system produce to the client?|
|Satisfaction|Utility|In which way must the software be designed to help the user to perceive the consequences of its use?|
||Pleasure|In which degree must the system provide pleasure to its users?|
||Comfort|In which degree must the system preserve or improve physical and mental user comfort?|
||Trust|In which way must the system be designed so that the stakeholders trust it will do the work?|
|Freedom from risk|Economic risk mitigation Health and safety risk mitigation|What kind of financial risk (including property and moral damage) must the system reduce? What kind of physical risk to people must the system reduce?|
||Environmental risk mitigation|What kind of environmental and property risks must the system reduce?|
|Context coverage|Context completeness|In which degree must the system be used effectively, efficiently, without risks, and with user satisfaction in its use contexts? Which are those use contexts? Are there legal requirements related to the use of the software?|
||Flexibility|In which degree must the system be used effectively, efficiently, without risks, and with user satisfaction in use contexts other than the ones it was originally designed? Which are those use contexts?|

## 4.8 Preliminary conceptual model

*Chapter 4 · p. 59*

Although further chapters present conceptual modeling techniques in detail, it is interesting to mention here that a preliminary conceptual model (Larman, 2004) can be derived from the high-level system use cases.

### 4.8.1 Finding concepts by examining system use cases — 4.8 Preliminary conceptual model

The preliminary conceptual model consists of a class diagram that represents the main information units of the system. Usually, only classes are used to represent the concepts the user has about the information managed by the system. Associations between classes may be added too if possible, but not necessarily detailed, and attributes are not necessarily used at this time.

One of the main utilities for this diagram at this point is to discover which are the concepts derived from the high-level use cases and then, use this class diagram to discover which use cases may be lacking from the use case diagram. That allows the team to discover new use cases and complete the use case list for the system.

For exemplifying this technique, let’s consider again our SISMOB example. From Fig. 3–5, we identified a series of system use cases that are listed in the center of Table 4–3. Just to remember, we consider that activities that must be executed immediately after another are part of the same use case, automatic tasks just after user tasks are part of the same use case, and activities that are simply manual ones are not use cases.

Below, the reasoning for each choice of identifying a concept from a high-level use case is explained:

- Register proposal: A Proposal is a central concept. Registering is merely the fact of recording it in the system and therefore, not a concept.

- Send proposal: A Proposal was already identified. Now it can be associated with a Sending event.

**Table 4–3: System use cases and concepts derived from them.**

|Actor|High-level system use case|Concepts|
|---|---|---|
|Municipal manager|Register proposal|Proposal|
|Municipal manager|Send proposal|Sending|
|Municipal manager|Refactor proposal||
|Federal manager|Produce assessment about proposal|Proposal Assessment|
|Federal manager|Cancel proposal|Cancellation|
|FNS|Allocate funds|Funds Allocation, Publication|
|Municipal manager|Require phase completion|Phase Completion Requisition|
|Federal manager|Produce assessment about phase|Phase Assessment, Funds Deallocation|

- Refactor proposal: As is consists only of adjustments in the proposal and its new submission, there is no new concept here.

- Produce assessment about proposal: Here, a new concept is Assessment that will be associated to Proposal.

- Cancel proposal: To cancel an event or object is not usually just erasing it from the system. That is why a “Cancelation” concept is identified here and would be associated to a proposal if the last one is canceled.

- Allocate funds: this use case has an included fragment that is the task “Publish funds allocation.” Then, two new concepts appear: “Funds Allocation” and “Publication.”

- Require phase completion: at this point, a Proposal (if approved) will be transformed into an ongoing project. For that to happen, it is necessary that a “Phase Completion Requisition” concept to be associated to the Proposal.

- Produce assessment about phase: This use case has an extension fragment that is the “Deallocate funds” task, which will be performed if the evaluation is not good. Thus it completes our model with concepts Phase Assessment and Funds Deallocation.

Fig. 4–5 shows a possible configuration of the class diagram that represents a preliminary conceptual model. Many doubts remain, however, and the diagram will possibly change after analysis is deepened. Since we use multiplicity annotations in the diagram, notice that:

- “0..1” represents an optional single role. For example, a Proposal may have a Cancelation.

**Figure 4–5: Preliminary conceptual model.** *(p. 60)*

> **Diagram content (transcribed from the figure image):** Preliminary conceptual model (classes without attributes) with multiplicities: Proposal 1 — 0..1 Cancellation; Municipal Manager 1 — * Proposal; Proposal 1 — * Sending; Federal Manager 1 — * Sending; Sending 1 — 0..1 Proposal Assessment; Sending 1 — 0..1 Funds Allocation; Funds Allocation 1 — 0..1 Funds Deallocation; Funds Allocation 1 — 0..1 Publication; Funds Allocation 1 — 0..1 Phase Completion Requisition; Phase Completion Requisition 1 — 0..1 Phase Assessment.

- “1” represents a mandatory single role. For example, a Proposal must have a Municipal Manager.

- “– ” represents an optional multiple role. For example, a Proposal may be associated to a set of “Sending” objects depending on how many times it is refactored and resent.

### 4.8.2 Finding new use cases using the CRUDL pattern — 4.8 Preliminary conceptual model

A next step in analysis could be to verify if the set of use cases is minimally complete. This can be done by comparing each concept discovered with the four operations of the CRUDL patterns. Remember that “C” stands for “create,” “R” for “retrieve,” “U” for “update,” “D” for “delete,” and “L” for list.

If you look at the use case diagram or list, you could see that there are already use cases that create certain concepts, use cases that retrieve information about concepts, use cases that update information about concepts instances, and use cases that delete instances of concepts.

The set would be incomplete, however, if there are use cases that create information, but no use case retrieves or consumes that information, or if there are use cases that consume information that is nor created neither updated by any other use case. These gaps in the Concept/CRUDL matrix should be filled with new use cases.

However, before proceeding, we must remember that there are concepts that not necessarily implement all four CRUDL operations. For example, the list of weekdays has seven elements. We cannot delete, create, or update new weekdays. Thus the only operation that it implements is Retrieve.

Moreover, in many cases there are concepts which instances cannot be deleted. For example, a product once sold in a store may not be deleted from the catalog, or older sales would be inconsistent. This product may be marked as “out of sale” or something else. Then, this concept only implements the concepts of Creating, Retrieving, Updating, and Listing.

Other concepts can even be created and deleted but not updated. A sale, after completed, may not be changed anymore. Thus it implements only Create, Retrieve, Delete, and Listing.

Our first attempt to complete the use case list will populate the Concept/CRUDL table (Table 4–4) with the concepts discovered so far, the use cases that we know that operate at least one of the CRUDL operations on them and a mark “X” indicating a CRUDL operation that this concept must not implement.

Finally, we can complete the table with a set of use cases that appear to be missing. This may be just a guess unless the client is present with the team at this point. But it is a good exercise to think about the completion of the operations necessary to the system. Table 4–5 shows the complete set of use cases.

Those in italic are new use cases that should be implemented in order to the information to complete its life cycle of being created, used, and disposed, when it is the case. Cells marked with “X” continue to be operations possible but not acceptable by the business rules.

**Table 4–4: Concepts versus CRUDL operations: before completion.**

|Concept|Create|Retrieve|Update|Delete|Listing|
|---|---|---|---|---|---|
|Proposal|Register proposal|Refactor proposal|Send Proposal|X|Refactor proposal, Send Proposal|
|Sending|Send proposal||X||Send Proposal|
|Proposal assessment|Produce assessment about proposal|Refactor proposal|X||Produce assessment about proposal|
|Cancellation|Cancel proposal||X|X||
|Funds Allocation|Allocate funds|Require phase completion|X|X||
|Publication|Allocate funds|Require phase completion|X|X||
|Phase Completion|Require phase completion||X||Require phase completion|
|Requisition|Require phase completion||X|||
|Phase Assessment|Produce assessment about phase||X|||
|Funds Deallocation|Produce assessment about phase||X|X||

**Table 4–5: Concepts versus CRUD operations: before completion.**

|Concept|Create|Retrieve|Update|Delete|Listing|
|---|---|---|---|---|---|
|Proposal|Register proposal|Refactor proposal|Send Proposal|X|Refactor proposal, Send Proposal|
|Sending|Send proposal|Report on sent proposals|X|Delete proposal|Send Proposal|
|Proposal assessment|Produce assessment about proposal|Refactor proposal|X|Delete assessment|Produce assessment about proposal|
|Cancelation|Cancel proposal|Report on cancelations|X|X|Report on cancelations|
|Funds Allocation|Allocate funds|Require phase completion|X|X|Report on funds allocation|
|Publication|Allocate funds|Require phase completion|X|X|Report on publications|
|Phase Completion|Require phase completion|Report on phase requirements|X|Delete phase requirement|Require phase completion|
|Requisition|Require phase completion|Report on requisitions|X|Delete requisition|Report on requisitions|
|Phase Assessment|Produce assessment about phase|(Would appear in the continuation of the diagram inFig. 3–7)|X|Delete phase assessment|Report on assessments|
|Funds Deallocation|Produce assessment about phase|Report on funds deallocation|X|X|Report on funds deallocation|

## 4.9 Discussion

*Chapter 4 · p. 64*

The identification of that preliminary conceptual model is especially useful to ease the visualization of the structure of the information that is going to be managed by the system; this helps in unifying the vocabulary among the team members and other stakeholders. The decisions about changing use case names to clean the vocabulary should be used in the tables and diagrams every time it seems reasonable to do.

Also, the conceptual model at this point helps in identifying possible missing use cases, which can then be identified and introduced in the diagram.

## Questions (Chapter 4)

1. Explain the differences between a business use case and a system use case.

2. What is the utility of a system use case through the software development process?

3. Which business actors and business workers are converted into system actors?

4. What are functional, nonfunctional, and supplementary requirements and what features might they have?

5. Why must a preliminary conceptual model be made during the Inception phase?

