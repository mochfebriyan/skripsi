<!-- Knowledge file: Chapter 11 — Perspectives: The Business Intelligence Perspective -->
> **About this file.** Part of a cleaned, AI-ready edition of the BABOK® Guide v3 (IIBA, 2015). 
> **Covers:** 11.2 The Business Intelligence Perspective: change scope, business analysis scope, methodologies/approaches/techniques, underlying competencies, and impact on each knowledge area.  
> **Use this file when:** the question is about doing business analysis in a Business Intelligence context.
> **Sections:** 11.2 The Business Intelligence Perspective (p. 381)

# Chapter 11: Perspectives (continued)

## 11.2 The Business Intelligence Perspective

*BABOK® Guide v3 (IIBA, 2015) · Chapter 11 · p. 381*

The Business Intelligence Perspective highlights the unique characteristics of business analysis when practiced in the context of transforming, integrating, and enhancing data.

The focus of business intelligence is the transformation of data into value-added information: where to source it, how to integrate it, and how to enhance and deliver it as analytic insight to support business decision making.

Business intelligence initiatives apply data-centric system architectures as well as technologies and tools to deliver reliable, consistent, high-quality information that enables stakeholders to better manage strategic, tactical, and operational performance.

### 11.2.1 Change Scope — The Business Intelligence Perspective

#### 11.2.1.1 Breadth of Change — The Business Intelligence Perspective

A key objective of a business intelligence system is the consistent definition and usage of information throughout an organization by establishing a 'single point of truth' for diverse business data. A solution architecture that can integrate multiple data sources from within (and potentially from outside) the organization provides the foundation of a business intelligence solution.

**Figure 11.2.1: Business Intelligence Solution - Conceptual Framework**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Data Data Enterprise Decision Decision · Sources Integration Data View Support Points · EXTERNAL · SYSTEMS · Partner · Cyclical Reports · Industry · Public Operational Data Marts · Data Stores · INTERNAL Data Data Ad-hoc Queries · SYSTEMS Transformation Analytics · Corporate Data · Business Area Data Quality Warehouse Information · Ad-hoc, isolated Interactive · Management Delivery · Dashboards · OTHER · SOURCES · Conditional Alerts · Machine data Unstructured Analytical · Web data Data Sandboxes · Audio Visual · data · Documents & · Automated · text · Decision Data

The business intelligence promotes an enterprise-wide view of information management. To support that conceptual framework, a business intelligence initiative may also involve the development of infrastructure services in the organization, such as data governance and metadata management.

#### 11.2.1.2 Depth of Change — The Business Intelligence Perspective

Business intelligence initiatives focus on the information needed to support decision making at, or across, different levels within the organization:

- **executive level**: supports strategic decisions,

- **management level**: supports tactical decisions, or

- **process level**: supports operational decisions.

Where information needs are initially expressed or identified at a particular level, the business analyst investigates the business implications at other levels to assess the overall impact of the change on the organization.

At each level, the business needs may involve any or all of the following:

- communication requirements for the development of new reporting or the replacement of existing reporting,

- information requirements for the addition or extension of analytic functionality, and/or

- data integration requirements for the construction or modification of the enterprise data view with regard to data sources, definitions, transformation rules and quality issues.

#### 11.2.1.3 Value and Solutions Delivered — The Business Intelligence Perspective

The value of a business intelligence initiative is in its ability to provide timely, accurate, high value, and actionable information to those people and systems who can use it effectively in making business decisions.

Better informed decision making at all levels can lead to improved business performance in:

- strategic processes such as market analysis, customer engagement, and product development,

- tactical processes such as stock control and financial planning, and

- operational processes such as credit assessment, fault detection, and accounts payable monitoring.

These improvements in an organization’s current and future performance may be realized as increased revenues and reduced costs.

#### 11.2.1.4 Delivery Approach — The Business Intelligence Perspective

A business intelligence solution presents a range of delivery options to meet the emerging information needs of stakeholders and the priorities of the organization.

The extensibility and scalability of the solution architecture provide for the support of business decision making to be progressively introduced or enhanced:

- at different levels in the organization, from strategic (senior executive), through tactical (management), to operational (staff and systems), and

- in target functional areas in the organization, from a specific area through to an enterprise-wide implementation.

The infrastructure services that provide data management, analytics, and presentation capabilities, facilitate a phased or incremental development strategy in respect of:

- the inclusion, coordination and control of different data sources, and

- the analysis and development of business information and insights.

Infrastructure components of a business intelligence solution are often provided by a commercial off-the-shelf package configured to the specific business environment and needs.

#### 11.2.1.5 Major Assumptions — The Business Intelligence Perspective

The following is a list of major assumptions of a business intelligence initiative:

- existing business processes and transactional systems can provide source data that is definable and predictable,

- the cross-functional data infrastructure that is needed to support a business intelligence solution has not been precluded by the organization on technical, financial, political/cultural, or other grounds, and

- the organization recognizes that process re-engineering and change management might be needed in order to effectively realize the value from a business intelligence solution.

### 11.2.2 Business Analysis Scope — The Business Intelligence Perspective

#### 11.2.2.1 Change Sponsor — The Business Intelligence Perspective

The change sponsor of a business intelligence initiative is ideally the highest level role from the organizational unit affected by the change. This provides for a consistent, cohesive approach to the shared usage of data assets within the crossfunctional architecture of a business intelligence solution.

#### 11.2.2.2 Change Targets — The Business Intelligence Perspective

The targets of a business intelligence initiative are the business decisions made by people or processes at multiple levels in the organization that can be improved by better reporting, monitoring, or predictive modelling of performance-related data.

#### 11.2.2.3 Business Analyst Position — The Business Intelligence Perspective

As in other initiatives, the business analyst acts as the primary liaison between business intelligence stakeholders and solution providers in the elicitation, analysis, and specification of business needs.

In addition to that role, the business analyst may also participate in technical activities that are specific to business intelligence, including:

- enterprise data modelling,

- decision modelling,

- specialized presentation design (for example, dashboards), and

- ad hoc query design.

A business analyst working on a business intelligence initiative serves in one or in a combination of the following roles:

- business analyst who is competent in the definition of business requirements and the assessment of potential solutions,

- business intelligence functional analyst who has an understanding of data mining and predictive analytic techniques, as well as skills in developing visualizations,

- data analyst who is experienced at defining source systems data to be used for the required analytical purposes, or

- data modeller/architect who is skilled in defining the source and target data structures in logical data models.

#### 11.2.2.4 Business Analysis Outcomes — The Business Intelligence Perspective

In the business intelligence discipline, business analysis is focused on the major components of the solution architecture:

- the specification of business decisions to be influenced or changed,

- the collection of data from source systems,

- the integration of divergent sources into a convergent enterprise framework, and

- the provision of targeted information and analytic insight to business stakeholders.

The business analyst is responsible for the analysis and specification of the business requirements for all of these components and collaborates with technical specialists to assess solution artifacts.

The major outcomes of business analysis are:

- **Business process coverage**: defines the scope of the change with a highlevel overview of the business decisions within the enterprise that are to be supported by the solution. It identifies how the information output will be used and what value it will provide.

- **Decision models**: identify the information requirements of each business decision to be supported and specify the business rules logic of how the individual information components contribute to the decision outcome.

- **Source logical data model and data dictionary**: the source logical data model provides a standard definition of the required data as held in each source system. The source data dictionary provides a definition of each element and the business rules applied to it: business description, type, format and length, legal values, and any inter-dependencies.

- **Source data quality assessment**: evaluates the completeness, validity, and reliability of the data from source systems. It identifies where further verification and enhancement of source data is required to ensure consistent business definitions and rules apply across the enterprise-wide data asset.

- **Target logical data model and data dictionary**: the target logical data model presents an integrated, normalized view of the data structures required to support the business domain. The target data dictionary provides the standardized enterprise-wide definition of data elements and integrity rules.

- **Transformation rules**: map source and target data elements to specify requirements for the decoding/encoding of values and for data correction (error values) and enrichment (missing values) in the transformation process.

- **Business analytics requirements**: define the information and communication requirements for decision support outputs. These include:

- predefined reports,

- dashboards,

- balanced scorecards,

- ad hoc reports,

- online analytical processing (OLAP) queries,

- data mining,

- prescriptive analytics,

- conditional alerts,

- complex event processing, and

- predictive modelling.

- Specifications for each output can include: (1) data selections/dimensions, level of granularity, filtering criterion applied, possibilities for drill down, slice and dice, and user access and permissions; and (2) presentation rules to define data element format, translation (labels, look-ups), calculations, and data aggregations.

- **Solution architecture**: provides a high-level design view of how the decision support requirements of each functional area will map to the business intelligence framework. It is typically presented in the form of a process (or data flow) model that defines:

- where the source data is held,

- how (pull/push) and when (frequency, latency) the data will be extracted,

- where the transformations will take place (cleansing, encoding, enhancement),

- where the data will be physically stored (data warehouse, data marts), and

- how the data will flow to presentation outputs (reporting facilities, query tools).

### 11.2.3 Methodologies and Approaches — The Business Intelligence Perspective

#### 11.2.3.1 Methodologies — The Business Intelligence Perspective

There are no formalized business intelligence methodologies that impact the responsibilities and activities of the business analyst. However, a business intelligence initiative can operate within or alongside methodologies applicable to other disciplines or perspectives which themselves might impact the business analysis role.

#### 11.2.3.2 Approaches — The Business Intelligence Perspective

Within the business intelligence framework there are a number of less formal and potentially overlapping approaches that map to particular business and technical contexts.

##### Types of Analytics

There are three types of data analytics that represent incremental solutions, with increasing levels of systems complexity, cost, and value:

- **Descriptive analytics**: uses historical data to understand and analyze past business performance. Business information can be categorized and consolidated to best suit the stakeholder’s view including executive management dashboards, middle level management key performance indicator (KPI) scorecards, and operational level management charts. No assumptions are made as to which situations are of interest to the stakeholders, what decisions need to be made, or what actions might be carried out. The business analysis focus is on the information and communication requirements for standard reporting and dashboards, ad hoc reporting, and query functionality.

- **Predictive analytics**: applies statistical analysis methods to historical data to identify patterns, and then uses that understanding of relationships and trends to make predictions about future events. The particular situations that are of interest to the stakeholders are specified, and their business rules are defined. The business analysis focus is on the information requirements for pattern recognition through data mining, predictive modelling, forecasting, and condition-driven alerts.

- **Prescriptive analytics**: expands on predictive analytics to identify decisions to be made and to initiate appropriate action to improve business performance. Statistical optimization and simulation techniques can be used to determine the best solution or outcome among various choices. For situations of interest to stakeholders, full specification of the associated decisions and potential actions are required. The business analysis focus is on the business objectives, constraints criteria, and the business rules that underpin the decision-making process.

##### Supply and Demand Driven

The objectives and priorities of a business intelligence initiative can be based on the technical goals of improving existing information delivery systems (supplydriven) or on the business goals of providing the appropriate information to improve decision-making processes (demand-driven):

- **Supply-driven**: assumes the view of "for a given cost, what value can we deliver?". This approach maps existing systems data to define what data is available. A common implementation strategy would be to:

1. phase the inclusion of existing databases into the business intelligence solution architecture, 2. progressively replace or repair existing outputs, and 3. explore new insights that might be gained from the consolidated data.

- **Demand-driven**: assumes the view of "for a given value, what cost do we incur?". This approach starts with identifying the information output needed to support business decisions, and then tracing that information back to the underlying data sources to determine feasibility and cost. It provides for incremental implementation strategies that are not determined by existing database structures, and allows for early exploratory usage of business intelligence beyond existing reporting requirements.

##### Structured and Unstructured Data

There are two types of data that business intelligence approaches consider:

- **Structured data**: traditional data warehouse solutions have been based on consolidating the structured data (numerical and categorical) recorded in operational systems where business information sets are identified by predefined structures (referred to as 'schema on write') and where a rulesdriven template ensures data integrity. The business analysis focus is on data models, data dictionaries, and business rules to define information requirements and capabilities.

- **Unstructured data**: business intelligence solutions can include semistructured or unstructured data which includes text, images, audio, and video. This data frequently comes from external sources. For this type of data, the structure and relationships are not predefined and no specific organization rules have been applied to ensure data integrity. Information sets are derived from the raw data (referred to as 'schema on read'). The business analysis focus is on metadata definitions and data matching algorithms to define information requirements and capabilities.

### 11.2.4 Underlying Competencies — The Business Intelligence Perspective

As in any business analysis discipline, the business analyst requires the fundamental communication and analytical competencies to be effective in liaising with both business stakeholders and technical solution providers.

In the business intelligence discipline, this coordination of business information requirements with business intelligence systems outcomes can be further enhanced by the business analyst’s specific competencies in:

- business data and functional usage, including terminology and rules,

- the analysis of complex data structures and their translation into standardized format,

- business processes affected including KPIs and metrics,

- decision modelling,

- data analysis techniques including basic statistics, data profiling,and pivoting,

- data warehouse and business intelligence concepts and architecture,

- logical and physical data models,

- ETL (Extract, Transform, Load) best practices including historical data track and reference data management, and

- business intelligence reporting tools.

### 11.2.5 Impact on Knowledge Areas — The Business Intelligence Perspective

This section explains how specific business analysis practices within business intelligence are mapped to business analysis tasks and practices as defined by the *BABOK® Guide*. This section describes how each knowledge area is applied or modified with the business intelligence discipline.

Each knowledge area lists techniques relevant to a business intelligence perspective. Techniques used in the discipline of business intelligence do not deviate, to any great extent, from the *BABOK® Guide* techniques. *BABOK® Guide* techniques are found in the Techniques chapter of the *BABOK® Guide*. This is not intended to be an exhaustive list of techniques but rather to highlight the types of techniques used by business analysts while performing the tasks within the knowledge area.

#### 11.2.5.1 Business Analysis Planning and Monitoring — The Business Intelligence Perspective

A business intelligence initiative may require establishing an underlying data infrastructure to support the solution, or it might be an enhancement based on the infrastructure of an existing solution. Scope Modelling is frequently used to differentiate between these alternatives and plan the relevant business analysis activities accordingly.

The business intelligence paradigm of information delivery might be a new, unfamiliar approach for business stakeholders and for the business analysts themselves. In planning the initiative, the business analyst considers:

- how experienced the stakeholders are in expressing their information and communication requirements in the business intelligence context, and

- how skilled the business analysts are in interpreting those requirements into detailed specifications for business intelligence technical specialists.

Business intelligence solutions typically provide frameworks, tools, and techniques that can assist in requirements definition and solution modelling. The level of stakeholders’ and business analysts’ expertise in these can have an impact on the planned approach.

When assessing stakeholder attitudes towards the business intelligence initiative, the business analyst should be aware that an enterprise-wide business intelligence solution might not provide direct value to some operational stakeholders, but will deliver it elsewhere in the organization, and the flexibility and extensibility provided by the business intelligence infrastructure delivers longer-term strategic value that goes beyond short-term operational benefits.

A business intelligence solution that integrates multiple data sources typically engages many stakeholders with overlapping information requirements. Business analysts prepare for the analysis and synthesis of individual requirements into a set that is complete and cohesive without conflicts and redundancies.

##### BABOK® Guide Techniques

- Acceptance and Evaluation Criteria (p. 217)

- Balanced Scorecard (p. 223)

- Brainstorming (p. 227)

- Decision Analysis (p. 261)

- Estimation (p. 271)

- Functional Decomposition (p. 283)

- Interviews (p. 290)

- Item Tracking (p. 294)

- Metrics and Key Performance Indicators (KPIs) (p. 297)

- Risk Analysis and Management (p. 329)

- Roles and Permissions Matrix (p. 333)

- Root Cause Analysis (p. 335)

- Scope Modelling (p. 338)

- Stakeholder List, Map, or Personas (p. 344)

- Survey or Questionnaire (p. 350)

- Use Cases and Scenarios (p. 356)

- User Stories (p. 359)

- Workshops (p. 363)

- Non-Functional Requirements Analysis (p. 302)

- Organizational Modelling (p. 308)

- Prioritization (p. 311)

- Process Modelling (p. 318)

- Reviews (p. 326)

#### 11.2.5.2 Elicitation and Collaboration — The Business Intelligence Perspective

The cross-functional nature of business intelligence typically requires business analysts to employ specialized documentation tools and techniques to elicit particular types of requirements from stakeholders, both business and technical.

Individual stakeholders may only possess partial knowledge and expertise regarding:

- the business decisions that need support,

- the data elements that support those business decisions,

- the data sourcing, transformation, and integration rules, and

- the presentation of the required information.

Interviews with individual stakeholders identify the information and analytic insight required to support their decision making. Workshops with stakeholders from across different functional areas of the business can help detect common, overlapping information requirements that would be better met with an integrated solution.

Data models and data dictionaries provide definitions of the structure and business rules of existing systems data. The business analyst assesses available documentation to identify incompleteness of a model or inconsistencies between models.

Process models that are extended to include data artifacts can help identify the data sources required at decision points. Decision models specify the data analytic requirements and business rules for decisions.

Commercial off-the-shelf packages of business intelligence functionality can provide the business analyst with a set of highly effective prototyping tools to elicit and clarify stakeholder information and communication requirements.

##### BABOK® Guide Techniques

- Brainstorming (p. 227) • Item Tracking (p. 294)

- Document Analysis (p. 269) • Observation (p. 305)

- Focus Groups (p. 279)

- Prototyping (p. 323)

- Functional Decomposition (p. 283)

- Workshops (p. 363)

- Glossary (p. 286) • Stakeholder List, Map, or Personas (p. 344)

- Interface Analysis (p. 287)

- Survey or Questionnaire (p. 350)

- Interviews (p. 290)

- **.3 Requirements Life Cycle Management**

The architectural nature of the business intelligence discipline requires establishing the infrastructure capabilities in the solution. This can introduce structural dependencies within the solution, particularly where delivery is phased, that affect the prioritization of individual business needs. It is often possible to achieve efficiencies by implementing related requirements at the same time.

##### BABOK® Guide Techniques

- Item Tracking (p. 294) • Roles and Permissions Matrix (p. 333)

- Organizational Modelling (p. 308)

- Stakeholder List, Map, or Personas (p. 344)

- Prioritization (p. 311)

- Reviews (p. 326)

- Workshops (p. 363)

#### 11.2.5.4 Strategy Analysis — The Business Intelligence Perspective

Business analysts can use high-level conceptual data models to map the current state of corporate information, to identify information silos, and to assess their related problems and opportunities. Organization Modelling can be used to evaluate any current data management infrastructure, such as metadata management and data governance.

In defining the future state strategy, business analysts can use high-level models to map the architecture for data storage and for data conveyance and transformation:

- **Logical data models**: provide a static view of the solution architecture, representing the information portal that connects the sourcing of operational data inputs with the delivery of the business information outputs.

- **Data flow diagrams**: are commonly used to map the dynamic aspects of the solution (data-in-motion) and to identify other architectural constructs such as latency and accessibility.

- **Decision models**: are useful for defining how relevant business decisions are made and where and how data analytics can be effectively used to meet these needs.

- **Physical data models**: show the implementation environment including the data warehouse and data marts.

The extensible architecture provided by business intelligence solutions can support incremental implementation across different functional areas of the business. Business analysts can define change strategy options based on business needs and priorities, impact on the business operations, and the usability of existing infrastructure components.

##### BABOK® Guide Techniques

- Backlog Management (p. 220)

- Benchmarking and Market Analysis (p. 226)

- Brainstorming (p. 227)

- Business Rules Analysis (p. 240)

- Data Flow Diagrams (p. 250)

- Data Modelling (p. 256)

- Decision Analysis (p. 261)

- Decision Modelling (p. 265)

- Document Analysis (p. 269)

- Estimation (p. 271)

- Focus Groups (p. 279)

- Functional Decomposition (p. 283)

- Glossary (p. 286)

- Organizational Modelling (p. 308)

- Risk Analysis and Management (p. 329)

- Root Cause Analysis (p. 335)

- Stakeholder List, Map, or Personas (p. 344)

- SWOT Analysis (p. 353)

#### 11.2.5.5 Requirements Analysis and Design Definition — The Business Intelligence Perspective

When modelling and specifying back office data capture and storage requirements, business analysts use specific data-oriented modelling techniques such as Data Modelling, Data Dictionary, Decision Modelling, and Business Rules Analysis.

Models of an existing system's data help to define data availability and identify redundancies, inconsistencies, and data quality issues. Where existing systems documentation is non-existent or out of date, reverse-engineered modelling can be a substantial component of work, and frequently requires collaboration with technical experts such as database administrators and application programmers.

A future state data model demonstrates how the source information is generically structured in the proposed solution. The overall transformation process is commonly modelled using Data Flow Diagrams to illustrate the management of latency and accessibility requirements in the solution. Business analysts define specific business rules for data integrity checking and for data transformation.

For modelling and specifying front office information outputs, business analysts:

- analyze existing reports to determine if they are candidates to be replaced or repaired with business intelligence outputs, and

- use business intelligence capabilities such as ad hoc queries, data mining, and complex event processing to identify and specify the content and format of new business intelligence outputs.

Business analysts are involved in assessing the capability of a proposed solution (typically a commercial off-the-shelf software package) in respect of the specified requirements. In the business intelligence context, these include functional requirements such as self-serve facilities, data analytics tools, data presentation tools, drill down capabilities, and non-functional requirements related to issues such as data quality, data latency, and query performance.

**.6 BABOK**® **Guide Techniques**

- Acceptance and Evaluation Criteria (p. 217)

- Balanced Scorecard (p. 223)

- Business Rules Analysis (p. 240)

- Data Dictionary (p. 247)

- Data Flow Diagrams (p. 250)

- Data Modelling (p. 256)

- Decision Modelling (p. 265)

- Document Analysis (p. 269)

- Functional Decomposition (p. 283)

- Glossary (p. 286)

- Interface Analysis (p. 287)

- Interviews (p. 290)

- Metrics and Key Performance Indicators (KPIs) (p. 297)

- Non-Functional Requirements Analysis (p. 302)

- Observation (p. 305)

- Organizational Modelling (p. 308)

- Prioritization (p. 311)

- Process Modelling (p. 318)

- Prototyping (p. 323)

- Reviews (p. 326)

- Scope Modelling (p. 338)

- Sequence Diagrams (p. 341)

- Stakeholder List, Map, or Personas (p. 344)

- State Modelling (p. 348)

- Use Cases and Scenarios (p. 356)

- Vendor Assessment (p. 361)

#### 11.2.5.7 Solution Evaluation — The Business Intelligence Perspective

A common enterprise limitation with the introduction of a business intelligence solution is the under-utilization of the information resource and analytic functionality that the solution provides. Stakeholders who are not familiar with the capabilities of business intelligence might focus on simply replacing or repairing existing information outputs. Business analysts explore and evaluate opportunities for additional value that are enabled by a business intelligence solution.

#### 11.2.5.8 BABOK® Guide Techniques — The Business Intelligence Perspective

- Acceptance and Evaluation Criteria (p. 217)

- Balanced Scorecard (p. 223)

- Business Rules Analysis (p. 240)

- Data Flow Diagrams (p. 250)

- Data Modelling (p. 256)

- Decision Analysis (p. 261)

- Decision Modelling (p. 265)

- Estimation (p. 271)

- Focus Groups (p. 279)

- Functional Decomposition (p. 283)

- Glossary (p. 286)

- Interviews (p. 290)

- Item Tracking (p. 294)

- Metrics and Key Performance Indicators (KPIs) (p. 297)

- Observation (p. 305)

- Organizational Modelling (p. 308)

- Prioritization (p. 311)

- Process Modelling (p. 318)

- Risk Analysis and Management (p. 329)

- Stakeholder List, Map, or Personas (p. 344)

- Survey or Questionnaire (p. 350)

- SWOT Analysis (p. 353)

- Use Cases and Scenarios (p. 356)

- User Stories (p. 359)

- Vendor Assessment (p. 361)
