<!-- Knowledge file: Chapter 10 — Techniques 10.41–10.50 -->
> **About this file.** Part of a cleaned, AI-ready edition of the BABOK® Guide v3 (IIBA, 2015). 
> **Covers:** Techniques: 10.41 Scope Modelling; 10.42 Sequence Diagrams; 10.43 Stakeholder List, Map, or Personas; 10.44 State Modelling; 10.45 Survey or Questionnaire; 10.46 SWOT Analysis; 10.47 Use Cases and Scenarios; 10.48 User Stories; 10.49 Vendor Assessment; 10.50 Workshops. Each technique has Purpose, Description, Elements, Usage Considerations (Strengths/Limitations), and a card listing every task that uses it and how.  
> **Use this file when:** the question is about how to perform, or when to use, one of these techniques.
> **Sections:** 10.41 Scope Modelling (p. 338); 10.42 Sequence Diagrams (p. 341); 10.43 Stakeholder List, Map, or Personas (p. 344); 10.44 State Modelling (p. 348); 10.45 Survey or Questionnaire (p. 350); 10.46 SWOT Analysis (p. 353); 10.47 Use Cases and Scenarios (p. 356); 10.48 User Stories (p. 359); 10.49 Vendor Assessment (p. 361); 10.50 Workshops (p. 363)

# Chapter 10: Techniques (continued)

## 10.41 Scope Modelling

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 338*

> **Where this technique is used — 10.41 Scope Modelling** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **3.1 Plan Business Analysis Approach** (Business Analysis Planning and Monitoring): used to determine the boundaries of the solution as an input to planning and to estimating.
> - **3.2 Plan Stakeholder Engagement** (Business Analysis Planning and Monitoring): used to develop scope models to show stakeholders that fall outside the scope of the solution but still interact with it in some way.
> - **5.1 Trace Requirements** (Requirements Life Cycle Management): used to visually depict scope, as well as trace requirements to the area of scope the requirement supports.
> - **6.1 Analyze Current State** (Strategy Analysis): helps define the boundaries on the current state description.
> - **6.2 Define Future State** (Strategy Analysis): used to define the boundaries of the enterprise in the future state.
> - **6.4 Define Change Strategy** (Strategy Analysis): used to define the boundaries on the solution scope and change scope descriptions.
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to visually show a scope boundary.
> - **7.4 Define Requirements Architecture** (Requirements Analysis and Design Definition): used to identify the elements and boundaries of the requirements architecture.

### 10.41.1 Purpose — Scope Modelling

Scope models define the nature of one or more limits or boundaries and place elements inside or outside those boundaries.

### 10.41.2 Description — Scope Modelling

Scope models are commonly used to describe the boundaries of control, change, a solution, or a need. They may also be used to delimit any simple boundary (as distinct from horizons, emergent properties, and recursive systems).

These models may show elements that include:

- **In-scope**: the model identifies a boundary as seen from inside, as well as the elements contained by that boundary (for example, functional decomposition).

- **Out-of-scope**: the model identifies a boundary as seen from outside, as well as the elements that are not contained by that boundary (for example, context diagram).

- **Both**: the model identifies a boundary as seen from both sides, as well as elements on both sides of the boundary (for example, venn diagram or use case model).

Scope models provide the basis for understanding the boundaries of:

- **Scope of Control**: what is being analyzed, roles and responsibilities, and what is internal and external to the organization.

- **Scope of Need**: stakeholder needs, value to be delivered, functional areas, and organizational units to be explored.

- **Scope of Solution**: requirements met, value delivered, and impact of change.

- **Scope of Change**: actions to be taken, stakeholders affected or involved, and events to cause or prevent.

Scope models are typically represented as a combination of diagrams, matrices, and textual explanations. If the scope is implemented in phases or iterations, the scope model should be described per each phase or iteration.

### 10.41.3 Elements — Scope Modelling

#### 10.41.3.1 Objectives — Scope Modelling

Scope models are typically used to clarify the:

- span of control,

- relevance of elements, and

- where effort will be applied.

Depending on the action or stakeholder needs the model supports, a business analyst determines the types of models to be used and selects boundaries and elements.

#### 10.41.3.2 Scope of Change and Context — Scope Modelling

Typically, business analysts are concerned with elements that will be altered as part of a change, as well as external elements that are relevant to the change. For elements inside the scope of change, the business analyst is involved in establishing the ways those elements are modified. For elements outside the scope of change but relevant to the change, the business analyst is involved in establishing the interactions between the change, the current and proposed solutions, and the context.

The business analyst often determines:

- business processes to be defined or modified,

- business functions to be added, changed, optimized, or re-assigned,

- new capabilities to be built or existing capabilities to be changed,

- external and internal events to be responded to,

- use cases and situations to be supported,

- technologies to be changed or replaced,

- informational assets to be acquired, produced, or processed,

- stakeholders and organizational roles impacted by the change,

- external and internal agents and entities impacted by the change,

- organizations and organizational units (departments, teams, groups) impacted by the change, and

- systems, components, tools, and physical assets required for the change or impacted by the change.

#### 10.41.3.3 Level of Detail — Scope Modelling

The purpose of analysis defines the appropriate level of abstraction at which scope elements are described. A proper level of detail provides a meaningful reduction of uncertainty while preventing 'analysis paralysis' at a scope definition stage. The elements of the final scope model can be described by enumerating them, by referring to a specific level of their decomposition hierarchy, or by grouping them into logically bound sets. For example, a subject of change can be defined as a list of specific business processes, as a high-level business process encompassing all of them, or as a generic business function. Similarly, stakeholders included in the scope can be defined by enumerating specific titles or by referring to their common organizational role.

#### 10.41.3.4 Relationships — Scope Modelling

Exploring relationships between potential scope elements helps to ensure completeness and integrity of the scope model by identifying their dependencies or by discovering other elements involved in or impacted by the change.

Various diagramming techniques are available for exploring relationships of specific types, including:

- **Parent-Child or Composition-Subset**: relates elements of the same type by way of hierarchical decomposition. Relationships of this type appear as an organization chart, in a class or entity-relationship diagram, as subprocesses in a business process model, or as composite states on a state diagram.

- **Function-Responsibility**: relates a function with the agent (stakeholder, organizational unit, or solution component) that is responsible for its execution. Relationships of this type appear on business process models and on collaboration, sequence, and use case diagrams.

- **Supplier-Consumer**: relates elements by way of the transmission of information or materials between them. Elements can be processes, systems, solution components, and organizational units, for both internal and external entities. Relationships of this type occur in data flow diagrams, business process models, and in collaboration, sequence, and robustness diagrams.

- **Cause-Effect**: relates elements by logical contingency in order to identify chains of associated elements that are involved in or impacted by the change. Relationships of this type appear in fishbone (Ishikawa) diagrams and other cause-effect diagrams.

- **Emergent**: in most complex systems, several elements can interact to produce results that cannot be predicted or understood based on the components alone.

#### 10.41.3.5 Assumptions — Scope Modelling

At a time of scope modelling, the validity of the model heavily relies on assumptions such as the definition of needs, causality of outcomes, impact of changes, applicability, and feasibility of the solution. The resulting scope model should include explicit statements of critical assumptions and their implications.

#### 10.41.3.6 Scope Modelling Results — Scope Modelling

Results of scope modelling can be represented as:

- textual descriptions of elements, including criteria for making in-scope or out-of-scope decisions,

- diagrams illustrating relationships of scope elements, and

- matrices depicting dependencies between scope elements.

### 10.41.4 Usage Considerations — Scope Modelling

#### 10.41.4.1 Strengths — Scope Modelling

- A scope model facilitates agreement as a basis for:

- defining contractual obligations,

- estimating the project effort,

- justifying in-scope/out-of-scope decisions in requirements analysis, and

- assessing the completeness and impact of solutions.

#### 10.41.4.2 Limitations — Scope Modelling

- An initial, high-level model can lack a sufficient level of granularity, particularly for boundary elements, that is needed to ensure clear scope identification.

- Once a scope is defined, changing it may be difficult due to political reasons and contractual obligations. Meanwhile, many factors can affect the scope validity before the targets are achieved. Such factors as wrong initial assumptions, situation change, evolution of stakeholder needs, or technology innovations may cause a need for revising the scope partially or entirely.

- Traditional scope models cannot address common complex boundaries, such as a horizon (a boundary that is completely dependent on the position of the stakeholder).

## 10.42 Sequence Diagrams

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 341*

> **Where this technique is used — 10.42 Sequence Diagrams** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to specify and model requirements to show how processes operate and interact with one another, and in what order.

### 10.42.1 Purpose — Sequence Diagrams

Sequence diagrams are used to model the logic of usage scenarios by showing the information passed between objects in the system through the execution of the scenario.

### 10.42.2 Description — Sequence Diagrams

A sequence diagram shows how processes or objects interact during a scenario. The classes required to execute the scenario and the messages they pass to one another (triggered by steps in the use case) are displayed on the diagram. The sequence diagram shows how objects used in the scenario interact, but not how they are related to one another. Sequence diagrams are also often used to show how user interface components or software components interact.

The diagram represents information in a horizontal and vertical alignment. The objects that send messages to each other are represented as boxes that are aligned at the top of the page from the left to the right, with each object occupying a column of space on the page bordered by a vertical line stretching down to the bottom of the page. The messages that are sent from one object to the next are represented as horizontal arrows. The order of the messages is represented in a top-down and left-to-right sequence beginning with the first message at the top left of the page and subsequent messages occurring to the right and below. Sequence diagrams are sometimes called event diagrams.

The standard notation for sequence diagrams is defined as part of the Unified Modelling Language™ (UML® ) specification.

### 10.42.3 Elements — Sequence Diagrams

#### 10.42.3.1 Lifeline — Sequence Diagrams

A lifeline represents the lifespan of an object during the scenario being modelled in a sequence diagram. The example below shows the object order. A lifeline is drawn as a dashed line that vertically descends from each object box to the bottom of the page.

**Figure 10.42.1: Lifeline**

#### 10.42.3.2 Activation Box — Sequence Diagrams

An activation box represents the period during which an operation is executed. A call to activate is represented by an arrow with a solid arrowhead leading to the activation object. The lifeline can be terminated with an X.

**Figure 10.42.2: Activation Box**

#### 10.42.3.3 Message — Sequence Diagrams

A message is an interaction between two objects. A message is shown as an arrow coming from the activation box of the object that sends the message to the activation box of the object that receives the message.

The name of the message is placed on top of the arrowed line. There are different types of messages:

- **Synchronous Call**: transfers control to the receiving object. The sender cannot act until a return message is received.

- **Asynchronous Call**: (also known as a signal) allows the object to continue with its own processing after sending the signal. The object may send many signals simultaneously, but may only accept one signal at a time.

**Figure 10.42.3: Message**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Object 1 Object 2 Object 3 · Call · Synchronous · Message · Asynchronous · Message · Response · Execution · Specification X · Lifeline Destruction

### 10.42.4 Usage Considerations — Sequence Diagrams

#### 10.42.4.1 Strengths — Sequence Diagrams

- Shows the interaction between the objects of a system in the chronological order that the interactions occur.

- Shows the interaction between the objects in a visual manner that allows the logic to be validated by stakeholders with relative ease.

- Use cases can be refined into one or more sequence diagrams in order to provide added detail and a more in-depth understanding of a business process.

#### 10.42.4.2 Limitations — Sequence Diagrams

- Time and effort can be wasted creating a complete set of sequence diagrams for each use case of a system, which may not be necessary.

- Have historically been used for modelling system flows and may be considered too technical in other circumstances.

## 10.43 Stakeholder List, Map, or Personas

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 344*

> **Where this technique is used — 10.43 Stakeholder List, Map, or Personas** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **3.2 Plan Stakeholder Engagement** (Business Analysis Planning and Monitoring): used to depict the relationship of stakeholders to the solution and to one another.
> - **4.1 Prepare for Elicitation** (Elicitation and Collaboration): used to determine who should be consulted while preparing for the elicitation, who should participate in the event, and the appropriate roles for each stakeholder.
> - **4.5 Manage Stakeholder Collaboration** (Elicitation and Collaboration): used to determine who is available to participate in the business analysis work, show the informal relationships between stakeholders, and understand which stakeholders should be consulted about different kinds of business analysis information.
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to identify the stakeholders and their characteristics.

### 10.43.1 Purpose — Stakeholder List, Map, or Personas

Stakeholder lists, maps, and personas assist the business analyst in analyzing stakeholders and their characteristics. This analysis is important in ensuring that the business analyst identifies all possible sources of requirements and that the stakeholder is fully understood so decisions made regarding stakeholder engagement, collaboration, and communication are the best choices for the stakeholder and for the success of the initiative.

### 10.43.2 Description — Stakeholder List, Map, or Personas

Stakeholder analysis involves identifying the stakeholders that may be affected by a proposed initiative or that share a common business need. Stakeholder analysis notes, considers, and analyzes the various characteristics of the identified stakeholders.

Common types of stakeholder characteristics that are worth identifying and analyzing include:

- level of authority within the domain of change and within the organization,

- attitudes toward or interest in the change being undertaken,

- attitudes toward the business analysis work and role, and

- level of decision-making authority.

For details on the work involved in conducting a thorough stakeholder analysis, see Plan Stakeholder Engagement (p. 31).

When analyzing stakeholders, business analysts utilize one or more techniques to draw out a list of stakeholders and analyze them. Stakeholder lists, maps, and personas are three tools that can be utilized when conducting this work.

### 10.43.3 Elements — Stakeholder List, Map, or Personas

#### 10.43.3.1 Stakeholder Lists — Stakeholder List, Map, or Personas

A business analyst may apply a number of techniques to generate a stakeholder list. Brainstorming and interviews are two common techniques that can be used. The goal is to ensure a thorough list is produced because this list is central to both stakeholder analysis activities and the planning work the business analyst performs for elicitation, collaboration, and communication.

Stakeholder lists may become quite lengthy. As the analysis is conducted, the business analyst categorizes and adds structure to the list. It is important to have an exhaustive list to ensure that no important stakeholder or stakeholder group has been overlooked, which opens up the risk that requirements will be missed later on.

#### 10.43.3.2 Stakeholder Map — Stakeholder List, Map, or Personas

Stakeholder maps are diagrams that depict the relationship of stakeholders to the solution and to one another.

There are many forms of stakeholder maps, but two common ones include:

- **Stakeholder Matrix**: maps the level of stakeholder influence against the level of stakeholder interest.

- **Onion Diagram**: indicates how involved the stakeholders are with the solution, which stakeholders will directly interact with the solution or participate in a business process, which are part of the larger organization, and which are outside the organization.

The business analyst typically starts their stakeholder analysis by reviewing the proposed scope of the solution and then analyzing which groups will be impacted. At the start of this analysis, the business analyst may produce a stakeholder matrix to identify each stakeholder and their role as it pertains to the development of the requirements. Throughout a project, a stakeholder’s position on the matrix can change due to organizational, environmental, or requirement scope changes. Due to these potential changes, stakeholder analysis is considered iterative and reviewed frequently by the business analyst.

**Figure 10.43.1: Stakeholder Matrix**

|**Influence of** **High**|Ensure stakeholder remains satisfied.|Work closely with stakeholder to ensure that they are in agreement with and support the change.|
|---|---|---|
|**Stakeholder**|||
||Monitor to ensure stakeholders interest or influence do not change.|Keep informed; stakeholder is likely to be very concerned and may feel anxious about lack of control.|
|**Low**|||
||**Imp** **Stake** **Low**|**act on** **holder** **High**|

- **High Influence/High Impact**: the stakeholders are key players in the change effort. The business analyst should focus their efforts and engage this group regularly.

- **High Influence/Low Impact**: the stakeholders have needs that should be met. The business analyst should engage and consult with them, while also attempting to engage them and increase their level of interest with the change activity.

- **Low Influence/High Impact**: the stakeholders are supporters of and potential goodwill ambassadors for the change effort. The business analyst should engage this group for their input and show interest in their needs.

- **Low Influence/Low Impact**: the stakeholders can be kept informed using general communications. Additional engagement may move them into the goodwill ambassador quadrant, which can help the effort gain additional support.

**Figure 10.43.2: Stakeholder Onion Diagram**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Customers, suppliers, · regulators, and others. · Affected External Stakeholders Sponsors, executives, · domain SMEs, and · others who interact with · Organization or Enterprise · the affected group. · End users, help desk, · Affected Organizational Unit · and others whose work · changes when the · solution is delivered. · Solution Delivery · Project team and others · directly involved with · creating the solution.

#### 10.43.3.3 Responsibility (RACI) Matrix — Stakeholder List, Map, or Personas

Another popular stakeholder matrix is the responsibility (RACI) matrix. RACI stands for the four types of responsibility that a stakeholder may hold on the initiative: Responsible, Accountable, Consulted, and Informed. When completing a RACI matrix, it is important to ensure that all stakeholders or stakeholder groups have been identified. Further analysis is then conducted to assign the RACI designation in order to specify the level of responsibility expected from each stakeholder and/or group. It is common practice to define each term so that a consistent understanding of the assignment and associated roles are understood by any stakeholders utilizing the RACI matrix.

- **Responsible (R)**: the persons who will be performing the work on the task.

- **Accountable (A)**: the person who is ultimately held accountable for successful completion of the task and is the decision maker. Only one stakeholder receives this assignment.

- **Consulted (C)**: the stakeholder or stakeholder group who will be asked to provide an opinion or information about the task. This assignment is often provided to the subject matter experts (SMEs).

- **Informed (I)**: a stakeholder or stakeholder group that is kept up to date on the task and notified of its outcome. Informed is different from Consulted as with Informed the communication is one-direction (business analyst to stakeholder) and with Consulted the communication is two-way.

**Figure 10.43.3: RACI Matrix**

|**Change Request Process**||**RACI**|
|---|---|---|
|Executive Sponsor||**A**|
|Business Analyst||**R**|
|Project Manager||**C**|
|Developer||**C**|
|Tester||**I**|
|Trainer||**I**|
|Application Architect||**C**|
|Data Modeller||**C**|
|Database Analyst (DBA)||**C**|
|Infrastructure Analyst||**C**|
|Business Architect||**R**|
|Information Architect||**C**|
|Solution Owner||**C**|
|Subject Matter Expert (SME)||**C**|
|Other Stakeholders|**R**|**C** **I** (varies)|

#### 10.43.3.4 Personas — Stakeholder List, Map, or Personas

A persona is defined as a fictional character or archetype that exemplifies the way a typical user interacts with a product. Personas are helpful when there is a desire to understand the needs held by a group or class of users. Although the user groups are fictional, they are built to represent actual users. Research is conducted to understand the user group, and the personas are then created based upon knowledge rather than opinion. A number of elicitation techniques can be utilized to conduct this research. Interviews and surveys/questionnaires are two techniques commonly used to elicit this information. The persona is written in narrative form and focuses on providing insight into the goals of the group. This allows the reader to see the story from the point of view of the stakeholder group. Personas help bring the user to life, which in turn makes the needs feel real to those who design and build solutions.

### 10.43.4 Usage Considerations — Stakeholder List, Map, or Personas

#### 10.43.4.1 Strengths — Stakeholder List, Map, or Personas

- Identifies the specific people who must be engaged in requirements elicitation activities.

- Helps the business analyst plan collaboration, communication, and facilitation activities to engage all stakeholder groups.

- Useful to understand changes in impacted groups over time.

#### 10.43.4.2 Limitations — Stakeholder List, Map, or Personas

- Business analysts who are continuously working with the same teams may not utilize the stakeholder analysis and management technique because they perceive change as minimal within their respective groups.

- Assessing information about a specific stakeholder representative, such as influence and interest, can be complicated and may feel politically risky.

## 10.44 State Modelling

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 348*

> **Where this technique is used — 10.44 State Modelling** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to specify the different states of a part of the solution throughout a life cycle, in terms of the events that occur.

### 10.44.1 Purpose — State Modelling

State modelling is used to describe and analyze the different possible states of an entity within a system, how that entity changes from one state to another, and what can happen to the entity when it is in each state.

### 10.44.2 Description — State Modelling

An entity is an object or concept within a system. An entity may be used in several processes. The life cycle of every entity has a beginning and an end.

In a state model (also sometimes called a state transition model), a state is a formal representation of a status. It is used when it is necessary to have a precise and consistent understanding of an entity that has complex behaviour and complex rules about that behaviour.

A state model describes:

- a set of possible states for an entity,

- the sequence of states that the entity can be in,

- how an entity changes from one state to another,

- the events and conditions that cause the entity to change states, and

- the actions that can or must be performed by the entity in each state as it moves through its life cycle.

While a process model can show all of the entities that are used in or affected by that process, a state model shows a complementary view: what happens to one entity across all the processes that affect it or use it.

### 10.44.3 Elements — State Modelling

#### 10.44.3.1 State — State Modelling

An entity has a finite number of states during its life cycle, although it can be in more than one state at a time. Each state is described with a name and the activities that could be performed while in that state. There may be rules about which activities must or can be performed and which events it can respond to or trigger.

A complex state can be decomposed into sub-states.

#### 10.44.3.2 State Transition — State Modelling

How the entity changes or transitions from one state to another could be determined by the steps of a process, by business rules, or by information content. The sequence of states of an entity are not always linear; an entity could skip over several states or revert to a previous state, perhaps more than once.

A transition may be conditional (triggered by a specific event or a condition being reached) or automatic (triggered by the completion of the required activities while in the previous state or by the passage of time). It may also be recursive, leaving one state and returning back to the same state. A transition is described in terms of the event that causes the transition, conditions which determine whether or not the entity must respond to that event, and actions that occur in association with the event.

#### 10.44.3.3 State Diagram — State Modelling

A state diagram shows the life cycle of one entity, beginning when the entity first comes into existence and moving through all of the different states that the entity may have until it is discarded and no longer of use.

A state on a state diagram is shown as a rectangle with rounded corners. There may be any number of states. A state may be decomposed into sub-states.

The transition from one state to another state is shown with a one-directional arrow pointing from the start state to the destination state, optionally labelled with the name of the event that causes the entity’s state to change from one state to another, and optionally with conditions and actions.

The beginning and end of the entity’s life cycle are shown with special symbols for both the initial state, which indicates that the entity has come into existence, and the final state, which indicates that the entity is discarded and the life cycle is complete.

**Figure 10.44.1: State Transition Diagram**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** Initial State · State 1 State 2 · Transition · State 3 · Final State

#### 10.44.3.4 State Tables — State Modelling

A state table is a two-dimensional matrix showing states and the transitions between them. It can be used during elicitation and analysis either as an alternative, a precursor, or a complement to a state diagram. It is a simple way to get started on a state model in order to elicit the state names and event names from the domain subject matter experts.

Each row shows a starting state, the transition, and the end state. If one state could respond to several transitions, there will be a separate row for each transition.

A state that appears as an end state in one row could be a start state in another row. **10.44.4 Usage Considerations**

### 10.44.4 Usage Considerations — State Modelling

#### 10.44.4.1 Strengths — State Modelling

- Identifies business rules and information attributes that apply to the entity being modelled.

- Identifies and describes the activities that apply to the entity at different states of the entity.

- Is a more effective documentation and communication tool than plain text, especially if the entity being described has more than a few states, transitions, and conditions governing those transitions.

#### 10.44.4.2 Limitations — State Modelling

- Is usually only used to understand and communicate about information entities that are perceived to be complex; simple entities may be understood without the time and effort required to build a state model.

- Building a state model appears simple at the start, but achieving a consensus among domain SMEs about the details required by the model can be difficult and time-consuming.

- A high degree of precision about states and transitions is required to build a state diagram; some domain SMEs and business analysis practitioners are uncomfortable trying to describe such a level of detail.

## 10.45 Survey or Questionnaire

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 350*

> **Where this technique is used — 10.45 Survey or Questionnaire** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **3.1 Plan Business Analysis Approach** (Business Analysis Planning and Monitoring): used to identify possible business analysis activities, techniques, risks and other relevant items to help build the business analysis approach.
> - **3.2 Plan Stakeholder Engagement** (Business Analysis Planning and Monitoring): used to identify shared characteristics of a stakeholder group.
> - **3.3 Plan Business Analysis Governance** (Business Analysis Planning and Monitoring): used to identify possible decision-making, change control, approval, or prioritization approaches and participants.
> - **3.4 Plan Business Analysis Information Management** (Business Analysis Planning and Monitoring): used to ask stakeholders to provide input into defining business analysis information management.
> - **3.5 Identify Business Analysis Performance Improvements** (Business Analysis Planning and Monitoring): used to gather feedback from stakeholders about their satisfaction with business analysis activities and deliverables.
> - **4.2 Conduct Elicitation** (Elicitation and Collaboration): used to elicit business analysis information, including information about customers, products, work practices, and attitudes, from a group of people in a structured way and in a relatively short period of time.
> - **6.1 Analyze Current State** (Strategy Analysis): helps to gain an understanding of the current state from a large, varied, or disparate group of stakeholders.
> - **6.2 Define Future State** (Strategy Analysis): used to understand stakeholders' desired future state, which needs they want to address, and what desired business objectives they want to meet.
> - **6.3 Assess Risks** (Strategy Analysis): used to understand what stakeholders think might be risks and the various factors of those risks.
> - **7.5 Define Design Options** (Requirements Analysis and Design Definition): used to help identify improvement opportunities and design options.
> - **7.6 Analyze Potential Value and Recommend Solution** (Requirements Analysis and Design Definition): used to get stakeholder input on which design options best meet the requirements, and to identify stakeholders’ value expectations.
> - **8.1 Measure Solution Performance** (Solution Evaluation): used to gather opinions and attitudes about solution performance. Surveys and questionnaires can be effective when large or disparate groups need to be polled.
> - **8.2 Analyze Performance Measures** (Solution Evaluation): used to determine expected value of a solution and its perceived performance.
> - **8.3 Assess Solution Limitations** (Solution Evaluation): used to help perform problem analysis.
> - **8.4 Assess Enterprise Limitations** (Solution Evaluation): used to identify organizational gaps or stakeholder concerns.
> - **8.5 Recommend Actions to Increase Solution Value** (Solution Evaluation): used to gather feedback from a wide variety of stakeholders to determine if value has been met or exceeded, if the metrics are still valid or relevant in the current context, and what actions might be taken to improve the solution.

### 10.45.1 Purpose — Survey or Questionnaire

A survey or questionnaire is used to elicit business analysis information—including information about customers, products, work practices, and attitudes—from a group of people in a structured way and in a relatively short period of time.

### 10.45.2 Description — Survey or Questionnaire

A survey or questionnaire presents a set of questions to stakeholders and subject matter experts (SMEs), whose responses are then collected and analyzed in order to formulate knowledge about the subject matter of interest. The questions can be submitted in written form or can be administered in person, over the telephone, or using technology that can record responses.

There are two types of questions used in a survey or questionnaire:

- **Close-ended**: the respondent is asked to select from a list of predefined responses, such as a Yes/No response, a multiple-choice selection, a rank/ order decision, or a statement requiring a level of agreement. This is useful when the anticipated range of user responses is fairly well defined and understood. The responses to close-ended questions are easier to analyze than those gained from open-ended questions because they can be tied to numerical coefficients.

- **Open-ended**: the respondent is asked to answer questions in a free form without having to select an answer from a list of predefined responses. Open-ended questions are useful when the issues are known and the range of user responses is not. Open-ended questions may result in more detail and a wider range of responses than closed-ended questions. The responses to open-ended questions are more difficult and time-consuming to categorize, quantify, and summarize as they are unstructured and often include subjective language with incomplete or superfluous content.

Questions should be asked in a way that does not influence the response data. They should be expressed in neutral language and should not be structured or sequenced to condition the respondent to provide perceived desirable answers.

### 10.45.3 Elements — Survey or Questionnaire

#### 10.45.3.1 Prepare — Survey or Questionnaire

An effective survey or questionnaire requires detailed planning in order to ensure that the needed information is obtained in an efficient manner.

When preparing for a survey or questionnaire, business analysts do the following:

- **Define the objective**: a clear and specific objective establishes a defined purpose of the survey or questionnaire. Questions are formulated with the intent of meeting the objective.

- **Define the target survey group**: identifying the group to be surveyed in terms of population size and any perceived variations (for example, culture, language, or location) helps identify factors that can impact survey design.

- **Choose the appropriate survey or questionnaire type**: the objective of the survey or questionnaire determines the appropriate combination of close-ended questions and open-ended questions to elicit the information required.

- **Select the sample group**: consider both the survey or questionnaire type and the number of people in the identified user group in order to determine if it is necessary and feasible to survey the entire group. It may be important to survey all members—even of a large group—if their demographics indicate a wide variance due to geographic distribution, regulatory differences, or lack of standardization in job function or business process. If the population is large and the survey type is open-ended, it may be necessary to identify a subset of users to engage in the questionnaire process. Using a statistical sampling method will help ensure that the sample selected is representative of the population so that the survey results can be reliably generalized.

- **Select the distribution and collection methods**: determine the appropriate communication mode for each sample group.

- **Set the target level and timeline for response**: determine what response rate is acceptable and when it should be closed or considered complete. If the actual response rate is lower than the acceptable threshold, the use of the survey results may be limited.

- **Determine if the survey or questionnaire should be supported with individual interviews**: as a survey or questionnaire does not provide the depth of data that can be obtained from individual interviews, consider either pre- or post-survey or questionnaire interviews.

- **Write the survey questions**: ensure that all the questions support the stated objectives.

- **Test the survey or questionnaire**: a usability test on the survey identifies errors and opportunities for improvement.

#### 10.45.3.2 Distribute the Survey or Questionnaire — Survey or Questionnaire

When distributing the survey or questionnaire it is important to communicate the survey's objectives, how its results will be used, as well as any arrangements for confidentiality or anonymity that have been made.

When deciding on a method of distribution (for example, in-person, e-mail, or survey tool), business analysts consider:

- the urgency of obtaining the results,

- the level of security required, and

- the geographic distribution of the respondents.

#### 10.45.3.3 Document the Results — Survey or Questionnaire

When documenting the results of the survey or questionnaire, business analysts:

- collate the responses,

- summarize the results,

- evaluate the details and identify any emerging themes,

- formulate categories for encoding the data, and

- break down the data into measurable increments.

### 10.45.4 Usage Considerations — Survey or Questionnaire

#### 10.45.4.1 Strengths — Survey or Questionnaire

- Quick and relatively inexpensive to administer.

- Easier to collect information from a larger audience than other techniques such as interviews.

- Does not typically require significant time from the respondents.

- Effective and efficient when stakeholders are geographically dispersed.

- When using closed-ended questions, surveys can be effective for obtaining quantitative data for use in statistical analysis.

- When using open-ended questions, survey results may yield insights and opinions not easily obtained through other elicitation techniques.

#### 10.45.4.2 Limitations — Survey or Questionnaire

- To achieve unbiased results, specialized skills in statistical sampling methods are needed when surveying a subset of potential respondents.

- The response rates may be too low for statistical significance.

- Use of open-ended questions requires more analysis.

- Ambiguous questions may be left unanswered or answered incorrectly.

- May require follow-up questions or more survey iterations depending on the answers provided.

## 10.46 SWOT Analysis

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 353*

> **Where this technique is used — 10.46 SWOT Analysis** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **6.1 Analyze Current State** (Strategy Analysis): evaluates the strengths, weaknesses, opportunities, and threats to the current state enterprise.
> - **6.2 Define Future State** (Strategy Analysis): used to evaluate the strengths, weaknesses, opportunities, and threats that may be exploited or mitigated by the future state.
> - **6.4 Define Change Strategy** (Strategy Analysis): used to make decisions about which change strategy is appropriate.
> - **7.6 Analyze Potential Value and Recommend Solution** (Requirements Analysis and Design Definition): used to identify areas of strength and weakness that will impact the value of the solutions.
> - **8.4 Assess Enterprise Limitations** (Solution Evaluation): used to demonstrate how a change will help the organization maximize strengths and minimize weaknesses, and to assess strategies developed to respond to identified issues.

### 10.46.1 Purpose — SWOT Analysis

SWOT analysis is a simple yet effective tool used to evaluate an organization's strengths, weaknesses, opportunities, and threats to both internal and external conditions.

### 10.46.2 Description — SWOT Analysis

SWOT analysis is used to identify the overall state of an organization both internally and externally.

The language used in a SWOT analysis is brief, specific, realistic, and supported by evidence. SWOT analysis serves as an evaluation of an organization against identified success factors. SWOT can be performed at any scale from the enterprise as a whole to a division, a business unit, a project, or even an individual. By performing SWOT in a disciplined way, stakeholders can have a clearer understanding of the impact of an existing set of conditions on a future set of conditions.

A SWOT analysis can be used to:

- evaluate an organization's current environment,

- share information learned with stakeholders,

- identify the best possible options to meet an organization’s needs,

- identify potential barriers to success and create action plans to overcome barriers,

- adjust and redefine plans throughout a project as new needs arise,

- identify areas of strength that will assist an organization in implementing new strategies,

- develop criteria for evaluating project success based on a given set of requirements,

- identify areas of weakness that could undermine project goals, and

- develop strategies to address outstanding threats.

### 10.46.3 Elements — SWOT Analysis

SWOT is an acronym for Strengths, Weaknesses, Opportunities, and Threats:

- **Strengths (S)**: anything that the assessed group does well. May include experienced personnel, effective processes, IT systems, customer relationships, or any other internal factor that leads to success.

- **Weaknesses (W)**: actions or functions that the assessed group does poorly or not at all.

- **Opportunities (O)**: external factors of which the assessed group may be able to take advantage. May include new markets, new technology, changes in the competitive marketplace, or other forces.

- **Threats (T)**: external factors that can negatively affect the assessed group. They may include factors such as the entrance into the market of a new competitor, economic downturns, or other forces.

Beginning a SWOT analysis with opportunities and threats sets the context to identify strengths and weaknesses.

**Figure 10.46.1: SWOT Matrix**

||**Opportunities** Opportunity Opportunity Opportunity|**Threats** Threat Threat Threat|
|---|---|---|
|**Strengths**|**SO Strategies**|**STStrategies**|
|Strength Strength Strength|How can the group's strength be used to exploit potential opportunities? SO strategies are fairly straightforward to implement.|How can the group use its strengths to ward off potential threats? Can the threats be turned into opportunities?|
|**Weaknesses**|**WO Strategies**|**WT Strategies**|
|Weakness Weakness Weakness|Can the group use an opportunity to eliminate or mitigate a weakness? Does the opportunity warrant the development of new capabilities?|Can the group restructure itself to avoid the threat? Should the group consider getting out of this market? WT strategies involve worst-case scenarios.|

### 10.46.4 Usage Considerations — SWOT Analysis

#### 10.46.4.1 Strengths — SWOT Analysis

- Is a valuable tool to aid in understanding the organization, product, process, or stakeholders.

- Enables business analysts to direct the stakeholders’ focus to the factors that are important to the business.

#### 10.46.4.2 Limitations — SWOT Analysis

- The results of a SWOT analysis provide a high-level view; more detailed analysis is often needed.

- Unless a clear context is defined for the SWOT analysis the result may be unfocused and contain factors which are not relevant to the current situation.

## 10.47 Use Cases and Scenarios

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 356*

> **Where this technique is used — 10.47 Use Cases and Scenarios** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **5.2 Maintain Requirements** (Requirements Life Cycle Management): used to identify a solution component that may be utilized by more than one solution.
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to model the desired behaviour of a solution, by showing user interactions with the solution, to achieve a specific goal or accomplish a particular task.
> - **8.1 Measure Solution Performance** (Solution Evaluation): used to define the expected outcomes of a solution.

### 10.47.1 Purpose — Use Cases and Scenarios

Use cases and scenarios describe how a person or system interacts with the solution being modelled to achieve a goal.

### 10.47.2 Description — Use Cases and Scenarios

Use cases describe the interactions between the primary actor, the solution, and any secondary actors needed to achieve the primary actor's goal. Use cases are usually triggered by the primary actor, but in some methods may also be triggered by another system or by an external event or timer.

A use case describes the possible outcomes of an attempt to accomplish a particular goal that the solution will support. It details different paths that can be followed by defining primary and alternative flows. The primary or basic flow represents the most direct way to accomplish the goal of the use case. Special circumstances and exceptions that result in a failure to complete the goal of the use case are documented in alternative or exception flows. Use cases are written from the point of view of the actor and avoid describing the internal workings of the solution.

Use case diagrams are a graphical representation of the relationships between actors and one or more use cases supported by the solution.

Some use case approaches distinguish between business use cases and system use cases, with business use cases describing how actors interact with a particular process or business function, and system use cases describing the interaction between an actor and a software application.

A scenario describes just one way that an actor can accomplish a particular goal. Scenarios are written as a series of steps performed by actors or by the solution that enable an actor to achieve a goal. A use case describes several scenarios.

### 10.47.3 Elements — Use Cases and Scenarios

There is no fixed, universal format for use cases. The following elements are frequently captured in a use case description.

#### 10.47.3.1 Use Case Diagram — Use Cases and Scenarios

A use case diagram visually depicts the scope of the solution, by showing the actors who interact with the solution, which use cases they interact with, and any relationships between the use cases. Unified Modelling Language™ (UML® ) describes the standard notation for a use case diagram.

##### Relationships

Relationships between actors and use cases are called associations. An association line indicates that an actor has access to the functionality represented by the use case. Associations do not represent input, output, time, or dependency.

There are two commonly used relationships between use cases:

- **Extend**: allows for the insertion of additional behavior into a use case. The use case that is being extended must be completely functional in its own right and must not depend on the extending use case for its successful execution. This relationship may be used to show that an alternate flow has been added to an existing use case (representing new requirements).

- **Include**: allows for the use case to make use of functionality present in another use case. The included use case does not need to be a complete use case in its own right if it is not directly triggered by an actor. This relationship is most often used either when some shared functionality is required by several use cases or to abstract out a complex piece of logic.

**Figure 10.47.1: Use Case Diagram**

> **Diagram labels (extracted from the figure; spatial layout not preserved):** System · Use Case 3 Use Case 4 · «extend» «include» · Use Case 2 · Use Case 1 Extension points: · Call Use Case 3 · Actor 1 Actor 2

#### 10.47.3.2 Use Case Description — Use Cases and Scenarios

##### Name

The use case has a unique name. The name generally includes a verb that describes the action taken by the actor and a noun that describes either what is being done or the target of the action.

##### Goal

The goal is a brief description of a successful outcome of the use case from the perspective of the primary actor. This acts as a summary of the use case.

##### Actors

An actor is any person or system external to the solution that interacts with that solution. Each actor is given a unique name that represents the role they play in interactions with the solution. Some use case authoring approaches recommend against the use of systems or events as actors.

A use case is started by an actor, referred to as the primary actor for that use case. Other actors who participate in the use case in a supporting role are called secondary actors.

##### Preconditions

A precondition is any fact that must be true before the use case can begin. The precondition is not tested in the use case but acts as a constraint on its execution.

##### Trigger

A trigger is an event that initiates the flow of events for a use case. The most common trigger is an action taken by the primary actor.

A temporal event (for example, time) can initiate a use case. This is commonly used to trigger a use case that must be executed based on the time of day or a specific calendar date, such as an end-of-day routine or an end-of-month reconciliation of a system.

##### Flow of Events

The flow of events is the set of steps performed by the actor and the solution during the execution of the use case. Most use case descriptions separate out a basic, primary, or main success flow that represents the shortest or simplest successful path that accomplishes the goal of the actor.

Use cases may also include alternative and exception flows. Alternative flows describe other paths that may be followed to allow the actor to successfully achieve the goal of the use case. Exception flows describe the desired response by the solution when the goal is unachievable and the use case cannot be successfully completed.

##### Post-conditions or Guarantees

A post-condition is any fact that must be true when the use case is complete. The post-conditions must be true for all possible flows through the use case, including both the primary and alternative flows. The use case may describe separate postconditions that are true for successful and unsuccessful executions of the use case. These can be called guarantees; the success guarantee describes the postconditions for success. Minimal guarantees describe the conditions that are required to be true, even if the actor’s goal is not achieved, and may address concerns such as security requirements or data integrity.

### 10.47.4 Usage Considerations — Use Cases and Scenarios

#### 10.47.4.1 Strengths — Use Cases and Scenarios

- Use case diagrams can clarify scope and provide a high-level understanding of requirements.

- Use case descriptions are easily understood by stakeholders due to their narrative flow.

- The inclusion of a desired goal or outcome ensures that the business value of the use case is articulated.

- Use case descriptions articulate the functional behaviour of a system.

#### 10.47.4.2 Limitations — Use Cases and Scenarios

- The flexibility of the use case description format may lead to information being embedded that would be better captured using other techniques such as user interface interactions, non-functional requirements, and business rules.

- Decisions and the business rules that define them should not be recorded directly in use cases, but managed separately and linked from the appropriate step.

- The flexible format of use cases may result in capturing inappropriate or unnecessary detail in the attempt to show every step or interaction.

- Use cases intentionally do not relate to the design of the solution and as a result, significant effort may be required in development to map use case steps to software architecture.

## 10.48 User Stories

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 359*

> **Where this technique is used — 10.48 User Stories** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **5.2 Maintain Requirements** (Requirements Life Cycle Management): used to identify requirements associated with the story that may be available for reuse.
> - **7.1 Specify and Model Requirements** (Requirements Analysis and Design Definition): used to specify requirements as a brief statement about what people do or need to do when using the solution.

### 10.48.1 Purpose — User Stories

A user story represents a small, concise statement of functionality or quality needed to deliver value to a specific stakeholder.

### 10.48.2 Description — User Stories

User stories capture the needs of a specific stakeholder and enable teams to define features of value to a stakeholder using short, simple documentation. They can serve as a basis for identifying needs and allow for the prioritizing, estimating, and planning of solutions. A user story is typically a sentence or two that describes who has the need addressed by the story, the goal the user is trying to accomplish, and any additional information that may be critical to understanding the scope of the story. With a focus on stakeholder value, user stories invite exploration of the requirements by promoting additional conversations with stakeholders and grouping functional requirements for delivery.

User stories can be used:

- to capture stakeholder needs and prioritize development of solutions,

- as a basis of estimating and planning solution delivery,

- as a basis for generating user acceptance tests,

- as a metric for measuring the delivery of value,

- as a unit for tracing related requirements,

- as a basis for additional analysis, and

- as a unit of project management and reporting.

### 10.48.3 Elements — User Stories

#### 10.48.3.1 Title (optional) — User Stories

The title of the story describes an activity the stakeholder wants to carry out with the system. Typically, it is an active-verb goal phrase similar to the way use cases are titled.

#### 10.48.3.2 Statement of Value — User Stories

There is no mandatory structure for user stories.

The most popular format includes three components:

- **Who**: a user role or persona.

- **What**: a necessary action, behaviour, feature, or quality.

- **Why**: the benefit or value received by the user when the story is implemented.

For example, "As a <who>, I need to <what>, so that <why>." "Given...When...Then" is another common format.

#### 10.48.3.3 Conversation — User Stories

User stories help teams to explore and understand the feature described in the story and the value it will deliver to the stakeholder. The story itself doesn't capture everything there is to know about the stakeholder need and the information in the story is supplemented by further modelling as the story is delivered.

#### 10.48.3.4 Acceptance Criteria — User Stories

A user story may be supported through the development of detailed acceptance criteria (see Acceptance and Evaluation Criteria (p. 217)). Acceptance criteria define the boundaries of a user story and help the team to understand what the solution needs to provide in order to deliver value for the stakeholders. Acceptance criteria may be supplemented with other analysis models as needed.

### 10.48.4 Usage Considerations — User Stories

#### 10.48.4.1 Strengths — User Stories

- Easily understandable by stakeholders.

- Can be developed through a variety of elicitation techniques.

- Focuses on value to stakeholders.

- A shared understanding of the business domain is enhanced through collaboration on defining and exploring user stories.

- Tied to small, implementable, and testable slices of functionality, which facilitates rapid delivery and frequent customer feedback.

#### 10.48.4.2 Limitations — User Stories

In general, user stories are intended as a tool for short-term capture and prioritization of requirements and not for long-term knowledge retention or to provide a detailed analysis. Neglecting this principle can lead to the following issues:

- This conversational approach can challenge the team since they do not have all the answers and detailed specifications upfront.

- Requires context and visibility; the team can lose sight of the big picture if stories are not traced back through validation or supplemented with higherlevel analysis and visual artifacts.

- May not provide enough documentation to meet the need for governance, a baseline for future work, or stakeholder expectations. Additional documentation may be required.

## 10.49 Vendor Assessment

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 361*

> **Where this technique is used — 10.49 Vendor Assessment** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **6.1 Analyze Current State** (Strategy Analysis): determines whether any vendors that are part of the current state are adequately meeting commitments, or if any changes are needed.
> - **6.2 Define Future State** (Strategy Analysis): used to assess potential value provided by vendor solution options.
> - **6.4 Define Change Strategy** (Strategy Analysis): used to determine whether any vendors are part of the change strategy, either to implement the change or to be part of the solution.
> - **7.5 Define Design Options** (Requirements Analysis and Design Definition): used to couple the assessment of a third party solution with an assessment of the vendor to ensure that the solution is viable and all parties will be able to develop and maintain a healthy working relationship.
> - **8.1 Measure Solution Performance** (Solution Evaluation): used to assess which of the vendor’s performance measures should be included in the solution’s performance assessment.

### 10.49.1 Purpose — Vendor Assessment

A vendor assessment assesses the ability of a vendor to meet commitments regarding the delivery and the consistent provision of a product or service.

### 10.49.2 Description — Vendor Assessment

When solutions are in part provided by external vendors (who may be involved in design, construction, implementation, or maintenance of the solution or solution components), or when the solution is outsourced, there may be specific requirements in regard to the involvement of a third party. There may be a need to ensure that the supplier is financially secure, capable of maintaining specific staffing levels, compliant with standards, and able to commit appropriate skilled staff to support the solution. Non-functional requirements can be used to define the service levels expected of a third party, due diligence may be conducted, or certification from an independent authority may be requested.

A vendor assessment is conducted to ensure that the vendor is reliable and that the product and service meet the organization's expectations and requirements. The assessment may be formal through the submission of a Request for Information (RFI), Request for Quote (RFQ), Request for Tender (RFT), or Request for Proposal (RFP). It may also be very informal through word of mouth and recommendations. The standards of the organization, the complexity of the initiative, and the criticality of the solution may influence the level of formality in which vendors are assessed.

### 10.49.3 Elements — Vendor Assessment

#### 10.49.3.1 Knowledge and Expertise — Vendor Assessment

A common reason for using third-party vendors is that they can provide knowledge and expertise not available within the organization. It may be desirable to target vendors with expertise in particular methodologies or technologies with the goal of having that expertise transferred to people within the enterprise.

#### 10.49.3.2 Licensing and Pricing Models — Vendor Assessment

The licensing or pricing model is taken into account in cases where a solution or solution component is purchased from or outsourced to a third party vendor. In many cases, solutions that offer similar functionality may differ greatly in their licensing models, which then requires analysis of different usage scenarios to determine which option will provide the best cost-benefit ratio under the scenarios likely to be encountered in the enterprise.

#### 10.49.3.3 Vendor Market Position — Vendor Assessment

It is important to be able to compare each vendor with the competitors and decide with which market players the organization wants to get involved. The comparison of the organization’s profile with each vendor’s customer community may also be a factor in the assessment. The dynamics of the vendors’ market position are also very important, especially if the organization intends to establish a long-term partnership with that vendor.

#### 10.49.3.4 Terms and Conditions — Vendor Assessment

Terms and conditions refer to the continuity and integrity of the provided products and services. The organization investigates whether the vendor's licensing terms, intellectual property rights and technology infrastructure are likely to turn into challenges if the organization later chooses to transition to another supplier. There may also be considerations regarding the vendor's use of, and responsibility for protecting, the organization's confidential data. The terms under which customizations of the product will be executed, as well as the availability of a regular update schedule and roadmap of features that are planned for delivery, are considered.

#### 10.49.3.5 Vendor Experience, Reputation, and Stability — Vendor Assessment

Vendors' experience with other customers may provide valuable information on how likely it is that they will be able to meet their contractual and noncontractual obligations. Vendors can also be evaluated for conformance and compliance with external relevant standards for quality, security, and professionalism. It may be necessary to request that steps be taken to ensure there are no risks if a vendor encounters financial difficulties, and that it will be possible to maintain and enhance the solution even if the vendor's situation changes radically.

### 10.49.4 Usage Considerations — Vendor Assessment

#### 10.49.4.1 Strengths — Vendor Assessment

- Increases the chances of the organization to develop a productive and fair relationship with a suitable and reliable vendor, and to improve long-term satisfaction with the decision.

#### 10.49.4.2 Limitations — Vendor Assessment

- May be consuming in regards to time and resources.

- Does not prevent risk of failure as the partnership evolves.

- Subjectivity may bias the evaluation outcome.

## 10.50 Workshops

*BABOK® Guide v3 (IIBA, 2015) · Chapter 10 · p. 363*

> **Where this technique is used — 10.50 Workshops** (tasks whose Techniques section lists it; this is the Appendix B mapping plus the task-specific usage text)
> - **3.1 Plan Business Analysis Approach** (Business Analysis Planning and Monitoring): used to help build the plan in a team setting.
> - **3.2 Plan Stakeholder Engagement** (Business Analysis Planning and Monitoring): used to interact with groups of stakeholders to gain more information about stakeholder groups.
> - **3.3 Plan Business Analysis Governance** (Business Analysis Planning and Monitoring): used to identify possible decision-making, change control, approval, or prioritization approaches and participants within a team setting.
> - **3.4 Plan Business Analysis Information Management** (Business Analysis Planning and Monitoring): used to uncover business analysis information management needs in a group setting.
> - **3.5 Identify Business Analysis Performance Improvements** (Business Analysis Planning and Monitoring): used to gather assessments of business analysis performance and generate ideas for improvement opportunities.
> - **4.2 Conduct Elicitation** (Elicitation and Collaboration): used to elicit business analysis information, including information about customers, products, work practices, and attitudes, from a group of people in a collaborative, facilitated way.
> - **4.3 Confirm Elicitation Results** (Elicitation and Collaboration): used to conduct reviews of the drafted elicitation results using any level of formality. A predetermined agenda, scripts, or scenario tests may be used to walk through the elicitation results, and feedback is requested from the participants and recorded.
> - **4.4 Communicate Business Analysis Information** (Elicitation and Collaboration): used to provide stakeholders with an opportunity to express feedback and to understand required adjustments, responses, and actions. They are also useful for gaining consensus and providing approvals. Typically used during group collaboration.
> - **5.3 Prioritize Requirements** (Requirements Life Cycle Management): used to gain an understanding of stakeholders' basis of prioritization or priorities in a facilitated group setting.
> - **5.4 Assess Requirements Changes** (Requirements Life Cycle Management): used to gain an understanding of the impact or to resolve changes in a group setting.
> - **5.5 Approve Requirements** (Requirements Life Cycle Management): used to facilitate obtaining approval.
> - **6.1 Analyze Current State** (Strategy Analysis): engage stakeholders to collaboratively describe the current state and their needs.
> - **6.2 Define Future State** (Strategy Analysis): used to work with stakeholders to collaboratively describe the future state.
> - **6.3 Assess Risks** (Strategy Analysis): used to understand what stakeholders think might be risks and the various factors of those risks.
> - **6.4 Define Change Strategy** (Strategy Analysis): used in work with stakeholders to collaboratively develop change strategies.
> - **7.4 Define Requirements Architecture** (Requirements Analysis and Design Definition): used to define the requirements structure collaboratively.
> - **7.5 Define Design Options** (Requirements Analysis and Design Definition): used to help identify improvement opportunities and design options.
> - **7.6 Analyze Potential Value and Recommend Solution** (Requirements Analysis and Design Definition): used to get stakeholder input on which design options best meet the requirements, and to evaluate stakeholders’ value expectations.
> - **8.4 Assess Enterprise Limitations** (Solution Evaluation): used to identify organizational gaps or stakeholder concerns.

### 10.50.1 Purpose — Workshops

Workshops bring stakeholders together in order to collaborate on achieving a predefined goal.

### 10.50.2 Description — Workshops

A workshop is a focused event attended by key stakeholders and subject matter experts (SMEs) for a concentrated period of time. A workshop may be held for different purposes including planning, analysis, design, scoping, requirements elicitation, modelling, or any combination of these. A workshop may be used to generate ideas for new features or products, to reach consensus on a topic, or to review requirements or designs.

Workshops generally include:

- a representative group of stakeholders,

- a defined goal,

- interactive and collaborative work,

- a defined work product, and

- a facilitator.

Workshops can promote trust, mutual understanding, and strong communication among the stakeholders and produce deliverables that structure and guide future work efforts.

The workshop is ideally facilitated by an experienced, neutral facilitator; however, a team member may also serve as the facilitator. A scribe documents the decisions reached and any outstanding issues. A business analyst may be the facilitator or the scribe in these workshops. In situations where the business analyst is a subject matter expert on the topic, they may serve as a workshop participant. This must be approached with caution as it can confuse others as to the role of the business analyst.

### 10.50.3 Elements — Workshops

#### 10.50.3.1 Prepare for the Workshop — Workshops

When preparing for a workshop, business analysts:

- define the purpose and desired outcomes,

- identify key stakeholders to participate,

- identify the facilitator and scribe,

- create the agenda,

- determine how the outputs will be captured,

- schedule the session and invite the participants,

- arrange room logistics and equipment,

- send the agenda and other materials in advance to prepare the attendees and increase productivity at the meeting, and

- if appropriate, conduct pre-workshop interviews with participants.

#### 10.50.3.2 Workshop Roles — Workshops

There are several roles involved in a successful workshop:

- **Sponsor**: frequently not a participant in the workshop, but does have ultimate accountability for its outcome.

- **Facilitator**: establishes a professional and objective tone for the workshop, introduces the goals and agenda for the workshop, enforces structure and ground rules, keeps activities focused on the purpose and desired outcomes, facilitates decision making and conflict resolution, and ensures that all participants have an opportunity to be heard.

- **Scribe**: documents the decisions in the format determined prior to the workshop and keeps track of any items or issues that are deferred during the session.

- **Timekeeper**: may be used to keep track of the time spent on each agenda item.

- **Participants**: includes key stakeholders and subject matter experts. They are responsible for providing their input and views, listening to other views, and discussing the issues without bias.

#### 10.50.3.3 Conduct the Workshop — Workshops

To ensure that all participants have a common understanding, facilitators generally begin the workshop with a statement of its purpose and desired outcomes. Some workshops may also start with an easy or fun task to break the ice and get the participants comfortable working together.

Establishing agreed-upon ground rules can be an effective method for establishing a productive environment for collaboration. Ground rules can include:

- respect the opinions of others,

- everyone is expected to contribute,

- discussion that is off-topic should be limited to a specific set time,

- discuss the issues, not the people, and

- an agreement on how decisions are made.

Throughout the workshop, the facilitator maintains focus by frequently validating the session’s activities with the workshop’s purpose and outcomes.

#### 10.50.3.4 Post Workshop Wrap-up — Workshops

After the workshop, the facilitator follows up on any open action items that were recorded at the workshop, completes the documentation, and distributes it to the workshop attendees and any stakeholders who need to be kept informed of the work done.

### 10.50.4 Usage Considerations — Workshops

#### 10.50.4.1 Strengths — Workshops

- Can be a means to achieve agreement in a relatively short period of time.

- Provides a means for stakeholders to collaborate, make decisions, and gain a mutual understanding.

- Costs are often lower than the cost of performing multiple interviews.

- Feedback on the issues or decisions can be provided immediately by the participants.

#### 10.50.4.2 Limitations — Workshops

- Stakeholder availability may make it difficult to schedule the workshop.

- The success of the workshop is highly dependent on the expertise of the facilitator and knowledge of the participants.

- Workshops that involve too many participants can slow down the workshop process. Conversely, collecting input from too few participants can lead to the overlooking of needs or issues that are important to some stakeholders, or to the arrival at decisions that don't represent the needs of the majority of the stakeholders.
