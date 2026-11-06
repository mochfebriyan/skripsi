<!-- Knowledge file: Chapter 3 — Business modeling -->
> **About this file.** Chapter 3 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Business modeling: BPMN tasks, events, gateways, pools and lanes, recommendations; state machine diagrams for state-dependent aspects of a business.  
> **Use this file when:** modeling an AS-IS or TO-BE business process (BPMN), swimlanes, gateways, or the life cycle/status of a business object.  
> **Sections:** 3.1 Introduction to business modeling (p. 25); 3.2 Business Process Modeling and Notation (p. 29); 3.3 State-dependent aspects of a business (p. 36); 3.4 Discussion (p. 38)  
> **Contains:** 11 figures transcribed as text, 0 code listings.

# Chapter 3: Business modeling

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 25*

Key topics in this chapter

- BPMN—Business Process Modeling and Notation

- State Machine Diagram

## 3.1 Introduction to business modeling

*Chapter 3 · p. 25*

In the beginning of the analysis process, the team must understand not only what is going to be developed but also the environment where this system is going to work. For example, a team that is going to develop a vaccination app could think about registering the name of the patient, some identification number, address, allergies, age, etc. However, why to register all that information if it is already available in other health record systems that the app could eventually interact with? Thus the team cannot start by focusing only on the system they are going to develop, they must understand the surroundings of the system, and business analysis is what they can use to accomplish it.

In the beginning of this process, it is assumed that the knowledge that the team has about the business is minimal, and that the interaction with the stakeholders will be intense. One of the goals in this stage is to discover if it is worth to do the analysis without dwelving too deep into the project.

Business modeling is, therefore, an activity that supports the discovery of user needs by helping the team to perceive the wider business context where the future system will operate. Different text or diagram artifacts can support it, as this chapter presents.

The artifacts in this phase usually do not need to be too detailed. Meetings with stakeholders could produce a record (minutes) that probably can register several ideas about the goals of the organization and the automation opportunities.

Business modeling starts with business use case diagrams, as seen in Chapter 2. Some business use cases would be very simple to understand, but others may be complex and need a deeper analysis to be completely understood. As business use cases are processes, diagrams such as the UML activity diagram and fluxograms could be used. However, the Business Process Model and Notation^1 , BPMN^2 , became dominant as a language for modeling processes, and for this reason, it will be introduced in this chapter.

> *Footnote 1:* Formerly known as “Business Process Modeling Notation.”

> *Footnote 2:* http://www.bpmn.org/

27

Business modeling consists of studying and understanding the organization and its context, because usually the system to be developed will not be an isolated product, but an organic part of the organization environment. The goals of this discipline are to:

- Understand the structure and dynamics of the target organization in which the software will be used.

- Understand the current problems of the target organization and identify potential improvements that can be obtained with the software.

- Assure that clients, users, and the development team share a consistent understanding of the target organization.

- Derive the requirements that will lead to the desired improvements.

Another important aspect of business modeling is to bring the business team and the software engineering team closer, so that the actual problems of the users and their needs are understood, analyzed, and solved using information technology.

Business modeling is more important when significant behavioral changes are introduced to a group of people. In this case, business context and the consequences of installing a new system must be acknowledged and studied. It may be less important when such behavioral changes are not expected.

Thus business modeling may have different levels of importance depending on the project’s needs. Kruchten (2003) identifies six scenarios of growing complexity in terms of the need for business modeling:

- Organizational chart: It may be necessary only to build an organizational chart to know the sectors and responsibilities related to the area in which the system is inserted. In this case, business modeling, in general, is very simple. The organizational chart will help analysts to locate the people that are responsible for the different aspects related to the future system, and what degree of authority is assigned to each one when deciding the requirements.

- Domain modeling: If the goal of the project is to build applications to manage and present information, then business modeling may be performed during domain analysis, that is, when a static model of the information (conceptual model) is produced.

- One organization, many systems: It may be the case that the team is developing a whole family of systems for an organization. In this case, business modeling is not only about one system, but spreads along many projects, and could even be a separated project of its own. It will help to discover individual system’s requirements as well as to determine a common architecture for the whole family.

- Generic business model: If the goal is to build one or more systems that will serve a pool of organizations, then business modeling is useful in order to align the different organizations to a common business view, or, if that is not possible, to obtain a business view in which the specifics of the organizations are visible.

- New business: If an organization decides to start a new business, and a whole set of systems must be developed to give support to it, then a significant business modeling

effort must be undertaken. In this case, the goal of business modeling is not only to help finding system requirements but also to verify the effective viability of the new business. Thus business modeling, in that situation, could be an independent project.

- Renewal: If an organization decides to completely renew its way of business, then business modeling will be a separate project, performed in several steps: vision of the new business, reverse engineering of the existing business, direct engineering of the new business, and installation of the new business.

Other factors that increase or decrease the need for business modeling in a project are:

- Well-defined and stable requirements at the beginning of the project (e.g., creating a substitute for an existing system) reduce the need to perform intense business modeling.

- If the new system is going to change the way people do their work, then special attention must be paid to business modeling, especially when the business model is going to be changed or rebuilt after the automation of some business use cases.

- If the project has important risks, especially business risks, then business modeling must be more detailed and intense.

- If the user community is large and heterogeneous, then business modeling probably will be more difficult.

- If it is necessary to integrate the new system with hardware and legacy systems, then the comprehension of those elements must be included in business modeling, generating more work.

- More uncertainty about requirements means more attention to business modeling.

No matter the level of detail and effort to be put into business modeling, every project must begin with preliminary documentation that allows for an understanding of its scope. A project with poorly defined scope may give rise to discomfort or even fights between the client and development team, regarding the inclusion (or lack of inclusion) of certain features.

## 3.2 Business Process Modeling and Notation

*Chapter 3 · p. 29*

The Business Process Modeling and Notation (BPMN) is a very popular option for studying the details of a business use case. With this diagram, the different tasks performed by business actors and workers to reach the general goal of the use case can be specified.

For a better understanding of the way the organization works through its use cases, it is possible to create a BPMN diagram for the nontrivial business use cases that are going to be developed. This is especially important when the team and even the users are not very sure about how the different activities are performed by the actors involved.

BPMN is a notation similar to fluxograms and UML activity diagrams, in the sense that it represents tasks by nodes and dependencies by arrows. But it introduces several new elements that help to improve the understanding on how the tasks are really performed and what kind of dependency exists among them.

### 3.2.1 Tasks — 3.2 Business Process Modeling and Notation

Before introducing a first example of business use case modeling with BPMN, let’s look at the basic types of BPMN nodes, which represent different kinds of tasks. First, a task is an atomic activity, that is, a task cannot be broken into smaller complete activities—by complete it is meant that the task must start, happen, and finish without being allowed to be interrupted and resumed later. A task is usually performed by a human or a system. BPMN defines seven types of tasks:

- Service task: a task that is performed by an automated system. For example, an automated credit card paying system registering payment.

- Send task: a task that sends a message from an actor to another. For example, a reviewer informing the manager of a project that she has completed a review.

- Receive task: a task that indicates that the process must wait until a message arrives. For example, a manager that must wait until all expected reviews have come before deciding on funding or not a project.

- User task: a task that is performed by a human user using an application. For example, a proponent registering her project in the system.

- Manual task: a task that is performed by a human without the use of an application. For example, a municipal manager monitoring the works under her jurisdiction.

- Business task: a task that provides data to a business rule engine (BRE) and receives output from it. A BRE is an application that runs a logic program that takes decisions based on previously defined rules written in an appropriate language.

- Script task: a task that corresponds to a script that a business engine may interpret and execute.

A task may also be left as generic if there is doubt about its kind. Fig. 3–1 summarizes the representation of the task types in BPMN.

Fig. 3–2^3 presents a simplified version of one of the core processes of SISMOB. It uses three kinds of tasks: manual, user, and service, and aims to explain the initial understanding of the flow of activities for proposing and executing a construction work.

Besides the already mentioned tasks, other elements appear in the diagram of Fig. 3–2, such as the start and end events, a gateway (decision node) and flows (labeled or not). Fig. 3–3 shows their respective representations.

### 3.2.2 Gateways — 3.2 Business Process Modeling and Notation

BPMN introduces a series of different kinds of gateways. In Fig. 3–2, two exclusive gateways were used: “Decision” and “Assessment.” Gateways can be used, as in this example, to allow the process to follow different paths depending on one or more conditions. Gateways may also be used to allow parallel paths, or even a combination of decision and parallelism as necessary. Each kind of gateway is explained below:

> *Footnote 3:* Syntactically, a task node in BPMN should not receive more than one incoming flow such as happens with “Register proposal” and “Monitoring” and a merge gateway should be used instead of two flows as seen in the figure. However, as the purpose of this diagram is to discover and document and not automatically generate systems, this syntactic flaw may be acceptable.

**Figure 3–1: Different types of tasks in BPMN. BPMN, Business Process Modeling and Notation.** *(p. 31)*

> **Diagram content (transcribed from the figure image):** BPMN task types (rounded rectangles with icons): Service task (gears), Send task (filled envelope), Receive task (empty envelope), User task (person), Manual task (hand), Business rule task (table), Script task (script), Generic task (no icon).

**Figure 3–2: An initial BPMN diagram for use case “Manage work.” BPMN, Business Process Modeling and Notation.** *(p. 31)*

> **Diagram content (transcribed from the figure image):** Initial BPMN diagram for business use case "Manage work" (single lane): Start → Register proposal (user) → Proposal assessment (user) → exclusive gateway "Decision": [changes needed] back to Register proposal; [not favorable] → End; [favorable] → Publication (service) → Monitoring (user) → Conclusion (user) → exclusive gateway "Assessment": [approved] → End; [changes needed] back to Monitoring; [not approved] → Refund investment (manual) → End.

**Figure 3–3: Other elements of a BPMN diagram. BPMN, Business Process Modeling and Notation.** *(p. 31)*

> **Diagram content (transcribed from the figure image):** Basic BPMN elements: Start event (thin green circle), End event (thick red circle), Gateway (diamond), Sequence flow (solid arrow between two tasks).

- Exclusive gateway: when a process comes to this gateway, a decision is taken and only one of the flows out of the gateway may be followed. In Fig. 3–2, the exclusive gateway “Decision” has three flows out of it: “favorable,” “not favorable,” and “changes needed,” meaning that only one of those paths may be followed after the decision represented in the gateway. In this case, it can be said that the gateway splits the flow of the process. Optionally, another exclusive gateway can be used to represent the merge of the paths,

**Figure 3–4: Types of gateways in BPMN. BPMN, Business Process Modeling and Notation.** *(p. 32)*

> **Diagram content (transcribed from the figure image):** BPMN gateway semantics. Exclusive gateway (split, plain diamond) with [true] → Optional tasks 1 and [false] → Optional tasks 2, then exclusive merge — only one path can be followed. Parallel gateway (fork, diamond with +) → Parallel tasks 1 and Parallel tasks 2 → parallel join — all paths are followed. Inclusive gateway (fork, diamond with circle) [condition 1] → Optional tasks 1, [condition 2] → Optional tasks 2 → inclusive join — one or more paths can be followed.

as seen in Fig. 3–4 (upper part). In this case, the paths that enter the gateway may be the same that have left the gateway used to split the process and only one flow may leave the gateway. There is no decision being made in a merge gateway; this is only a notation that serves to represent that after following different flows, the process proceeds in a reunified flow. • Parallel gateway: it can be used to define parallel paths, that is, different sequences of tasks that may be executed at the same time or, at least, without any dependency among them. As seen in Fig. 3–4 (middle), when a process comes to a parallel gateway, a fork happens, that is, all the flows out of the gateway may be executed in parallel (usually by different actors). The parallel gateway is also used to join the parallel paths back into a single flow. In the case of merging, the flow that goes out of the gateway can only be followed when all the incoming flows reach it. That means that if a path is completed before another, the gateway will hold the execution until the other process is also complete.

- Inclusive gateway: it is a combination of decision and parallelism. In this case, one or more decisions are taken, and one or more outgoing paths may be executed. The condition must be true for at least one of the outgoing flows. If it is true for more than one flow, then each flow for which it is true is executed in parallel from this point.

BPMN has other types of gateways, but they are used only in more advanced cases and will not be described here. For more information, see Shapiro et al. (2012).

### 3.2.3 Pools and lanes — 3.2 Business Process Modeling and Notation

Sometimes, BPMN diagrams represent activities that are performed by more than one actor. This situation can be described using pools and lanes. Just like in the case of a swimming pool, each lane is reserved for one actor; the tasks performed by each actor are represented inside her respective lane. Fig. 3–5 presents the first part of a complete diagram for the SISMOB project indicating the final understanding of the flow of the business use case “Manage work.” Three actors are participating in this use case: the municipal manager (who asks for money to build/reform a health facility), the federal manager (who assess and approves or denies proposals and reports), and an organization, the National Health Fund (FNS), which allocates money to the projects.

The flow of the process initiates with the municipal manager registering a proposal for a construction or reformation of a municipal healthcare building (user task “Register proposal”). After finishing registering all the information necessary (it can take days), she sends the proposal to the federal manager (sending task “Send proposal”).

Then, the federal manager will read and evaluate the proposal (user task “Produce assessment”). After that, there is an exclusive gateway that splits the flow into three possibilities:

**Figure 3–5: First part of a complete BPMN diagram for “Manage work.” BPMN, Business Process Modeling and Notation.** *(p. 33)*

> **Diagram content (transcribed from the figure image):** BPMN with pool "Manage Work" and lanes Municipal Manager, Federal Manager, National Health Fund. Municipal Manager: Start → Register proposal → Send proposal → (Federal Manager) Produce assessment → gateway: [changes needed] → Refactor proposal (Municipal) → Send proposal; [not favorable] → Cancel proposal → End; [favorable] → (National Health Fund) Allocate funds → Publish funds allocation (service) → (Municipal) Follow the progress of the preparatory phase → Require phase completion (send) → (Federal) Produce assessment → gateway: [changes needed] → Refactor requirement (Municipal) → Require phase completion; [not favorable] → (NHF) Deallocate funds (service) → End; [favorable] → link intermediate event MW1 (continues in Fig 3–7).

1. If the decision is “not favorable,” the federal manager cancels the proposal (user task “Cancel proposal”) and the process is finished.

2. If the decision is “changes needed,” the federal manager will return the flow to the municipal manager who, based on the information reported in the system by the federal manager in the task “Produce assessment,” will try to refactor the initial proposal (task “refactor proposal”). The refactored proposal is then sent back to the federal manager, and this decision cycle may be repeated one or more times.

3. If the decision is “favorable,” then the National Health Fund may allocate funds to the project (user task “Allocate funds”), and the official legal publication must be generated (automatic task “Publish funds allocation”).

Notice that in case (1), the process is finished; in case (2), the process enters a cycle and returns to this decision point; and in case (3), the process proceeds further.

If the process proceeds further, the municipal manager must follow the preparations for the beginning of the construction works (manual task “Follow the progress of the preparatory phase”). When she decides that all necessary prerequisites are in order, she requires from the federal manager the completion of the preparatory phase (user task “Require phase completion”). That starts a decision cycle very similar to the last one. However, this time, instead of assessing the initial project, the federal manager will evaluate the completion of the preparatory phase as informed by the municipal manager.

The federal manager then produces an assessment on the preparation phase and decides:

1. If “not favorable,” then the FNS deallocates money and the process is canceled.

2. If “changes needed,” then the municipal manager refactors the requirement and restarts the decision cycle.

3. If “favorable,” the process moves forward.

There is no space in Fig. 3–5 to conclude the diagram and keep a good visualization size. In this case, a continuation link (labeled as “MW1” in the example) can be used to continue the flow in another diagram. The link intermediate event (Fig. 3–6) is a node that can be used to indicate both incoming and outcoming flow between diagrams.

Fig. 3–7 shows the continuation of the diagram in Fig. 3–5. Instead of an initial event, it has a link intermediate event that specifies that this is a continuation of another diagram. The label MW1 is (and must be) the same used in the previous diagram. In this case, labels are mandatory because many diagrams may have different continuation diagrams and only the labels can help in knowing which is the correct one.

The second diagram then starts with a parallel node, representing a fork event. In this case, tasks “Follow work” allocated to the municipal manager and “Issue payment” allocated to the FNS may be executed in parallel. After both tasks are concluded, another parallel link will join both paths and the municipal manager may perform the task “Require work conclusion” when she seems convenient. Notice that the last task can only be initiated after “Issue payment” and “Follow work” are both completed.

**Figure 3–6: Link intermediate event.** *(p. 34)*

> **Diagram content (transcribed from the figure image):** BPMN link intermediate event symbol (double circle with arrow), used to continue a diagram elsewhere ("go to"/"continue from").

**Figure 3–7: Second part of a complete BPMN diagram for “Manage work.” BPMN, Business Process Modeling and Notation.** *(p. 35)*

> **Diagram content (transcribed from the figure image):** Continuation "Manage Work 1" (same three lanes). Link event MW1 → parallel gateway fork → Follow work (Municipal manager) and Issue payment (National Health Fund) → parallel join → Require work conclusion (Municipal, send) → Produce assessment (Federal manager) → gateway: [changes needed] → Refactor requirement (Municipal) → Require work conclusion; [favorable] → Follow operation (Municipal) → End; [not favorable] → Cancel project (NHF) → Refund resources (Municipal) → End.

A third decision cycle is then initiated with the following differences from the previous others:

1. If “not favorable,” then the FNS cancels the project (user task “Cancel project”), and the municipal manager must return the funds received (manual task “Refund resources”). This is a failure ending for this process.

2. If “changes needed,” then the municipal manager refactors the requirement and restarts the decision cycle.

3. If “favorable,” then the project has been completed with success and the municipal manager can follow the operation of the healthcare unit until a reform or deactivation of the unit is necessary.

Other elements exist in BPMN. If the reader is looking for a more profound view of the language, Shapiro et al. (2012) is a recommended reference.

### 3.2.4 General recommendations — 3.2 Business Process Modeling and Notation

Although BNPN seems to be a clear and understandable notation, as many other, modelers must take care not to violate some syntactic and sematic rules that may render the diagram obscure. D. Silingas and E. Milleviciene^4 present some antipatterns that would be avoided.

> *Footnote 4:* https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/2438/Efficient-BPMN-from-Anti-Patterns-toBest-Practices.aspx

One mistake is to name tasks with noun-based expressions, for example, “Project analysis.” That indicates that the element is in fact an object of information and not a task. It would be better to use a strong verb and a domain-specific noun, for example, “Analyze project.”

Another common mistake is to name a gateway with a label that indicates that it performs some tasks. The gateway is only a decision point. All tasks necessary to take the decision must be performed before the gateway. Gateways should not be labeled except for reference purposes.

Using the words “and” and “or” in task names is also not recommended because this indicates that the task is in fact a set of tasks that should be represented individually. Other option is to raise the level of abstraction for representing the different tasks by a single name.

## 3.3 State-dependent aspects of a business

*Chapter 3 · p. 36*

Besides business use cases, which may be detailed by BPMN diagrams, it may be important to understand other aspects of a business that do not always appear clearly in those diagrams, such as some key business objects that change state during their life cycle.

A UML diagram that can help the team to understand the organization’s business objects is the state machine diagram. It is a behavioral diagram, but, instead of modeling activities in processes, it represents a set of states in which a system, actor, or entity could be at a given instant.

The state machine diagram specifies events in its flows. An event triggers the flow that takes the entity from one state to another. That is, the flows are labeled with events that, if they occur, make the entity change from one state to another.

Those occurrences may be, however, restricted by guard conditions. For example, the login event may only send the system to a logged state if the password is correct.

Graphically, the events are represented in the flows by simple expressions, and guard conditions are represented between brackets as, shown in Fig. 3–8. In it, the entity goes from “State 1” to “State 2” when the event “login” happens, but only if the guard condition “password is correct” is true.

The transitions in a state machine diagram can also include effects that are performed in response to a state transition. For example, the transition activated by the event “login” and guarded by the condition “password is correct” can activate the action “grant access,” which is an effect of the transition (not its cause). Actions associated to transitions are represented by expressions initiated by a slash (/) as shown in Fig. 3–9.

**Figure 3–8: An event and guard transition between two states.** *(p. 36)*

> **Diagram content (transcribed from the figure image):** State machine transition: State 1 —login [password is correct]→ State 2 (event "login" with guard condition in brackets).

**Figure 3–9: An event, action, and guard condition between two states.** *(p. 37)*

> **Diagram content (transcribed from the figure image):** Transition with event, action and guard: State 1 —login / grant access [password is correct]→ State 2 (syntax event / action [guard]).

**Figure 3–10: Initial (incomplete) state machine diagram for a construction work.** *(p. 37)*

> **Diagram content (transcribed from the figure image):** State machine of a proposal: initial ● → Under preparation —propose→ Under assessment; Under assessment —approve→ Approved; —refuse→ final state "Canceled" (◉); —request changes→ back to Under preparation.

As an example on how that diagram can be useful during business analysis, we can imagine that a team is interested in understanding the life cycle of a construction work in the SISMOB project. Examining the different states of a key business object such as a work for this project may reduce the risk of underestimating the complexity of the system requirements.

Using the BPMN diagram of Figs. 3–5 and 3–7 as a basis, some different states of a work and some different events can be identified. Initially, a proposal for a work is in state “Under preparation,” meaning that it is being written or modified by a municipal manager. After the event “propose,” it changes to the state “Under assessment” meaning that it is being assessed by a federal manager and cannot be further modified unless another event occurs changing state again to “Under preparation.” After assessment, three possibilities can happen. If modifications are needed, the state returns to “Under preparation.” If the project is rejected, a final state is reached. If the proposal is approved, then the state changes to “Approved.”

The team could continue to complete this state machine diagram with information taken from the BPMN diagrams. But the question now is “Why?”: Why taking information from one diagram and represent it in another diagram? The answer is that the state machine diagram can help the team to see events that are not so easily seen in the BPMN diagram. At this point, the team would ask: “What other events and transitions could be possible between states that are not yet represented.” In Fig. 3–10, there are four states to consider. Some pairs have a transition between them and others not as seen in Table 3.1.

The question that the team now must clarify with the client/user is if there is a possibility of new events/transitions that are not represented in the state diagram. For example, may an approved project return to the assessment phase? If the answer is “yes,” which event allows this?

**Table 3–1: States and transitions.**

|From: To:|Under preparation|Under assessment|Approved|Canceled|
|---|---|---|---|---|
|Under preparation||Request changes|||
|Under assessment|Propose||||
|Approved||Approve|||
|Canceled||Refuse|||

**Figure 3–11: A state machine diagram with new transition/event.** *(p. 38)*

> **Diagram content (transcribed from the figure image):** Same proposal state machine but Canceled is a normal state (not final): Canceled —reactivate canceled proposal→ Under preparation; other transitions as Fig 3–10 (propose, approve, refuse, request changes). Shows how a state diagram reveals a new use case (reactivation).

In the case of the SISMOB project, for example, Phase 3 introduced a new feature that allows a canceled project to be reactivated. In the state diagram, it would be a transition from state “Canceled” that is not anymore a final state, to the state “Under preparation.” The event that triggers this transition is “reactivate canceled proposal,” which corresponds to a business new use case to be added to the set in Figure 2–4. Fig. 3–11 shows the state machine diagram updated with this transition. Notice that this new event is not necessarily part of the “Manage work” business use case, but a different use case. In this sense, the state machine diagram is important to help the team to discover different effects on a business object that may occur in different business use cases.

## 3.4 Discussion

*Chapter 3 · p. 38*

It is important to remember that the goal of business modeling is usually to find a general view of the business and not a detailed specification of its processes. Thus in most cases, the team’s goal is to concentrate on discovering information about the business and not on formally specifying how the business works as if it was a machine.

A question still may be asked: Which business use cases and objects deserve the production of a BPMN or state machine diagram? Unless stated to the contrary, it is not advisable to prepare a diagram for every business element, because some of them would be trivial. What is usually needed at this point is a model for some key elements, so that their behavior can be better understood, and their requirements derived later.

A clue to identify those key elements is to ask what the business objects are. In the case of a bookstore, they are books, in the case of a hotel, lodging, in the case of a court, criminal processes, and so on. Thus those are the key elements that must be modeled in greater detail to help in understanding the business.

A second question could be the following: Which diagram should we use—BPMN or state machine? The answer depends on the nature of the element to be modeled. BPMN models processes, that is, a set of tasks, while state machine diagrams model states of an object, not tasks.

In order to perceive that a state is different from a task, try to imagine a TV set. It may be in state “Off” and during it, it is not performing any task.

If the business object is active, then it may be executing some action during a state. For example, an elevator that is going up (task) and is in the state “Ascending.” However, many business objects may be passive and not active. Those kinds of objects cannot perform any action. They only can suffer the effects of actions done by others. For example, a book is incapable of performing any task. But it can have states, such as “Available,” “Sold,” “Damaged,” and “Lost.”

A BPMN diagram is useful when modeling people, organizations, or systems doing things. On the other hand, the state machine diagram is useful when a single entity passes through different states in which it is not necessarily doing something. Furthermore, the activity diagram usually details a business use case (i.e., a process such as selling, buying, checking), while the state machine diagram is usually associated with a business object (such as books, people, orders).

Business modeling is not just about building diagrams, however. The purpose of diagrams is to help understand the context and the initial general requirements of a project and a system. Business modeling is one of the key activities that help a team to identify and prepare for project risks. Other risk mitigation activities may also be performed during analysis, such as proof-ofconcept, workshops, prototyping, and early tests. Any strategy that helps in understanding the big picture and identifying the major risks and complexities of a project is valid.

## Questions (Chapter 3)

1. What is the purpose of business modeling?

2. Business modeling can occur with different levels of intensity for different kinds of projects. Explain and give examples!

3. Which aspects of a business may be detailed by a BPMN diagram? Which may be detailed by a state machine diagram?

4. Which kind of gateways does BPMN have, and which are their purpose?

5. Can active objects have a state in which they are not performing any task? Give an example.

This page intentionally left blank

