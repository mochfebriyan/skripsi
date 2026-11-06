<!-- Knowledge file: Chapter 5 — Knowledge Area: Requirements Life Cycle Management -->
> **About this file.** Part of a cleaned, AI-ready edition of the BABOK® Guide v3 (IIBA, 2015). 
> **Covers:** Knowledge Area overview, Core Concept Model table, and the full text of every task: 5.1 Trace Requirements; 5.2 Maintain Requirements; 5.3 Prioritize Requirements; 5.4 Assess Requirements Changes; 5.5 Approve Requirements. Each task starts with a Task Summary Card (inputs with their producing tasks, guidelines/tools, techniques, stakeholders, outputs with consuming tasks).  
> **Use this file when:** the question concerns any of these tasks, their inputs/outputs, elements, or which techniques/stakeholders apply in Requirements Life Cycle Management.
> **Sections:** 5.1 Trace Requirements (p. 79); 5.2 Maintain Requirements (p. 83); 5.3 Prioritize Requirements (p. 86); 5.4 Assess Requirements Changes (p. 91); 5.5 Approve Requirements (p. 95)

# Chapter 5: Requirements Life Cycle Management

*Source: BABOK® Guide v3 (IIBA, 2015), starts p. 75*

The Requirements Life Cycle Management knowledge area describes the tasks that business analysts perform in order to manage and maintain requirements and design information from inception to retirement. These tasks describe establishing meaningful relationships between related requirements and designs, assessing changes to requirements and designs when changes are proposed, and analyzing and gaining consensus on changes.

The purpose of requirements life cycle management is to ensure that business, stakeholder, and solution requirements and designs are aligned to one another and that the solution implements them. It involves a level of control over requirements and over how requirements will be implemented in the actual solution to be constructed and delivered. It also helps to ensure that business analysis information is available for future use.

The requirements life cycle:

- begins with the representation of a business need as a requirement,

- continues through the development of a solution, and

- ends when a solution and the requirements that represent it are retired.

The management of requirements does not end once a solution is implemented. Throughout the life of a solution, requirements continue to provide value when they are managed appropriately.

Within the Requirements Life Cycle Management knowledge area, the concept of a life cycle is separate from a methodology or process used to govern business analysis work. Life cycle refers to the existence of various phases or states that requirements pass through as part of any change. Requirements may be in multiple states at one time.

The states listed here are not intended to be a comprehensive listing.

**Figure 5.0.1: Requirements Life Cycle Management**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Bring Forward · Manage · Yes Approval/ Yes Trace · Assess Maintain · Consensus · Prioritize · No No · Potential · Requirement

The Requirements Life Cycle Management knowledge area includes the following tasks:

- **Trace Requirements**: analyzes and maintains the relationships between requirements, designs, solution components, and other work products for impact analysis, coverage, and allocation.

- **Maintain Requirements**: ensures that requirements and designs are accurate and current throughout the life cycle and facilitates reuse where appropriate.

- **Prioritize Requirements**: assesses the value, urgency, and risks associated with particular requirements and designs to ensure that analysis and/or delivery work is done on the most important ones at any given time.

- **Assess Requirements Changes**: evaluates new and changing stakeholder requirements to determine if they need to be acted on within the scope of a change.

- **Approve Requirements**: works with stakeholders involved in the governance process to reach approval and agreement on requirements and designs.

## The Core Concept Model in Requirements Life Cycle Management

The _Business Analysis Core Concept Model™_ (_BACCM™_) describes the relationships among the six core concepts.

The following table describes the usage and application of each of the core concepts within the context of Requirements Life Cycle Management.

**Table 5.0.1: The Core Concept Model in Requirements Life Cycle Management**

|**Core Concept**|**During Requirements Life Cycle** **Management, business analysts...**|
|---|---|
|**Change**: the act of transformation in response to a need.|manage how proposed changes to requirements and designs are evaluated during an initiative.|
|**Need**: a problem or opportunity to be addressed.|trace, prioritize and maintain requirements to ensure that the need is met.|
|**Solution**: a specific way of satisfying one or more needs in a context.|trace requirements and designs to solution components to ensure that the solution satisfies the need.|
|**Stakeholder**: a group or individual with a relationship to the change, the need, or the solution.|work closely with key stakeholders to maintain understanding, agreement, and approval of requirements and designs.|
|**Value**: the worth, importance, or usefulness of something to a stakeholder within a context.|maintain requirements for reuse to extend value beyond the current initiative.|
|**Context**: the circumstances that influence, are influenced by, and provide understanding of the change.|analyze the context to support tracing and prioritization activities.|

**Figure 5.0.1: Requirements Life Cycle Management Input/Output Diagram**

> *(Knowledge-area Input/Output diagram: the inputs, guidelines/tools and outputs of every task in this chapter are listed in the Task Summary Card at the top of each task below, and the full output→task flow is in B_Techniques_to_Task_Mapping_REBUILT.md.)*

## 5.1 Trace Requirements

*BABOK® Guide v3 (IIBA, 2015) · Chapter 5 · p. 79*

> **Task Summary Card — 5.1 Trace Requirements** (Knowledge Area: Requirements Life Cycle Management; reconstructed from the task text and its Input/Output diagram)
> - **Inputs:** Requirements; Designs
> - **Guidelines and Tools:** Domain Knowledge; Information Management Approach *(produced by 3.4)*; Legal/Regulatory Information; Requirements Management Tools/Repository
> - **Techniques:** Business Rules Analysis; Functional Decomposition; Process Modelling; Scope Modelling
> - **Stakeholders:** Customers; Domain Subject Matter Expert; End User; Implementation Subject Matter Expert; Operational Support; Project Manager; Sponsor; Suppliers; Tester
> - **Outputs:** Requirements (traced) *(input to 5.2, 5.3, 5.4, 5.5, 6.3, 7.2, 7.3, 7.4, 7.5; guideline/tool for 7.5, 8.1)*; Designs (traced) *(input to 5.2, 5.3, 5.4, 5.5)*

### 5.1.1 Purpose — Trace Requirements

The purpose of Trace Requirements is to ensure that requirements and designs at different levels are aligned to one another, and to manage the effects of change to one level on related requirements.

### 5.1.2 Description — Trace Requirements

Requirements traceability identifies and documents the lineage of each requirement, including its backward traceability, its forward traceability, and its relationship to other requirements. Traceability is used to help ensure that the solution conforms to requirements and to assist in scope, change, risk, time, cost, and communication management. It is also used to detect missing functionality or to identify if there is implemented functionality that is not supported by any requirement.

Traceability enables:

- faster and simpler impact analysis,

- more reliable discovery of inconsistencies and gaps in requirements,

- deeper insights into the scope and complexity of a change, and

- reliable assessment of which requirements have been addressed and which have not.

It is often difficult to accurately represent needs and solutions without taking into account the relationships that exist between them. While traceability is valuable, the business analyst balances the number of relationship types with the benefit gained by representing them. Traceability also supports both requirements allocation and release planning by providing a direct line of sight from requirement to expressed need.

The following images show examples of visual representations of traceability for a process and for software requirements.

**Figure 5.1.1: Process Traceability**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Value Chain · Business · Process · Sub-process · Activity · Task

**Figure 5.1.2: Software Requirements Traceability**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Business Needs · Business · Requirements · Design · Stakeholder · Requirements Code · Solution · Test · Requirements

### 5.1.3 Inputs — Trace Requirements

- **Requirements**: may be traced to other requirements (including goals, objectives, business requirements, stakeholder requirements, solution requirements, and transition requirements), solution components, visuals, business rules, and other work products.

- **Designs**: may be traced to other requirements, solution components, and other work products.

**Figure 5.1.3: Trace Requirements Input/Output Diagram**

> *(Diagram: inputs, guidelines/tools and outputs of this task — see the Task Summary Card at the top of this task and the Inputs/Outputs sections.)*

### 5.1.4 Elements — Trace Requirements

#### 5.1.4.1 Level of Formality — Trace Requirements

When tracing requirements, business analysts consider the value that each link is supposed to deliver, as well as the nature and use of the specific relationships that are being created.

The effort to trace requirements grows significantly when the number of requirements or level of formality increases.

#### 5.1.4.2 Relationships — Trace Requirements

There are several types of relationships that the business analyst considers when defining the traceability approach:

- **Derive**: relationship between two requirements, used when a requirement is derived from another requirement. This type of relationship is appropriate to link the requirements on different levels of abstraction. For example, a solution requirement derived from a business or a stakeholder requirement.

- **Depends**: relationship between two requirements, used when a requirement depends on another requirement. Types of dependency relationships include:

- **Necessity**: when it only makes sense to implement a particular requirement if a related requirement is also implemented.

- **Effort**: when a requirement is easier to implement if a related requirement is also implemented.

- **Satisfy**: relationship between an implementation element and the requirements it is satisfying. For example, the relationship between a functional requirement and a solution component that is implementing it.

- **Validate**: relationship between a requirement and a test case or other element that can determine whether a solution fulfills the requirement.

#### 5.1.4.3 Traceability Repository — Trace Requirements

Requirements traceability is documented and maintained in accordance with the methods identified by the business analysis approach. Requirements management tools can provide significant benefits when there is a need to trace a large number of requirements that may be deemed unmanageable with manual approaches.

### 5.1.5 Guidelines and Tools — Trace Requirements

- **Domain Knowledge**: knowledge of and expertise in the business domain needed to support traceability.

- **Information Management Approach**: provides decisions from planning activities concerning the traceability approach.

- **Legal/Regulatory Information**: describes legislative rules or regulations that must be followed. These may need to be considered when defining traceability rules.

- **Requirements Management Tools/Repository**: used to store and manage business analysis information. The tool may be as simple as a text document or as complex as a dedicated requirements management tool.

### 5.1.6 Techniques — Trace Requirements

- **Business Rules Analysis**: used to trace business rules to requirements that they support, or rules that support requirements.

- **Functional Decomposition**: used to break down solution scope into smaller components for allocation, as well as to trace high-level concepts to low-level concepts.

- **Process Modelling**: used to visually show the future state process, as well as tracing requirements to the future state process.

- **Scope Modelling**: used to visually depict scope, as well as trace requirements to the area of scope the requirement supports.

### 5.1.7 Stakeholders — Trace Requirements

- **Customers**: are affected by how and when requirements are implemented, and may have to be consulted about, or agree to, the traceability relationships.

- **Domain Subject Matter Expert**: may have recommendations regarding the set of requirements to be linked to a solution component or to a release.

- **End User**: may require specific dependency relationships that allow certain requirements to be implemented at the same time or in a specific sequence.

- **Implementation Subject Matter Expert**: traceability ensures that the solution being developed meets the business need and brings awareness of dependencies between solution components during implementation.

- **Operational Support**: traceability documentation provides another reference source for help desk support.

- **Project Manager**: traceability supports project change and scope management.

- **Sponsor**: is required to approve the various relationships.

- **Suppliers**: are affected by how and when requirements are implemented.

- **Tester**: needs to understand how and where requirements are implemented when creating test plans and test cases, and may trace test cases to requirements.

### 5.1.8 Outputs — Trace Requirements

- **Requirements (traced)**: have clearly defined relationships to other requirements, solution components, or releases, phases, or iterations, within a solution scope, such that coverage and the effects of change are clearly identifiable.

- **Designs (traced)**: clearly defined relationships to other requirements, solution components, or releases, phases, or iterations, within a solution scope, such that coverage and the effects of change are clearly identifiable.

## 5.2 Maintain Requirements

*BABOK® Guide v3 (IIBA, 2015) · Chapter 5 · p. 83*

> **Task Summary Card — 5.2 Maintain Requirements** (Knowledge Area: Requirements Life Cycle Management; reconstructed from the task text and its Input/Output diagram)
> - **Inputs:** Requirements; Designs
> - **Guidelines and Tools:** Information Management Approach *(produced by 3.4)*
> - **Techniques:** Business Rules Analysis; Data Flow Diagrams; Data Modelling; Document Analysis; Functional Decomposition; Process Modelling; Use Cases and Scenarios; User Stories
> - **Stakeholders:** Domain Subject Matter Expert; Implementation Subject Matter Expert; Operational Support; Regulator; Tester
> - **Outputs:** Requirements (maintained) *(input to 5.1, 5.3, 5.4, 5.5, 6.3, 7.2, 7.3, 7.4, 7.5; guideline/tool for 7.5, 8.1)*; Designs (maintained) *(input to 5.1, 5.3, 5.4, 5.5)*

### 5.2.1 Purpose — Maintain Requirements

The purpose of Maintain Requirements is to retain requirement accuracy and consistency throughout and beyond the change during the entire requirements life cycle, and to support reuse of requirements in other solutions.

### 5.2.2 Description — Maintain Requirements

A requirement that represents an ongoing need must be maintained to ensure that it remains valid over time.

In order to maximize the benefits of maintaining and reusing requirements, the requirements should be:

- consistently represented,

- reviewed and approved for maintenance using a standardized process that defines proper access rights and ensures quality, and

- easily accessible and understandable.

### 5.2.3 Inputs — Maintain Requirements

- **Requirements**: include goals, objectives, business requirements, stakeholder requirements, solution requirements, and transition requirements. These should be maintained throughout their life cycle.

- **Designs**: can be maintained throughout their life cycle, as needed.

**Figure 5.2.1: Maintain Requirements Input/Output Diagram**

> *(Diagram: inputs, guidelines/tools and outputs of this task — see the Task Summary Card at the top of this task and the Inputs/Outputs sections.)*

### 5.2.4 Elements — Maintain Requirements

#### 5.2.4.1 Maintain Requirements — Maintain Requirements

Requirements are maintained so that they remain correct and current after an approved change. Business analysts are responsible for conducting maintenance to ensure this level of accuracy is retained. For requirements to be properly maintained they must be clearly named and defined, and easily available to stakeholders.

Business analysts also maintain the relationships among requirements, sets of requirements, and associated business analysis information to ensure the context and original intent of the requirement is preserved. Repositories with accepted taxonomies assist in establishing and maintaining links between maintained requirements, and facilitate requirements and designs traceability.

#### 5.2.4.2 Maintain Attributes — Maintain Requirements

While eliciting requirements, business analysts elicit requirement attributes. Information such as the requirement’s source, priority, and complexity aid in managing each requirement throughout the life cycle. Some attributes change as the business analyst uncovers more information and conducts further analysis. An attribute may change even though the requirement does not.

#### 5.2.4.3 Reusing Requirements — Maintain Requirements

There are situations in which requirements can be reused.

Requirements that are candidates for long-term use by the organization are identified, clearly named, defined, and stored in a manner that makes them easily retrievable by other stakeholders. Depending on the level of abstraction and intended need being addressed, requirements can be reused:

- within the current initiative,

- within similar initiatives,

- within similar departments, and

- throughout the entire organization.

Requirements at high levels of abstraction may be written with limited reference to specific solutions. Requirements that are represented in a general manner, without direct ties to a particular tool or organizational structure, tend to be more reusable. These requirements are also less subject to revision during a change. As requirements are expressed in more detail, they become more tightly associated with a specific solution or solution option. Specific references to applications or departments limit the reuse of requirements and designs across an organization.

Requirements that are intended for reuse reflect the current state of the organization. Stakeholders validate the proposed requirements for reuse before they can be accepted into a change.

### 5.2.5 Guidelines and Tools — Maintain Requirements

- **Information Management Approach**: indicates how requirements will be managed for reuse.

### 5.2.6 Techniques — Maintain Requirements

- **Business Rules Analysis**: used to identify business rules that may be similar across the enterprise in order to facilitate reuse.

- **Data Flow Diagrams**: used to identify information flow that may be similar across the enterprise in order to facilitate reuse.

- **Data Modelling**: used to identify data structure that may be similar across the enterprise in order to facilitate reuse.

- **Document Analysis**: used to analyze existing documentation about an enterprise that can serve as the basis for maintaining and reusing requirements.

- **Functional Decomposition**: used to identify requirements associated with the components and available for reuse.

- **Process Modelling**: used to identify requirements associated with the processes that may be available for reuse.

- **Use Cases and Scenarios**: used to identify a solution component that may be utilized by more than one solution.

- **User Stories**: used to identify requirements associated with the story that may be available for reuse.

### 5.2.7 Stakeholders — Maintain Requirements

- **Domain Subject Matter Expert**: references maintained requirements on a regular basis to ensure they are accurately reflecting stated needs.

- **Implementation Subject Matter Expert**: utilizes maintained requirements when developing regression tests and conducting impact analysis for an enhancement.

- **Operational Support**: maintained requirements are likely to be referenced to confirm the current state.

- **Regulator**: maintained requirements are likely to be referenced to confirm compliance to standards.

- **Tester**: maintained requirements are used by testers to aid in test plan and test case creation.

### 5.2.8 Outputs — Maintain Requirements

- **Requirements (maintained)**: defined once and available for long-term usage by the organization. They may become organizational process assets or be used in future initiatives. In some cases, a requirement that was not approved or implemented may be maintained for a possible future initiative.

- **Designs (maintained)**: may be reusable once defined. For example, as a selfcontained component that can be made available for possible future use.

## 5.3 Prioritize Requirements

*BABOK® Guide v3 (IIBA, 2015) · Chapter 5 · p. 86*

> **Task Summary Card — 5.3 Prioritize Requirements** (Knowledge Area: Requirements Life Cycle Management; reconstructed from the task text and its Input/Output diagram)
> - **Inputs:** Requirements; Designs
> - **Guidelines and Tools:** Business Constraints; Change Strategy *(produced by 6.4)*; Domain Knowledge; Governance Approach *(produced by 3.3)*; Requirements Architecture *(produced by 7.4)*; Requirements Management Tools/Repository; Solution Scope *(produced by 6.4)*
> - **Techniques:** Backlog Management; Business Cases; Decision Analysis; Estimation; Financial Analysis; Interviews; Item Tracking; Prioritization; Risk Analysis and Management; Workshops
> - **Stakeholders:** Customer; End User; Implementation Subject Matter Expert; Project Manager; Regulator; Sponsor
> - **Outputs:** Requirements (prioritized) *(input to 5.1, 5.2, 5.4, 5.5, 6.3, 7.2, 7.3, 7.4, 7.5; guideline/tool for 7.5, 8.1)*; Designs (prioritized) *(input to 5.1, 5.2, 5.4, 5.5)*

### 5.3.1 Purpose — Prioritize Requirements

The purpose of Prioritize Requirements is to rank requirements in the order of relative importance.

### 5.3.2 Description — Prioritize Requirements

Prioritization is the act of ranking requirements to determine their relative importance to stakeholders. When a requirement is prioritized, it is given greater or lesser priority. Priority can refer to the relative value of a requirement, or to the sequence in which it will be implemented. Prioritization is an ongoing process, with priorities changing as the context changes.

Inter-dependencies between requirements are identified and may be used as the basis for prioritization. Prioritization is a critical exercise that seeks to ensure the maximum value is achieved.

### 5.3.3 Inputs — Prioritize Requirements

- **Requirements**: any requirements in the form of text, matrices, or diagrams that are ready to prioritize.

- **Designs**: any designs in the form of text, prototypes, or diagrams that are ready to prioritize.

**Figure 5.3.1: Prioritize Requirements Input/Output Diagram**

> *(Diagram: inputs, guidelines/tools and outputs of this task — see the Task Summary Card at the top of this task and the Inputs/Outputs sections.)*

### 5.3.4 Elements — Prioritize Requirements

#### 5.3.4.1 Basis for Prioritization — Prioritize Requirements

The basis on which requirements are prioritized is agreed upon by relevant stakeholders as defined in the Business Analysis Planning and Monitoring knowledge area.

Typical factors that influence prioritization include:

- **Benefit**: the advantage that accrues to stakeholders as a result of requirement implementation, as measured against the goals and objectives for the change. The benefit provided can refer to a specific functionality, desired quality, or strategic goal or business objective. If there are multiple stakeholders, each group may perceive benefits differently. Conflict resolution and negotiation may be employed to come to consensus on overall benefit.

- **Penalty**: the consequences that result from not implementing a given requirement. This includes prioritizing requirements in order to meet regulatory or policy demands imposed on the organization, which may take precedence over other stakeholder interests. Penalty may also refer to the negative consequence of not implementing a requirement that improves the experience of a customer.

- **Cost**: the effort and resources needed to implement the requirement. Information about cost typically comes from the implementation team or the vendor. Customers may change the priority of a requirement after learning the cost. Cost is often used in conjunction with other criteria, such as cost-benefit analysis.

- **Risk**: the chance that the requirement cannot deliver the potential value, or cannot be met at all. This may include many factors such as the difficulty of implementing a requirement, or the chance that stakeholders will not accept a solution component. If there is a risk that the solution is not technically feasible, the requirement that is most difficult to implement may be prioritized to the top of the list in order to minimize the resources that are spent before learning that a proposed solution cannot be delivered. A proof of concept may be developed to establish that high risk options are possible.

- **Dependencies**: relationships between requirements where one requirement cannot be fulfilled unless the other requirement is fulfilled. In some situations, it may be possible to achieve efficiencies by implementing related requirements at the same time. Dependencies may also be external to the initiative, including but not limited to other teams’ decisions, funding commitments, and resource availability. Dependencies are identified as part of the task Trace Requirements (p. 79).

- **Time Sensitivity**: the 'best before' date of the requirement, after which the implementation of the requirement loses significant value. This includes time-to-market scenarios, in which the benefit derived will be exponentially greater if the functionality is delivered ahead of the competition. It can also refer to seasonal functionality that only has value at a specific time of year.

- **Stability**: the likelihood that the requirement will change, either because it requires further analysis or because stakeholders have not reached a consensus about it. If a requirement is not stable, it may have a lower priority in order to minimize unanticipated rework and wasted effort.

- **Regulatory or Policy Compliance**: requirements that must be implemented in order to meet regulatory or policy demands imposed on the organization, which may take precedence over other stakeholder interests.

#### 5.3.4.2 Challenges of Prioritization — Prioritize Requirements

Prioritization is an assessment of relative value. Each stakeholder may value something different. When this occurs, there may be conflict amongst stakeholders. Stakeholders may also have difficulty characterizing any requirement as a lower priority, and this may impact the ability to make necessary trade-offs. In addition, stakeholders may (intentionally or unintentionally) indicate priority to influence the result to their desired outcome.

Different types of requirements may not all respond to the criteria in the same way and may appear to conflict. There may be a need for stakeholders to make trade-offs in prioritization.

#### 5.3.4.3 Continual Prioritization — Prioritize Requirements

Priorities may shift as the context evolves and as more information becomes available. Initially, prioritization is done at a higher level of abstraction. As the requirements are further refined, prioritization is done at a more granular level and will incorporate additional bases for prioritization as they become appropriate. The basis for prioritization may be different at various stages of the change. For example, stakeholders may initially prioritize based on benefits. The implementation team may then re-prioritize the requirements based on the sequence in which they must be implemented due to technical constraints. Once the implementation team has provided the cost of each requirement, the stakeholders may re-prioritize yet again.

### 5.3.5 Guidelines and Tools — Prioritize Requirements

- **Business Constraints**: regulatory statutes, contractual obligations and business policies that may define priorities.

- **Change Strategy**: provides information on costs, timelines, and value realization which are used to determine priority of requirements.

- **Domain Knowledge**: knowledge and expertise of the business domain needed to support prioritization.

- **Governance Approach**: outlines the approach for prioritizing requirements.

- **Requirements Architecture**: utilized to understand the relationship with other requirements and work products.

- **Requirements Management Tools/Repository**: including a requirements attribute for prioritization can help the business analyst to sort and access requirements by priority.

- **Solution Scope**: considered when prioritizing requirements to ensure scope is managed.

### 5.3.6 Techniques — Prioritize Requirements

- **Backlog Management**: used to compare requirements to be prioritized. The backlog can be the location where the prioritization is maintained.

- **Business Cases**: used to assess requirements against identified business goals and objectives to determine importance.

- **Decision Analysis**: used to identify high-value requirements.

- **Estimation**: used to produce estimates for the basis of prioritization.

- **Financial Analysis**: used to assess the financial value of a set of requirements and how the timing of delivery will affect that value.

- **Interviews**: used to gain an understanding of a single or small group of stakeholders' basis of prioritization or priorities.

- **Item Tracking**: used to track issues raised by stakeholders during prioritization.

- **Prioritization**: used to facilitate the process of prioritization.

- **Risk Analysis and Management**: used to understand the risks for the basis of prioritization.

- **Workshops**: used to gain an understanding of stakeholders' basis of prioritization or priorities in a facilitated group setting.

### 5.3.7 Stakeholders — Prioritize Requirements

- **Customer**: verifies that the prioritized requirements will deliver value from a customer or end-user perspective. The customer can also negotiate to have the prioritization changed based on relative value.

- **End User**: verifies that the prioritized requirements will deliver value from a customer or end-user perspective.

- **Implementation Subject Matter Expert**: provides input relating to technical dependencies and can negotiate to have the prioritization changed based on technical constraints.

- **Project Manager**: uses the prioritization as input into the project plan and into the allocation of requirements to releases.

- **Regulator**: can verify that the prioritization is consistent with legal and regulatory constraints.

- **Sponsor**: verifies that the prioritized requirements will deliver value from an organizational perspective.

### 5.3.8 Outputs — Prioritize Requirements

- **Requirements (prioritized)**: prioritized or ranked requirements are available for additional work, ensuring that the highest valued requirements are addressed first.

- **Designs (prioritized)**: prioritized or ranked designs are available for additional work, ensuring that the highest valued designs are addressed first.

## 5.4 Assess Requirements Changes

*BABOK® Guide v3 (IIBA, 2015) · Chapter 5 · p. 91*

> **Task Summary Card — 5.4 Assess Requirements Changes** (Knowledge Area: Requirements Life Cycle Management; reconstructed from the task text and its Input/Output diagram)
> - **Inputs:** Proposed Change; Requirements; Designs
> - **Guidelines and Tools:** Change Strategy *(produced by 6.4)*; Domain Knowledge; Governance Approach *(produced by 3.3)*; Legal/Regulatory Information; Requirements Architecture *(produced by 7.4)*; Solution Scope *(produced by 6.4)*
> - **Techniques:** Business Cases; Business Rules Analysis; Decision Analysis; Document Analysis; Estimation; Financial Analysis; Interface Analysis; Interviews; Item Tracking; Risk Analysis and Management; Workshops
> - **Stakeholders:** Customer; Domain Subject Matter Expert; End User; Operational Support; Project Manager; Regulator; Sponsor; Tester
> - **Outputs:** Requirements Change Assessment; Designs Change Assessment

### 5.4.1 Purpose — Assess Requirements Changes

The purpose of Assess Requirements Changes is to evaluate the implications of proposed changes to requirements and designs.

### 5.4.2 Description — Assess Requirements Changes

The Assess Requirements Changes task is performed as new needs or possible solutions are identified. These may or may not align to the change strategy and/ or solution scope. Assessment must be performed to determine whether a proposed change will increase the value of the solution, and if so, what action should be taken.

Business analysts assess the potential effect of the change to solution value, and whether proposed changes introduce conflicts with other requirements or increase the level of risk. Business analysts also ensure each proposed change can be traced back to a need.

When assessing changes, business analysts consider if each proposed change:

- aligns with the overall strategy,

- affects value delivered to the business or stakeholder groups,

- impacts the time to deliver or the resources required to deliver the value, and

- alters any risks, opportunities, or constraints associated with the overall initiative.

The results of the assessment must support the decision making and change control approaches defined by the task Plan Business Analysis Governance (p. 37).

### 5.4.3 Inputs — Assess Requirements Changes

- **Proposed Change**: can be identified at any time and impact any aspect of business analysis work or deliverables completed to date. There are many triggers for a proposed change including business strategy changes, stakeholders, legal requirements, or regulatory changes.

- **Requirements**: may need to be assessed to identify the impact of a proposed modification.

- **Designs**: may need to be assessed to identify the impact of a proposed modification.

**Figure 5.4.1: Assess Requirements Changes Input/Output Diagram**

> *(Diagram: inputs, guidelines/tools and outputs of this task — see the Task Summary Card at the top of this task and the Inputs/Outputs sections.)*

### 5.4.4 Elements — Assess Requirements Changes

#### 5.4.4.1 Assessment Formality — Assess Requirements Changes

Business analysts will determine the formality of the assessment process based on the information available, the apparent importance of the change, and the governance process. Many proposed changes may be withdrawn from consideration or declined before any formal approval is required. A predictive approach may indicate a more formal assessment of proposed changes. In predictive approaches, the impact of each change can be disruptive; the change can potentially generate a substantial reworking of tasks and activities completed in previous activities. An adaptive approach may require less formality in the assessment of proposed changes. While there may be reworking needed as a result of each change, adaptive approaches try to minimize the impact of changes by utilizing iterative and incremental implementation techniques. This idea of continuous evolution may reduce the need for formal impact assessment.

#### 5.4.4.2 Impact Analysis — Assess Requirements Changes

Impact analysis is performed to assess or evaluate the effect of a change. Traceability is a useful tool for performing impact analysis. When a requirement changes, its relationships to other requirements or solution components can be reviewed. Each related requirement or component may also require a change to support the new requirement.

When considering changes or additions to existing requirements, business analysts assess the impact of the proposed change by considering:

- **Benefit**: the benefit that will be gained by accepting the change.

- **Cost**: the total cost to implement the change including the cost to make the change, the cost of associated rework, and the opportunity costs such as the number of other features that may need to be sacrificed or deferred if the change is approved.

- **Impact**: the number of customers or business processes affected if the change is accepted.

- **Schedule**: the impact to the existing delivery commitments if the change is approved.

- **Urgency**: the level of importance including the factors which drive necessity such as regulator or safety issues.

#### 5.4.4.3 Impact Resolution — Assess Requirements Changes

Depending on the planned approach, various stakeholders (including the business analyst) may be authorized to approve, deny, or defer the proposed change. All impacts and resolutions resulting from the change analysis are to be documented and communicated to all stakeholders. How decisions and changes will be made and communicated across an initiative is determined by the task Plan Business Analysis Governance (p. 37).

### 5.4.5 Guidelines and Tools — Assess Requirements Changes

- **Change Strategy**: describes the purpose and direction for changes, establishes the context for the change, and identifies the critical components for change.

- **Domain Knowledge**: knowledge of and expertise in the business domain is needed to assess proposed requirements changes.

- **Governance Approach**: provides guidance regarding the change control and decision-making processes, as well as the roles of stakeholders within this process.

- **Legal/Regulatory Information**: describes legislative rules or regulations that must be followed. These may impact requirements and must be considered when making changes.

- **Requirements Architecture**: requirements may be related to each other, therefore the business analyst examines and analyzes the requirement relationships to determine which requirements will be impacted by a requested requirements change.

- **Solution Scope**: must be considered when assessing changes to fully understand the impact of a proposed change.

### 5.4.6 Techniques — Assess Requirements Changes

- **Business Cases**: used to justify a proposed change.

- **Business Rules Analysis**: used to assess changes to business policies and business rules, and develop revised guidance.

- **Decision Analysis**: used to facilitate the change assessment process.

- **Document Analysis**: used to analyze any existing documents that facilitate an understanding of the impact of the change.

- **Estimation**: used to determine the size of the change.

- **Financial Analysis**: used to estimate the financial consequences of a proposed change.

- **Interface Analysis**: used to help business analysts identify interfaces that can be affected by the change.

- **Interviews**: used to gain an understanding of the impact on the organization or its assets from a single or small group of stakeholders.

- **Item Tracking**: used to track any issues or conflicts discovered during impact analysis.

- **Risk Analysis and Management**: used to determine the level of risk associated with the change.

- **Workshops**: used to gain an understanding of the impact or to resolve changes in a group setting.

### 5.4.7 Stakeholders — Assess Requirements Changes

- **Customer**: provides feedback concerning the impact the change will have on value.

- **Domain Subject Matter Expert**: has expertise in some aspect of the situation and can provide insight into how the change will impact the organization and value.

- **End User**: uses the solution or is a component of the solution, and can offer information about the impact of the change on their activities.

- **Operational Support**: provides information on both their ability to support the operation of the solution and their need to understand the nature of the change in the solution in order to be able to support it.

- **Project Manager**: reviews the requirements change assessment to determine if additional project work is required for a successful implementation of the solution.

- **Regulator**: changes are likely to be referenced by auditors to confirm compliance to standards.

- **Sponsor**: accountable for the solution scope and can provide insight to be utilized when assessing change.

- **Tester**: consulted for establishing impact of the proposed changes.

### 5.4.8 Outputs — Assess Requirements Changes

- **Requirements Change Assessment**: the recommendation to approve, modify, or deny a proposed change to requirements.

- **Designs Change Assessment**: the recommendation to approve, modify, or deny a proposed change to one or more design components.

## 5.5 Approve Requirements

*BABOK® Guide v3 (IIBA, 2015) · Chapter 5 · p. 95*

> **Task Summary Card — 5.5 Approve Requirements** (Knowledge Area: Requirements Life Cycle Management; reconstructed from the task text and its Input/Output diagram)
> - **Inputs:** Requirements (verified); Designs
> - **Guidelines and Tools:** Change Strategy *(produced by 6.4)*; Governance Approach *(produced by 3.3)*; Legal/Regulatory Information; Requirement Management Tools/Repository; Solution Scope *(produced by 6.4)*
> - **Techniques:** Acceptance and Evaluation Criteria; Decision Analysis; Item Tracking; Reviews; Workshops
> - **Stakeholders:** Customer; Domain Subject Matter Expert; End User; Operational Support; Project Manager; Regulator; Sponsor; Tester
> - **Outputs:** Requirements (approved) *(input to 5.1, 5.2, 5.3, 5.4, 6.3, 7.2, 7.3, 7.4, 7.5; guideline/tool for 7.5, 8.1)*; Designs (approved) *(input to 5.1, 5.2, 5.3, 5.4)*

### 5.5.1 Purpose — Approve Requirements

The purpose of Approve Requirements is to obtain agreement on and approval of requirements and designs for business analysis work to continue and/or solution construction to proceed.

### 5.5.2 Description — Approve Requirements

Business analysts are responsible for ensuring clear communication of requirements, designs, and other business analysis information to the key stakeholders responsible for approving that information.

Approval of requirements and designs may be formal or informal. Predictive approaches typically perform approvals at the end of the phase or during planned change control meetings. Adaptive approaches typically approve requirements only when construction and implementation of a solution meeting the requirement can begin. Business analysts work with key stakeholders to gain consensus on new and changed requirements, communicate the outcome of discussions, and track and manage the approval.

### 5.5.3 Inputs — Approve Requirements

- **Requirements (verified)**: a set of requirements that have been verified to be of sufficient quality to be used as a reliable body of work for further specification and development.

- **Designs**: a set of designs that have been determined as ready to be used for further specification and development.

**Figure 5.5.1: Approve Requirements Input/Output Diagram**

> *(Diagram: inputs, guidelines/tools and outputs of this task — see the Task Summary Card at the top of this task and the Inputs/Outputs sections.)*

### 5.5.4 Elements — Approve Requirements

#### 5.5.4.1 Understand Stakeholder Roles — Approve Requirements

The approval process is defined by the task Plan Business Analysis Governance (p. 37). Part of defining the approval process is understanding stakeholder roles and authority levels. Business analysts are responsible for obtaining stakeholder approvals and are required to understand who holds decision-making responsibility and who possesses authority for sign-off across the initiative. Business analysts also consider any influential stakeholders who should be consulted or informed about the requirements. Few stakeholders may have the authority to approve or deny changes, but many stakeholders may be able to influence these decisions.

#### 5.5.4.2 Conflict and Issue Management — Approve Requirements

To maintain stakeholder support for the solution, consensus among stakeholders is usually sought prior to requesting approval of requirements. The approach for determining how to secure decisions and resolve conflicts across an initiative is planned for in the task Plan Business Analysis Governance (p. 37).

Stakeholder groups frequently have varying points of view and conflicting priorities. A conflict may arise among stakeholders as a result of different interpretations of requirements or designs and conflicting values placed on them. The business analyst facilitates communication between stakeholders in areas of conflict so that each group has an improved appreciation for the needs of the others. Conflict resolution and issue management may occur quite often, as the business analyst is reviewing requirements and designs, and aiming to secure sign-off.

#### 5.5.4.3 Gain Consensus — Approve Requirements

Business analysts are responsible for ensuring that the stakeholders with approval authority understand and accept the requirements. Approval may confirm that stakeholders believe that sufficient value will be created for the organization to justify investment in a solution. Business analysts obtain approval by reviewing the requirements or changes to requirements with the accountable individuals or groups and requesting that they approve, indicating their agreement with the solution or designs described.

Using the methods and means established in the tasks Plan Business Analysis Governance (p. 37) and Communicate Business Analysis Information (p. 67) business analysts present the requirements to stakeholders for approval. Business analysts facilitate this approval process by addressing any questions or providing additional information when requested.

Complete agreement may not be necessary for a successful change, but if there is a lack of agreement, the associated risks are to be identified and managed accordingly.

#### 5.5.4.4 Track and Communicate Approval — Approve Requirements

The business analyst records approval decisions, possibly in requirements maintenance and tracking tools. In order to communicate the status of requirements, it is necessary to keep accurate records of current approval status. Stakeholders must be able to determine what requirements and designs are currently approved and in line for implementation. There may be value in maintaining an audit history of changes to requirements: what was changed, who made the change, the reason for the change, and when it was made.

### 5.5.5 Guidelines and Tools — Approve Requirements

- **Change Strategy**: provides information which assists in managing stakeholder consensus regarding the needs of all stakeholders.

- **Governance Approach**: identifies the stakeholders who have the authority and responsibility to approve business analysis information, and explains when such approvals will take place and how they will align to organizational policies.

- **Legal/Regulatory Information**: describes legislative rules or regulations that must be followed. They may impact the requirements and designs approval process.

- **Requirement Management Tools/Repository**: tool to record requirements approvals.

- **Solution Scope**: must be considered when approving requirements to accurately assess alignment and completeness.

### 5.5.6 Techniques — Approve Requirements

- **Acceptance and Evaluation Criteria**: used to define approval criteria.

- **Decision Analysis**: used to resolve issues and gain agreement.

- **Item Tracking**: used to track issues identified during the agreement process.

- **Reviews**: used to evaluate requirements.

- **Workshops**: used to facilitate obtaining approval.

### 5.5.7 Stakeholders — Approve Requirements

- **Customer**: may play an active role in reviewing and approving requirements and designs to ensure needs are met.

- **Domain Subject Matter Expert**: may be involved in the review and approval of requirements and designs as defined by stakeholder roles and responsibilities designation.

- **End User**: people who use the solution, or who are a solution component, and may be involved in the review, validation, and prioritization of requirements and designs as defined by the stakeholder roles and responsibilities designation.

- **Operational Support**: responsible for ensuring that requirements and designs are supportable within the constraints imposed by technology standards and organizational capability plans. Operational support personnel may have a role in reviewing and approving requirements.

- **Project Manager**: responsible for identifying and managing risks associated with solution design, development, delivery, implementation, operation and sustainment. The project manager may manage the project plan activities pertaining to review and/or approval.

- **Regulator**: external or internal party who is responsible for providing opinions on the relationship between stated requirements and specific regulations, either formally in an audit, or informally as inputs to requirements life cycle management tasks.

- **Sponsor**: responsible to review and approve the business case, solution or product scope, and all requirements and designs.

- **Tester**: responsible for ensuring quality assurance standards are feasible within the business analysis information. For example, requirements have the testable characteristic.

### 5.5.8 Outputs — Approve Requirements

- **Requirements (approved)**: requirements which are agreed to by stakeholders and are ready for use in subsequent business analysis efforts.

- **Designs (approved)**: designs which are agreed to by stakeholders and are ready for use in subsequent business analysis or solution development efforts.
