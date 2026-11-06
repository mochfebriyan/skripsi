<!-- Knowledge file: Chapter 10 — Techniques 10.11–10.20 -->
> **About this file.** Part of a cleaned, AI-ready edition of the BABOK® Guide v3 (IIBA, 2015). 
> **Covers:** Techniques: 10.11 Concept Modelling; 10.12 Data Dictionary; 10.13 Data Flow Diagrams; 10.14 Data Mining; 10.15 Data Modelling; 10.16 Decision Analysis; 10.17 Decision Modelling; 10.18 Document Analysis; 10.19 Estimation; 10.20 Financial Analysis. Each technique has Purpose, Description, Elements, Usage Considerations (Strengths/Limitations), and a card listing every task that uses it and how.  
> **Use this file when:** the question is about how to perform, or when to use, one of these techniques.
> **Sections:** 10.11 Concept Modelling (p. 245); 10.12 Data Dictionary (p. 247); 10.13 Data Flow Diagrams (p. 250); 10.14 Data Mining (p. 253); 10.15 Data Modelling (p. 256); 10.16 Decision Analysis (p. 261); 10.17 Decision Modelling (p. 265); 10.18 Document Analysis (p. 269); 10.19 Estimation (p. 271); 10.20 Financial Analysis (p. 274)

# Chapter 10: Techniques (continued)

## 10.11 Concept Modelling

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 245*

> **Where this technique is used — 10.11 Concept Modelling** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **4.2 Conduct Elicitation** (Elicitation and Collaboration): used to identify key terms and ideas of importance and define the relationships between them.
> - **6.1 Analyze Current State** (Strategy Analysis): used to capture key terms and concepts in the business domain and define the relationships between them.
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to define terms and relationships relevant to the change and the enterprise.

### 10.11.1 Purpose — Concept Modelling

A concept model is used to organize the business vocabulary needed to consistently and thoroughly communicate the knowledge of a domain.

### 10.11.2 Description — Concept Modelling

A concept model starts with a glossary, which typically focuses on the core noun concepts of a domain. Concept models put a premium on high-quality, designindependent definitions that are free of data or implementation biases. Concept models also emphasize rich vocabulary.

A concept model identifies the correct choice of terms to use in communications, including all business analysis information. It is especially important where high precision and subtle distinctions need to be made.

Concept models can be effective where:

- the enterprise seeks to organize, retain, build-on, manage, and communicate core knowledge,

- the initiative needs to capture large numbers of business rules,

- there is resistance from stakeholders about the perceived technical nature of data models, class diagrams, or data element nomenclature and definition,

- innovative solutions are sought when re-engineering business processes or other aspects of business capability, and

- the enterprise faces regulatory or compliance challenges.

A concept model differs from a data model. The goal of a concept model is to support the expression of natural language statements, and supply their semantics. Concept models are not intended to unify, codify, and simplify data. Therefore the vocabulary included in a concept model is far richer, as suits knowledge-intensive domains. Concept models are often rendered graphically.

### 10.11.3 Elements — Concept Modelling

#### 10.11.3.1 Noun Concepts — Concept Modelling

The most basic concepts in a concept model are the noun concepts of the domain, which are simply ‘givens’ for the space.

#### 10.11.3.2 Verb Concepts — Concept Modelling

Verb concepts provide basic structural connections between noun concepts. These verb concepts are given standard wordings, so they can be referenced unambiguously. These wordings by themselves are not necessarily sentences; rather, they are the building blocks of sentences (such as business rule statements). Sometimes verb concepts are derived, inferred, or computed by definitional rules. This is how new knowledge or information is built up from more basic facts.

#### 10.11.3.3 Other Connections — Concept Modelling

Since concept models must support rich meaning (semantics), other types of standard connections are used besides verb concepts.

These include but are not limited to:

- categorizations,

- classifications,

- partitive (whole-part) connections, and

- roles.

### 10.11.4 Usage Considerations — Concept Modelling

#### 10.11.4.1 Strengths — Concept Modelling

- Provide a business-friendly way to communicate with stakeholders about precise meanings and subtle distinctions.

- Is independent of data design biases and the often limited business vocabulary coverage of data models.

- Proves highly useful for white-collar, knowledge-rich, decision-laden business processes.

- Helps ensure that large numbers of business rules and complex decision tables are free of ambiguity and fit together cohesively.

#### 10.11.4.2 Limitations — Concept Modelling

- May set expectations too high about how much integration based on business semantics can be achieved on relatively short notice.

- Requires a specialized skill set based on the ability to think abstractly and nonprocedurally about know-how and knowledge.

- The knowledge-and-rule focus may be foreign to stakeholders.

- Requires tooling to actively support real-time use of standard business terminology in writing business rules, requirements, and other forms of business communication.

## 10.12 Data Dictionary

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 247*

> **Where this technique is used — 10.12 Data Dictionary** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to record details about the data involved in the change. Details may include definitions, relationships with other data, origin, format, and usage.

### 10.12.1 Purpose — Data Dictionary

A data dictionary is used to standardize a definition of a data element and enable a common interpretation of data elements.

### 10.12.2 Description — Data Dictionary

A data dictionary is used to document standard definitions of data elements, their meanings, and allowable values. A data dictionary contains definitions of each data element and indicates how those elements combine into composite data elements. Data dictionaries are used to standardize usage and meanings of data elements between solutions and between stakeholders.

Data dictionaries are sometimes referred to as metadata repositories and are used to manage the data within the context of a solution. As organizations adopt data mining and more advanced analytics, a data dictionary may provide the metadata required by these more complex scenarios. A data dictionary is often used in conjunction with an entity relationship diagram (see Data Modelling (p. 256)) and may be extracted from a data model.

Data dictionaries can be maintained manually (as a spreadsheet) or via automated tools.

**Figure 10.12.1: Example of a Data Dictionary**

|**Primitive Data**|**Data Element**|**Data Element**|**Data Element**|
|---|---|---|---|
|**Elements**|**1**|**2**|**3**|
|**Name** Name referenced by data elements|First Name|Middle Name|Last Name|
|**Alias** Alternate name referenced by stakeholders|Given Name|Middle Name|Surname|
|**Values/Meanings** Enumerated list or description of data element|Minimum 2 characters|Can be omitted|Minimum 2 characters|
|**Description** Definition|First Name|Middle Name|Family Name|
|**Composite**|**Customer Name =**|First Name + Middle N|ame + Family Name|

### 10.12.3 Elements — Data Dictionary

#### 10.12.3.1 Data Elements — Data Dictionary

Data dictionaries describe data element characteristics including the description of the data element in the form of a definition that will be used by stakeholders. Data dictionaries include standard definitions of data elements, their meanings, and allowable values. A data dictionary contains definitions of each primitive data element and indicates how those elements combine into composite data elements.

#### 10.12.3.2 Primitive Data Elements — Data Dictionary

The following information must be recorded about each data element in the data dictionary:

- **Name**: a unique name for the data element, which will be referenced by the composite data elements.

- **Aliases**: alternate names for the data element used by various stakeholders.

- **Values/Meanings**: a list of acceptable values for the data element. This may be expressed as an enumerated list or as a description of allowed formats for the data (including information such as the number of characters). If the values are abbreviated this will include an explanation of the meaning.

- **Description**: the definition of the data element in the context of the solution.

#### 10.12.3.3 Composite Elements — Data Dictionary

Composite data elements are built using data elements to build composite structures, which may include:

- **Sequences**: required ordering of primitive data elements within the composite structure. For example, a plus sign indicates that one element is followed by or concatenated with another element: Customer Name = First Name+Middle Name+Family Name.

- **Repetitions**: whether one or more data elements may be repeated multiple times.

- **Optional Elements**: may or may not occur in a particular instance of the composite element.

### 10.12.4 Usage Considerations — Data Dictionary

#### 10.12.4.1 Strengths — Data Dictionary

- Provides all stakeholders with a shared understanding of the format and content of relevant information.

- A single repository of corporate metadata promotes the use of data throughout the organization in a consistent manner.

#### 10.12.4.2 Limitations — Data Dictionary

- Requires regular maintenance, otherwise the metadata could become obsolete or incorrect.

- All maintenance is required to be completed in a consistent manner in order to ensure that stakeholders can quickly and easily retrieve the information they need. This requires time and effort on the part of the stewards responsible for the accuracy and completeness of the data dictionary.

- Unless care is taken to consider the metadata required by multiple scenarios, it may have limited value across the enterprise.

## 10.13 Data Flow Diagrams

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 250*

> **Where this technique is used — 10.13 Data Flow Diagrams** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **5.2 Maintain Requirements** (Requirements Life Cycle Management): used to identify information flow that may be similar across the enterprise in order to facilitate reuse.
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to visualize data flow requirements.

### 10.13.1 Purpose — Data Flow Diagrams

Data flow diagrams show where data comes from, which activities process the data, and if the output results are stored or utilized by another activity or external entity.

### 10.13.2 Description — Data Flow Diagrams

Data flow diagrams portray the transformation of data. They are useful for depicting a transaction-based system and illustrating the boundaries of a physical, logical, or manual system.

A data flow diagram illustrates the movement and transformation of data between externals (entities) and processes. The output from one external or process is the input to another. The data flow diagram also illustrates the temporary or permanent repositories (referred to as data stores or terminators) where data is stored within a system or an organization. The data defined should be described in a data dictionary (see Data Dictionary (p. 247)).

Data flow diagrams can consist of multiple layers of abstraction. The highest level diagram is a context diagram which represents the entire system. Context diagrams show the system in its entirety, as a transformation engine with externals as the source or consumer of data.

**Figure 10.13.1: Context Diagram Gane-Sarson Notation**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** External External · Agent Agent · Noun Noun · Output Data Output Data · Input Data Data Process Input Data · Verb/Noun · Phrase Naming · Input Data Input Data · External Output Data Output Data External · Agent Agent · Noun Noun

The next level of data flow diagrams is the level 1 diagram. Level 1 diagrams illustrate the processes related to the system with the respective input data, output transformed data, and data stores.

**Figure 10.13.2: Level 1 Diagram Yourdon Notation**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** External External · Agent Agent · Noun Output Data Noun · Noun · Data Data · Input Data · Noun Process Noun Process · Verb/Noun Verb/Noun · Input Data · Input Data Data Transformed Data Store Noun · Process · Noun Output Data · Verb/Noun · External External · Agent Agent · Noun Noun

Further levels of the data flow diagram (level 2, level 3 and so forth) break down the major processes from the level 1 diagram. Level 1 diagrams are useful to show the internal partitioning of the work and the data that flows between the partitions, as well as the stored data used by each of the partitions. Each of the partitions can be further decomposed if needed. The externals remain the same and additional flows and stores are defined.

Logical data flow diagrams represent the future or essential state—that is, what transformations need to occur regardless of the current physical limitations. Physical data flow diagrams model all of the data stores, printers, forms, devices, and other manifestations of data. The physical diagram can show either the current state or how it will be implemented.

### 10.13.3 Elements — Data Flow Diagrams

#### 10.13.3.1 Externals (Entity, Source, Sink) — Data Flow Diagrams

An external (entity, source, sink) is a person, organization, automated system, or any device capable of producing data or receiving data. An external is an object which is outside of the system under analysis. Externals are the sources and/or destinations (sinks) of the data. Each external must have at least one data flow going to or coming from it. Externals are represented by using a noun inside a rectangle and are found within context-level diagrams as well as lower levels of abstraction.

#### 10.13.3.2 Data Store — Data Flow Diagrams

A data store is a collection of data where data may be read repeatedly and where it can be stored for future use. In essence, it is data at rest. Each data store must have at least one data flow going to or coming from it. A data store is represented as either two parallel lines or as an open-ended rectangle with a label.

#### 10.13.3.3 Process — Data Flow Diagrams

A process can be a manual or automated activity performed for a business reason. A process transforms the data into an output. Naming standards for a process should contain a verb and a noun. Each process must have at least one data flow going to it and one data flow coming from it. A data process is represented as a circle or rectangle with rounded corners.

#### 10.13.3.4 Data Flow — Data Flow Diagrams

The movement of data between an external, a process, and a data store is represented by data flows. The data flows hold processes together. Every data flow will connect to or from a process (transformation of the data). Data flows show the inputs and outputs of each process. Every process transforms an input into an output. Data flows are represented as a line with an arrow displayed between processes. The data flow is named using a noun.

**Figure 10.13.3: Data Flow Diagram Gane-Sarson Notation**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** 1 2 · Input Data from Output Data from · parent diagram Process 1 Process 2 parent diagram · (System Input 1) Verb/Noun Verb/Noun (System Output 1) · Phrase Naming Phrase Naming · Input Data · Output Data · Data Store · Figure 10.13.4: Data Flow Diagram Yourdon Notation · External Input Data Store · Data Process · Agent Data · Output · Data

**Figure 10.13.4: Data Flow Diagram Yourdon Notation**

**10.13.4 Usage Considerations**

### 10.13.4 Usage Considerations — Data Flow Diagrams

#### 10.13.4.1 Strengths — Data Flow Diagrams

- May be used as a discovery technique for processes and data or as a Technique for the verification of functional decompositions or data models.

- Are excellent ways to define the scope of a system and all of the systems, interfaces, and user interfaces that attach to it. Allows for estimation of the effort needed to study the work.

- Most users find these data flow diagrams relatively easy to understand.

- Helps to identify duplicated data elements or misapplied data elements.

- Illustrates connections to other systems.

- Helps define the boundaries of a system.

- Can be used as part of system documentation.

- Helps to explain the logic behind the data flow within a system.

#### 10.13.4.2 Limitations — Data Flow Diagrams

- Using data flow diagrams for large-scale systems can become complex and difficult for stakeholders to understand.

- Different methods of notation with different symbols could create challenges pertaining to documentation.

- Does not illustrate a sequence of activities.

- Data transformations (processes) say little about the process or stakeholder.

## 10.14 Data Mining

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 253*

> **Where this technique is used — 10.14 Data Mining** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **4.1 Prepare for Elicitation** (Elicitation and Collaboration): used to identify information or patterns that require further investigation.
> - **4.2 Conduct Elicitation** (Elicitation and Collaboration): used to identify relevant information and patterns.
> - **6.1 Analyze Current State** (Strategy Analysis): used to obtain information on the performance of the enterprise.
> - **8.1 Measure Solution Performance** (Solution Evaluation): used to collect and analyze large amounts of data regarding solution performance.
> - **8.2 Analyze Performance Measures** (Solution Evaluation): used to collect data regarding performance, trends, common issues, and variances from expected performance levels and understand patterns and meaning in that data.
> - **8.3 Assess Solution Limitations** (Solution Evaluation): used to identify factors constraining performance of the solution.
> - **8.4 Assess Enterprise Limitations** (Solution Evaluation): used to identify factors constraining performance of the solution.
> - **8.5 Recommend Actions to Increase Solution Value** (Solution Evaluation): used to generate predictive estimates of solution performance.

### 10.14.1 Purpose — Data Mining

Data mining is used to improve decision making by finding useful patterns and insights from data.

### 10.14.2 Description — Data Mining

Data mining is an analytic process that examines large amounts of data from different perspectives and summarizes the data in such a way that useful patterns and relationships are discovered.

The results of data mining techniques are generally mathematical models or equations that describe underlying patterns and relationships. These models can be deployed for human decision making through visual dashboards and reports, or for automated decision-making systems through business rule management systems or in-database deployments.

Data mining can be utilized in either supervised or unsupervised investigations. In a supervised investigation, users can pose a question and expect an answer that can drive their decision making. An unsupervised investigation is a pure pattern discovery exercise where patterns are allowed to emerge, and then considered for applicability to business decisions.

Data mining is a general term that covers descriptive, diagnostic, and predictive techniques:

- **Descriptive**: such as clustering make it easier to see the patterns in a set of data, such as similarities between customers.

- **Diagnostic**: such as decision trees or segmentation can show why a pattern exists, such as the characteristics of an organization's most profitable customers.

- **Predictive**: such as regression or neural networks can show how likely something is to be true in the future, such as predicting the probability that a particular claim is fraudulent.

In all cases it is important to consider the goal of the data mining exercise and to be prepared for considerable effort in securing the right type, volume, and quality of data with which to work.

### 10.14.3 Elements — Data Mining

#### 10.14.3.1 Requirements Elicitation — Data Mining

The goal and scope of data mining is established either in terms of decision requirements for an important identified business decision, or in terms of a functional area where relevant data will be mined for domain-specific pattern discovery. This top-down versus a bottom-up mining strategy allows analysts to pick the correct set of data mining techniques.

Formal decision modelling techniques (see Decision Modelling (p. 265)) are used to define requirements for top-down data mining exercises. For bottom-up pattern discovery exercises it is useful if the discovered insight can be placed on existing decision models, allowing rapid use and deployment of the insight.

Data mining exercises are productive when managed as an agile environment. They assist rapid iteration, confirmation, and deployment while providing project controls.

#### 10.14.3.2 Data Preparation: Analytical Dataset — Data Mining

Data mining tools work on an analytical dataset. This is generally formed by merging records from multiple tables or sources into a single, wide dataset. Repeating groups are typically collapsed into multiple sets of fields. The data may be physically extracted into an actual file or it may be a virtual file that is left in the database or data warehouse so it can be analyzed. Analytical datasets are split into a set to be used for analysis, a completely independent set for confirming that the model developed works on data not used to develop it, and a validation set for final confirmation. Data volumes can be very large, sometimes resulting in the need to work with samples or to work in-datastore so that the data does not have to be moved around.

#### 10.14.3.3 Data Analysis — Data Mining

Once the data is available, it is analyzed. A wide variety of statistical measures are typically applied and visualization tools used to see how data values are distributed, what data is missing, and how various calculated characteristics behave. This step is often the longest and most complex in a data mining effort and is increasingly the focus of automation. Much of the power of a data mining effort typically comes from identifying useful characteristics in the data. For instance, a characteristic might be the number of times a customer has visited a store in the last 80 days. Determining that the count over the last 80 days is more useful than the count over the last 70 or 90 is key.

#### 10.14.3.4 Modelling Techniques — Data Mining

There are a wide variety of data mining techniques.

Some examples of data mining techniques are:

- classification and regression trees (CART), C5 and other decision tree analysis techniques,

- linear and logistic regression,

- neural networks,

- support sector machines, and

- predictive (additive) scorecards.

The analytical dataset and the calculated characteristics are fed into these algorithms which are either unsupervised (the user does not know what they are looking for) or supervised (the user is trying to find or predict something specific). Multiple techniques are often used to see which is most effective. Some data is held out from the modelling and used to confirm that the result can be replicated with data that was not used in the initial creation.

#### 10.14.3.5 Deployment — Data Mining

Once a model has been built, it must be deployed to be useful. Data mining models can be deployed in a variety of ways, either to support a human decision maker or to support automated decision-making systems. For human users, data mining results may be presented using visual metaphors or as simple data fields. Many data mining techniques identify potential business rules that can be deployed using a business rules management system. Such executable business rules can be fitted into a decision model along with expert rules as necessary. Some data mining techniques—especially those described as predictive analytic techniques—result in mathematical formulas. These can also be deployed as executable business rules but can also be used to generate SQL or code for deployment. An increasingly wide range of in-database deployment options allow such models to be integrated into an organization's data infrastructure.

### 10.14.4 Usage Considerations — Data Mining

#### 10.14.4.1 Strengths — Data Mining

- Reveal hidden patterns and create useful insight during analysis—helping determine what data might be useful to capture or how many people might be impacted by specific suggestions.

- Can be integrated into a system design to increase the accuracy of the data.

- Can be used to eliminate or reduce human bias by using the data to determine the facts.

#### 10.14.4.2 Limitations — Data Mining

- Applying some techniques without an understanding of how they work can result in erroneous correlations and misapplied insight.

- Access to big data and to sophisticated data mining tool sets and software may lead to accidental misuse.

- Many techniques and tools require specialist knowledge to work with.

- Some techniques use advanced math in the background and some stakeholders may not have direct insights into the results. A perceived lack of transparency can cause resistance from some stakeholders.

- Data mining results may be hard to deploy if the decision making they are intended to influence is poorly understood.

## 10.15 Data Modelling

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 256*

> **Where this technique is used — 10.15 Data Modelling** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **4.2 Conduct Elicitation** (Elicitation and Collaboration): used to understand entity relationships during elicitation.
> - **5.2 Maintain Requirements** (Requirements Life Cycle Management): used to identify data structure that may be similar across the enterprise in order to facilitate reuse.
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to model requirements to show how data will be used to meet stakeholder information needs.
> - **7.4 Define Requirements Architecture** (Requirements Analysis and Design Definition): used to describe the requirements structure as it relates to data.

### 10.15.1 Purpose — Data Modelling

A data model describes the entities, classes or data objects relevant to a domain, the attributes that are used to describe them, and the relationships among them to provide a common set of semantics for analysis and implementation.

### 10.15.2 Description — Data Modelling

A data model usually takes the form of a diagram that is supported by textual descriptions. It visually represents the elements that are important to the business (for example, people, places, things, and business transactions), the attributes associated with those elements, and the significant relationships among them. Data models are frequently used in elicitation and requirements analysis and design, as well as to support implementation and continuous improvement. There are several variations of data models:

- **Conceptual data model**: is independent of any solution or technology and can be used to represent how the business perceives its information. It can be used to help establish a consistent vocabulary describing business information and the relationships within that information.

- **Logical data model**: is an abstraction of the conceptual data model that incorporates rules of normalization to formally manage the integrity of the data and relationships. It is associated with the design of a solution.

- **Physical data model**: is used by implementation subject matter experts to describe how a database is physically organized. It addresses concerns like performance, concurrency, and security.

The conceptual, logical, and physical data models are developed for different purposes and may be significantly different even when depicting the same domain.

At the conceptual level, different data modelling notations are likely to produce broadly similar results and can be thought of as a single technique (as presented here). Logical and physical data models include elements specific to the solutions they support, and are generally developed by stakeholders with expertise in implementing particular technical solutions. For instance, logical and physical entity-relationship diagrams (ERDs) would be used to implement a relational database, whereas a logical or physical class diagram would be used to support object-oriented software development.

Object diagrams can be used to illustrate particular instances of entities from a data model. They can include actual sample values for the attributes, making object diagrams more concrete and more easily understood.

### 10.15.3 Elements — Data Modelling

#### 10.15.3.1 Entity or Class — Data Modelling

In a data model, the organization keeps data on entities (or classes or data objects). An entity may represent something physical (such as a Warehouse), something organizational (such as a Sales Area), something abstract (such as a Product Line), or an event (such as an Appointment). An entity contains attributes and has relationships to other entities in the model.

In a class diagram, entities are referred to as classes. Like an entity in a data model, a class contains attributes and has relationships with other classes. A class also contains operations or functions that describe what can be done with the class, such as generating an invoice or opening a bank account.

Each instance of an entity or class will have a unique identifier that sets it apart from other instances.

#### 10.15.3.2 Attribute — Data Modelling

An attribute defines a particular piece of information associated with an entity, including how much information can be captured in it, its allowable values, and the type of information it represents. Attributes can be described in a data dictionary (see Data Dictionary (p. 247)). Allowable values may be specified through business rules (see Business Rules Analysis (p. 240)).

Attributes can include such values as:

- **Name**: a unique name for the attribute. Other names used by stakeholders may be captured as aliases.

- **Values/Meanings**: a list of acceptable values for the attribute. This may be expressed as an enumerated list or as a description of allowed formats for the data (including information such as the number of characters). If the values are abbreviated this will include an explanation of the meaning.

- **Description**: the definition of the attribute in the context of the solution.

#### 10.15.3.3 Relationship or Association — Data Modelling

The relationships between entities provide structure for the data model, specifically indicating which entities relate to which others and how. Specifications for a relationship typically indicate the number of minimum and maximum occurrences allowed on each side of that relationship (for example, every customer is related to exactly one sales area, while a sales area may be related to zero, one, or many customers). The term cardinality is used to refer to the minimum and maximum number of occurrences to which an entity may be related. Typical cardinality values are zero, one, and many.

The relationship between two entities may be read in either direction, using this format:

_Each occurrence (of this entity) is related to (minimum, maximum) (of this other entity)._

In a class model, the term association is used instead of relationship and multiplicity is used instead of cardinality.

#### 10.15.3.4 Diagrams — Data Modelling

Both data models and class models may have one or more diagrams that show entities, attributes, and relationships.

The diagram in a data model is called an entity-relationship diagram (ERD). In a class model, the diagram is called a class diagram.

**Figure 10.15.1: Entity-Relationship Diagram (Crow's Foot Notation)**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Each entity is shown as a The unique identifier of the · rectangle with the entity entity is shown under the · name. entity name. · Entity 1 relationship left to right Entity 2 · Unique Identifier Unique Identifier · Attribute relationship right to left Attribute · Entity 3 Entity 4 · Unique Identifier Unique Identifier · Attribute 1 · Attribute · Attribute 2 · The attributes of the entity Relationships are indicated by · are listed below the unique a line, which is annotated to · identifier. show cardinality. · Cardinality · Entity Entity Entity Entity · Any number (zero Zero to One Only One Any number · to many) from one to · many

**Figure 10.15.2: Class Diagram (UML®)**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** The name of the class is listed here. It Relationships are indicated · may optionally have a stereotype which by a line, which may also show · defines additional properties. multiplicity. · «stereotype» Class 2 · Class 1 · Attribute 1 · Attribute 1: Attribute Type 1 0..* Attribute 2 · Attribute 2: Attribute Type Attribute 3 · Attribute 4 · Operation 1 · Operation 2 · Operation 3 · The attributes of the class are · listed in a box below the name. · Operations are listed below the · attributes. · Multiplicity · * X X..Y 1..* · Class Class Class Class · Any number Must be exactly X Any number Any number from · (zero to many) from X to Y one to many

#### 10.15.3.5 Metadata — Data Modelling

A data model optionally contains metadata describing what the entities represent, when and why they were created or changed, how they should be used, how often they are used, when, and by whom. There could be restrictions on their creation or use, as well as security, privacy, and audit constraints on specific entities or whole groups of entities.

### 10.15.4 Usage Considerations — Data Modelling

#### 10.15.4.1 Strengths — Data Modelling

- Can be used to define and communicate a consistent vocabulary used by domain subject matter experts and implementation subject matter experts.

- Review of a logical data model helps to ensure that the logical design of persistent data correctly represents the business need.

- Provides a consistent approach to analyzing and documenting data and its relationships.

- Offers the flexibility of different levels of detail, which provides just enough information for the respective audience.

- Formal modelling of the information held by the business may expose new requirements as inconsistencies are identified.

#### 10.15.4.2 Limitations — Data Modelling

- Following data modelling standards too rigorously may lead to models that are unfamiliar to people without a background in IT.

- May extend across multiple functional areas of the organization, and so beyond the business knowledge base of individual stakeholders.

## 10.16 Decision Analysis

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 261*

> **Where this technique is used — 10.16 Decision Analysis** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **5.3 Prioritize Requirements** (Requirements Life Cycle Management): used to identify high-value requirements.
> - **5.4 Assess Requirements Changes** (Requirements Life Cycle Management): used to facilitate the change assessment process.
> - **5.5 Approve Requirements** (Requirements Life Cycle Management): used to resolve issues and gain agreement.
> - **6.2 Define Future State** (Strategy Analysis): used to compare the different future state options and understand which is the best choice.
> - **6.3 Assess Risks** (Strategy Analysis): used to assess problems.
> - **6.4 Define Change Strategy** (Strategy Analysis): used to compare different change strategies and choose which is most appropriate.
> - **7.6 Analyze Potential Value and Recommend Solution** (Requirements Analysis and Design Definition): used to support the assessment and ranking of design options.
> - **8.1 Measure Solution Performance** (Solution Evaluation): used to assist stakeholders in deciding on suitable ways to measure solution performance and acceptable levels of performance.
> - **8.3 Assess Solution Limitations** (Solution Evaluation): used to illustrate the current business decisions and the changes required to achieve the potential value of the change.
> - **8.4 Assess Enterprise Limitations** (Solution Evaluation): used to assist in making an optimal decision under conditions of uncertainty and may be used in the assessment to make decisions about functional, technical, or procedural gaps.
> - **8.5 Recommend Actions to Increase Solution Value** (Solution Evaluation): used to determine the impact of acting on any of the potential value or performance issues.

### 10.16.1 Purpose — Decision Analysis

Decision analysis formally assesses a problem and possible decisions in order to determine the value of alternate outcomes under conditions of uncertainty.

### 10.16.2 Description — Decision Analysis

Decision analysis examines and models the possible consequences of different decisions about a given problem. A decision is the act of choosing a single course of action from several uncertain outcomes with different values. The outcome value may take different forms depending on the domain, but commonly include financial value, scoring, or a relative ranking dependent on the approach and evaluation criteria used by the business analyst.

Decisions are often difficult to assess when:

- the problem is poorly defined,

- the action leading to a desired outcome is not fully understood,

- the external factors affecting a decision are not fully understood, or

- the value of different outcomes is not understood or agreed upon by the various stakeholders and does not allow for direct comparison.

Decision analysis helps business analysts evaluate different outcome values under conditions of uncertainty or in highly complex situations. A variety of decision analysis approaches are available. The appropriate approach depends on the level of uncertainty, risk, quality of information, and available evaluation criteria. Effective decision analysis requires an understanding of:

- the values, goals, and objectives that are relevant to the decision problem,

- the nature of the decision that must be made,

- the areas of uncertainty that affect the decision, and

- the consequences of each potential decision.

Decision analysis approaches use the following activities:

1. **Define Problem Statement**: clearly describe the decision problem to be addressed.

2. **Define Alternatives**: identify possible propositions or courses of action.

3. **Evaluate Alternatives**: determine a logical approach to analyze the alternatives. An agreement of evaluation criteria can also be determined at the beginning of this activity.

4. **Choose Alternative to Implement**: the stakeholders responsible for making the decision choose which alternative will be implemented based on the decision analysis results.

5. **Implement Choice**: implement the chosen alternative.

There are a number of decision analysis tools available to assist the business analyst and decision makers in making objective decisions. Some of the tools and techniques are best for deciding between two alternatives, while others handle multiple alternatives.

Some general decision analysis tools and techniques include:

- pro versus con considerations,

- force field analysis,

- decision tables,

- decision trees,

- comparison analysis,

- analytical hierarchy process (AHP),

- totally-partially-not (TPN),

- multi-criteria decision analysis (MCDA), and

- computer-based simulations and algorithms.

### 10.16.3 Elements — Decision Analysis

#### 10.16.3.1 Components of Decision Analysis — Decision Analysis

General components of decision analysis include:

- **Decision to be Made or Problem Statement**: a description of what the decision question or problem is about.

- **Decision Maker**: person or people responsible for making the final decision.

- **Alternative**: a possible proposition or course of action.

- **Decision Criteria**: evaluation criteria used to evaluate the alternatives.

#### 10.16.3.2 Decision Matrices — Decision Analysis

The tables below provide examples of a a simple decision matrix and a weighted decision matrix.

A simple decision matrix checks whether or not each alternate meets each criterion being evaluated, and then totals the number of criteria matched for each alternate. In this example, Alternate 1 would likely be selected because it matches the most criteria.

**Table 10.16.1: Simple Decision Matrix**

||**Alternate 1**|**Alternate 2**|**Alternate 3**|
|---|---|---|---|
|**Criterion 1**|Meets criterion|n/a|n/a|
|**Criterion 2**|Meets criterion|Meets criterion|Meets criterion|
|**Criterion 3**|n/a|Meets criterion|Meets criterion|
|**Criterion 4**|Meets criterion|n/a|n/a|
|**Score**|3|2|2|

A weighted decision matrix assesses options in which each criterion is weighted based on importance. The higher the weighting, the more important the criterion. In this example, the criteria are weighted on a scale of 1-5, where 5 indicates the most important. The alternates are ranked per criterion on a scale of 1-5, where 5 indicates the best match. In this example, Alternate 3 would likely be selected due to its high weighted score.

**Table 10.16.2: Weighted Decision Matrix**

||**Criterion** **Weighting**|**Alternate 1**|**Alt 1** **Value**|**Alternate 2**|**Alt 2** **Value**|**Alternate 3**|**Alt 3** **Value**|
|---|---|---|---|---|---|---|---|
|**Criterion 1**|1|Rank = 1*3|3|Rank = 1*5|5|Rank = 1*2|2|
|**Criterion 2**|1|Rank = 1*5|5|Rank = 1*4|4|Rank = 1*3|8|
|**Criterion 3**|3|Rank = 3*5|15|Rank = 3*1|3|Rank = 3*5|15|
|**Criterion 4**|5|Rank = 5*1|5|Rank = 5*5|25|Rank = 5*3|15|
|**Weighted** **Score**|||28||37||40|

#### 10.16.3.3 Decision Trees — Decision Analysis

A decision tree is a method of assessing the preferred outcome where multiple sources of uncertainty may exist. A decision tree allows for assessment of responses to uncertainty to be factored across multiple strategies.

Decision trees include:

- **Decision Nodes**: that include different strategies.

- **Chance Nodes**: that define uncertain outcomes.

- **Terminator or End Nodes**: that identify a final outcome of the tree.

#### 10.16.3.4 Trade-offs — Decision Analysis

Trade-offs become relevant whenever a decision problem involves multiple, possibly conflicting, objectives. Because more than one objective is relevant, it is not sufficient to simply find the maximum value for one variable (such as the financial benefit for the organization). When making trade-offs, effective methods include:

- **Elimination of dominated alternatives**: a dominated alternative is any option that is clearly inferior to some other option. If an option is equal to or worse than some other option when rated against the objectives, the other option can be said to dominate it. In some cases, an option may also be dominated if it only offers very small advantages but has significant disadvantages.

- **Ranking objectives on a similar scale**: one method of converting rankings to a similar scale is proportional scoring. Using this method, the best outcome is assigned a rating of 100, the worst a rating of 0, and all other outcomes are given a rating based on where they fall between those two scores. If the outcomes are then assigned weights based on their relative importance, a score can be assigned to each outcome and the best alternative assigned using a decision tree.

### 10.16.4 Usage Considerations — Decision Analysis

#### 10.16.4.1 Strengths — Decision Analysis

- Provides business analysts with a prescriptive approach for determining alternate options, especially in complex or uncertain situations.

- Helps stakeholders who are under pressure to assess options based on criteria, thus reducing decisions based on descriptive information and emotions.

- Requires stakeholders to honestly assess the importance they place on different alternate outcomes in order to help avoid false assumptions.

- Enables business analysts to construct appropriate metrics or introduce relative rankings for outcome evaluation in order to directly compare both the financial and non-financial outcome evaluation criteria.

#### 10.16.4.2 Limitations — Decision Analysis

- The information to conduct proper decision analysis may not be available in time to make the decision.

- Many decisions must be made immediately, without the luxury of employing a formal or even informal decision analysis process.

- The decision maker must provide input to the process and understand the assumptions and model limitations. Otherwise, they may perceive the results provided by the business analyst as more certain than they are.

- Analysis paralysis can occur when too much dependence is placed on the decision analysis and in determining probabilistic values.

- Some decision analysis models require specialized knowledge (for example, mathematical knowledge in probability and strong skills with decision analysis tools).

## 10.17 Decision Modelling

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 265*

> **Where this technique is used — 10.17 Decision Modelling** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **6.2 Define Future State** (Strategy Analysis): used to model complex decisions regarding future state options.
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to represent decisions in a model in order to show the elements of decision making required.

### 10.17.1 Purpose — Decision Modelling

Decision modelling shows how repeatable business decisions are made.

### 10.17.2 Description — Decision Modelling

Decision models show how data and knowledge are combined to make a specific decision. Decision models can be used for both straightforward and complex decisions. Straightforward decision models use a single decision table or decision tree to show how a set of business rules that operate on a common set of data elements combine to create a decision. Complex decision models break down decisions into their individual components so that each piece of the decision can be separately described and the model can show how those pieces combine to make an overall decision. The information that needs to be available to make the decision and any sub-decisions can be decomposed. Each sub-decision is described in terms of the business rules required to make that part of the decision.

A comprehensive decision model is an overarching model that is linked to processes, performance measures, and organizations. It shows where the business rules come from and represents decisions as analytical insight.

The business rules involved in a given decision may be definitional or behavioural. For instance, a decision 'Validate order' might check that the tax amount is calculated correctly (a definitional rule) and that the billing address matches the credit card provided (a behavioural rule).

Decision tables and decision trees define how a specific decision is made. A graphical decision model can be constructed at various levels. A high-level model may only show the business decisions as they appear in business processes, while a more detailed model might show as-is or to-be decision making in enough detail to act as a structure for all the relevant business rules.

### 10.17.3 Elements — Decision Modelling

#### 10.17.3.1 Types of Models and Notations — Decision Modelling

There are several different approaches to decision modelling. Decision tables represent all the rules required to make an atomic decision. Decision trees are common in some industries, but are generally used much less often than decision tables. Complex decisions require the combination of multiple simple decisions into a network. This is shown using dependency or requirements notations.

All of these approaches involve three key elements:

- decision,

- information, and

- knowledge.

##### Decision Tables

Business decisions use a specific set of input values to determine a particular outcome by using a defined set of business rules to select one from the available outcomes. A decision table is a compact, tabular representation of a set of these rules. Each row (or column) is a rule and each column (or row) represents one of the conditions of that rule. When all the conditions in a particular rule evaluate to true for a set of input data, the outcome or action specified for that rule is selected.

Decision tables generally contain one or more condition columns that map to specific data elements, as well as one or more action or outcome columns. Each row can contain a specific condition in each condition column. These are evaluated against the value of the data element being considered. If all the cells in a rule are either blank or evaluate to true, the rule is true and the result specified in the action or outcome column occurs.

**Figure 10.17.1: Decision Table**

|**Eligibility Rules**|||
|---|---|---|
|**Loan Amount**|**Age**|**Eligibility**|
|<=1000|>18|Eligible|
||<=18|Ineligible|
|1000–2000|>21|Eligible|
||<=21|Ineligible|
|>2000|>=25|Eligible|
||<25|Ineligible|

##### Decision Trees

Decision trees are also used to represent a set of business rules. Each path on a decision tree leaf node is a single rule. Each level in the tree represents a specific data element; the downstream branches represent the different conditions that must be true to continue down that branch. Decision trees can be very effective for representing certain kinds of rule sets, especially those relating to customer segmentation.

As with decision tables, a decision tree selects one of the available actions or outcomes (a leaf node shown on the far right or bottom of the tree) based on the specific values passed to it by the data elements that represent the branching nodes.

In the following decision tree, the rules in the tree share conditions (represented by earlier nodes in the tree).

**Figure 10.17.2: Decision Tree**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Eligible · Age · Ineligible · Eligible · Amount 1000-2000 Age · Ineligible · Eligible · Age · Ineligible · <=18 · >=25 · >21 · <=21 · <25 · >18 · <=1000 · >2000

##### Decision Requirements Diagrams

A decision requirements diagram is a visual representation of the information, knowledge, and decision making involved in a more complex business decision.

Decision requirement diagrams contain the following elements:

- **Decisions**: shown as rectangles. Each decision takes a set of inputs and selects from a defined set of possible outputs by applying business rules and other decision logic.

- **Input Data**: shown as ovals, representing data that must be passed as an input to a decision on the diagram.

- **Business Knowledge Models**: shown as a rectangle with the corners cut off, representing sets of business rules, decision tables, decision trees, or even predictive analytic models that describe precisely how to make a decision.

- **Knowledge Sources**: shown as a document, representing the original source documents or people from which the necessary decision logic can be or has been derived.

These nodes are linked together into a network to show the decomposition of complex decision making into simpler building blocks. Solid arrows show the information requirements for a decision. These information requirements might link input data to a decision, to show that this decision requires that data to be available, or might link two decisions together.

Business knowledge models which describe how to make a specific decision can be linked to that decision with dashed arrows to display knowledge requirements. Knowledge sources can be linked to decisions with a dashed, rounded arrow to show that a knowledge source (for example, a document or person) is an authority for the decision. This is called an authority requirement.

**Figure 10.17.3: Decision Requirements Diagram**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Knowledge · Source · Business · Decision · Knowledge · Business · Decision Input Data · Knowledge · Input Data

### 10.17.4 Usage Considerations — Decision Modelling

#### 10.17.4.1 Strengths — Decision Modelling

- Decision models are easy to share with stakeholders, facilitate a shared understanding, and support impact analysis.

- Multiple perspectives can be shared and combined, especially when a diagram is used.

- Simplifies complex decision making by removing business rules management from the process.

- Assists with managing large numbers of rules in decision tables by grouping rules by decision. This also helps with reuse.

- These models work for rules-based automation, data mining, and predictive analytics, as well as for manual decisions or business intelligence projects.

#### 10.17.4.2 Limitations — Decision Modelling

- Adds a second diagram style when modelling business processes that contain decisions.This may add unnecessary complexity if the decision is simple and tightly coupled with the process.

- May limit rules to those required by known decisions and so limit the capture of rules not related to a known decision.

- Defining decision models may allow an organization to think it has a standard way of making decisions when it does not. May lock an organization into a current-state decision-making approach.

- Cuts across organizational boundaries, which can make it difficult to acquire any necessary sign-off.

- May not address behavioural business rules in a direct fashion.

- Business terminology must be clearly defined and shared definitions developed to avoid data quality issues affecting automated decisions.

## 10.18 Document Analysis

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 269*

> **Where this technique is used — 10.18 Document Analysis** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **3.1 Plan Business Analysis Approach** (Business Analysis Planning and Monitoring): used to review existing organizational assets that might assist in planning the approach.
> - **3.2 Plan Stakeholder Engagement** (Business Analysis Planning and Monitoring): used to review existing organizational assets that might assist in planning stakeholder engagement.
> - **3.3 Plan Business Analysis Governance** (Business Analysis Planning and Monitoring): used to evaluate existing governance processes or templates.
> - **4.1 Prepare for Elicitation** (Elicitation and Collaboration): used to identify and assess candidate sources of supporting materials.
> - **4.2 Conduct Elicitation** (Elicitation and Collaboration): used to review existing systems, contracts, business procedures and policies, standards, and regulations.
> - **4.3 Confirm Elicitation Results** (Elicitation and Collaboration): used to confirm elicitation results against source information or other existing documents.
> - **5.2 Maintain Requirements** (Requirements Life Cycle Management): used to analyze existing documentation about an enterprise that can serve as the basis for maintaining and reusing requirements.
> - **5.4 Assess Requirements Changes** (Requirements Life Cycle Management): used to analyze any existing documents that facilitate an understanding of the impact of the change.
> - **6.1 Analyze Current State** (Strategy Analysis): analyzes any existing documentation about the current state, including (but not limited to) documents created during the implementation of a solution, training manuals, issue reports, competitor information, supplier agreements, published industry benchmarks, published technology trends, and performance metrics.
> - **6.3 Assess Risks** (Strategy Analysis): used to analyze existing documents for potential risks, constraints, assumptions, and dependencies.
> - **7.3 Validate Requirements** (Requirements Analysis and Design Definition): used to identify previously documented business needs in order to validate requirements.
> - **7.5 Define Design Options** (Requirements Analysis and Design Definition): used to provide information needed to describe design options and design elements.
> - **8.4 Assess Enterprise Limitations** (Solution Evaluation): used to gain an understanding of the culture, operations, and structure of the organization.

### 10.18.1 Purpose — Document Analysis

Document analysis is used to elicit business analysis information, including contextual understanding and requirements, by examining available materials that describe either the business environment or existing organizational assets.

### 10.18.2 Description — Document Analysis

Document analysis may be used to gather background information in order to understand the context of a business need, or it may include researching existing solutions to validate how those solutions are currently implemented. Document analysis may also be used to validate findings from other elicitation efforts such as interviews and observations. Data mining is one approach to document analysis that is used to analyze data in order to determine patterns, group the data into categories, and determine opportunities for change. The purpose, scope, and topics to be researched through document analysis are determined based on the business analysis information being explored. When performing document analysis, business analysts methodically review the materials and determine whether the information should be recorded within a work product.

Background research gathered through document analysis may include reviewing materials such as marketing studies, industry guidelines or standards, company memos, and organizational charts. By researching a wide variety of source materials, the business analyst can ensure the need is fully understood in terms of the environment in which it exists. Document analysis about an existing solution may include reviewing business rules, technical documentation, training documentation, problem reports, previous requirements documents, and procedure manuals in order to validate both how the current solution works and why it was implemented in its current form. Document analysis can also help address information gaps that may occur when the subject matter experts (SMEs) for the existing solution are no longer present or will not be available for the duration of the elicitation process.

### 10.18.3 Elements — Document Analysis

#### 10.18.3.1 Preparation — Document Analysis

Document analysis materials may originate from public or proprietary sources. When assessing source documents for analysis, business analysts consider:

- whether or not the source’s content is relevant, current, genuine, and credible,

- whether or not the content is understandable and can be easily conveyed to stakeholders as needed, and

- defining both the data to be mined (based on the classes of data needed) and the data clusters that provide items grouped by logical relationships.

#### 10.18.3.2 Document Review and Analysis — Document Analysis

Performing document analysis includes:

- Conducting a detailed review of each document’s content and recording relevant notes associated with each topic. Notes can be recorded using a document analysis chart that includes the topic, type, source, verbatim details, a paraphrased critique, and any follow-up issues or actions for each document that is reviewed.

- Identifying if any notes conflict or are duplicates.

- Noting any gaps in knowledge in which the findings about certain topics are limited. It may be necessary to perform additional research to revisit these topics, or to drill down at a sub-topic level.

#### 10.18.3.3 Record Findings — Document Analysis

When the information elicited through document analysis is used in a work product, the business analyst considers:

- if the content and level of detail is appropriate for the intended audience, and

- if the material should be transformed into visual aids such as graphs, models, process flows, or decision tables in order to help improve understanding.

### 10.18.4 Usage Considerations — Document Analysis

#### 10.18.4.1 Strengths — Document Analysis

- Existing source material may be used as a basis for analysis.

- The business analyst does not need to create content.

- Existing sources, although possibly outdated, can be used as a point of reference to determine what is current and what has changed.

- Results can be used to validate against the results of other requirements elicitation techniques.

- Findings can be presented in formats that permit ease of review and reuse.

#### 10.18.4.2 Limitations — Document Analysis

- Existing documentation may be out of date or invalid (incorrect, missing information, unreadable, unreviewed or unapproved).

- Authors may not be available for questions.

- Primarily helpful only for evaluating the current state, via review of as-is documentation.

- If there is a wide range of sources, the effort may be very time-consuming and lead to information overload and confusion.

## 10.19 Estimation

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 271*

> **Where this technique is used — 10.19 Estimation** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **3.1 Plan Business Analysis Approach** (Business Analysis Planning and Monitoring): used to determine how long it may take to perform business analysis activities.
> - **4.1 Prepare for Elicitation** (Elicitation and Collaboration): used to estimate the time and effort required for the elicitation and the associated cost.
> - **5.3 Prioritize Requirements** (Requirements Life Cycle Management): used to produce estimates for the basis of prioritization.
> - **5.4 Assess Requirements Changes** (Requirements Life Cycle Management): used to determine the size of the change.
> - **6.4 Define Change Strategy** (Strategy Analysis): used to determine timelines for activities within the change strategy.
> - **7.6 Analyze Potential Value and Recommend Solution** (Requirements Analysis and Design Definition): used to forecast the costs and efforts of meeting the requirements as a step towards estimating their value.

### 10.19.1 Purpose — Estimation

Estimation is used by business analysts and other stakeholders to forecast the cost and effort involved in pursuing a course of action.

### 10.19.2 Description — Estimation

Estimation is used to support decision making by predicting attributes such as:

- cost and effort to pursue a • potential value anticipated from course of action, a solution, and

- expected solution benefits, • costs of creating a solution,

- project cost, • costs of operating a solution,

- business performance, • potential risk impact.

The result of estimation is sometimes expressed as a single number. Representing the results of estimation as a range, with minimum and maximum values along with probability, may present a higher degree of effectiveness for stakeholders. This range is referred to as a confidence interval and serves as a measure of the level of uncertainty. The less information that is available to the estimator, the wider the confidence interval will be.

Estimation is an iterative process. Estimates are reviewed as more information becomes available, and are also revised (if appropriate). Many estimation techniques rely on historical performance records from the organization in order to calibrate estimates against prior experience. Each estimate can include an assessment of its associated level of uncertainty.

### 10.19.3 Elements — Estimation

#### 10.19.3.1 Methods — Estimation

Various methods of estimation are used for specific situations. In each case it is important for the estimators to have an agreed-upon description of the elements to be estimated, often in the form of a work breakdown structure or some other decomposition of all the work being estimated. When developing and delivering an estimate, constraints and assumptions also need to be clearly communicated.

Common estimation methods include:

- **Top-down**: examining the components at a high level in a hierarchical breakdown.

- **Bottom-up**: using the lowest-level elements of a hierarchical breakdown to examine the work in detail and estimate the individual cost or effort, and then summing across all elements to provide an overall estimate.

- **Parametric Estimation**: use of a calibrated parametric model of the element attributes being estimated. It is important that the organization uses its own history to calibrate any parametric model, since the attribute values reflect the skills and abilities of both its staff and the processes used to do work.

- **Rough Order of Magnitude (ROM)**: a high-level estimate, generally based on limited information, which may have a very wide confidence interval.

- **Rolling Wave**: repeated estimates throughout an initiative or project, providing detailed estimates for near-term activities (such as an iteration of the work) extrapolated for the remainder of the initiative or project.

- **Delphi**: uses a combination of expert judgment and history. There are several variations on this process, but they all include individual estimates, sharing the estimates with experts, and having several rounds of estimation until consensus is reached. An average of the three estimates is used.

- **PERT**: each component of the estimate is given three values: (1) Optimistic value, representing the best-case scenario, (2) Pessimistic value, representing the worst-case scenario, (3) Most Likely value. Then a PERT value for each estimated component is computed as a weighted average: (Optimistic + Pessimistic + (4 times Most Likely))/6.

#### 10.19.3.2 Accuracy of the Estimate — Estimation

The accuracy of an estimate is a measure of uncertainty that evaluates how close an estimate is to the actual value measured later. It can be calculated as a ratio of the width of the confidence interval to its mean value and then expressed as a percentage. When there is little information, such as early in the development of a solution approach, a Rough Order of Magnitude (ROM) estimate is delivered, which is expected to have a wide range of possible values and a high level of uncertainty.

ROM estimates are often no more than +50% to -50% accurate. A definitive estimate, which is much more accurate, can be made as long as more real-world data is collected. Definitive estimates that are used for predicting timelines, final budgets, and resource needs should ideally be accurate within 10% or less.

Teams can combine the use of ROM estimates and definitive estimates throughout a project or initiative using rolling wave estimates. A team creates a definitive estimate for the next iteration or phase (for which they have adequate information), while the remainder of the work is given a ROM estimate. As the end of the iteration or phase approaches, a definitive estimate is made for the work of the next iteration or phase and the ROM estimate for remaining activities is refined.

#### 10.19.3.3 Sources of Information — Estimation

Estimators consider available information from prior experience along with the attributes being estimated.

Some common sources of information include:

- **Analogous Situations**: using an element (project, initiative, risk, or other) that is like the element being estimated.

- **Organization History**: previous experiences of the organization with similar work. This is most helpful if the prior work was done by the same or a similarly-skilled team and by using the same techniques.

- **Expert Judgment**: leveraging the knowledge of individuals about the element being estimated. Estimating often relies on the expertise of those who have performed the work in the past, internal or external to the organization. When using external experts, estimators take into account the relevant skills and abilities of those doing the work being estimated.

#### 10.19.3.4 Precision and Reliability of Estimates — Estimation

When multiple estimates are made for a particular attribute, the precision of the resulting estimate is a measure of agreement between the estimates (how close they are to each other). By examining measures of imprecision such as variance or standard deviation, estimators can determine their level of agreement.

The reliability of an estimate (its repeatability) is reflected in the variation of estimates made by different methods of estimating or by different estimators.

To illustrate the level of reliability and precision, an estimate is often expressed as a range of values with an associated confidence level. That is, for a given summary estimate value and confidence level, the range of values is the expected range of possible values based on the estimates provided. For example, if a team estimated that some task would take 40 hours, a 90% confidence interval might be 36 to 44 hours, depending on what they gave as individual estimates. A 95% confidence interval might be 38 to 42 hours. In general, the higher the confidence level in the estimate, the narrower the range would be.

To provide estimates with a particular level of confidence, estimators can use a technique such as PERT. Using the multiple estimates for each component of the estimate, a probability distribution can be constructed. This distribution provides a way to compute an overall estimate (incorporating all of the estimated elements) as a range of values, with an associated level of confidence.

#### 10.19.3.5 Contributors to Estimates — Estimation

The estimators of an element are frequently those responsible for that element. The estimate of a team is usually more accurate than the estimate of one individual, since it incorporates the expertise of all team members.

In some cases, an organization has a group that performs estimation for much of the work of the organization. This is done with care, so that the estimate reflects the likely context of the element being estimated.

When an organization needs a high level of confidence in the estimate of some critical element, it may call on an external expert to perform or review the estimate. The organization may compare an independent estimate against their internal estimate to determine what adjustments may be needed.

### 10.19.4 Usage Considerations — Estimation

#### 10.19.4.1 Strengths — Estimation

- Estimates provide a rationale for an assigned budget, time frame, or size of a set of elements.

- Without an estimate, teams making a change may be provided an unrealistic budget or schedule for their work.

- Having a small team of knowledgeable individuals provide an estimate by following a defined technique generally results in a closer predictor of the actual value than if an estimate was made by one individual.

- Updating an estimate throughout a work cycle, in which the estimated elements are refined over time, incorporates knowledge and helps ensure success.

#### 10.19.4.2 Limitations — Estimation

- Estimates are only as accurate as the level of knowledge about the elements being estimated. Without organization or local knowledge, estimates can vary widely from the actual values determined later.

- Using just one estimation method may lead stakeholders to have unrealistic expectations.

## 10.20 Financial Analysis

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 274*

> **Where this technique is used — 10.20 Financial Analysis** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **3.1 Plan Business Analysis Approach** (Business Analysis Planning and Monitoring): used to assess how different approaches (and the supported delivery options) affect the value delivered.
> - **5.3 Prioritize Requirements** (Requirements Life Cycle Management): used to assess the financial value of a set of requirements and how the timing of delivery will affect that value.
> - **5.4 Assess Requirements Changes** (Requirements Life Cycle Management): used to estimate the financial consequences of a proposed change.
> - **6.1 Analyze Current State** (Strategy Analysis): used to understand the profitability of the current state and the financial capability to deliver change.
> - **6.2 Define Future State** (Strategy Analysis): used to estimate the potential financial returns to be delivered by a proposed future state.
> - **6.3 Assess Risks** (Strategy Analysis): used to understand the potential effect of risks on the financial value of the solution.
> - **6.4 Define Change Strategy** (Strategy Analysis): used to understand the potential value associated with a change strategy, and evaluate strategies against targets set for return on investments.
> - **7.3 Validate Requirements** (Requirements Analysis and Design Definition): used to define the financial benefits associated with requirements.
> - **7.6 Analyze Potential Value and Recommend Solution** (Requirements Analysis and Design Definition): used to evaluate the financial return of different options and choose the best possible return on investment.
> - **8.5 Recommend Actions to Increase Solution Value** (Solution Evaluation): used to assess the potential costs and benefits of a change.

### 10.20.1 Purpose — Financial Analysis

Financial analysis is used to understand the financial aspects of an investment, a solution, or a solution approach.

### 10.20.2 Description — Financial Analysis

Financial analysis is the assessment of the expected financial viability, stability, and benefit realization of an investment option. It includes a consideration of the total cost of the change as well as the total costs and benefits of using and supporting the solution.

Business analysts use financial analysis to make a solution recommendation for an investment in a specific change initiative by comparing one solution or solution approach to others, based on analysis of the:

- initial cost and the time frame in which those costs are incurred,

- expected financial benefits and the time frame in which they will be incurred,

- ongoing costs of using the solution and supporting the solution,

- risks associated with the change initiative, and

- ongoing risks to business value of using that solution.

A combination of analysis techniques are typically used because each provides a different perspective. Executives compare the financial analysis results of one investment option with that of other possible investments to make decisions about which change initiatives to support.

Financial analysis deals with uncertainty, and as a change initiative progresses through its life cycle, the effects of that uncertainty become better understood. Financial analysis is continuously applied during the initiative to determine if the change is likely to deliver enough business value such that it should continue. A business analyst may recommend that a change initiative be adjusted or stopped if new information causes the financial analysis results to no longer support the initial solution recommendation.

### 10.20.3 Elements — Financial Analysis

#### 10.20.3.1 Cost of the Change — Financial Analysis

The cost of a change includes the expected cost of building or acquiring the solution components and the expected costs of transitioning the enterprise from the current state to the future state. This could include the costs associated with changing equipment and software, facilities, staff and other resources, buying out existing contracts, subsidies, penalties, converting data, training, communicating the change, and managing the roll out. These costs may be shared between organizations within the enterprise.

#### 10.20.3.2 Total Cost of Ownership (TCO) — Financial Analysis

The total cost of ownership (TCO) is the cost to acquire a solution, the cost of using the solution, and the cost of supporting the solution for the foreseeable future, combined to help understand the potential value of a solution. In the case of equipment and facilities, there is often a generally agreed to life expectancy. However, in the case of processes and software, the life expectancy is often unknown. Some organizations assume a standard time period (for example, three to five years) to understand the costs of ownership of intangibles like processes and software.

#### 10.20.3.3 Value Realization — Financial Analysis

Value is typically realized over time. The planned value could be expressed on an annual basis, or could be expressed as a cumulative value over a specific time period.

#### 10.20.3.4 Cost-Benefit Analysis — Financial Analysis

Cost-benefit analysis (sometimes called benefit-cost analysis) is a prediction of the expected total benefits minus the expected total costs, resulting in an expected net benefit (the planned business value).

Assumptions about the factors that make up the costs and benefits should be clearly stated in the calculations so they can be reviewed, challenged and approved. The costs and benefits will often be estimated based on those assumptions, and the estimating methodology should be described so that it can be reviewed and adjusted if necessary.

The time period of a cost-benefit analysis should look far enough into the future that the solution is in full use, and the planned value is being realized. This will help to understand which costs will be incurred and when, and when the expected value should be realized.

**Table 10.20.1: Example of a Cost-Benefit Analysis**

||**Year 0**|**Year 1**|**Year 2**|**Year 3**|
|---|---|---|---|---|
|**Expected Benefits**|||||
|Revenue||$XXXX|$XXXX|$XXXX|
|Reduced operating costs||$XXXX|$XXXX|$XXXX|
|Time savings||$XXXX|$XXXX|$XXXX|
|Reduced cost of errors||$XXXX|$XXXX|$XXXX|
|Increased customer satisfaction||$XXXX|$XXXX|$XXXX|
|Decreased cost of compliance||$XXXX|$XXXX|$XXXX|
|Other||$XXXX|$XXXX|$XXXX|
|**Total Annual benefits**|**$0**|**$XXXX**|**$XXXX**|**$XXXX**|
|**Costs**|||||
|Project costs|$XXXX|$XXXX|$0|$0|
|Ongoing support|$0|$XXXX|$XXXX|$XXXX|
|New facilities|$XXXX|$0|$0|$XXXX|
|Licensing|$0|$XXXX|$XXXX|$XXXX|
|Infrastructure renewal|$XXXX|$0|$XXXX|$0|
|Other|$0|$XXXX|$0|$XXXX|
|**Total Costs**|**$XXXX**|**$XXXX**|**$XXXX**|**$XXXX**|
|**Net Benefits**|**-$XXXX**|**$XXXX**|**$XXXX**|**$XXXX**|
|**Cumulative Net Benefits**|**-$XXXX**|**-$XXXX**|**-$XXXX**|**$XXXX**|

Some benefits may not be realized until future years. Some project and operating costs may be recognized in future years. The cumulative net benefits could be negative for some time until the future.

In some organizations, all or part of the costs associated with the change may be amortized over several years, and the organization may require the cost-benefit analysis to reflect this.

During a change initiative, as the expected costs become real costs, the business analyst may re-examine the cost-benefit analysis to determine if the solution or solution approach is still viable.

#### 10.20.3.5 Financial Calculations — Financial Analysis

Organizations use a combination of standard financial calculations to understand different perspectives about when and how different investments deliver value. These calculations take into consideration the inherent risks in different investments, the amount of upfront money to be invested compared to when the benefits will be realized, a comparison to other investments the organization could make, and the amount of time it will take to recoup the original investment.

Financial software, including spreadsheets, typically provide pre-programmed functions to correctly perform these financial calculations.

##### Return on Investment

The return on investment (ROI) of a planned change is expressed as a percentage measuring the net benefits divided by the cost of the change. One change initiative, solution, or solution approach may be compared to that of others to determine which one provides the greater overall return relative to the amount of the investment.

The formula to calculate ROI is:

_Return on Investment = (Total Benefits – Cost of the Investment) / Cost of the Investment._

The higher the ROI, the better the investment.

When making a comparison between potential investments, the business analyst should use the same time period for both.

##### Discount Rate

The discount rate is the assumed interest rate used in present value calculations. In general, this is similar to the interest rate that the organization would expect to earn if it invested its money elsewhere. Many organizations use a standard discount rate, usually determined by its finance officers, to evaluate potential investments such as change initiatives using the same assumptions about expected interest rates. Sometimes a larger discount rate is used for time periods that are more than a few years into the future to reflect greater uncertainty and risk.

##### Present Value

Different solutions and different solution approaches could realize benefits at different rates and over a different time. To objectively compare the effects of these different rates and time periods, the benefits are calculated in terms of present-day value. The benefit to be realized sometime in the future is reduced by the discount rate to determine its worth today.

The formula to calculate present value is:

_Present Value = Sum of (Net Benefits in that period / (1 + Discount Rate for that period)) for all periods in the cost-benefit analysis._

Present value is expressed in currency. The higher the present value, the greater the total benefit.

Present value does not consider the cost of the original investment.

##### Net Present Value

Net present value (NPV) is the present value of the benefits minus the original cost of the investment. In this way, different investments, and different benefit patterns can be compared in terms of present day value. The higher the NPV, the better the investment.

The formula to calculate net present value is:

_Net Present Value = Present Value – Cost of Investment_

Net present value is expressed in currency. The higher the NPV, the better the investment.

##### Internal Rate of Return

The internal rate of return (IRR) is the interest rate at which an investment breaks even, and is usually used to determine if the change, solution or solution approach is worth investing in. The business analyst may compare the IRR of one solution or solution approach to a minimum threshold that the organization expects to earn from its investments (called the hurdle rate). If the change initiative’s IRR is less than the hurdle rate, then the investment should not be made.

Once the planned investment passes the hurdle rate, it could be compared to other investments of the same duration. The investment with the higher IRR would be the better investment. For example, the business analyst could compare two solution approaches over the same time period, and would recommend the one with the higher IRR.

The IRR is internal to one organization since it does not consider external influencers such as inflation or fluctuating interest rates or a changing business context.

The IRR calculation is based on the interest rate at which the NPV is 0:

_Net Present Value = (-1 x Original Investment) + Sum of (net benefit for that period / (1 + IRR) for all periods) = 0._

##### Payback Period

The payback period provides a projection on the time period required to generate enough benefits to recover the cost of the change, irrespective of the discount rate. Once the payback period has passed the initiative would normally show a net financial benefit to the organization, unless operating costs rise. There is no standard formula for calculating the payback period. The time period is usually expressed in years or years and months.

### 10.20.4 Usage Considerations — Financial Analysis

#### 10.20.4.1 Strengths — Financial Analysis

- Financial analysis allows executive decision makers to objectively compare very different investments from different perspectives.

- Assumptions and estimates built into the benefits and costs, and into the financial calculations, are clearly stated so that they may be challenged or approved.

- It reduces the uncertainty of a change or solution by requiring the identification and analysis of factors that will influence the investment.

- If the context, business need, or stakeholder needs change during a change initiative, it allows the business analyst to objectively re-evaluate the recommended solution.

#### 10.20.4.2 Limitation — Financial Analysis

- Some costs and benefits are difficult to quantify financially.

- Because financial analysis is forward looking, there will always be some uncertainty about expected costs and benefits

- Positive financial numbers may give a false sense of security—they may not provide all the information required to understand an initiative.
